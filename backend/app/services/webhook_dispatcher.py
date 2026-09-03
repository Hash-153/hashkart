import hashlib
import hmac
import json
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.webhooks_events import (
    WebhookDeliveryAttempt,
    WebhookDeliveryStatus,
    WebhookEventType,
    WebhookSubscription,
)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


def compute_hmac_signature(secret: str, payload_str: str) -> str:
    """Compute HMAC-SHA256 hex digest signature for webhook payload authenticity."""
    return hmac.new(
        secret.encode("utf-8"),
        payload_str.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


async def trigger_event_webhooks(
    db: AsyncSession,
    event_type: WebhookEventType,
    payload_data: Dict[str, Any],
    seller_id: Optional[int] = None,
) -> List[WebhookDeliveryAttempt]:
    """Broadcast an enterprise platform event to all registered active webhook subscribers."""
    stmt = (
        select(WebhookSubscription)
        .where(
            WebhookSubscription.is_active == True,
            (WebhookSubscription.seller_id == seller_id) | (WebhookSubscription.seller_id.is_(None)),
        )
    )
    res = await db.execute(stmt)
    subscriptions = res.scalars().all()

    payload_str = json.dumps(
        {
            "event": event_type.value,
            "timestamp": utcnow().isoformat(),
            "data": payload_data,
        },
        default=str,
    )

    created_deliveries: List[WebhookDeliveryAttempt] = []

    for sub in subscriptions:
        sub_events = json.loads(sub.subscribed_events_json) if sub.subscribed_events_json else []
        if event_type.value in sub_events or "*" in sub_events:
            sig = compute_hmac_signature(sub.secret_key, payload_str)
            delivery = WebhookDeliveryAttempt(
                subscription_id=sub.id,
                event_type=event_type,
                payload_json=payload_str,
                signature=sig,
                attempt_number=1,
                status=WebhookDeliveryStatus.PENDING,
                next_retry_at=utcnow(),
            )
            db.add(delivery)
            created_deliveries.append(delivery)

    await db.flush()
    return created_deliveries


async def record_delivery_result(
    db: AsyncSession,
    delivery_id: int,
    success: bool,
    http_status: Optional[int],
    response_body: Optional[str] = None,
    error_msg: Optional[str] = None,
) -> None:
    """Record delivery response and calculate exponential retry backoff or DLQ."""
    stmt = select(WebhookDeliveryAttempt).where(WebhookDeliveryAttempt.id == delivery_id)
    res = await db.execute(stmt)
    delivery = res.scalar_one_or_none()

    if not delivery:
        return

    delivery.http_status_code = http_status
    delivery.response_body = response_body
    delivery.error_message = error_msg

    if success:
        delivery.status = WebhookDeliveryStatus.SUCCESS
        delivery.delivered_at = utcnow()
        delivery.next_retry_at = None
    else:
        # Retry with exponential backoff: 2min, 10min, 60min, then DLQ
        if delivery.attempt_number >= 3:
            delivery.status = WebhookDeliveryStatus.DEAD_LETTER
            delivery.next_retry_at = None
        else:
            delivery.status = WebhookDeliveryStatus.FAILED_RETRYING
            delay_minutes = 2 ** (delivery.attempt_number) * 5
            delivery.next_retry_at = utcnow() + timedelta(minutes=delay_minutes)
            delivery.attempt_number += 1

    await db.flush()
