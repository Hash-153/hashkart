from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import require_staff
from app.database import get_db
from app.models.user import User
from app.schemas.warehouse_receiving import (
    WarehouseInspectionCreate,
    WarehouseInspectionResponse,
    WarehouseReceiptCreate,
    WarehouseReceiptResponse,
)
from app.services.warehouse_receiving_service import create_receipt, inspect_receipt, list_receipts

router = APIRouter()


@router.post("/receipts", response_model=WarehouseReceiptResponse, status_code=status.HTTP_201_CREATED)
async def receive_purchase(
    payload: WarehouseReceiptCreate,
    _: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await create_receipt(db, payload)


@router.get("/receipts", response_model=list[WarehouseReceiptResponse])
async def receipts(_: User = Depends(require_staff), db: AsyncSession = Depends(get_db)):
    return await list_receipts(db)


@router.post("/inspections", response_model=WarehouseInspectionResponse, status_code=status.HTTP_201_CREATED)
async def inspect(
    payload: WarehouseInspectionCreate,
    user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await inspect_receipt(db, user.id, payload)
