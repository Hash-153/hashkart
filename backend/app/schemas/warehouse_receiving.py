from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class WarehouseReceiptCreate(BaseModel):
    warehouse_id: int = Field(gt=0)
    supplier_name: str = Field(min_length=2, max_length=160)
    purchase_reference: str = Field(min_length=3, max_length=100)
    notes: Optional[str] = Field(default=None, max_length=1000)


class WarehouseReceiptResponse(WarehouseReceiptCreate):
    id: int
    status: str
    received_by: Optional[int]
    received_at: Optional[datetime]
    created_at: datetime


class WarehouseInspectionCreate(BaseModel):
    receipt_id: int = Field(gt=0)
    variant_id: int = Field(gt=0)
    expected_quantity: int = Field(gt=0)
    accepted_quantity: int = Field(ge=0)
    rejected_quantity: int = Field(ge=0)
    condition: str = Field(pattern="^(GOOD|DAMAGED|MIXED|EXPIRED)$")
    notes: Optional[str] = Field(default=None, max_length=1000)


class WarehouseInspectionResponse(WarehouseInspectionCreate):
    id: int
    inspected_by: Optional[int]
    inspected_at: Optional[datetime]
