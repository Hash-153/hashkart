import uuid
from datetime import datetime, timedelta
from typing import Optional, List, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, or_, and_, desc
from sqlalchemy.orm import selectinload

from app.models.catalog import ProductVariant
from app.models.inventory import Inventory, InventoryTransaction
from app.models.inventory_reservation import InventoryReservation


class InventoryService:
    """Centralized inventory service enforcing concurrency-safe stock reservations & audit tracking."""

    @staticmethod
    async def get_available_stock(db: AsyncSession, variant_id: int) -> int:
        """Calculate available stock: available_stock = stock_quantity - active_reservations."""
        var_res = await db.execute(select(ProductVariant).where(ProductVariant.id == variant_id))
        variant = var_res.scalar_one_or_none()
        if not variant or not variant.is_active:
            return 0

        # Calculate active unexpired reservations
        res_stmt = select(InventoryReservation).where(
            InventoryReservation.variant_id == variant_id,
            InventoryReservation.status == "RESERVED",
            InventoryReservation.expires_at > datetime.utcnow(),
        )
        active_res = await db.execute(res_stmt)
        total_reserved = sum(r.quantity for r in active_res.scalars().all())

        return max(0, variant.stock_quantity - total_reserved)

    @staticmethod
    async def reserve_stock(
        db: AsyncSession, variant_id: int, quantity: int, user_id: Optional[int] = None, ttl_minutes: int = 15
    ) -> Tuple[bool, Optional[InventoryReservation], str]:
        """
        Concurrency-safe temporary inventory reservation using pessimistic row locking (with_for_update).
        Prevents overselling race conditions under concurrent load.
        """
        if quantity <= 0:
            return False, None, "Requested quantity must be positive."

        # Lock ProductVariant row for update
        stmt = (
            select(ProductVariant)
            .where(ProductVariant.id == variant_id, ProductVariant.is_active == True)
            .with_for_update()
        )
        res = await db.execute(stmt)
        variant = res.scalar_one_or_none()

        if not variant:
            return False, None, "Product variant unavailable."

        # Clean expired reservations for this variant first
        await InventoryService.cleanup_expired_reservations(db, variant_id=variant_id)

        # Check current available stock
        avail_stock = await InventoryService.get_available_stock(db, variant_id)
        if avail_stock < quantity:
            return False, None, f"Only {avail_stock} units available in stock."

        res_key = f"RES-{uuid.uuid4().hex[:12].upper()}"
        expires_at = datetime.utcnow() + timedelta(minutes=ttl_minutes)

        reservation = InventoryReservation(
            reservation_key=res_key,
            user_id=user_id,
            variant_id=variant_id,
            quantity=quantity,
            status="RESERVED",
            expires_at=expires_at,
        )
        db.add(reservation)

        # Record inventory transaction audit
        tx = InventoryTransaction(
            variant_id=variant_id,
            transaction_type="RESERVATION",
            quantity=-quantity,
            reference_id=res_key,
            notes=f"Reserved {quantity} units for checkout key {res_key}",
        )
        db.add(tx)

        await db.commit()
        await db.refresh(reservation)
        return True, reservation, "Stock reserved successfully."

    @staticmethod
    async def confirm_reservation(db: AsyncSession, reservation_key: str) -> bool:
        """Confirm reservation and permanently deduct stock quantity upon successful order payment."""
        stmt = select(InventoryReservation).where(
            InventoryReservation.reservation_key == reservation_key,
            InventoryReservation.status == "RESERVED",
        ).with_for_update()
        res = await db.execute(stmt)
        reservation = res.scalar_one_or_none()

        if not reservation:
            return False

        # Lock variant and deduct physical stock
        v_res = await db.execute(
            select(ProductVariant).where(ProductVariant.id == reservation.variant_id).with_for_update()
        )
        variant = v_res.scalar_one_or_none()
        if variant:
            variant.stock_quantity = max(0, variant.stock_quantity - reservation.quantity)

        reservation.status = "CONFIRMED"
        await db.commit()
        return True

    @staticmethod
    async def release_reservation(db: AsyncSession, reservation_key: str) -> bool:
        """Release reservation upon payment cancellation or failure."""
        stmt = select(InventoryReservation).where(
            InventoryReservation.reservation_key == reservation_key,
            InventoryReservation.status == "RESERVED",
        )
        res = await db.execute(stmt)
        reservation = res.scalar_one_or_none()

        if not reservation:
            return False

        reservation.status = "RELEASED"
        tx = InventoryTransaction(
            variant_id=reservation.variant_id,
            transaction_type="RELEASE",
            quantity=reservation.quantity,
            reference_id=reservation.reservation_key,
            notes=f"Released reservation {reservation.reservation_key}",
        )
        db.add(tx)
        await db.commit()
        return True

    @staticmethod
    async def cleanup_expired_reservations(db: AsyncSession, variant_id: Optional[int] = None) -> int:
        """Cleanup worker to expire overdue reservations."""
        stmt = select(InventoryReservation).where(
            InventoryReservation.status == "RESERVED",
            InventoryReservation.expires_at <= datetime.utcnow(),
        )
        if variant_id:
            stmt = stmt.where(InventoryReservation.variant_id == variant_id)

        res = await db.execute(stmt)
        expired_items = res.scalars().all()
        count = 0
        for item in expired_items:
            item.status = "EXPIRED"
            count += 1

        if count > 0:
            await db.commit()
        return count

    @staticmethod
    async def admin_adjust_stock(
        db: AsyncSession, variant_id: int, new_quantity: int, reason: str, actor_id: Optional[int] = None
    ) -> ProductVariant:
        """Admin stock adjustment with audit transaction record."""
        stmt = select(ProductVariant).where(ProductVariant.id == variant_id).with_for_update()
        res = await db.execute(stmt)
        variant = res.scalar_one_or_none()

        if not variant:
            raise ValueError("Product variant not found.")

        old_qty = variant.stock_quantity
        diff = new_quantity - old_qty
        variant.stock_quantity = new_quantity

        tx = InventoryTransaction(
            variant_id=variant_id,
            transaction_type="RESTOCK" if diff > 0 else "ADJUSTMENT",
            quantity=diff,
            notes=f"Admin adjustment by user {actor_id or 'system'}: {reason} (Old: {old_qty}, New: {new_quantity})",
        )
        db.add(tx)
        await db.commit()
        await db.refresh(variant)
        return variant
