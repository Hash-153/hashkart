from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.deps import get_current_user, get_db, require_role
from app.models.helpdesk_qa import (
    HelpdeskTicket,
    HelpdeskTicketMessage,
    TicketCategory,
    TicketPriority,
    TicketStatus,
)
from app.models.user import User
from app.schemas.helpdesk_qa import (
    TicketCreate,
    TicketMessageCreate,
    TicketMessageResponse,
    TicketResponse,
)
from app.services.helpdesk_service import (
    add_ticket_reply,
    create_support_ticket,
    resolve_ticket,
    utcnow,
)

router = APIRouter()


@router.post("/tickets", response_model=TicketResponse)
async def open_support_ticket(
    payload: TicketCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Customer endpoint to raise an inquiry, cancellation, refund, or return support ticket."""
    ticket = await create_support_ticket(db, current_user.id, payload)
    await db.commit()

    stmt = (
        select(HelpdeskTicket)
        .options(
            selectinload(HelpdeskTicket.messages).selectinload(HelpdeskTicketMessage.sender),
            selectinload(HelpdeskTicket.user),
        )
        .where(HelpdeskTicket.id == ticket.id)
    )
    res = await db.execute(stmt)
    full_ticket = res.scalar_one()

    return TicketResponse(
        id=full_ticket.id,
        ticket_number=full_ticket.ticket_number,
        user_id=full_ticket.user_id,
        customer_name=full_ticket.user.full_name if full_ticket.user else None,
        customer_email=full_ticket.user.email if full_ticket.user else None,
        order_id=full_ticket.order_id,
        category=full_ticket.category,
        priority=full_ticket.priority,
        status=full_ticket.status,
        subject=full_ticket.subject,
        assigned_agent_id=full_ticket.assigned_agent_id,
        sla_target_hours=full_ticket.sla_target_hours,
        sla_due_at=full_ticket.sla_due_at,
        is_sla_breached=full_ticket.sla_due_at < utcnow() and full_ticket.status not in (TicketStatus.RESOLVED, TicketStatus.CLOSED),
        resolved_at=full_ticket.resolved_at,
        satisfaction_rating=full_ticket.satisfaction_rating,
        customer_feedback=full_ticket.customer_feedback,
        created_at=full_ticket.created_at,
        updated_at=full_ticket.updated_at,
        messages=[
            TicketMessageResponse(
                id=m.id,
                ticket_id=m.ticket_id,
                sender_user_id=m.sender_user_id,
                sender_name=m.sender.full_name if (m.sender and m.sender.full_name) else "Support Agent",
                is_staff_reply=m.is_staff_reply,
                message_text=m.message_text,
                attachment_urls=[],
                created_at=m.created_at,
            )
            for m in full_ticket.messages
        ],
    )


@router.get("/my-tickets", response_model=List[TicketResponse])
async def list_customer_tickets(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """List all support tickets created by the logged-in customer."""
    stmt = (
        select(HelpdeskTicket)
        .options(
            selectinload(HelpdeskTicket.messages).selectinload(HelpdeskTicketMessage.sender),
            selectinload(HelpdeskTicket.user),
        )
        .where(HelpdeskTicket.user_id == current_user.id)
        .order_by(HelpdeskTicket.created_at.desc())
    )
    res = await db.execute(stmt)
    tickets = res.scalars().all()

    return [
        TicketResponse(
            id=t.id,
            ticket_number=t.ticket_number,
            user_id=t.user_id,
            customer_name=t.user.full_name if t.user else None,
            customer_email=t.user.email if t.user else None,
            order_id=t.order_id,
            category=t.category,
            priority=t.priority,
            status=t.status,
            subject=t.subject,
            assigned_agent_id=t.assigned_agent_id,
            sla_target_hours=t.sla_target_hours,
            sla_due_at=t.sla_due_at,
            is_sla_breached=t.sla_due_at < utcnow() and t.status not in (TicketStatus.RESOLVED, TicketStatus.CLOSED),
            resolved_at=t.resolved_at,
            satisfaction_rating=t.satisfaction_rating,
            customer_feedback=t.customer_feedback,
            created_at=t.created_at,
            updated_at=t.updated_at,
            messages=[
                TicketMessageResponse(
                    id=m.id,
                    ticket_id=m.ticket_id,
                    sender_user_id=m.sender_user_id,
                    sender_name=m.sender.full_name if (m.sender and m.sender.full_name) else "Support Agent",
                    is_staff_reply=m.is_staff_reply,
                    message_text=m.message_text,
                    attachment_urls=[],
                    created_at=m.created_at,
                )
                for m in t.messages
            ],
        )
        for t in tickets
    ]


@router.post("/tickets/{ticket_id}/reply", response_model=TicketMessageResponse)
async def reply_to_ticket(
    ticket_id: int,
    payload: TicketMessageCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Post a reply on an active support ticket."""
    is_staff = any(r.name in ("ADMIN", "STAFF", "SUPPORT") for r in (current_user.roles or []))
    msg = await add_ticket_reply(db, ticket_id, current_user.id, payload, is_staff=is_staff)
    await db.commit()

    return TicketMessageResponse(
        id=msg.id,
        ticket_id=msg.ticket_id,
        sender_user_id=msg.sender_user_id,
        sender_name=current_user.full_name or "User",
        is_staff_reply=msg.is_staff_reply,
        message_text=msg.message_text,
        attachment_urls=[],
        created_at=msg.created_at,
    )
