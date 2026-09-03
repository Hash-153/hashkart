from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ShipmentDispatchRequest(BaseModel):
    order_number: str = Field(min_length=3, max_length=50)
    postal_code: str = Field(min_length=4, max_length=12)


class ShipmentDispatchResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    tracking_number: str
    carrier_name: str
    shipment_status: str
    shipped_at: Optional[datetime]
    estimated_delivery: Optional[datetime]


class FulfillmentTaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_id: int
    shipment_id: Optional[int]
    task_type: str
    status: str
    assigned_to: Optional[int]
    notes: Optional[str]
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    created_at: datetime


class FulfillmentTaskTransition(BaseModel):
    status: str = Field(pattern="^(OPEN|IN_PROGRESS|COMPLETED|CANCELLED)$")
    notes: Optional[str] = Field(default=None, max_length=500)
