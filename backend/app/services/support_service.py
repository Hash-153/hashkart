from datetime import datetime
from uuid import uuid4

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.support import SupportMessage, SupportTicket
from app.schemas.support import SupportMessageCreate, SupportStatusUpdate, SupportTicketCreate


async def create_ticket(db: AsyncSession, customer_id: int, payload: SupportTicketCreate) -> SupportTicket:
    ticket = SupportTicket(
        ticket_number=f"HK-{datetime.utcnow():%Y%m%d}-{uuid4().hex[:6].upper()}",
        customer_id=customer_id,
        **payload.model_dump(),
    )
    db.add(ticket)
    await db.flush()
    return ticket


async def list_tickets(
    db: AsyncSession, customer_id: int | None = None, status_filter: str | None = None
) -> list[SupportTicket]:
    query = select(SupportTicket).order_by(SupportTicket.created_at.desc())
    if customer_id is not None:
        query = query.where(SupportTicket.customer_id == customer_id)
    if status_filter:
        query = query.where(SupportTicket.status == status_filter)
    result = await db.execute(query)
    return list(result.scalars().all())


async def add_message(
    db: AsyncSession, ticket_id: int, author_id: int, payload: SupportMessageCreate
) -> SupportMessage:
    ticket = await db.get(SupportTicket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Support ticket not found")
    if ticket.status in {"CLOSED", "RESOLVED"}:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ticket is closed")
    message = SupportMessage(ticket_id=ticket_id, author_id=author_id, body=payload.body)
    if ticket.first_response_at is None and ticket.customer_id != author_id:
        ticket.first_response_at = datetime.utcnow()
    db.add(message)
    await db.flush()
    return message


async def update_ticket(
    db: AsyncSession, ticket_id: int, payload: SupportStatusUpdate
) -> SupportTicket:
    ticket = await db.get(SupportTicket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Support ticket not found")
    ticket.status = payload.status
    ticket.assigned_to = payload.assigned_to
    if payload.status in {"RESOLVED", "CLOSED"}:
        ticket.resolved_at = datetime.utcnow()
    await db.flush()
    return ticket
