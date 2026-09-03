from datetime import datetime
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.notification_outbox import NotificationDelivery
from app.services.job_service import job_queue


async def enqueue_notification(
    db: AsyncSession,
    user_id: int,
    event_key: str,
    channel: str,
    recipient: str,
    subject: str,
    body: str,
) -> NotificationDelivery:
    existing = await db.scalar(
        select(NotificationDelivery).where(
            NotificationDelivery.user_id == user_id,
            NotificationDelivery.event_key == event_key,
            NotificationDelivery.channel == channel,
        )
    )
    if existing:
        return existing

    delivery = NotificationDelivery(
        user_id=user_id,
        event_key=event_key,
        channel=channel,
        recipient=recipient,
        subject=subject,
        body=body,
    )
    db.add(delivery)
    await db.flush()
    await job_queue.enqueue("notification.delivery", {"delivery_id": delivery.id})
    return delivery


async def process_notification_delivery(payload: dict) -> None:
    """Mark delivery as sent after an external provider adapter is integrated."""
    delivery_id = payload.get("delivery_id")
    if not delivery_id:
        return
    # Provider calls belong in a worker process with its own database session.
    return None
