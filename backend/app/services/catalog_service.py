from typing import List, Optional, Dict, Any, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_, and_, desc, asc
from sqlalchemy.orm import selectinload

from app.models.catalog import (
    Product,
    ProductVariant,
    Category,
    Brand,
    AttributeValue,
    AttributeDefinition,
)
from app.services.search_service import SearchService
from app.services.pricing_service import PricingService
from app.services.facet_service import FacetService


class CatalogService:
    """Catalog filtering, searching, sorting, pagination, dynamic facets, and recommendation service."""

    @staticmethod
    async def filter_and_search_products(
        db: AsyncSession,
        query: Optional[str] = None,
        category_id: Optional[int] = None,
        category_slug: Optional[str] = None,
        brand_ids: Optional[List[int]] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        min_rating: Optional[float] = None,
        in_stock_only: bool = False,
        min_discount_percent: Optional[int] = None,
        is_featured: Optional[bool] = None,
        is_bestseller: Optional[bool] = None,
        sort_by: str = "relevance",
        page: int = 1,
        limit: int = 20,
        status_allowlist: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Execute robust composable product catalog query with multi-filtering, relevance scoring,
        dynamic facets, spelling suggestions, sorting, and pagination.
        """
        status_filter = status_allowlist or ["ACTIVE"]

        # Base query joining Product, ProductVariant, Brand, Category
        stmt = (
            select(Product)
            .options(
                selectinload(Product.category),
                selectinload(Product.brand),
                selectinload(Product.variants).selectinload(ProductVariant.images),
                selectinload(Product.images),
                selectinload(Product.attributes),
                selectinload(Product.typed_attribute_values).selectinload(AttributeValue.definition),
            )
            .where(or_(Product.status == None, Product.status.in_(status_filter)), Product.is_active == True)
        )

        # 1. Category Filter (Supports Category and its Subcategories)
        if category_slug:
            cat_res = await db.execute(select(Category).where(Category.slug == category_slug))
            cat_obj = cat_res.scalar_one_or_none()
            if cat_obj:
                category_id = cat_obj.id

        if category_id is not None:
            # Fetch all subcategory IDs
            subcat_res = await db.execute(
                select(Category.id).where(or_(Category.id == category_id, Category.parent_id == category_id))
            )
            cat_ids = [r for r in subcat_res.scalars().all()]
            stmt = stmt.where(Product.category_id.in_(cat_ids))

        # 2. Brand Filter
        if brand_ids and len(brand_ids) > 0:
            stmt = stmt.where(Product.brand_id.in_(brand_ids))

        # 3. Rating Filter
        if min_rating is not None and min_rating > 0:
            stmt = stmt.where(Product.rating_avg >= min_rating)

        # 4. Featured & Bestseller Flags
        if is_featured is not None:
            stmt = stmt.where(Product.is_featured == is_featured)
        if is_bestseller is not None:
            stmt = stmt.where(Product.is_bestseller == is_bestseller)

        # Execute query to retrieve candidate products for in-memory pricing/variant filtering & scoring
        exec_res = await db.execute(stmt)
        products = list(exec_res.scalars().unique().all())

        # Extract dynamic facets from all matching candidate products
        facets = FacetService.calculate_facets(products)

        # 5. Filter variants by Price Range, Stock Availability, and Discount %
        filtered_products: List[Tuple[Product, float, List[str]]] = []

        for p in products:
            if not p.variants:
                continue

            # Find matching active variants for price/stock criteria
            active_vars = [v for v in p.variants if v.is_active]
            if in_stock_only:
                active_vars = [v for v in active_vars if v.stock_quantity > 0]
            if not active_vars:
                continue

            # Calculate min price among active variants
            v_prices = []
            for v in active_vars:
                p_info = PricingService.calculate_discount_details(float(v.price), float(v.discount_price) if v.discount_price else None)
                final_p = p_info["sale_price"]
                v_prices.append((final_p, p_info["discount_percentage"]))

            min_final_price = min(vp[0] for vp in v_prices)
            max_disc_pct = max(vp[1] for vp in v_prices)

            if min_price is not None and min_final_price < min_price:
                continue
            if max_price is not None and min_final_price > max_price:
                continue
            if min_discount_percent is not None and max_disc_pct < min_discount_percent:
                continue

            # Calculate Relevance Score & Match Tags if Query Present
            score = 0.0
            reasons = []
            if query and query.strip():
                skus = [v.sku for v in p.variants]
                attrs = [f"{a.attribute_name} {a.attribute_value}" for a in p.attributes]
                score, reasons = SearchService.calculate_relevance_score(
                    query_raw=query,
                    product_name=p.name,
                    sku_list=skus,
                    brand_name=p.brand.name if p.brand else None,
                    category_name=p.category.name if p.category else None,
                    description=p.description,
                    attributes_list=attrs,
                )
                if score <= 0.0:
                    continue  # Exclude non-matching products when search query provided
            else:
                score = 1.0
                reasons = ["CATALOG_LISTING"]

            filtered_products.append((p, score, reasons))

        # Check Did You Mean spelling suggestion if low/zero results and query present
        did_you_mean = None
        if query and len(filtered_products) == 0:
            vocabulary = set()
            for p in products:
                vocabulary.update(SearchService.tokenize(p.name))
                if p.brand:
                    vocabulary.update(SearchService.tokenize(p.brand.name))
                if p.category:
                    vocabulary.update(SearchService.tokenize(p.category.name))

            did_you_mean = SearchService.generate_did_you_mean(query, vocabulary)

        # 6. Sorting
        if sort_by == "relevance" and query:
            filtered_products.sort(key=lambda item: item[1], reverse=True)
        elif sort_by == "price_asc":
            filtered_products.sort(
                key=lambda item: min((float(v.discount_price or v.price) for v in item[0].variants if v.is_active), default=0.0)
            )
        elif sort_by == "price_desc":
            filtered_products.sort(
                key=lambda item: min((float(v.discount_price or v.price) for v in item[0].variants if v.is_active), default=0.0),
                reverse=True,
            )
        elif sort_by == "rating_desc" or sort_by == "rating":
            filtered_products.sort(key=lambda item: item[0].rating_avg, reverse=True)
        elif sort_by == "newest":
            filtered_products.sort(key=lambda item: item[0].created_at, reverse=True)
        elif sort_by == "popularity" or sort_by == "best_selling":
            filtered_products.sort(key=lambda item: item[0].review_count, reverse=True)
        elif sort_by == "discount_desc":
            filtered_products.sort(
                key=lambda item: max(
                    (
                        PricingService.calculate_discount_details(float(v.price), float(v.discount_price) if v.discount_price else None)["discount_percentage"]
                        for v in item[0].variants
                        if v.is_active
                    ),
                    default=0,
                ),
                reverse=True,
            )

        # 7. Pagination
        total_items = len(filtered_products)
        page_size = min(max(1, limit), 100)
        total_pages = max(1, (total_items + page_size - 1) // page_size)
        current_page = min(max(1, page), total_pages)

        start_idx = (current_page - 1) * page_size
        end_idx = start_idx + page_size
        paginated_tuples = filtered_products[start_idx:end_idx]
        paginated_products = [item[0] for item in paginated_tuples]

        return {
            "items": paginated_products,
            "total": total_items,
            "page": current_page,
            "limit": page_size,
            "pages": total_pages,
            "has_next": current_page < total_pages,
            "has_prev": current_page > 1,
            "query": query,
            "did_you_mean": did_you_mean,
            "facets": facets,
        }

    @staticmethod
    async def get_related_products(
        db: AsyncSession, product: Product, limit: int = 6
    ) -> List[Product]:
        """
        Deterministic algorithm to resolve related products:
        Matches same category or subcategory, same brand, similar price range (+/- 30%).
        """
        stmt = (
            select(Product)
            .options(
                selectinload(Product.category),
                selectinload(Product.brand),
                selectinload(Product.variants).selectinload(ProductVariant.images),
                selectinload(Product.images),
            )
            .where(
                Product.id != product.id,
                Product.status == "ACTIVE",
                Product.is_active == True,
                or_(
                    Product.category_id == product.category_id,
                    Product.brand_id == product.brand_id,
                ),
            )
            .order_by(Product.rating_avg.desc(), Product.review_count.desc())
            .limit(limit)
        )
        res = await db.execute(stmt)
        return list(res.scalars().all())
