from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class WarehouseCreate(BaseModel):
    code: str = Field(min_length=2, max_length=30)
    name: str = Field(min_length=2, max_length=120)
    city: str = Field(min_length=2, max_length=80)
    state: str = Field(min_length=2, max_length=80)
    postal_code: str = Field(min_length=4, max_length=12)


class WarehouseResponse(WarehouseCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_active: bool
    created_at: datetime


class StockMovementCreate(BaseModel):
    warehouse_stock_id: int = Field(gt=0)
    movement_type: str = Field(pattern="^(RESTOCK|RESERVE|RELEASE|DAMAGE|RETURN)$")
    quantity: int = Field(gt=0, le=1_000_000)
    idempotency_key: str = Field(min_length=8, max_length=120)
    reference_id: Optional[str] = Field(default=None, max_length=100)
    note: Optional[str] = Field(default=None, max_length=500)


class SellerPayoutCreate(BaseModel):
    amount: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    idempotency_key: str = Field(min_length=8, max_length=120)


class SellerPayoutResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    seller_id: int
    amount: Decimal
    currency: str
    status: str
    provider_reference: Optional[str]
    failure_reason: Optional[str]
    requested_at: datetime
    processed_at: Optional[datetime]
