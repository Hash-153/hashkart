from datetime import datetime
from decimal import Decimal
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class PaymentWebhookEvent(Base):
    """Idempotent record of a gateway webhook received from an external provider."""

    __tablename__ = "payment_webhook_events"
    __table_args__ = (UniqueConstraint("provider", "event_id", name="uq_payment_webhook_event"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    provider: Mapped[str] = mapped_column(String(40), nullable=False)
    event_id: Mapped[str] = mapped_column(String(160), nullable=False)
    event_type: Mapped[str] = mapped_column(String(60), nullable=False)
    transaction_reference: Mapped[Optional[str]] = mapped_column(String(120), index=True)
    payload: Mapped[str] = mapped_column(Text, nullable=False)
    signature_valid: Mapped[bool] = mapped_column(nullable=False)
    processed: Mapped[bool] = mapped_column(default=False, nullable=False, index=True)
    received_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    processed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class PaymentReconciliation(Base):
    """Daily gateway-to-order reconciliation result for finance operations."""

    __tablename__ = "payment_reconciliations"
    __table_args__ = (UniqueConstraint("provider", "settlement_reference", name="uq_payment_settlement"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    provider: Mapped[str] = mapped_column(String(40), nullable=False, index=True)
    settlement_reference: Mapped[str] = mapped_column(String(160), nullable=False)
    transaction_reference: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    expected_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    received_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2), nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    reconciled_by: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    reconciled_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
