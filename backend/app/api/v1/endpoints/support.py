from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user, require_staff
from app.database import get_db
from app.models.user import User
from app.schemas.support import (
    SupportMessageCreate,
    SupportMessageResponse,
    SupportStatusUpdate,
    SupportTicketCreate,
    SupportTicketResponse,
)
from app.services.support_service import add_message, create_ticket, list_tickets, update_ticket

router = APIRouter()


@router.post("/tickets", response_model=SupportTicketResponse, status_code=status.HTTP_201_CREATED)
async def open_ticket(
    payload: SupportTicketCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await create_ticket(db, user.id, payload)


@router.get("/tickets", response_model=list[SupportTicketResponse])
async def tickets(user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await list_tickets(db, user.id)


@router.get("/admin/tickets", response_model=list[SupportTicketResponse])
async def all_tickets(
    status_filter: str | None = None,
    _: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await list_tickets(db, status_filter=status_filter)


@router.post("/tickets/{ticket_id}/messages", response_model=SupportMessageResponse, status_code=status.HTTP_201_CREATED)
async def message(
    ticket_id: int,
    payload: SupportMessageCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await add_message(db, ticket_id, user.id, payload)


@router.patch("/admin/tickets/{ticket_id}", response_model=SupportTicketResponse)
async def update(
    ticket_id: int,
    payload: SupportStatusUpdate,
    _: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await update_ticket(db, ticket_id, payload)
