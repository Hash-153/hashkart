from datetime import datetime, timedelta

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order_payment import Order, OrderItem
from app.models.seller import SellerListing, SellerProfile


async def seller_dashboard(db: AsyncSession, user_id: int, days: int = 30) -> dict:
    seller = await db.scalar(select(SellerProfile).where(SellerProfile.user_id == user_id))
    if not seller:
        return {
            "seller_id": None,
            "period_days": days,
            "active_listings": 0,
            "orders": 0,
            "revenue": 0.0,
            "pending_payout": 0.0,
        }

    cutoff = datetime.utcnow() - timedelta(days=days)
    listing_count = await db.scalar(
        select(func.count(SellerListing.id)).where(
            SellerListing.seller_id == seller.id, SellerListing.status == "ACTIVE"
        )
    )
    order_count = await db.scalar(
        select(func.count(func.distinct(Order.id)))
        .join(OrderItem, OrderItem.order_id == Order.id)
        .join(SellerListing, SellerListing.variant_id == OrderItem.variant_id)
        .where(
            SellerListing.seller_id == seller.id,
            Order.created_at >= cutoff,
            Order.status != "CANCELLED",
        )
    )
    revenue = await db.scalar(
        select(func.coalesce(func.sum(OrderItem.line_subtotal), 0))
        .join(Order, Order.id == OrderItem.order_id)
        .join(SellerListing, SellerListing.variant_id == OrderItem.variant_id)
        .where(
            SellerListing.seller_id == seller.id,
            Order.created_at >= cutoff,
            Order.status != "CANCELLED",
        )
    )
    return {
        "seller_id": seller.id,
        "period_days": days,
        "active_listings": int(listing_count or 0),
        "orders": int(order_count or 0),
        "revenue": float(revenue or 0),
        "pending_payout": 0.0,
    }
