from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, update, delete
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.user import User
from app.models.catalog import (
    Category,
    Brand,
    Product,
    ProductVariant,
    ProductImage,
    ProductAttribute,
    AttributeDefinition,
)
from app.models.order_payment import Order, OrderItem
from app.models.promotion_review import Coupon, Review
from app.models.system import AuditLog, Notification
from app.schemas.system import DashboardStatsResponse, AuditLogResponse
from app.schemas.catalog import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    ProductVariantCreate,
    ProductVariantResponse,
    ProductImageCreate,
    ProductImageResponse,
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
    BrandCreate,
    BrandUpdate,
    BrandResponse,
    AttributeDefinitionCreate,
    AttributeDefinitionResponse,
)
from app.schemas.order_payment import OrderResponse, OrderStatusUpdate
from app.schemas.promotion_review import CouponCreate, CouponResponse, ReviewResponse
from app.schemas.checkout_enhanced import InventoryAdjustmentRequest
from app.services.inventory_service import InventoryService
from app.core.deps import require_admin, require_staff
from app.services.category_service import CategoryService

router = APIRouter()


@router.get("/dashboard/stats", response_model=DashboardStatsResponse)
async def get_dashboard_stats(
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Fetch high-level admin KPI metrics."""
    rev_res = await db.execute(select(func.sum(Order.grand_total)).where(Order.payment_status == "PAID"))
    total_sales_revenue = float(rev_res.scalar() or 0.0)

    orders_res = await db.execute(select(func.count(Order.id)))
    total_orders_count = orders_res.scalar() or 0

    cust_res = await db.execute(select(func.count(User.id)))
    total_customers_count = cust_res.scalar() or 0

    prod_res = await db.execute(select(func.count(Product.id)))
    total_products_count = prod_res.scalar() or 0

    low_stock_res = await db.execute(
        select(func.count(ProductVariant.id)).where(ProductVariant.stock_quantity <= 5)
    )
    low_stock_products_count = low_stock_res.scalar() or 0

    pending_res = await db.execute(
        select(func.count(Order.id)).where(Order.status.in_(["PENDING", "CONFIRMED", "PACKED"]))
    )
    pending_orders_count = pending_res.scalar() or 0

    average_order_value = round(total_sales_revenue / total_orders_count, 2) if total_orders_count > 0 else 0.0

    return DashboardStatsResponse(
        total_sales_revenue=round(total_sales_revenue, 2),
        total_orders_count=total_orders_count,
        total_customers_count=total_customers_count,
        total_products_count=total_products_count,
        low_stock_products_count=low_stock_products_count,
        pending_orders_count=pending_orders_count,
        average_order_value=average_order_value,
    )


# --- CATEGORY ADMINISTRATION ---
@router.post("/categories", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    cat_in: CategoryCreate,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Create a catalog category."""
    slug = cat_in.name.lower().replace(" ", "-").replace("/", "-")
    existing = await db.execute(select(Category).where(Category.slug == slug))
    if existing.scalar_one_or_none():
        slug = f"{slug}-{int(func.now())}"

    new_cat = Category(
        name=cat_in.name,
        slug=slug,
        parent_id=cat_in.parent_id,
        description=cat_in.description,
        image_url=cat_in.image_url,
        display_order=cat_in.display_order,
        is_active=cat_in.is_active,
    )
    db.add(new_cat)

    audit = AuditLog(
        user_id=admin_user.id,
        action="CATEGORY_CREATE",
        entity_type="Category",
        details=f"Created category {cat_in.name}",
    )
    db.add(audit)
    await db.commit()
    await db.refresh(new_cat)
    return new_cat


@router.put("/categories/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: int,
    cat_in: CategoryUpdate,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Update a category with circular parent validation."""
    cat_res = await db.execute(select(Category).where(Category.id == category_id))
    cat = cat_res.scalar_one_or_none()
    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found.")

    if cat_in.parent_id is not None:
        await CategoryService.validate_no_circular_parent(db, category_id, cat_in.parent_id)

    for field, val in cat_in.model_dump(exclude_unset=True).items():
        setattr(cat, field, val)

    audit = AuditLog(
        user_id=admin_user.id,
        action="CATEGORY_UPDATE",
        entity_type="Category",
        entity_id=str(category_id),
        details=f"Updated category {cat.name}",
    )
    db.add(audit)
    await db.commit()
    await db.refresh(cat)
    return cat


@router.delete("/categories/{category_id}")
async def delete_category(
    category_id: int,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Delete a category."""
    cat_res = await db.execute(select(Category).where(Category.id == category_id))
    cat = cat_res.scalar_one_or_none()
    if not cat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found.")

    await db.delete(cat)
    await db.commit()
    return {"message": f"Category {category_id} deleted."}


# --- BRAND ADMINISTRATION ---
@router.post("/brands", response_model=BrandResponse, status_code=status.HTTP_201_CREATED)
async def create_brand(
    brand_in: BrandCreate,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Create a catalog brand."""
    slug = brand_in.name.lower().replace(" ", "-").replace("/", "-")
    existing = await db.execute(select(Brand).where(Brand.slug == slug))
    if existing.scalar_one_or_none():
        slug = f"{slug}-{int(func.now())}"

    new_brand = Brand(
        name=brand_in.name,
        slug=slug,
        logo_url=brand_in.logo_url,
        description=brand_in.description,
        is_active=brand_in.is_active,
        is_featured=brand_in.is_featured,
    )
    db.add(new_brand)
    await db.commit()
    await db.refresh(new_brand)
    return BrandResponse(
        id=new_brand.id,
        name=new_brand.name,
        slug=new_brand.slug,
        logo_url=new_brand.logo_url,
        description=new_brand.description,
        is_active=new_brand.is_active,
        is_featured=new_brand.is_featured,
        product_count=0,
        created_at=new_brand.created_at,
    )


@router.put("/brands/{brand_id}", response_model=BrandResponse)
async def update_brand(
    brand_id: int,
    brand_in: BrandUpdate,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Update a catalog brand."""
    b_res = await db.execute(select(Brand).where(Brand.id == brand_id))
    brand = b_res.scalar_one_or_none()
    if not brand:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Brand not found.")

    for field, val in brand_in.model_dump(exclude_unset=True).items():
        setattr(brand, field, val)

    await db.commit()
    await db.refresh(brand)
    return BrandResponse(
        id=brand.id,
        name=brand.name,
        slug=brand.slug,
        logo_url=brand.logo_url,
        description=brand.description,
        is_active=brand.is_active,
        is_featured=brand.is_featured,
        product_count=0,
        created_at=brand.created_at,
    )


# --- PRODUCT & VARIANT ADMINISTRATION ---
@router.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Create a catalog product with full metadata."""
    base_slug = product_in.name.lower().replace(" ", "-").replace("/", "-")
    slug = base_slug
    idx = 1
    while True:
        existing = await db.execute(select(Product).where(Product.slug == slug))
        if not existing.scalar_one_or_none():
            break
        slug = f"{base_slug}-{idx}"
        idx += 1

    new_product = Product(
        category_id=product_in.category_id,
        brand_id=product_in.brand_id,
        name=product_in.name,
        slug=slug,
        description=product_in.description,
        short_description=product_in.short_description,
        highlight_features=product_in.highlight_features,
        status=product_in.status,
        visibility=product_in.visibility,
        is_active=product_in.is_active,
        is_featured=product_in.is_featured,
        is_bestseller=product_in.is_bestseller,
        meta_title=product_in.meta_title,
        meta_keywords=product_in.meta_keywords,
        meta_description=product_in.meta_description,
    )
    db.add(new_product)

    audit = AuditLog(
        user_id=admin_user.id,
        action="PRODUCT_CREATE",
        entity_type="Product",
        details=f"Created product {product_in.name}",
    )
    db.add(audit)

    await db.commit()
    
    res = await db.execute(
        select(Product)
        .options(
            selectinload(Product.category),
            selectinload(Product.brand),
            selectinload(Product.variants),
            selectinload(Product.images),
            selectinload(Product.attributes),
        )
        .where(Product.id == new_product.id)
    )
    return res.scalar_one()


@router.put("/products/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: int,
    product_in: ProductUpdate,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Update a product."""
    res = await db.execute(select(Product).where(Product.id == product_id))
    prod = res.scalar_one_or_none()
    if not prod:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found.")

    for field, val in product_in.model_dump(exclude_unset=True).items():
        setattr(prod, field, val)

    await db.commit()
    
    res = await db.execute(
        select(Product)
        .options(
            selectinload(Product.category),
            selectinload(Product.brand),
            selectinload(Product.variants),
            selectinload(Product.images),
            selectinload(Product.attributes),
        )
        .where(Product.id == product_id)
    )
    return res.scalar_one()


@router.post("/products/{product_id}/variants", response_model=ProductVariantResponse, status_code=status.HTTP_201_CREATED)
async def add_product_variant(
    product_id: int,
    variant_in: ProductVariantCreate,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Add a variant SKU to an existing product."""
    sku_exist = await db.execute(select(ProductVariant).where(ProductVariant.sku == variant_in.sku))
    if sku_exist.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Variant SKU '{variant_in.sku}' already exists.",
        )

    new_variant = ProductVariant(
        product_id=product_id,
        sku=variant_in.sku,
        title=variant_in.title,
        price=variant_in.price,
        discount_price=variant_in.discount_price,
        stock_quantity=variant_in.stock_quantity,
        weight_grams=variant_in.weight_grams,
        dimensions=variant_in.dimensions,
        is_active=variant_in.is_active,
    )
    db.add(new_variant)
    await db.commit()
    await db.refresh(new_variant)
    return new_variant


# --- INVENTORY CONTROL ---
@router.post("/inventory/adjust", response_model=ProductVariantResponse)
async def admin_adjust_inventory(
    adj_in: InventoryAdjustmentRequest,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Manual inventory stock adjustment with audit logging."""
    try:
        return await InventoryService.admin_adjust_stock(
            db=db,
            variant_id=adj_in.variant_id,
            new_quantity=adj_in.new_quantity,
            reason=adj_in.reason,
            actor_id=admin_user.id,
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/inventory/cleanup-reservations")
async def cleanup_expired_inventory_reservations(
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Force release expired inventory reservations."""
    released_count = await InventoryService.cleanup_expired_reservations(db)
    return {"message": f"Successfully released {released_count} expired inventory reservations."}


# --- ORDERS & AUDIT ---
@router.get("/orders", response_model=List[OrderResponse])
async def list_all_orders(
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """List all customer orders platform-wide."""
    result = await db.execute(select(Order).order_by(Order.created_at.desc()))
    return result.scalars().all()


@router.put("/orders/{order_id}/status", response_model=OrderResponse)
async def update_order_status(
    order_id: int,
    status_in: OrderStatusUpdate,
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Update order lifecycle status (PACKED, SHIPPED, DELIVERED)."""
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found.")

    order.status = status_in.status

    if status_in.status == "DELIVERED":
        order.payment_status = "PAID"
        if order.shipment:
            order.shipment.shipment_status = "DELIVERED"

    notif = Notification(
        user_id=order.user_id,
        title="Order Status Updated",
        message=f"Your order {order.order_number} status has been updated to {status_in.status}.",
        notification_type="ORDER",
        link=f"/orders/{order.order_number}",
    )
    db.add(notif)

    audit = AuditLog(
        user_id=admin_user.id,
        action="ORDER_STATUS_UPDATE",
        entity_type="Order",
        entity_id=str(order_id),
        details=f"Updated order {order.order_number} status to {status_in.status}",
    )
    db.add(audit)

    await db.commit()
    await db.refresh(order)
    return order


@router.get("/audit-logs", response_model=List[AuditLogResponse])
async def list_audit_logs(
    admin_user: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    """View system security audit trail."""
    result = await db.execute(select(AuditLog).order_by(AuditLog.created_at.desc()).limit(100))
    return result.scalars().all()
