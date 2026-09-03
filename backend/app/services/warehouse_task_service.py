from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.warehouse_tasks import FulfillmentTask
from app.schemas.carrier import FulfillmentTaskTransition

_ALLOWED_TRANSITIONS = {
    "OPEN": {"IN_PROGRESS", "CANCELLED"},
    "IN_PROGRESS": {"COMPLETED", "CANCELLED"},
    "COMPLETED": set(),
    "CANCELLED": set(),
}


async def create_order_tasks(db: AsyncSession, order_id: int, shipment_id: int | None = None) -> list[FulfillmentTask]:
    tasks: list[FulfillmentTask] = []
    for task_type in ("PICK", "PACK"):
        existing = await db.scalar(
            select(FulfillmentTask).where(
                FulfillmentTask.order_id == order_id, FulfillmentTask.task_type == task_type
            )
        )
        if not existing:
            task = FulfillmentTask(order_id=order_id, shipment_id=shipment_id, task_type=task_type)
            db.add(task)
            tasks.append(task)
    await db.flush()
    return tasks


async def list_tasks(db: AsyncSession, status_filter: str | None = None) -> list[FulfillmentTask]:
    query = select(FulfillmentTask).order_by(FulfillmentTask.created_at.desc())
    if status_filter:
        query = query.where(FulfillmentTask.status == status_filter)
    result = await db.execute(query)
    return list(result.scalars().all())


async def transition_task(
    db: AsyncSession, task_id: int, worker_id: int, payload: FulfillmentTaskTransition
) -> FulfillmentTask:
    task = await db.get(FulfillmentTask, task_id, with_for_update=True)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fulfillment task not found")
    if payload.status not in _ALLOWED_TRANSITIONS.get(task.status, set()):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Cannot transition task from {task.status} to {payload.status}",
        )

    task.status = payload.status
    task.assigned_to = worker_id
    task.notes = payload.notes
    if payload.status == "IN_PROGRESS":
        task.started_at = datetime.utcnow()
    if payload.status in {"COMPLETED", "CANCELLED"}:
        task.completed_at = datetime.utcnow()
    await db.flush()
    return task
