from datetime import datetime
from decimal import Decimal
from typing import Any, Optional

from pydantic import BaseModel, Field


class PaymentWebhookPayload(BaseModel):
    event_id: str = Field(min_length=4, max_length=160)
    event_type: str = Field(min_length=3, max_length=60)
    transaction_reference: Optional[str] = Field(default=None, max_length=120)
    status: Optional[str] = Field(default=None, max_length=30)
    amount: Optional[Decimal] = Field(default=None, ge=0, max_digits=12, decimal_places=2)
    data: dict[str, Any] = Field(default_factory=dict)


class PaymentWebhookResponse(BaseModel):
    accepted: bool
    duplicate: bool = False
    event_id: str
    processed: bool


class ReconciliationCreate(BaseModel):
    provider: str = Field(min_length=2, max_length=40)
    settlement_reference: str = Field(min_length=3, max_length=160)
    transaction_reference: str = Field(min_length=3, max_length=120)
    expected_amount: Decimal = Field(ge=0, max_digits=12, decimal_places=2)
    received_amount: Decimal = Field(ge=0, max_digits=12, decimal_places=2)
    notes: Optional[str] = Field(default=None, max_length=1000)


class ReconciliationResponse(ReconciliationCreate):
    id: int
    status: str
    reconciled_by: Optional[int]
    reconciled_at: datetime
