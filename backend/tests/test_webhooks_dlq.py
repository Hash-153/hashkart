import json
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.webhooks_events import (
    WebhookDeliveryStatus,
    WebhookEventType,
    WebhookSubscription,
)
from app.services.webhook_dispatcher import (
    compute_hmac_signature,
    record_delivery_result,
    trigger_event_webhooks,
)


@pytest.mark.asyncio
async def test_webhook_dispatch_and_dlq(db_session: AsyncSession):
    """Test webhook payload HMAC signing, retry increments, and Dead-Letter Queue (DLQ)."""
    sub = WebhookSubscription(
        endpoint_url="https://api.sellerpartner.com/webhooks/orders",
        secret_key="top_secret_hmac_key",
        subscribed_events_json=json.dumps([WebhookEventType.ORDER_CREATED.value]),
        is_active=True,
    )
    db_session.add(sub)
    await db_session.flush()

    deliveries = await trigger_event_webhooks(
        db_session,
        event_type=WebhookEventType.ORDER_CREATED,
        payload_data={"order_id": 999, "amount": "4999.00"},
    )
    assert len(deliveries) == 1
    d = deliveries[0]
    assert d.event_type == WebhookEventType.ORDER_CREATED
    assert d.status == WebhookDeliveryStatus.PENDING
    assert len(d.signature) == 64  # SHA256 hex string

    # Simulate 3 consecutive failed delivery attempts
    await record_delivery_result(db_session, d.id, success=False, http_status=500, error_msg="Server timeout")
    assert d.attempt_number == 2
    assert d.status == WebhookDeliveryStatus.FAILED_RETRYING

    await record_delivery_result(db_session, d.id, success=False, http_status=502, error_msg="Bad gateway")
    assert d.attempt_number == 3

    await record_delivery_result(db_session, d.id, success=False, http_status=504, error_msg="Gateway timeout")
    assert d.status == WebhookDeliveryStatus.DEAD_LETTER
