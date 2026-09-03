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
from sqlalchemy.orm import relationship

from app.database import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class SettlementStatus(str, enum.Enum):
    PENDING = "PENDING"
    ON_HOLD = "ON_HOLD"
    ELIGIBLE = "ELIGIBLE"
    PROCESSING = "PROCESSING"
    SETTLED = "SETTLED"
    REVERSED = "REVERSED"
    FAILED = "FAILED"


class LedgerEntryType(str, enum.Enum):
    SALE_CREDIT = "SALE_CREDIT"
    COMMISSION_DEBIT = "COMMISSION_DEBIT"
    PAYMENT_GATEWAY_FEE = "PAYMENT_GATEWAY_FEE"
    LOGISTICS_FEE = "LOGISTICS_FEE"
    GST_TAX_TDS = "GST_TAX_TDS"
    TCS_WITHHOLDING = "TCS_WITHHOLDING"
    REFUND_CLAWBACK = "REFUND_CLAWBACK"
    PENALTY = "PENALTY"
    PAYOUT_TRANSFER = "PAYOUT_TRANSFER"
    ADJUSTMENT = "ADJUSTMENT"


class CommissionTierType(str, enum.Enum):
    PERCENTAGE = "PERCENTAGE"
    FIXED = "FIXED"
    HYBRID = "HYBRID"
    TIERED_SLAB = "TIERED_SLAB"


class SellerCommissionRate(Base):
    __tablename__ = "seller_commission_rates"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=True, index=True)
    seller_id = Column(Integer, ForeignKey("seller_profiles.id", ondelete="CASCADE"), nullable=True, index=True)
    tier_name = Column(String(100), nullable=False, default="STANDARD")
    commission_type = Column(SQLEnum(CommissionTierType), nullable=False, default=CommissionTierType.PERCENTAGE)
    base_percentage = Column(Numeric(5, 2), nullable=False, default=Decimal("5.00"))
    fixed_fee = Column(Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    min_commission = Column(Numeric(10, 2), nullable=False, default=Decimal("10.00"))
    max_commission = Column(Numeric(10, 2), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    __table_args__ = (
        Index("ix_commission_lookup", "category_id", "seller_id", "is_active"),
    )


class SellerEscrowAccount(Base):
    __tablename__ = "seller_escrow_accounts"

    id = Column(Integer, primary_key=True, index=True)
    seller_id = Column(Integer, ForeignKey("seller_profiles.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    available_balance = Column(Numeric(14, 2), nullable=False, default=Decimal("0.00"))
    held_balance = Column(Numeric(14, 2), nullable=False, default=Decimal("0.00"))
    pending_payout_balance = Column(Numeric(14, 2), nullable=False, default=Decimal("0.00"))
    total_lifetime_settled = Column(Numeric(14, 2), nullable=False, default=Decimal("0.00"))
    currency = Column(String(3), nullable=False, default="INR")
    is_locked = Column(Boolean, nullable=False, default=False)
    lock_reason = Column(String(255), nullable=True)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    seller = relationship("SellerProfile", backref="escrow_account")
    ledger_entries = relationship("SellerFinancialLedger", back_populates="escrow_account", cascade="all, delete-orphan")


class SellerFinancialLedger(Base):
    __tablename__ = "seller_financial_ledgers"

    id = Column(Integer, primary_key=True, index=True)
    escrow_account_id = Column(Integer, ForeignKey("seller_escrow_accounts.id", ondelete="CASCADE"), nullable=False, index=True)
    seller_id = Column(Integer, ForeignKey("seller_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="SET NULL"), nullable=True, index=True)
    order_item_id = Column(Integer, nullable=True, index=True)
    payout_batch_id = Column(Integer, ForeignKey("seller_payout_batches.id", ondelete="SET NULL"), nullable=True, index=True)
    entry_type = Column(SQLEnum(LedgerEntryType), nullable=False, index=True)
    gross_amount = Column(Numeric(14, 2), nullable=False)
    net_amount = Column(Numeric(14, 2), nullable=False)
    fee_deductions = Column(Numeric(14, 2), nullable=False, default=Decimal("0.00"))
    tax_deductions = Column(Numeric(14, 2), nullable=False, default=Decimal("0.00"))
    running_balance = Column(Numeric(14, 2), nullable=False)
    currency = Column(String(3), nullable=False, default="INR")
    reference_number = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    escrow_account = relationship("SellerEscrowAccount", back_populates="ledger_entries")
    payout_batch = relationship("SellerPayoutBatch", back_populates="ledger_entries")

    __table_args__ = (
        Index("ix_ledger_seller_created", "seller_id", "created_at"),
        Index("ix_ledger_type_created", "entry_type", "created_at"),
    )


class SellerPayoutBatch(Base):
    __tablename__ = "seller_payout_batches"

    id = Column(Integer, primary_key=True, index=True)
    batch_reference = Column(String(100), unique=True, index=True, nullable=False)
    seller_id = Column(Integer, ForeignKey("seller_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    status = Column(SQLEnum(SettlementStatus), nullable=False, default=SettlementStatus.PENDING, index=True)
    gross_payout = Column(Numeric(14, 2), nullable=False)
    total_deductions = Column(Numeric(14, 2), nullable=False, default=Decimal("0.00"))
    net_payout = Column(Numeric(14, 2), nullable=False)
    payout_method = Column(String(50), nullable=False, default="NEFT")  # NEFT, RTGS, IMPS, UPI
    bank_account_last4 = Column(String(4), nullable=True)
    bank_ifsc_code = Column(String(20), nullable=True)
    gateway_transaction_id = Column(String(100), nullable=True)
    failure_reason = Column(Text, nullable=True)
    processed_by_admin_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    scheduled_date = Column(DateTime(timezone=True), nullable=False)
    settled_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    ledger_entries = relationship("SellerFinancialLedger", back_populates="payout_batch")
    items = relationship("SellerPayoutItem", back_populates="batch", cascade="all, delete-orphan")


class SellerPayoutItem(Base):
    __tablename__ = "seller_payout_items"

    id = Column(Integer, primary_key=True, index=True)
    batch_id = Column(Integer, ForeignKey("seller_payout_batches.id", ondelete="CASCADE"), nullable=False, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    order_number = Column(String(50), nullable=False)
    item_gross_amount = Column(Numeric(12, 2), nullable=False)
    commission_amount = Column(Numeric(12, 2), nullable=False)
    shipping_charge_deducted = Column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    gst_tds_amount = Column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    tcs_amount = Column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    net_seller_credit = Column(Numeric(12, 2), nullable=False)
    is_settled = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    batch = relationship("SellerPayoutBatch", back_populates="items")
