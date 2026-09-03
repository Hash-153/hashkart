import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.catalog import Category, Brand, Product, ProductVariant


@pytest.mark.asyncio
async def test_get_categories_and_products(client: AsyncClient, db_session: AsyncSession):
    # Seed category & brand
    cat = Category(name="Mobiles", slug="mobiles", display_order=1, is_active=True)
    brand = Brand(name="Nexus", slug="nexus", is_active=True)
    db_session.add_all([cat, brand])
    await db_session.commit()

    prod = Product(
        category_id=cat.id,
        brand_id=brand.id,
        name="Nexus Phone 1",
        slug="nexus-phone-1",
        description="Flagship smartphone",
        status="ACTIVE",
        is_active=True,
    )
    db_session.add(prod)
    await db_session.commit()

    variant = ProductVariant(
        product_id=prod.id,
        sku="NEXUS-P1-128",
        title="128GB Black",
        price=30000.0,
        discount_price=25000.0,
        stock_quantity=10,
        is_active=True,
    )
    db_session.add(variant)
    await db_session.commit()
    db_session.expire_all()

    # Test /catalog/categories
    cat_res = await client.get("/catalog/categories")
    assert cat_res.status_code == 200
    assert len(cat_res.json()) == 1

    # Test /catalog/products
    prod_res = await client.get("/catalog/products?q=Nexus")
    assert prod_res.status_code == 200
    pdata = prod_res.json()
    assert pdata["total"] == 1
    assert pdata["items"][0]["name"] == "Nexus Phone 1"
