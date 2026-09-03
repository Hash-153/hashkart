import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.catalog import Category, Brand, Product, ProductVariant


@pytest.mark.asyncio
async def test_discovery_endpoints(client: AsyncClient, db_session: AsyncSession):
    cat = Category(name="Electronics", slug="electronics", display_order=1, is_active=True)
    brand = Brand(name="HashTech", slug="hashtech", is_active=True)
    db_session.add_all([cat, brand])
    await db_session.flush()

    prod = Product(
        category_id=cat.id,
        brand_id=brand.id,
        name="HashTech Wireless Buds",
        slug="hashtech-wireless-buds",
        description="Premium wireless earbuds",
        status="ACTIVE",
        is_active=True,
    )
    db_session.add(prod)
    await db_session.flush()

    variant = ProductVariant(
        product_id=prod.id,
        sku="HT-EAR-01",
        title="Default Variant",
        price=2999.0,
        discount_price=1999.0,
        stock_quantity=50,
        is_active=True,
    )
    db_session.add(variant)
    await db_session.commit()

    res_rec = await client.get("/discovery/recommended")
    assert res_rec.status_code == 200
    assert res_rec.json()["section_key"] == "recommended_for_you"

    res_best = await client.get("/discovery/best-selling")
    assert res_best.status_code == 200
    assert res_best.json()["section_key"] == "best_selling"

    res_deals = await client.get("/discovery/deals")
    assert res_deals.status_code == 200
    assert res_deals.json()["section_key"] == "top_deals"

    res_news = await client.get("/discovery/new-arrivals")
    assert res_news.status_code == 200
    assert res_news.json()["section_key"] == "new_arrivals"


@pytest.mark.asyncio
async def test_recently_viewed_tracking(client: AsyncClient, db_session: AsyncSession, customer_token: str):
    cat = Category(name="Mobiles", slug="mobiles", display_order=1, is_active=True)
    db_session.add(cat)
    await db_session.flush()

    prod = Product(category_id=cat.id, name="Test Mobile", slug="test-mobile", description="Test", status="ACTIVE", is_active=True)
    db_session.add(prod)
    await db_session.flush()

    variant = ProductVariant(product_id=prod.id, sku="TM-01", title="Default", price=10000.0, stock_quantity=10, is_active=True)
    db_session.add(variant)
    await db_session.commit()

    headers = {"Authorization": f"Bearer {customer_token}"}

    # Record product view
    rec_res = await client.post(f"/discovery/recently-viewed/{prod.id}", headers=headers)
    assert rec_res.status_code == 200

    # Retrieve recently viewed items
    get_res = await client.get("/discovery/recently-viewed", headers=headers)
    assert get_res.status_code == 200
    items = get_res.json()
    assert len(items) >= 1
    assert items[0]["id"] == prod.id
