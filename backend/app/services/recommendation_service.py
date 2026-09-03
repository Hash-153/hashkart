from typing import List, Dict, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, desc, or_
from sqlalchemy.orm import selectinload
from app.models.catalog import Product, ProductVariant, Category, Brand
from app.models.order_payment import OrderItem, Order
from app.models.cart_wishlist import WishlistItem, Wishlist
from app.models.discovery import RecentlyViewedProduct
from app.services.pricing_service import PricingService


class RecommendationService:
    """Deterministic recommendation and discovery service."""

    @staticmethod
    async def get_personalized_recommendations(
        db: AsyncSession, user_id: Optional[int] = None, limit: int = 10
    ) -> List[Product]:
        """
        Generate personalized product recommendations:
        For authenticated users, collects category and brand preferences from recent orders,
        wishlist items, and recently viewed products.
        Fallback to top-rated bestsellers for anonymous users.
        """
        preferred_cat_ids: set = set()
        preferred_brand_ids: set = set()

        if user_id:
            # 1. Categories from Wishlist
            wish_res = await db.execute(
                select(WishlistItem)
                .join(Wishlist)
                .options(selectinload(WishlistItem.variant).selectinload(ProductVariant.product))
                .where(Wishlist.user_id == user_id)
                .limit(10)
            )
            for witem in wish_res.scalars().all():
                if witem.variant and witem.variant.product:
                    preferred_cat_ids.add(witem.variant.product.category_id)
                    if witem.variant.product.brand_id:
                        preferred_brand_ids.add(witem.variant.product.brand_id)

            # 2. Categories from Recently Viewed
            rv_res = await db.execute(
                select(RecentlyViewedProduct)
                .options(selectinload(RecentlyViewedProduct.product))
                .where(RecentlyViewedProduct.user_id == user_id)
                .order_by(desc(RecentlyViewedProduct.viewed_at))
                .limit(10)
            )
            for rv in rv_res.scalars().all():
                if rv.product:
                    preferred_cat_ids.add(rv.product.category_id)
                    if rv.product.brand_id:
                        preferred_brand_ids.add(rv.product.brand_id)

        stmt = (
            select(Product)
            .options(
                selectinload(Product.category),
                selectinload(Product.brand),
                selectinload(Product.variants).selectinload(ProductVariant.images),
                selectinload(Product.images),
            )
            .where(Product.status == "ACTIVE", Product.is_active == True)
        )

        if preferred_cat_ids or preferred_brand_ids:
            conditions = []
            if preferred_cat_ids:
                conditions.append(Product.category_id.in_(list(preferred_cat_ids)))
            if preferred_brand_ids:
                conditions.append(Product.brand_id.in_(list(preferred_brand_ids)))
            stmt = stmt.where(or_(*conditions))

        stmt = stmt.order_by(desc(Product.rating_avg), desc(Product.review_count)).limit(limit)
        res = await db.execute(stmt)
        products = list(res.scalars().all())

        if len(products) < limit:
            # Backfill with popular products
            fallback_stmt = (
                select(Product)
                .options(
                    selectinload(Product.category),
                    selectinload(Product.brand),
                    selectinload(Product.variants).selectinload(ProductVariant.images),
                    selectinload(Product.images),
                )
                .where(Product.status == "ACTIVE", Product.is_active == True)
                .order_by(desc(Product.rating_avg), desc(Product.review_count))
                .limit(limit)
            )
            fb_res = await db.execute(fallback_stmt)
            for fb_prod in fb_res.scalars().all():
                if fb_prod not in products:
                    products.append(fb_prod)
                if len(products) >= limit:
                    break

        return products[:limit]

    @staticmethod
    async def get_best_selling_products(db: AsyncSession, limit: int = 10) -> List[Product]:
        """Rank products by order quantity from completed orders."""
        subq = (
            select(ProductVariant.product_id, func.sum(OrderItem.quantity).label("total_sold"))
            .join(OrderItem, OrderItem.variant_id == ProductVariant.id)
            .join(Order, Order.id == OrderItem.order_id)
            .where(Order.status != "CANCELLED")
            .group_by(ProductVariant.product_id)
            .subquery()
        )

        stmt = (
            select(Product)
            .outerjoin(subq, Product.id == subq.c.product_id)
            .options(
                selectinload(Product.category),
                selectinload(Product.brand),
                selectinload(Product.variants).selectinload(ProductVariant.images),
                selectinload(Product.images),
            )
            .where(Product.status == "ACTIVE", Product.is_active == True)
            .order_by(desc(func.coalesce(subq.c.total_sold, 0)), desc(Product.rating_avg))
            .limit(limit)
        )
        res = await db.execute(stmt)
        return list(res.scalars().all())

    @staticmethod
    async def get_top_deals(db: AsyncSession, limit: int = 10) -> List[Product]:
        """Rank products by discount percentage."""
        stmt = (
            select(Product)
            .options(
                selectinload(Product.category),
                selectinload(Product.brand),
                selectinload(Product.variants).selectinload(ProductVariant.images),
                selectinload(Product.images),
            )
            .where(Product.status == "ACTIVE", Product.is_active == True)
        )
        res = await db.execute(stmt)
        products = list(res.scalars().unique().all())

        # Sort in-memory by maximum variant discount percentage
        products_with_disc = []
        for p in products:
            max_disc = 0
            for v in p.variants:
                if v.is_active and v.discount_price:
                    disc_info = PricingService.calculate_discount_details(float(v.price), float(v.discount_price))
                    if disc_info["discount_percentage"] > max_disc:
                        max_disc = disc_info["discount_percentage"]
            if max_disc > 0:
                products_with_disc.append((p, max_disc))

        products_with_disc.sort(key=lambda item: item[1], reverse=True)
        return [item[0] for item in products_with_disc[:limit]]

    @staticmethod
    async def get_new_arrivals(db: AsyncSession, limit: int = 10) -> List[Product]:
        """Rank products by created_at timestamp."""
        stmt = (
            select(Product)
            .options(
                selectinload(Product.category),
                selectinload(Product.brand),
                selectinload(Product.variants).selectinload(ProductVariant.images),
                selectinload(Product.images),
            )
            .where(Product.status == "ACTIVE", Product.is_active == True)
            .order_by(desc(Product.created_at))
            .limit(limit)
        )
        res = await db.execute(stmt)
        return list(res.scalars().all())
