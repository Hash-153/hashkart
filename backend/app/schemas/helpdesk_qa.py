from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

from app.models.helpdesk_qa import TicketCategory, TicketPriority, TicketStatus


class TicketMessageCreate(BaseModel):
    message_text: str = Field(..., min_length=1)
    attachment_urls: List[str] = []


class TicketMessageResponse(BaseModel):
    id: int
    ticket_id: int
    sender_user_id: int
    sender_name: Optional[str] = None
    is_staff_reply: bool
    message_text: str
    attachment_urls: List[str] = []
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class TicketCreate(BaseModel):
    subject: str = Field(..., min_length=5, max_length=200)
    category: TicketCategory = TicketCategory.GENERAL_INQUIRY
    priority: TicketPriority = TicketPriority.MEDIUM
    order_id: Optional[int] = None
    initial_message: str = Field(..., min_length=5)
    attachment_urls: List[str] = []


class TicketResponse(BaseModel):
    id: int
    ticket_number: str
    user_id: int
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    order_id: Optional[int]
    category: TicketCategory
    priority: TicketPriority
    status: TicketStatus
    subject: str
    assigned_agent_id: Optional[int]
    assigned_agent_name: Optional[str] = None
    sla_target_hours: int
    sla_due_at: datetime
    is_sla_breached: bool = False
    resolved_at: Optional[datetime]
    satisfaction_rating: Optional[int]
    customer_feedback: Optional[str]
    created_at: datetime
    updated_at: datetime
    messages: List[TicketMessageResponse] = []
    model_config = ConfigDict(from_attributes=True)


class ProductQuestionCreate(BaseModel):
    question_text: str = Field(..., min_length=5, max_length=500)


class ProductAnswerCreate(BaseModel):
    answer_text: str = Field(..., min_length=3)


class ProductAnswerResponse(BaseModel):
    id: int
    question_id: int
    user_id: int
    author_name: str = "Shopper"
    is_seller_answer: bool
    is_verified_buyer: bool
    answer_text: str
    upvote_count: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class ProductQuestionResponse(BaseModel):
    id: int
    product_id: int
    user_id: int
    author_name: str = "Shopper"
    question_text: str
    upvote_count: int
    created_at: datetime
    answers: List[ProductAnswerResponse] = []
    model_config = ConfigDict(from_attributes=True)
