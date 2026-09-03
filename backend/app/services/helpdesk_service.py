import json
import uuid
from datetime import datetime, timedelta, timezone
from typing import List, Optional, Tuple
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.helpdesk_qa import (
    HelpdeskTicket,
    HelpdeskTicketMessage,
    TicketCategory,
    TicketPriority,
    TicketStatus,
)
from app.models.user import User
from app.schemas.helpdesk_qa import TicketCreate, TicketMessageCreate


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


SLA_HOURS_MAP = {
    TicketPriority.URGENT: 4,
    TicketPriority.HIGH: 12,
    TicketPriority.MEDIUM: 24,
    TicketPriority.LOW: 48,
}


async def create_support_ticket(
    db: AsyncSession, user_id: int, payload: TicketCreate
) -> HelpdeskTicket:
    """Create a new customer service ticket with calculated SLA due deadline."""
    ticket_num = f"TCK-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
    sla_hours = SLA_HOURS_MAP.get(payload.priority, 24)
    due_at = utcnow() + timedelta(hours=sla_hours)

    ticket = HelpdeskTicket(
        ticket_number=ticket_num,
        user_id=user_id,
        order_id=payload.order_id,
        category=payload.category,
        priority=payload.priority,
        status=TicketStatus.OPEN,
        subject=payload.subject,
        sla_target_hours=sla_hours,
        sla_due_at=due_at,
    )
    db.add(ticket)
    await db.flush()

    # Initial Message
    initial_msg = HelpdeskTicketMessage(
        ticket_id=ticket.id,
        sender_user_id=user_id,
        is_staff_reply=False,
        message_text=payload.initial_message,
        attachment_urls_json=json.dumps(payload.attachment_urls) if payload.attachment_urls else None,
    )
    db.add(initial_msg)
    await db.flush()
    await db.refresh(ticket)
    return ticket


async def add_ticket_reply(
    db: AsyncSession, ticket_id: int, user_id: int, payload: TicketMessageCreate, is_staff: bool = False
) -> HelpdeskTicketMessage:
    """Append a response message to a support ticket and update ticket status."""
    stmt = select(HelpdeskTicket).where(HelpdeskTicket.id == ticket_id)
    res = await db.execute(stmt)
    ticket = res.scalar_one_or_none()

    if not ticket:
        raise ValueError("Ticket not found")

    if is_staff:
        ticket.status = TicketStatus.WAITING_FOR_CUSTOMER
    else:
        ticket.status = TicketStatus.IN_PROGRESS

    msg = HelpdeskTicketMessage(
        ticket_id=ticket_id,
        sender_user_id=user_id,
        is_staff_reply=is_staff,
        message_text=payload.message_text,
        attachment_urls_json=json.dumps(payload.attachment_urls) if payload.attachment_urls else None,
    )
    db.add(msg)
    await db.flush()
    return msg


async def resolve_ticket(
    db: AsyncSession, ticket_id: int, agent_id: int, resolution_notes: Optional[str] = None
) -> bool:
    """Mark ticket as resolved by support staff."""
    stmt = select(HelpdeskTicket).where(HelpdeskTicket.id == ticket_id)
    res = await db.execute(stmt)
    ticket = res.scalar_one_or_none()

    if not ticket:
        return False

    ticket.status = TicketStatus.RESOLVED
    ticket.assigned_agent_id = agent_id
    ticket.resolved_at = utcnow()

    if resolution_notes:
        msg = HelpdeskTicketMessage(
            ticket_id=ticket_id,
            sender_user_id=agent_id,
            is_staff_reply=True,
            message_text=f"Resolution: {resolution_notes}",
        )
        db.add(msg)

    await db.flush()
    return True
