import json
import secrets
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user, get_db, require_role
from app.models.seller import SellerProfile
from app.models.user import User
from app.models.webhooks_events import (
    WebhookDeliveryAttempt,
    WebhookDeliveryStatus,
    WebhookEventType,
    WebhookSubscription,
)
from app.schemas.webhooks_events import (
    WebhookDeliveryResponse,
    WebhookSubscriptionCreate,
    WebhookSubscriptionResponse,
    WebhookTestTriggerRequest,
)
from app.services.webhook_dispatcher import trigger_event_webhooks

router = APIRouter()


@router.post("/subscriptions", response_model=WebhookSubscriptionResponse)
async def create_webhook_subscription(
    payload: WebhookSubscriptionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Register an outbound webhook callback URL with unique HMAC signing secret."""
    # Find seller if seller role
    seller_id = None
    stmt = select(SellerProfile).where(SellerProfile.user_id == current_user.id)
    res = await db.execute(stmt)
    seller = res.scalar_one_or_none()
    if seller:
        seller_id = seller.id

    secret = f"whsec_{secrets.token_hex(24)}"
    events_json = json.dumps([e.value for e in payload.subscribed_events])

    sub = WebhookSubscription(
        seller_id=seller_id,
        endpoint_url=str(payload.endpoint_url),
        secret_key=secret,
        subscribed_events_json=events_json,
        is_active=True,
        description=payload.description,
    )
    db.add(sub)
    await db.commit()
    await db.refresh(sub)

    return WebhookSubscriptionResponse(
        id=sub.id,
        seller_id=sub.seller_id,
        endpoint_url=sub.endpoint_url,
        secret_key=sub.secret_key,
        subscribed_events=[WebhookEventType(e) for e in json.loads(sub.subscribed_events_json)],
        is_active=sub.is_active,
        description=sub.description,
        consecutive_failures=sub.consecutive_failures,
        created_at=sub.created_at,
        updated_at=sub.updated_at,
    )


@router.get("/subscriptions", response_model=List[WebhookSubscriptionResponse])
async def list_webhook_subscriptions(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """List all registered webhook subscriptions for the authenticated account."""
    stmt = select(SellerProfile).where(SellerProfile.user_id == current_user.id)
    res = await db.execute(stmt)
    seller = res.scalar_one_or_none()

    sub_stmt = select(WebhookSubscription)
    if seller:
        sub_stmt = sub_stmt.where(WebhookSubscription.seller_id == seller.id)
    else:
        # Staff/Admin
        pass

    s_res = await db.execute(sub_stmt)
    subs = s_res.scalars().all()

    return [
        WebhookSubscriptionResponse(
            id=s.id,
            seller_id=s.seller_id,
            endpoint_url=s.endpoint_url,
            secret_key=s.secret_key,
            subscribed_events=[WebhookEventType(e) for e in json.loads(s.subscribed_events_json)],
            is_active=s.is_active,
            description=s.description,
            consecutive_failures=s.consecutive_failures,
            created_at=s.created_at,
            updated_at=s.updated_at,
        )
        for s in subs
    ]


@router.post("/test-trigger")
async def trigger_test_webhook_event(
    payload: WebhookTestTriggerRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "SELLER"])),
):
    """Trigger a mock event to test webhook delivery endpoints."""
    deliveries = await trigger_event_webhooks(
        db,
        event_type=payload.event_type,
        payload_data={"test": True, "triggered_by": current_user.email},
    )
    await db.commit()
    return {
        "success": True,
        "deliveries_queued": len(deliveries),
        "event": payload.event_type.value,
    }
