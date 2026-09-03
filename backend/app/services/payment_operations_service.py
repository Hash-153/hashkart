import hashlib
import hmac
import json
from datetime import datetime
from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models.order_payment import Payment
from app.models.payment_operations import PaymentReconciliation, PaymentWebhookEvent
from app.schemas.payment_operations import PaymentWebhookPayload, ReconciliationCreate


def verify_webhook_signature(raw_body: bytes, signature: str | None, secret: str) -> bool:
    if not signature or not secret:
        return False
    expected = hmac.new(secret.encode(), raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)


async def record_payment_webhook(
    db: AsyncSession,
    provider: str,
    payload: PaymentWebhookPayload,
    raw_body: bytes,
    signature: str | None,
) -> tuple[PaymentWebhookEvent, bool]:
    valid = verify_webhook_signature(raw_body, signature, settings.PAYMENT_WEBHOOK_SECRET)
    if not valid:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid webhook signature")

    existing = await db.scalar(
        select(PaymentWebhookEvent).where(
            PaymentWebhookEvent.provider == provider,
            PaymentWebhookEvent.event_id == payload.event_id,
        )
    )
    if existing:
        return existing, True

    event = PaymentWebhookEvent(
        provider=provider,
        event_id=payload.event_id,
        event_type=payload.event_type,
        transaction_reference=payload.transaction_reference,
        payload=json.dumps(payload.model_dump(mode="json")),
        signature_valid=True,
        processed=False,
    )
    db.add(event)
    await db.flush()

    if payload.transaction_reference and payload.status:
        payment = await db.scalar(
            select(Payment).where(Payment.transaction_reference == payload.transaction_reference)
        )
        if payment:
            payment.status = payload.status.upper()
            event.processed = True
            event.processed_at = datetime.utcnow()
    await db.flush()
    return event, False


async def reconcile_payment(
    db: AsyncSession, user_id: int, payload: ReconciliationCreate
) -> PaymentReconciliation:
    existing = await db.scalar(
        select(PaymentReconciliation).where(
            PaymentReconciliation.provider == payload.provider,
            PaymentReconciliation.settlement_reference == payload.settlement_reference,
        )
    )
    if existing:
        return existing

    status_value = "MATCHED" if payload.expected_amount == payload.received_amount else "MISMATCH"
    item = PaymentReconciliation(
        **payload.model_dump(), status=status_value, reconciled_by=user_id
    )
    db.add(item)
    await db.flush()
    return item


async def list_reconciliations(db: AsyncSession) -> list[PaymentReconciliation]:
    result = await db.execute(
        select(PaymentReconciliation).order_by(PaymentReconciliation.reconciled_at.desc())
    )
    return list(result.scalars().all())
