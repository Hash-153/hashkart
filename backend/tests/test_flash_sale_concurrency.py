from datetime import datetime, timedelta, timezone
from decimal import Decimal
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.catalog import Brand, Category, Product, ProductVariant
from app.models.loyalty_promotions import FlashSaleEvent, FlashSaleItem, FlashSaleStatus
from app.services.flash_sale_service import get_active_flash_sales, reserve_flash_sale_item


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


@pytest.mark.asyncio
async def test_flash_sale_stock_exhaustion(db_session: AsyncSession):
    """Test flash sale unit reservations and stock exhaustion behavior."""
    cat = Category(name="Mobiles", slug="mobiles-fs")
    brand = Brand(name="Realme", slug="realme-fs")
    db_session.add_all([cat, brand])
    await db_session.flush()

    prod = Product(
        name="Realme GT 6T 5G",
        slug="realme-gt-6t-5g",
        category_id=cat.id,
        brand_id=brand.id,
        description="High performance flagship smartphone with Snapdragon 7+ Gen 3",
    )
    db_session.add(prod)
    await db_session.flush()

    variant = ProductVariant(
        product_id=prod.id,
        sku="RME-GT6T-8-128",
        title="8GB RAM + 128GB Storage",
        price=Decimal("24999.00"),
        discount_price=Decimal("30999.00"),
        stock_quantity=50,
    )
    db_session.add(variant)
    await db_session.flush()

    event = FlashSaleEvent(
        title="Midnight Smartphone Blowout",
        slug="midnight-blowout",
        status=FlashSaleStatus.LIVE,
        starts_at=utcnow() - timedelta(minutes=10),
        ends_at=utcnow() + timedelta(hours=2),
        vip_early_access_minutes=30,
    )
    db_session.add(event)
    await db_session.flush()

    item = FlashSaleItem(
        event_id=event.id,
        product_id=prod.id,
        variant_id=variant.id,
        flash_price=Decimal("19999.00"),
        regular_price=Decimal("24999.00"),
        allocated_stock_units=2,
        claimed_units=0,
        max_units_per_user=1,
    )
    db_session.add(item)
    await db_session.flush()

    # User 1 claims 1 unit
    ok1, msg1, price1 = await reserve_flash_sale_item(db_session, event.id, prod.id, user_id=101, quantity=1)
    assert ok1 is True
    assert price1 == Decimal("19999.00")

    # User 2 claims 1 unit
    ok2, msg2, price2 = await reserve_flash_sale_item(db_session, event.id, prod.id, user_id=102, quantity=1)
    assert ok2 is True

    # User 3 attempts to claim (stock exhausted)
    ok3, msg3, price3 = await reserve_flash_sale_item(db_session, event.id, prod.id, user_id=103, quantity=1)
    assert ok3 is False
    assert "claimed" in msg3.lower()
