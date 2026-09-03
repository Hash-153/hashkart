import enum
from datetime import datetime, timezone
from decimal import Decimal
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
)

from app.database import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class RiskLevel(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL_BLOCK = "CRITICAL_BLOCK"


class FraudFlagType(str, enum.Enum):
    HIGH_COD_VELOCITY = "HIGH_COD_VELOCITY"
    MULTIPLE_ACCOUNTS_SAME_DEVICE = "MULTIPLE_ACCOUNTS_SAME_DEVICE"
    PROMO_ABUSE = "PROMO_ABUSE"
    SUSPICIOUS_ADDRESS = "SUSPICIOUS_ADDRESS"
    HIGH_RTO_HISTORY = "HIGH_RTO_HISTORY"
    CARD_CHARGEBACK_HISTORY = "CARD_CHARGEBACK_HISTORY"
    RAPID_ORDER_CANCELLATION = "RAPID_ORDER_CANCELLATION"


class OrderRiskScore(Base):
    __tablename__ = "order_risk_scores"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    risk_score = Column(Integer, nullable=False, default=0)  # 0 to 100
    risk_level = Column(SQLEnum(RiskLevel), nullable=False, default=RiskLevel.LOW, index=True)
    is_cod_restricted = Column(Boolean, nullable=False, default=False)
    requires_manual_verification = Column(Boolean, nullable=False, default=False)
    ip_address = Column(String(50), nullable=True)
    device_fingerprint = Column(String(100), nullable=True, index=True)
    risk_factors_json = Column(Text, nullable=True)  # Detailed JSON evaluation breakdown
    decision_action = Column(String(50), nullable=False, default="APPROVED")  # APPROVED, FLAGGED, BLOCKED
    reviewed_by_admin_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    reviewed_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    __table_args__ = (
        Index("ix_risk_level_created", "risk_level", "created_at"),
    )


class BlacklistRegistry(Base):
    __tablename__ = "blacklist_registries"

    id = Column(Integer, primary_key=True, index=True)
    entity_type = Column(String(50), nullable=False, index=True)  # PHONE, EMAIL, IP_ADDRESS, DEVICE_ID, PINCODE
    entity_value = Column(String(255), nullable=False, index=True)
    reason = Column(SQLEnum(FraudFlagType), nullable=False)
    notes = Column(Text, nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_by_user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    expires_at = Column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        Index("ix_blacklist_lookup", "entity_type", "entity_value", "is_active"),
    )


class UserSecurityMetric(Base):
    __tablename__ = "user_security_metrics"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    total_orders_count = Column(Integer, nullable=False, default=0)
    total_cod_orders_count = Column(Integer, nullable=False, default=0)
    total_rto_orders_count = Column(Integer, nullable=False, default=0)  # Return to origin
    total_returns_count = Column(Integer, nullable=False, default=0)
    total_refund_amount = Column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    account_trust_score = Column(Integer, nullable=False, default=85)  # 0 to 100
    is_trusted_buyer = Column(Boolean, nullable=False, default=True)
    last_evaluated_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
