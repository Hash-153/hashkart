from datetime import datetime
from decimal import Decimal
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.seller import SellerProfile
from app.models.seller_finance import SellerLedgerEntry, SellerPayout
from app.models.warehouse import Warehouse, WarehouseStock, WarehouseStockMovement
from app.schemas.operations import SellerPayoutCreate, StockMovementCreate, WarehouseCreate


async def create_warehouse(db: AsyncSession, payload: WarehouseCreate) -> Warehouse:
    duplicate = await db.execute(select(Warehouse).where(Warehouse.code == payload.code))
    if duplicate.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Warehouse code already exists")
    warehouse = Warehouse(**payload.model_dump())
    db.add(warehouse)
    await db.flush()
    return warehouse


async def list_warehouses(db: AsyncSession) -> list[Warehouse]:
    result = await db.execute(select(Warehouse).where(Warehouse.is_active.is_(True)).order_by(Warehouse.code))
    return list(result.scalars().all())


async def apply_stock_movement(db: AsyncSession, payload: StockMovementCreate) -> WarehouseStock:
    stock = await db.scalar(
        select(WarehouseStock)
        .where(WarehouseStock.id == payload.warehouse_stock_id)
        .with_for_update()
    )
    if not stock:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Warehouse stock not found")

    prior = await db.scalar(
        select(WarehouseStockMovement).where(
            WarehouseStockMovement.warehouse_stock_id == stock.id,
            WarehouseStockMovement.idempotency_key == payload.idempotency_key,
        )
    )
    if prior:
        return stock

    if payload.movement_type in {"RESTOCK", "RELEASE", "RETURN"}:
        stock.available_quantity += payload.quantity
    elif payload.movement_type == "RESERVE":
        if stock.available_quantity < payload.quantity:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Insufficient warehouse stock")
        stock.available_quantity -= payload.quantity
        stock.reserved_quantity += payload.quantity
    elif payload.movement_type == "DAMAGE":
        if stock.available_quantity < payload.quantity:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Insufficient warehouse stock")
        stock.available_quantity -= payload.quantity
        stock.damaged_quantity += payload.quantity

    db.add(WarehouseStockMovement(**payload.model_dump()))
    await db.flush()
    return stock


async def request_payout(
    db: AsyncSession, user_id: int, payload: SellerPayoutCreate
) -> SellerPayout:
    seller = await db.scalar(select(SellerProfile).where(SellerProfile.user_id == user_id))
    if not seller or seller.status != "APPROVED":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Approved seller required")

    existing = await db.scalar(
        select(SellerLedgerEntry).where(
            SellerLedgerEntry.seller_id == seller.id,
            SellerLedgerEntry.idempotency_key == payload.idempotency_key,
        )
    )
    if existing:
        payout = await db.scalar(
            select(SellerPayout).where(
                SellerPayout.seller_id == seller.id,
                SellerPayout.amount == existing.amount,
                SellerPayout.status == "REQUESTED",
            )
        )
        if payout:
            return payout

    ledger_entry = SellerLedgerEntry(
        seller_id=seller.id,
        entry_type="PAYOUT_HOLD",
        amount=-payload.amount,
        idempotency_key=payload.idempotency_key,
        reference_type="PAYOUT",
        notes="Funds held for payout review",
    )
    payout = SellerPayout(seller_id=seller.id, amount=payload.amount)
    db.add_all([ledger_entry, payout])
    await db.flush()
    return payout


async def list_payouts(db: AsyncSession, user_id: int) -> list[SellerPayout]:
    seller = await db.scalar(select(SellerProfile).where(SellerProfile.user_id == user_id))
    if not seller:
        return []
    result = await db.execute(
        select(SellerPayout).where(SellerPayout.seller_id == seller.id).order_by(SellerPayout.requested_at.desc())
    )
    return list(result.scalars().all())
