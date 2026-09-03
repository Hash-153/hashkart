from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ShipmentEventCreate(BaseModel):
    event_code: str = Field(min_length=2, max_length=40)
    status: str = Field(min_length=2, max_length=50)
    location: Optional[str] = Field(default=None, max_length=160)
    description: Optional[str] = Field(default=None, max_length=500)
    occurred_at: Optional[datetime] = None


class ShipmentEventResponse(ShipmentEventCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    shipment_id: int
    created_at: datetime


class ReturnRequestCreate(BaseModel):
    order_item_id: int = Field(gt=0)
    quantity: int = Field(gt=0)
    reason: str = Field(min_length=3, max_length=80)
    customer_note: Optional[str] = Field(default=None, max_length=1000)


class ReturnRequestDecision(BaseModel):
    status: str = Field(pattern="^(APPROVED|REJECTED|RECEIVED|COMPLETED)$")
    resolution: Optional[str] = Field(default=None, max_length=30)


class ReturnRequestResponse(ReturnRequestCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    status: str
    resolution: Optional[str]
    reviewed_by: Optional[int]
    reviewed_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
