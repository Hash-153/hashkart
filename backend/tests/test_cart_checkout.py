from datetime import datetime, timedelta
import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.catalog import Category, Brand, Product, ProductVariant
from app.models.user import User, Address, Role
from app.models.promotion_review import Coupon
from app.core.security import get_password_hash


@pytest.mark.asyncio
async def test_cart_and_checkout_flow(client: AsyncClient, db_session: AsyncSession):
    # 1. Fetch pre-seeded customer role
    role_res = await db_session.execute(select(Role).where(Role.name == "CUSTOMER"))
    role_cust = role_res.scalar_one()

    user = User(
        email="checkoutuser@example.com",
        password_hash=get_password_hash("CheckPass123!"),
        full_name="Checkout User",
        is_active=True,
        roles=[role_cust],
    )
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)

    addr = Address(
        user_id=user.id,
        full_name="Checkout User",
        phone_number="+91 9999911111",
        address_line1="123 Market Road",
        city="Mumbai",
        state="Maharashtra",
        postal_code="400001",
        country="India",
        is_default=True,
    )
    db_session.add(addr)
    await db_session.commit()
    await db_session.refresh(addr)

    # 2. Create Product and Variant
    cat = Category(name="Electronics", slug="elec")
    db_session.add(cat)
    await db_session.commit()

    prod = Product(
        category_id=cat.id,
        name="Wireless Earbuds",
        slug="wireless-earbuds",
        description="Noise cancelling earbuds",
        is_active=True,
    )
    db_session.add(prod)
    await db_session.commit()

    variant = ProductVariant(
        product_id=prod.id,
        sku="EARBUDS-BLK",
        title="Black",
        price=2000.0,
        discount_price=1500.0,
        stock_quantity=20,
        is_active=True,
    )
    db_session.add(variant)
    await db_session.commit()
    await db_session.refresh(variant)

    # 3. Create Coupon (Valid for 30 days)
    now = datetime.utcnow()
    coupon = Coupon(
        code="SAVE100",
        discount_type="FIXED",
        discount_value=100.0,
        min_order_value=500.0,
        is_active=True,
        valid_from=now - timedelta(days=1),
        valid_to=now + timedelta(days=30),
    )
    db_session.add(coupon)
    await db_session.commit()

    # 4. Login to get token
    login_res = await client.post(
        "/auth/login",
        json={"email": "checkoutuser@example.com", "password": "CheckPass123!"},
    )
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 5. Add to Cart
    cart_res = await client.post(
        "/cart/items",
        json={"variant_id": variant.id, "quantity": 2},
        headers=headers,
    )
    assert cart_res.status_code == 200
    cdata = cart_res.json()
    assert cdata["item_count"] == 2
    assert cdata["subtotal"] == 3000.0  # 1500 * 2

    # 6. Validate Coupon
    val_res = await client.post(
        f"/checkout/coupons/validate?code=SAVE100&subtotal={cdata['subtotal']}",
        headers=headers,
    )
    assert val_res.status_code == 200
    assert val_res.json()["discount_amount"] == 100.0

    # 7. Process Checkout & Order Creation
    checkout_res = await client.post(
        "/checkout/process",
        json={
            "address_id": addr.id,
            "coupon_code": "SAVE100",
            "payment_method": "CARD",
            "mock_payment_details": {"simulate_failure": False},
        },
        headers=headers,
    )
    assert checkout_res.status_code == 200
    order_data = checkout_res.json()
    assert order_data["status"] == "CONFIRMED"
    assert order_data["payment_status"] == "PAID"
    assert order_data["discount_amount"] == 100.0
    assert len(order_data["items"]) == 1

    # 8. Check Order History
    orders_res = await client.get("/orders", headers=headers)
    assert orders_res.status_code == 200
    assert len(orders_res.json()) == 1
