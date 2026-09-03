from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class SellerOnboardingCreate(BaseModel):
    business_name: str = Field(min_length=2, max_length=160)
    legal_name: str = Field(min_length=2, max_length=160)
    tax_identifier: str = Field(min_length=5, max_length=80)
    phone: str = Field(min_length=7, max_length=30)


class SellerProfileResponse(SellerOnboardingCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    status: str
    rejection_reason: Optional[str] = None
    approved_at: Optional[datetime] = None
    created_at: datetime


class SellerListingCreate(BaseModel):
    product_id: int = Field(gt=0)
    variant_id: int = Field(gt=0)
    seller_sku: str = Field(min_length=2, max_length=100)
    selling_price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    available_quantity: int = Field(ge=0, le=1_000_000)


class SellerListingResponse(SellerListingCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    seller_id: int
    status: str
    created_at: datetime
    updated_at: datetime


class SellerApprovalRequest(BaseModel):
    status: str = Field(pattern="^(APPROVED|REJECTED)$")
    rejection_reason: Optional[str] = Field(default=None, max_length=500)
