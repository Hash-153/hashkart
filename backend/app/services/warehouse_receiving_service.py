from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.warehouse import Warehouse, WarehouseStock
from app.models.warehouse_receiving import WarehouseInspection, WarehouseReceipt
from app.schemas.warehouse_receiving import WarehouseInspectionCreate, WarehouseReceiptCreate


async def create_receipt(db: AsyncSession, payload: WarehouseReceiptCreate) -> WarehouseReceipt:
    if not await db.get(Warehouse, payload.warehouse_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Warehouse not found")
    duplicate = await db.scalar(
        select(WarehouseReceipt).where(WarehouseReceipt.purchase_reference == payload.purchase_reference)
    )
    if duplicate:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Purchase reference already received")
    receipt = WarehouseReceipt(**payload.model_dump())
    db.add(receipt)
    await db.flush()
    return receipt


async def inspect_receipt(
    db: AsyncSession, inspector_id: int, payload: WarehouseInspectionCreate
) -> WarehouseInspection:
    if payload.accepted_quantity + payload.rejected_quantity != payload.expected_quantity:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Accepted and rejected quantities must equal expected quantity",
        )
    receipt = await db.get(WarehouseReceipt, payload.receipt_id)
    if not receipt or receipt.status == "CLOSED":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Open receipt not found")

    existing = await db.scalar(
        select(WarehouseInspection).where(
            WarehouseInspection.receipt_id == payload.receipt_id,
            WarehouseInspection.variant_id == payload.variant_id,
        )
    )
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Variant already inspected")

    inspection = WarehouseInspection(
        **payload.model_dump(), inspected_by=inspector_id, inspected_at=datetime.utcnow()
    )
    receipt.status = "RECEIVED"
    db.add(inspection)
    await db.flush()
    return inspection


async def list_receipts(db: AsyncSession) -> list[WarehouseReceipt]:
    result = await db.execute(select(WarehouseReceipt).order_by(WarehouseReceipt.created_at.desc()))
    return list(result.scalars().all())
