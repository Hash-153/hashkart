from datetime import datetime
from typing import List, Optional, Any, Dict
from pydantic import BaseModel, ConfigDict, Field
from app.schemas.promotion_review import CouponResponse


class PreviewLineItem(BaseModel):
    variant_id: int
    product_name: str
    variant_title: str
    sku: str
    unit_price: float
    quantity: int
    line_total: float


class CheckoutPreviewResponse(BaseModel):
    address_id: int
    items: List[PreviewLineItem]
    subtotal: float
    promotion_discount: float
    coupon_discount: float
    total_discount: float
    tax: float
    shipping: float
    grand_total: float
    applied_promotions: List[Dict[str, Any]] = []
    coupon: Optional[CouponResponse] = None
    price_changes: List[str] = []
    stock_warnings: List[str] = []


class OrderRefundRequest(BaseModel):
    reason: str = Field(..., min_length=3, description="Reason for refund request")
    amount: Optional[float] = Field(None, gt=0, description="Optional custom refund amount")


class OrderRefundResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_id: int
    refund_reference: str
    amount: float
    reason: str
    refund_status: str
    created_at: datetime


class InventoryAdjustmentRequest(BaseModel):
    variant_id: int
    new_quantity: int = Field(..., ge=0)
    reason: str = Field(..., min_length=3)
