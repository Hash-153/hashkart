from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SupportTicketCreate(BaseModel):
    subject: str = Field(min_length=4, max_length=180)
    category: str = Field(min_length=3, max_length=40)
    description: str = Field(min_length=10, max_length=5000)
    order_id: Optional[int] = Field(default=None, gt=0)
    priority: str = Field(default="NORMAL", pattern="^(LOW|NORMAL|HIGH|URGENT)$")


class SupportTicketResponse(SupportTicketCreate):
    id: int
    ticket_number: str
    customer_id: int
    status: str
    assigned_to: Optional[int]
    first_response_at: Optional[datetime]
    resolved_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime


class SupportMessageCreate(BaseModel):
    body: str = Field(min_length=1, max_length=5000)


class SupportMessageResponse(SupportMessageCreate):
    id: int
    ticket_id: int
    author_id: int
    created_at: datetime


class SupportStatusUpdate(BaseModel):
    status: str = Field(pattern="^(OPEN|IN_PROGRESS|WAITING_CUSTOMER|RESOLVED|CLOSED)$")
    assigned_to: Optional[int] = Field(default=None, gt=0)
