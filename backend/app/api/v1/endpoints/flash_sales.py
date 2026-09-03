from datetime import datetime, timezone
from decimal import Decimal
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.deps import get_current_user, get_db
from app.models.loyalty_promotions import FlashSaleEvent, FlashSaleItem, FlashSaleStatus, UserLoyaltyProfile
from app.models.user import User
from app.schemas.loyalty_promotions import (
    FlashSaleEventResponse,
    FlashSaleItemResponse,
    FlashSaleReserveRequest,
)
from app.services.flash_sale_service import (
    get_active_flash_sales,
    reserve_flash_sale_item,
)

router = APIRouter()


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


@router.get("/active", response_model=List[FlashSaleEventResponse])
async def list_active_flash_sales(
    db: AsyncSession = Depends(get_db),
):
    """Retrieve all current live and upcoming scheduled flash sale events."""
    events = await get_active_flash_sales(db)
    now = utcnow()

    response_list: List[FlashSaleEventResponse] = []
    for e in events:
        items_resp: List[FlashSaleItemResponse] = []
        for it in e.items:
            mrp = it.regular_price
            disc = int(((mrp - it.flash_price) / mrp) * 100) if mrp > it.flash_price else 0
            claimed_pct = int((it.claimed_units / it.allocated_stock_units) * 100) if it.allocated_stock_units > 0 else 100
            items_resp.append(
                FlashSaleItemResponse(
                    id=it.id,
                    event_id=it.event_id,
                    product_id=it.product_id,
                    product_name=it.product.name if it.product else "Deal Product",
                    product_slug=it.product.slug if it.product else f"deal-{it.product_id}",
                    product_image=it.product.images[0].image_url if (it.product and it.product.images) else None,
                    flash_price=it.flash_price,
                    regular_price=it.regular_price,
                    discount_percentage=disc,
                    allocated_stock_units=it.allocated_stock_units,
                    claimed_units=it.claimed_units,
                    claimed_percentage=min(100, claimed_pct),
                    max_units_per_user=it.max_units_per_user,
                    is_active=it.is_active,
                )
            )

        is_live = e.status == FlashSaleStatus.LIVE and e.starts_at <= now <= e.ends_at
        seconds_left = max(0, int((e.ends_at - now).total_seconds())) if is_live else max(0, int((e.starts_at - now).total_seconds()))

        response_list.append(
            FlashSaleEventResponse(
                id=e.id,
                title=e.title,
                slug=e.slug,
                banner_image_url=e.banner_image_url,
                status=e.status,
                starts_at=e.starts_at,
                ends_at=e.ends_at,
                vip_early_access_minutes=e.vip_early_access_minutes,
                description=e.description,
                is_live_now=is_live,
                seconds_remaining=seconds_left,
                items=items_resp,
            )
        )

    return response_list


@router.post("/reserve")
async def reserve_flash_deal(
    payload: FlashSaleReserveRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Reserve a flash sale product unit with concurrency locks."""
    # Check if user is VIP
    prof_stmt = select(UserLoyaltyProfile).where(UserLoyaltyProfile.user_id == current_user.id)
    prof_res = await db.execute(prof_stmt)
    prof = prof_res.scalar_one_or_none()
    is_vip = bool(prof and prof.is_flipkart_plus_member)

    success, msg, price = await reserve_flash_sale_item(
        db,
        event_id=payload.event_id,
        product_id=payload.product_id,
        user_id=current_user.id,
        is_vip=is_vip,
        quantity=payload.quantity,
    )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg,
        )

    await db.commit()
    return {
        "success": True,
        "message": msg,
        "flash_price": price,
    }
