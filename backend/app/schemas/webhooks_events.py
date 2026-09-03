from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, HttpUrl

from app.models.webhooks_events import WebhookDeliveryStatus, WebhookEventType


class WebhookSubscriptionCreate(BaseModel):
    endpoint_url: str
    subscribed_events: List[WebhookEventType]
    description: Optional[str] = None


class WebhookSubscriptionResponse(BaseModel):
    id: int
    seller_id: Optional[int]
    endpoint_url: str
    secret_key: str
    subscribed_events: List[WebhookEventType]
    is_active: bool
    description: Optional[str]
    consecutive_failures: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class WebhookDeliveryResponse(BaseModel):
    id: int
    subscription_id: int
    event_type: WebhookEventType
    payload_json: str
    signature: str
    attempt_number: int
    status: WebhookDeliveryStatus
    http_status_code: Optional[int]
    response_body: Optional[str]
    error_message: Optional[str]
    next_retry_at: Optional[datetime]
    delivered_at: Optional[datetime]
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class WebhookTestTriggerRequest(BaseModel):
    event_type: WebhookEventType
