from datetime import datetime
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.fulfillment import ReturnRequest, ShipmentEvent
from app.models.order_payment import Order, OrderItem, Shipment
from app.schemas.fulfillment import ReturnRequestCreate, ShipmentEventCreate


async def create_return_request(
    db: AsyncSession, user_id: int, payload: ReturnRequestCreate
) -> ReturnRequest:
    result = await db.execute(
        select(OrderItem)
        .join(Order, Order.id == OrderItem.order_id)
        .where(OrderItem.id == payload.order_item_id, Order.user_id == user_id)
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found")
    if payload.quantity > item.quantity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Return quantity exceeds purchased quantity")

    existing = await db.execute(
        select(ReturnRequest).where(
            ReturnRequest.order_item_id == payload.order_item_id,
            ReturnRequest.status.not_in(["REJECTED", "COMPLETED"]),
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="An active return already exists")

    request = ReturnRequest(user_id=user_id, **payload.model_dump())
    db.add(request)
    await db.flush()
    return request


async def list_returns(db: AsyncSession, user_id: Optional[int] = None) -> list[ReturnRequest]:
    query = select(ReturnRequest).order_by(ReturnRequest.created_at.desc())
    if user_id is not None:
        query = query.where(ReturnRequest.user_id == user_id)
    result = await db.execute(query)
    return list(result.scalars().all())


async def decide_return(
    db: AsyncSession, return_id: int, reviewer_id: int, decision: str, resolution: Optional[str]
) -> ReturnRequest:
    request = await db.get(ReturnRequest, return_id)
    if not request:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Return request not found")
    if request.status in {"REJECTED", "COMPLETED"}:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Return request is already closed")
    if decision == "COMPLETED" and not resolution:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Resolution is required")

    request.status = decision
    request.resolution = resolution
    request.reviewed_by = reviewer_id
    request.reviewed_at = datetime.utcnow()
    await db.flush()
    return request


async def add_shipment_event(
    db: AsyncSession, shipment_id: int, payload: ShipmentEventCreate
) -> ShipmentEvent:
    if not await db.get(Shipment, shipment_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shipment not found")
    event = ShipmentEvent(shipment_id=shipment_id, **payload.model_dump(exclude_none=True))
    db.add(event)
    await db.flush()
    return event
