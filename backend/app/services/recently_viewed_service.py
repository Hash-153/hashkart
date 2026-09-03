from datetime import datetime
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, desc
from sqlalchemy.orm import selectinload
from app.models.discovery import RecentlyViewedProduct
from app.models.catalog import Product, ProductVariant


class RecentlyViewedService:
    """Manages authenticated customer recently viewed product history."""

    @staticmethod
    async def record_product_view(db: AsyncSession, user_id: int, product_id: int) -> RecentlyViewedProduct:
        """Record product view with timestamp update for existing views."""
        existing = await db.execute(
            select(RecentlyViewedProduct).where(
                RecentlyViewedProduct.user_id == user_id,
                RecentlyViewedProduct.product_id == product_id,
            )
        )
        rv = existing.scalar_one_or_none()
        if rv:
            rv.viewed_at = datetime.utcnow()
        else:
            rv = RecentlyViewedProduct(user_id=user_id, product_id=product_id, viewed_at=datetime.utcnow())
            db.add(rv)

        await db.commit()
        await db.refresh(rv)
        return rv

    @staticmethod
    async def get_user_recently_viewed(db: AsyncSession, user_id: int, limit: int = 12) -> List[Product]:
        """Fetch recently viewed products ordered by most recent."""
        stmt = (
            select(RecentlyViewedProduct)
            .options(
                selectinload(RecentlyViewedProduct.product).selectinload(Product.category),
                selectinload(RecentlyViewedProduct.product).selectinload(Product.brand),
                selectinload(RecentlyViewedProduct.product).selectinload(Product.variants).selectinload(ProductVariant.images),
                selectinload(RecentlyViewedProduct.product).selectinload(Product.images),
            )
            .where(RecentlyViewedProduct.user_id == user_id)
            .order_by(desc(RecentlyViewedProduct.viewed_at))
            .limit(limit)
        )
        res = await db.execute(stmt)
        rv_items = res.scalars().all()
        products = [item.product for item in rv_items if item.product and item.product.is_active]
        return products

    @staticmethod
    async def clear_recently_viewed(db: AsyncSession, user_id: int) -> int:
        """Clear all recently viewed history for a customer."""
        res = await db.execute(delete(RecentlyViewedProduct).where(RecentlyViewedProduct.user_id == user_id))
        await db.commit()
        return res.rowcount
