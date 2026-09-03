from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

from app.models.settlement import (
    CommissionTierType,
    LedgerEntryType,
    SettlementStatus,
)


class CommissionRateBase(BaseModel):
    category_id: Optional[int] = None
    seller_id: Optional[int] = None
    tier_name: str = "STANDARD"
    commission_type: CommissionTierType = CommissionTierType.PERCENTAGE
    base_percentage: Decimal = Field(default=Decimal("5.00"), ge=0, le=100)
    fixed_fee: Decimal = Field(default=Decimal("0.00"), ge=0)
    min_commission: Decimal = Field(default=Decimal("10.00"), ge=0)
    max_commission: Optional[Decimal] = None
    is_active: bool = True


class CommissionRateCreate(CommissionRateBase):
    pass


class CommissionRateResponse(CommissionRateBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class EscrowAccountResponse(BaseModel):
    id: int
    seller_id: int
    available_balance: Decimal
    held_balance: Decimal
    pending_payout_balance: Decimal
    total_lifetime_settled: Decimal
    currency: str
    is_locked: bool
    lock_reason: Optional[str]
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)


class LedgerEntryResponse(BaseModel):
    id: int
    escrow_account_id: int
    seller_id: int
    order_id: Optional[int]
    order_item_id: Optional[int]
    payout_batch_id: Optional[int]
    entry_type: LedgerEntryType
    gross_amount: Decimal
    net_amount: Decimal
    fee_deductions: Decimal
    tax_deductions: Decimal
    running_balance: Decimal
    currency: str
    reference_number: str
    description: Optional[str]
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class PayoutBatchCreate(BaseModel):
    seller_id: int
    payout_method: str = "NEFT"
    scheduled_date: Optional[datetime] = None


class PayoutItemResponse(BaseModel):
    id: int
    batch_id: int
    order_id: int
    order_number: str
    item_gross_amount: Decimal
    commission_amount: Decimal
    shipping_charge_deducted: Decimal
    gst_tds_amount: Decimal
    tcs_amount: Decimal
    net_seller_credit: Decimal
    is_settled: bool
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class PayoutBatchResponse(BaseModel):
    id: int
    batch_reference: str
    seller_id: int
    status: SettlementStatus
    gross_payout: Decimal
    total_deductions: Decimal
    net_payout: Decimal
    payout_method: str
    bank_account_last4: Optional[str]
    bank_ifsc_code: Optional[str]
    gateway_transaction_id: Optional[str]
    failure_reason: Optional[str]
    scheduled_date: datetime
    settled_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    items: List[PayoutItemResponse] = []
    model_config = ConfigDict(from_attributes=True)


class SellerSettlementSummary(BaseModel):
    seller_id: int
    available_balance: Decimal
    held_balance: Decimal
    pending_payout_balance: Decimal
    total_lifetime_settled: Decimal
    total_orders_settled: int
    total_commission_paid: Decimal
    total_tax_withheld: Decimal
    recent_batches: List[PayoutBatchResponse] = []
