from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user, require_staff
from app.database import get_db
from app.models.fulfillment import ShipmentEvent
from app.models.order_payment import Shipment
from app.models.user import User
from app.schemas.fulfillment import (
    ReturnRequestDecision,
    ReturnRequestResponse,
    ShipmentEventCreate,
    ShipmentEventResponse,
)
from app.schemas.carrier import (
    FulfillmentTaskResponse,
    FulfillmentTaskTransition,
    ShipmentDispatchRequest,
    ShipmentDispatchResponse,
)
from app.services.carrier_service import dispatch_shipment
from app.services.fulfillment_service import (
    add_shipment_event,
    decide_return,
    list_returns,
)
from app.services.warehouse_task_service import list_tasks, transition_task

router = APIRouter()


@router.post("/shipments/{shipment_id}/dispatch", response_model=ShipmentDispatchResponse)
async def dispatch(
    shipment_id: int,
    payload: ShipmentDispatchRequest,
    _: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await dispatch_shipment(db, shipment_id, payload.order_number, payload.postal_code)


@router.get("/tasks", response_model=list[FulfillmentTaskResponse])
async def tasks(
    status_filter: str | None = None,
    _: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await list_tasks(db, status_filter)


@router.patch("/tasks/{task_id}", response_model=FulfillmentTaskResponse)
async def transition(
    task_id: int,
    payload: FulfillmentTaskTransition,
    user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await transition_task(db, task_id, user.id, payload)


@router.get("/returns", response_model=list[ReturnRequestResponse])
async def admin_returns(
    _: User = Depends(require_staff), db: AsyncSession = Depends(get_db)
):
    return await list_returns(db)


@router.patch("/returns/{return_id}", response_model=ReturnRequestResponse)
async def review_return(
    return_id: int,
    payload: ReturnRequestDecision,
    user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await decide_return(db, return_id, user.id, payload.status, payload.resolution)


@router.post(
    "/shipments/{shipment_id}/events",
    response_model=ShipmentEventResponse,
    status_code=status.HTTP_201_CREATED,
)
async def record_shipment_event(
    shipment_id: int,
    payload: ShipmentEventCreate,
    _: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await add_shipment_event(db, shipment_id, payload)


@router.get("/shipments/{shipment_id}/events", response_model=list[ShipmentEventResponse])
async def shipment_events(
    shipment_id: int,
    _: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    if not await db.get(Shipment, shipment_id):
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="Shipment not found")
    result = await db.execute(
        select(ShipmentEvent)
        .where(ShipmentEvent.shipment_id == shipment_id)
        .order_by(ShipmentEvent.occurred_at.asc())
    )
    return list(result.scalars().all())
