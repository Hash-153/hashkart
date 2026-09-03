from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import List, Optional, Tuple
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.catalog import Product
from app.models.loyalty_promotions import (
    FlashSaleEvent,
    FlashSaleItem,
    FlashSaleStatus,
    UserLoyaltyProfile,
)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


async def get_active_flash_sales(db: AsyncSession) -> List[FlashSaleEvent]:
    """Fetch ongoing or upcoming flash sale events."""
    now = utcnow()
    stmt = (
        select(FlashSaleEvent)
        .options(selectinload(FlashSaleEvent.items).selectinload(FlashSaleItem.product))
        .where(
            FlashSaleEvent.status.in_([FlashSaleStatus.SCHEDULED, FlashSaleStatus.LIVE]),
            FlashSaleEvent.ends_at >= now,
        )
        .order_by(FlashSaleEvent.starts_at.asc())
    )
    res = await db.execute(stmt)
    events = res.scalars().all()

    # Automatically flip status to LIVE if starts_at is past
    for event in events:
        if event.starts_at <= now <= event.ends_at and event.status != FlashSaleStatus.LIVE:
            event.status = FlashSaleStatus.LIVE
        elif now > event.ends_at and event.status != FlashSaleStatus.ENDED:
            event.status = FlashSaleStatus.ENDED

    await db.flush()
    return events


async def reserve_flash_sale_item(
    db: AsyncSession,
    event_id: int,
    product_id: int,
    user_id: int,
    is_vip: bool = False,
    quantity: int = 1,
) -> Tuple[bool, str, Optional[Decimal]]:
    """Concurrency-safe reservation of flash sale inventory units."""
    now = utcnow()
    stmt = (
        select(FlashSaleEvent)
        .where(FlashSaleEvent.id == event_id)
    )
    res = await db.execute(stmt)
    event = res.scalar_one_or_none()

    if not event:
        return False, "Flash sale event not found", None

    # VIP Early Access Window Check
    effective_start = event.starts_at
    if is_vip:
        effective_start -= timedelta(minutes=event.vip_early_access_minutes)

    if now < effective_start:
        return False, "Flash sale has not started yet", None
    if now > event.ends_at:
        return False, "Flash sale event has ended", None

    # Atomic Row Lock on Flash Item
    item_stmt = (
        select(FlashSaleItem)
        .where(
            FlashSaleItem.event_id == event_id,
            FlashSaleItem.product_id == product_id,
            FlashSaleItem.is_active == True,
        )
        .with_for_update()
    )
    item_res = await db.execute(item_stmt)
    item = item_res.scalar_one_or_none()

    if not item:
        return False, "Product not in flash sale event", None

    available_units = item.allocated_stock_units - item.claimed_units
    if available_units < quantity:
        return False, "100% of flash sale stock has been claimed!", None

    if quantity > item.max_units_per_user:
        return False, f"Maximum {item.max_units_per_user} unit(s) allowed per customer", None

    item.claimed_units += quantity
    await db.flush()

    return True, "Flash sale unit reserved successfully!", item.flash_price
