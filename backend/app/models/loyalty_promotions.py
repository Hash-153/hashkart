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


class LoyaltyTierLevel(str, enum.Enum):
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    VIP_PLUS = "VIP_PLUS"


class SuperCoinTransactionType(str, enum.Enum):
    EARNED_PURCHASE = "EARNED_PURCHASE"
    EARNED_PROMOTION = "EARNED_PROMOTION"
    EARNED_GAME = "EARNED_GAME"
    SPENT_CHECKOUT = "SPENT_CHECKOUT"
    SPENT_REWARD = "SPENT_REWARD"
    EXPIRED = "EXPIRED"
    REVERSED_RETURN = "REVERSED_RETURN"


class BankOfferType(str, enum.Enum):
    INSTANT_DISCOUNT_PERCENT = "INSTANT_DISCOUNT_PERCENT"
    FLAT_CASHBACK = "FLAT_CASHBACK"
    NO_COST_EMI = "NO_COST_EMI"
    STANDARD_EMI = "STANDARD_EMI"


class CardNetwork(str, enum.Enum):
    HDFC = "HDFC"
    ICICI = "ICICI"
    SBI = "SBI"
    AXIS = "AXIS"
    KOTAK = "KOTAK"
    ALL_BANKS = "ALL_BANKS"


class FlashSaleStatus(str, enum.Enum):
    SCHEDULED = "SCHEDULED"
    LIVE = "LIVE"
    ENDED = "ENDED"
    CANCELLED = "CANCELLED"


class UserLoyaltyProfile(Base):
    __tablename__ = "user_loyalty_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    tier = Column(SQLEnum(LoyaltyTierLevel), nullable=False, default=LoyaltyTierLevel.BRONZE)
    supercoin_balance = Column(Integer, nullable=False, default=0)
    lifetime_coins_earned = Column(Integer, nullable=False, default=0)
    lifetime_coins_spent = Column(Integer, nullable=False, default=0)
    tier_points = Column(Integer, nullable=False, default=0)
    is_flipkart_plus_member = Column(Boolean, nullable=False, default=False)
    plus_membership_expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    transactions = relationship("SuperCoinTransaction", back_populates="profile", cascade="all, delete-orphan")


class SuperCoinTransaction(Base):
    __tablename__ = "supercoin_transactions"

    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("user_loyalty_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="SET NULL"), nullable=True, index=True)
    transaction_type = Column(SQLEnum(SuperCoinTransactionType), nullable=False, index=True)
    coins = Column(Integer, nullable=False)
    running_balance = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    reference_id = Column(String(100), nullable=True, index=True)
    expires_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    profile = relationship("UserLoyaltyProfile", back_populates="transactions")

    __table_args__ = (
        Index("ix_coins_user_created", "user_id", "created_at"),
    )


class BankDiscountOffer(Base):
    __tablename__ = "bank_discount_offers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    bank_code = Column(SQLEnum(CardNetwork), nullable=False, index=True)
    offer_type = Column(SQLEnum(BankOfferType), nullable=False, default=BankOfferType.INSTANT_DISCOUNT_PERCENT)
    card_type = Column(String(50), nullable=False, default="CREDIT_CARD")  # CREDIT_CARD, DEBIT_CARD, EMI
    discount_percentage = Column(Numeric(5, 2), nullable=True)
    flat_discount_amount = Column(Numeric(10, 2), nullable=True)
    min_order_value = Column(Numeric(10, 2), nullable=False, default=Decimal("2000.00"))
    max_discount_cap = Column(Numeric(10, 2), nullable=True, default=Decimal("1500.00"))
    applicable_category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)
    applicable_brand_id = Column(Integer, ForeignKey("brands.id", ondelete="SET NULL"), nullable=True)
    terms_and_conditions = Column(Text, nullable=True)
    starts_at = Column(DateTime(timezone=True), nullable=False)
    ends_at = Column(DateTime(timezone=True), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    __table_args__ = (
        Index("ix_bank_offer_active_dates", "bank_code", "is_active", "starts_at", "ends_at"),
    )


class FlashSaleEvent(Base):
    __tablename__ = "flash_sale_events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    slug = Column(String(200), unique=True, index=True, nullable=False)
    banner_image_url = Column(String(500), nullable=True)
    status = Column(SQLEnum(FlashSaleStatus), nullable=False, default=FlashSaleStatus.SCHEDULED, index=True)
    starts_at = Column(DateTime(timezone=True), nullable=False, index=True)
    ends_at = Column(DateTime(timezone=True), nullable=False, index=True)
    vip_early_access_minutes = Column(Integer, nullable=False, default=30)  # Plus members get early access
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    items = relationship("FlashSaleItem", back_populates="event", cascade="all, delete-orphan")


class FlashSaleItem(Base):
    __tablename__ = "flash_sale_items"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("flash_sale_events.id", ondelete="CASCADE"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    variant_id = Column(Integer, ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=True)
    flash_price = Column(Numeric(10, 2), nullable=False)
    regular_price = Column(Numeric(10, 2), nullable=False)
    allocated_stock_units = Column(Integer, nullable=False)
    claimed_units = Column(Integer, nullable=False, default=0)
    max_units_per_user = Column(Integer, nullable=False, default=1)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    event = relationship("FlashSaleEvent", back_populates="items")
    product = relationship("Product")
