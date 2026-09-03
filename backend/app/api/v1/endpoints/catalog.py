from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, or_
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.catalog import (
    Category,
    Brand,
    Product,
    ProductVariant,
    AttributeDefinition,
)
from app.schemas.catalog import (
    CategoryResponse,
    CategoryTreeResponse,
    BrandResponse,
    ProductResponse,
    ProductDetailResponse,
    ProductListResponse,
    AttributeDefinitionResponse,
    PricingSummary,
)
from app.services.category_service import CategoryService
from app.services.catalog_service import CatalogService
from app.services.pricing_service import PricingService

router = APIRouter()


@router.get("/categories", response_model=List[CategoryResponse])
async def get_categories(db: AsyncSession = Depends(get_db)):
    """Fetch top-level active categories with direct subcategories."""
    result = await db.execute(
        select(Category)
        .options(
            selectinload(Category.subcategories).selectinload(Category.subcategories)
        )
        .where(Category.parent_id.is_(None), Category.is_active == True)
        .order_by(Category.display_order.asc(), Category.name.asc())
    )
    return result.scalars().all()


@router.get("/categories/tree", response_model=List[CategoryTreeResponse])
async def get_category_tree(db: AsyncSession = Depends(get_db)):
    """Fetch complete hierarchical category tree."""
    return await CategoryService.get_category_tree(db)


@router.get("/brands", response_model=List[BrandResponse])
async def get_brands(
    featured_only: bool = Query(False),
    db: AsyncSession = Depends(get_db),
):
    """Fetch active catalog brands with product counts."""
    stmt = (
        select(Brand, func.count(Product.id).label("product_count"))
        .outerjoin(Product, Product.brand_id == Brand.id)
        .where(Brand.is_active == True)
        .group_by(Brand.id)
        .order_by(Brand.name.asc())
    )
    if featured_only:
        stmt = stmt.where(Brand.is_featured == True)

    result = await db.execute(stmt)
    rows = result.all()

    brands_out = []
    for brand_obj, p_count in rows:
        b_dict = {
            "id": brand_obj.id,
            "name": brand_obj.name,
            "slug": brand_obj.slug,
            "logo_url": brand_obj.logo_url,
            "description": brand_obj.description,
            "is_active": brand_obj.is_active,
            "is_featured": brand_obj.is_featured,
            "product_count": p_count,
            "created_at": brand_obj.created_at,
        }
        brands_out.append(BrandResponse(**b_dict))

    return brands_out


@router.get("/attributes", response_model=List[AttributeDefinitionResponse])
async def get_attribute_definitions(
    category_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
):
    """Fetch attribute definitions, optionally filtered by category."""
    stmt = select(AttributeDefinition)
    if category_id:
        stmt = stmt.where(or_(AttributeDefinition.category_id == category_id, AttributeDefinition.category_id == None))
    stmt = stmt.order_by(AttributeDefinition.name.asc())

    res = await db.execute(stmt)
    return res.scalars().all()


@router.get("/products", response_model=ProductListResponse)
async def get_products(
    q: Optional[str] = Query(None, description="Search query string"),
    category_id: Optional[int] = Query(None),
    category_slug: Optional[str] = Query(None),
    brand_ids: Optional[List[int]] = Query(None),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    min_rating: Optional[float] = Query(None, ge=0, le=5),
    in_stock_only: bool = Query(False),
    min_discount: Optional[int] = Query(None, ge=0, le=100),
    featured: Optional[bool] = Query(None),
    bestseller: Optional[bool] = Query(None),
    sort: str = Query("relevance", description="relevance, price_asc, price_desc, rating, newest, popularity, discount_desc"),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    """
    Search and filter catalog products with multi-attribute criteria, weighted relevance,
    pricing calculations, sorting, and pagination.
    """
    res = await CatalogService.filter_and_search_products(
        db=db,
        query=q,
        category_id=category_id,
        category_slug=category_slug,
        brand_ids=brand_ids,
        min_price=min_price,
        max_price=max_price,
        min_rating=min_rating,
        in_stock_only=in_stock_only,
        min_discount_percent=min_discount,
        is_featured=featured,
        is_bestseller=bestseller,
        sort_by=sort,
        page=page,
        limit=limit,
    )
    return ProductListResponse(**res)


@router.get("/products/{id_or_slug}", response_model=ProductDetailResponse)
async def get_product_detail(
    id_or_slug: str,
    db: AsyncSession = Depends(get_db),
):
    """
    Fetch comprehensive product detail view including variants, images, specifications,
    pricing calculation breakdown, and related products recommendations.
    """
    stmt = (
        select(Product)
        .options(
            selectinload(Product.category),
            selectinload(Product.brand),
            selectinload(Product.variants).selectinload(ProductVariant.images),
            selectinload(Product.images),
            selectinload(Product.attributes),
            selectinload(Product.typed_attribute_values),
        )
        .where(Product.is_active == True, Product.status != "ARCHIVED")
    )

    if id_or_slug.isdigit():
        stmt = stmt.where(Product.id == int(id_or_slug))
    else:
        stmt = stmt.where(Product.slug == id_or_slug)

    result = await db.execute(stmt)
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product '{id_or_slug}' not found or unavailable.",
        )

    # Compute Pricing Summary based on primary variant
    pricing_sum = None
    if product.variants:
        active_vars = [v for v in product.variants if v.is_active]
        target_v = active_vars[0] if active_vars else product.variants[0]
        p_calc = PricingService.calculate_discount_details(
            float(target_v.price), float(target_v.discount_price) if target_v.discount_price else None
        )
        pricing_sum = PricingSummary(**p_calc)

    # Resolve Related Products
    related_objs = await CatalogService.get_related_products(db, product, limit=6)
    related_responses = [ProductResponse.model_validate(p) for p in related_objs]

    p_dict = ProductResponse.model_validate(product).model_dump()
    p_dict["pricing_summary"] = pricing_sum
    p_dict["related_products"] = related_responses

    return ProductDetailResponse(**p_dict)
