from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

from app.models.loyalty_promotions import (
    BankOfferType,
    CardNetwork,
    FlashSaleStatus,
    LoyaltyTierLevel,
    SuperCoinTransactionType,
)


class SuperCoinTransactionResponse(BaseModel):
    id: int
    user_id: int
    order_id: Optional[int]
    transaction_type: SuperCoinTransactionType
    coins: int
    running_balance: int
    description: str
    reference_id: Optional[str]
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class UserLoyaltyProfileResponse(BaseModel):
    id: int
    user_id: int
    tier: LoyaltyTierLevel
    supercoin_balance: int
    lifetime_coins_earned: int
    lifetime_coins_spent: int
    tier_points: int
    is_flipkart_plus_member: bool
    plus_membership_expires_at: Optional[datetime]
    recent_transactions: List[SuperCoinTransactionResponse] = []
    model_config = ConfigDict(from_attributes=True)


class SuperCoinRedemptionQuoteRequest(BaseModel):
    cart_total: Decimal
    requested_coins: int


class SuperCoinRedemptionQuoteResponse(BaseModel):
    requested_coins: int
    usable_coins: int
    coin_discount_value_inr: Decimal
    remaining_payable_inr: Decimal
    conversion_rate: Decimal = Decimal("1.00")  # 1 coin = 1 INR discount


class BankOfferBase(BaseModel):
    title: str
    bank_code: CardNetwork
    offer_type: BankOfferType = BankOfferType.INSTANT_DISCOUNT_PERCENT
    card_type: str = "CREDIT_CARD"
    discount_percentage: Optional[Decimal] = None
    flat_discount_amount: Optional[Decimal] = None
    min_order_value: Decimal = Field(default=Decimal("2000.00"), ge=0)
    max_discount_cap: Optional[Decimal] = Field(default=Decimal("1500.00"))
    applicable_category_id: Optional[int] = None
    applicable_brand_id: Optional[int] = None
    terms_and_conditions: Optional[str] = None
    starts_at: datetime
    ends_at: datetime
    is_active: bool = True


class BankOfferCreate(BankOfferBase):
    pass


class BankOfferResponse(BankOfferBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class FlashSaleItemResponse(BaseModel):
    id: int
    event_id: int
    product_id: int
    product_name: Optional[str] = None
    product_slug: Optional[str] = None
    product_image: Optional[str] = None
    flash_price: Decimal
    regular_price: Decimal
    discount_percentage: int
    allocated_stock_units: int
    claimed_units: int
    claimed_percentage: int
    max_units_per_user: int
    is_active: bool
    model_config = ConfigDict(from_attributes=True)


class FlashSaleEventResponse(BaseModel):
    id: int
    title: str
    slug: str
    banner_image_url: Optional[str]
    status: FlashSaleStatus
    starts_at: datetime
    ends_at: datetime
    vip_early_access_minutes: int
    description: Optional[str]
    is_live_now: bool
    seconds_remaining: int
    items: List[FlashSaleItemResponse] = []
    model_config = ConfigDict(from_attributes=True)


class FlashSaleReserveRequest(BaseModel):
    event_id: int
    product_id: int
    variant_id: Optional[int] = None
    quantity: int = Field(default=1, ge=1, le=2)
