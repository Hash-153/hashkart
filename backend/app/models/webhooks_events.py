import enum
from datetime import datetime, timezone
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.database import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class WebhookEventType(str, enum.Enum):
    ORDER_CREATED = "order.created"
    ORDER_PAID = "order.paid"
    ORDER_SHIPPED = "order.shipped"
    ORDER_DELIVERED = "order.delivered"
    ORDER_CANCELLED = "order.cancelled"
    RETURN_REQUESTED = "return.requested"
    RETURN_COMPLETED = "return.completed"
    INVENTORY_LOW = "inventory.low"
    SETTLEMENT_PROCESSED = "settlement.processed"
    SELLER_APPROVED = "seller.approved"


class WebhookDeliveryStatus(str, enum.Enum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED_RETRYING = "FAILED_RETRYING"
    DEAD_LETTER = "DEAD_LETTER"


class WebhookSubscription(Base):
    __tablename__ = "webhook_subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("seller_profiles.id", ondelete="CASCADE"), nullable=True, index=True)
    endpoint_url = Column(String(500), nullable=False)
    secret_key = Column(String(100), nullable=False)  # For HMAC-SHA256 signing
    subscribed_events_json = Column(Text, nullable=False)  # JSON array of WebhookEventType strings
    is_active = Column(Boolean, nullable=False, default=True)
    description = Column(String(255), nullable=True)
    consecutive_failures = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    deliveries = relationship("WebhookDeliveryAttempt", back_populates="subscription", cascade="all, delete-orphan")


class WebhookDeliveryAttempt(Base):
    __tablename__ = "webhook_delivery_attempts"

    id = Column(Integer, primary_key=True, index=True)
    subscription_id = Column(Integer, ForeignKey("webhook_subscriptions.id", ondelete="CASCADE"), nullable=False, index=True)
    event_type = Column(SQLEnum(WebhookEventType), nullable=False, index=True)
    payload_json = Column(Text, nullable=False)
    signature = Column(String(100), nullable=False)
    attempt_number = Column(Integer, nullable=False, default=1)
    status = Column(SQLEnum(WebhookDeliveryStatus), nullable=False, default=WebhookDeliveryStatus.PENDING, index=True)
    http_status_code = Column(Integer, nullable=True)
    response_body = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)
    next_retry_at = Column(DateTime(timezone=True), nullable=True)
    delivered_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    subscription = relationship("WebhookSubscription", back_populates="deliveries")

    __table_args__ = (
        Index("ix_webhook_retry_status", "status", "next_retry_at"),
    )


class ProductComparisonList(Base):
    """User comparison bucket for comparing 2-4 products side-by-side."""
    __tablename__ = "product_comparison_lists"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True, index=True)
    session_id = Column(String(100), nullable=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False, index=True)
    product_ids_json = Column(Text, nullable=False)  # JSON array of product IDs [1, 5, 8]
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)
