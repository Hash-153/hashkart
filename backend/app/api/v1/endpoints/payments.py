from fastapi import APIRouter, Depends, Header, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import require_staff
from app.database import get_db
from app.models.user import User
from app.schemas.payment_operations import (
    PaymentWebhookPayload,
    PaymentWebhookResponse,
    ReconciliationCreate,
    ReconciliationResponse,
)
from app.services.payment_operations_service import (
    list_reconciliations,
    reconcile_payment,
    record_payment_webhook,
)

router = APIRouter()


@router.post("/webhooks/{provider}", response_model=PaymentWebhookResponse)
async def payment_webhook(
    provider: str,
    request: Request,
    payload: PaymentWebhookPayload,
    x_webhook_signature: str | None = Header(default=None),
    db: AsyncSession = Depends(get_db),
):
    event, duplicate = await record_payment_webhook(
        db, provider, payload, await request.body(), x_webhook_signature
    )
    return PaymentWebhookResponse(
        accepted=True,
        duplicate=duplicate,
        event_id=event.event_id,
        processed=event.processed,
    )


@router.post("/reconciliation", response_model=ReconciliationResponse, status_code=status.HTTP_201_CREATED)
async def create_reconciliation(
    payload: ReconciliationCreate,
    user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await reconcile_payment(db, user.id, payload)


@router.get("/reconciliation", response_model=list[ReconciliationResponse])
async def reconciliation_report(
    _: User = Depends(require_staff), db: AsyncSession = Depends(get_db)
):
    return await list_reconciliations(db)
