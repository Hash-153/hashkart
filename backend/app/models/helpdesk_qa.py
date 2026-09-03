import enum
from datetime import datetime, timezone
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.database import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class TicketPriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"


class TicketCategory(str, enum.Enum):
    ORDER_STATUS = "ORDER_STATUS"
    CANCELLATION_REFUND = "CANCELLATION_REFUND"
    RETURN_REPLACEMENT = "RETURN_REPLACEMENT"
    PAYMENT_FAILURE = "PAYMENT_FAILURE"
    DEFECTIVE_PRODUCT = "DEFECTIVE_PRODUCT"
    ACCOUNT_SECURITY = "ACCOUNT_SECURITY"
    GENERAL_INQUIRY = "GENERAL_INQUIRY"


class TicketStatus(str, enum.Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    WAITING_FOR_CUSTOMER = "WAITING_FOR_CUSTOMER"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"


class HelpdeskTicket(Base):
    __tablename__ = "helpdesk_tickets"

    id = Column(Integer, primary_key=True, index=True)
    ticket_number = Column(String(50), unique=True, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="SET NULL"), nullable=True, index=True)
    category = Column(SQLEnum(TicketCategory), nullable=False, default=TicketCategory.GENERAL_INQUIRY, index=True)
    priority = Column(SQLEnum(TicketPriority), nullable=False, default=TicketPriority.MEDIUM, index=True)
    status = Column(SQLEnum(TicketStatus), nullable=False, default=TicketStatus.OPEN, index=True)
    subject = Column(String(200), nullable=False)
    assigned_agent_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    sla_target_hours = Column(Integer, nullable=False, default=24)
    sla_due_at = Column(DateTime(timezone=True), nullable=False)
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    satisfaction_rating = Column(Integer, nullable=True)  # 1 to 5 stars
    customer_feedback = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    messages = relationship("HelpdeskTicketMessage", back_populates="ticket", cascade="all, delete-orphan")
    user = relationship("User", foreign_keys=[user_id])
    assigned_agent = relationship("User", foreign_keys=[assigned_agent_id])

    __table_args__ = (
        Index("ix_helpdesk_ticket_status_priority", "status", "priority", "sla_due_at"),
    )


class HelpdeskTicketMessage(Base):
    __tablename__ = "helpdesk_ticket_messages"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("helpdesk_tickets.id", ondelete="CASCADE"), nullable=False, index=True)
    sender_user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    is_staff_reply = Column(Boolean, nullable=False, default=False)
    message_text = Column(Text, nullable=False)
    attachment_urls_json = Column(Text, nullable=True)  # JSON array of URLs
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    ticket = relationship("HelpdeskTicket", back_populates="messages")
    sender = relationship("User")


class ProductQuestion(Base):
    """Customer Q&A threads on Product Detail Page."""
    __tablename__ = "product_questions"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    question_text = Column(String(500), nullable=False)
    is_approved = Column(Boolean, nullable=False, default=True)
    upvote_count = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    answers = relationship("ProductAnswer", back_populates="question", cascade="all, delete-orphan")
    product = relationship("Product")
    user = relationship("User")


class ProductAnswer(Base):
    __tablename__ = "product_answers"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("product_questions.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    answer_text = Column(Text, nullable=False)
    is_seller_answer = Column(Boolean, nullable=False, default=False)
    is_verified_buyer = Column(Boolean, nullable=False, default=False)
    is_approved = Column(Boolean, nullable=False, default=True)
    upvote_count = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    question = relationship("ProductQuestion", back_populates="answers")
    user = relationship("User")
