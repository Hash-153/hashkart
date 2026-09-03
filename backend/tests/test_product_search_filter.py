import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.catalog import Category, Brand, Product, ProductVariant


@pytest.mark.asyncio
async def test_search_and_composable_filtering(client: AsyncClient, db_session: AsyncSession):
    """Test searching products by query, filtering by category/brand/price/rating, and sorting."""
    # Seed category & brand
    cat = Category(name="Mobiles Tech", slug="mobiles-tech")
    brand = Brand(name="HashMobile", slug="hashmobile")
    db_session.add_all([cat, brand])
    await db_session.flush()

    p1 = Product(
        category_id=cat.id,
        brand_id=brand.id,
        name="HashMobile Flagship Pro 5G",
        slug="hashmobile-flagship-pro-5g",
        description="Flagship smartphone with 50MP OIS camera and 120Hz display.",
        rating_avg=4.8,
        review_count=100,
        status="ACTIVE",
        is_active=True,
    )
    p2 = Product(
        category_id=cat.id,
        brand_id=brand.id,
        name="Budget Phone Lite",
        slug="budget-phone-lite",
        description="Basic entry level mobile phone.",
        rating_avg=3.5,
        review_count=10,
        status="ACTIVE",
        is_active=True,
    )
    db_session.add_all([p1, p2])
    await db_session.flush()

    v1 = ProductVariant(product_id=p1.id, sku="HM-PRO-5G", title="128GB", price=40000.0, discount_price=35000.0, stock_quantity=20)
    v2 = ProductVariant(product_id=p2.id, sku="BP-LITE-32", title="32GB", price=8000.0, discount_price=7500.0, stock_quantity=5)
    db_session.add_all([v1, v2])
    await db_session.commit()

    # 1. Search Query "Flagship"
    search_res = await client.get("/catalog/products?q=Flagship")
    assert search_res.status_code == 200
    s_data = search_res.json()
    assert s_data["total"] == 1
    assert s_data["items"][0]["slug"] == "hashmobile-flagship-pro-5g"

    # 2. Min Rating Filter >= 4.0
    rating_res = await client.get("/catalog/products?min_rating=4.0")
    assert rating_res.status_code == 200
    r_data = rating_res.json()
    assert r_data["total"] == 1
    assert r_data["items"][0]["slug"] == "hashmobile-flagship-pro-5g"

    # 3. Price Filter (min_price=30000, max_price=50000)
    price_res = await client.get("/catalog/products?min_price=30000&max_price=50000")
    assert price_res.status_code == 200
    p_data = price_res.json()
    assert p_data["total"] == 1
    assert p_data["items"][0]["slug"] == "hashmobile-flagship-pro-5g"
