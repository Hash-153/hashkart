from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user, require_staff
from app.database import get_db
from app.models.user import User
from app.schemas.operations import (
    SellerPayoutCreate,
    SellerPayoutResponse,
    StockMovementCreate,
    WarehouseCreate,
    WarehouseResponse,
)
from app.services.operations_service import (
    apply_stock_movement,
    create_warehouse,
    list_payouts,
    list_warehouses,
    request_payout,
)

router = APIRouter()


@router.post("/warehouses", response_model=WarehouseResponse, status_code=status.HTTP_201_CREATED)
async def add_warehouse(
    payload: WarehouseCreate,
    _: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    return await create_warehouse(db, payload)


@router.get("/warehouses", response_model=list[WarehouseResponse])
async def warehouses(_: User = Depends(require_staff), db: AsyncSession = Depends(get_db)):
    return await list_warehouses(db)


@router.post("/stock/movements", status_code=status.HTTP_201_CREATED)
async def move_stock(
    payload: StockMovementCreate,
    _: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    stock = await apply_stock_movement(db, payload)
    return {
        "status": "applied",
        "warehouse_stock_id": stock.id,
        "available_quantity": stock.available_quantity,
        "reserved_quantity": stock.reserved_quantity,
        "damaged_quantity": stock.damaged_quantity,
    }


@router.post("/seller/payouts", response_model=SellerPayoutResponse, status_code=status.HTTP_201_CREATED)
async def create_payout(
    payload: SellerPayoutCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await request_payout(db, user.id, payload)


@router.get("/seller/payouts", response_model=list[SellerPayoutResponse])
async def payouts(user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    return await list_payouts(db, user.id)
