from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


# Coupon Schemas
class CouponCreate(BaseModel):
    code: str = Field(..., min_length=3, max_length=50)
    discount_type: str = Field(..., description="PERCENTAGE, FIXED")
    discount_value: float = Field(..., gt=0)
    min_order_value: float = Field(default=0.0, ge=0)
    max_discount_amount: Optional[float] = Field(None, gt=0)
    usage_limit: Optional[int] = Field(None, ge=1)
    usage_per_user: int = Field(default=1, ge=1)
    valid_from: datetime
    valid_to: datetime
    is_active: bool = True


class CouponResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    code: str
    discount_type: str
    discount_value: float
    min_order_value: float
    max_discount_amount: Optional[float] = None
    usage_limit: Optional[int] = None
    usage_per_user: int
    times_used: int
    is_active: bool
    valid_from: datetime
    valid_to: datetime


class CouponValidateRequest(BaseModel):
    code: str
    cart_subtotal: float


class CouponValidateResponse(BaseModel):
    is_valid: bool
    message: str
    discount_amount: float = 0.0
    coupon: Optional[CouponResponse] = None


# Review Schemas
class ReviewCreate(BaseModel):
    product_id: int
    variant_id: Optional[int] = None
    rating: int = Field(..., ge=1, le=5)
    title: str = Field(..., min_length=2, max_length=150)
    comment: str = Field(..., min_length=10)


class ReviewResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    user_id: int
    variant_id: Optional[int] = None
    rating: int
    title: str
    comment: str
    is_verified_purchase: bool
    status: str
    created_at: datetime
    user_name: Optional[str] = None


class ReviewModerationUpdate(BaseModel):
    status: str = Field(..., description="APPROVED, REJECTED")
