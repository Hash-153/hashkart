from typing import List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, desc
from app.models.catalog import Category, Brand, Product
from app.models.discovery import SearchQueryAnalytics
from app.services.search_service import SearchService


class AutocompleteService:
    """Provides fast, non-blocking autocomplete search suggestions."""

    @staticmethod
    async def get_suggestions(
        db: AsyncSession, query_raw: str, limit: int = 8
    ) -> List[Dict[str, Any]]:
        """
        Generate ranked autocomplete suggestions matching prefix:
        - Matching Categories
        - Matching Brands
        - Matching Product Names
        - Synthetic Trending Search Terms
        """
        norm_q = SearchService.normalize_query(query_raw)
        if not norm_q or len(norm_q) < 2:
            return []

        suggestions: List[Dict[str, Any]] = []
        seen_labels = set()

        # 1. Matching Categories
        cat_res = await db.execute(
            select(Category)
            .where(Category.is_active == True, or_(Category.name.ilike(f"%{norm_q}%"), Category.slug.ilike(f"%{norm_q}%")))
            .limit(3)
        )
        for cat in cat_res.scalars().all():
            if cat.name.lower() not in seen_labels:
                seen_labels.add(cat.name.lower())
                suggestions.append({
                    "label": cat.name,
                    "type": "category",
                    "slug": cat.slug,
                    "id": cat.id,
                })

        # 2. Matching Brands
        brand_res = await db.execute(
            select(Brand)
            .where(Brand.is_active == True, or_(Brand.name.ilike(f"%{norm_q}%"), Brand.slug.ilike(f"%{norm_q}%")))
            .limit(3)
        )
        for brand in brand_res.scalars().all():
            if brand.name.lower() not in seen_labels:
                seen_labels.add(brand.name.lower())
                suggestions.append({
                    "label": brand.name,
                    "type": "brand",
                    "slug": brand.slug,
                    "id": brand.id,
                })

        # 3. Trending Search Queries
        analytics_res = await db.execute(
            select(SearchQueryAnalytics)
            .where(SearchQueryAnalytics.normalized_query.ilike(f"{norm_q}%"))
            .order_by(desc(SearchQueryAnalytics.search_count))
            .limit(3)
        )
        for sqa in analytics_res.scalars().all():
            if sqa.query.lower() not in seen_labels:
                seen_labels.add(sqa.query.lower())
                suggestions.append({
                    "label": sqa.query,
                    "type": "keyword",
                    "search_count": sqa.search_count,
                })

        # 4. Matching Product Titles
        prod_res = await db.execute(
            select(Product)
            .where(Product.is_active == True, Product.status == "ACTIVE", Product.name.ilike(f"%{norm_q}%"))
            .order_by(desc(Product.rating_avg))
            .limit(4)
        )
        for prod in prod_res.scalars().all():
            if prod.name.lower() not in seen_labels:
                seen_labels.add(prod.name.lower())
                suggestions.append({
                    "label": prod.name,
                    "type": "product",
                    "slug": prod.slug,
                    "id": prod.id,
                })

        return suggestions[:limit]
