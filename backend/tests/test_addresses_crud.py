import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User, Role
from app.core.security import get_password_hash


@pytest.mark.asyncio
async def test_address_book_crud_flow(client: AsyncClient, db_session: AsyncSession):
    """Test creating, listing, updating, setting default shipping, and deleting customer addresses."""
    role_res = await db_session.execute(select(Role).where(Role.name == "CUSTOMER"))
    cust_role = role_res.scalar_one()

    user = User(
        email="addruser@example.com",
        password_hash=get_password_hash("AddrPass123!"),
        full_name="Address User",
        account_status="ACTIVE",
        is_active=True,
        roles=[cust_role],
    )
    db_session.add(user)
    await db_session.commit()

    # Login
    login_res = await client.post(
        "/auth/login",
        json={"email": "addruser@example.com", "password": "AddrPass123!"},
    )
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 1. Invalid Postal Code (Not 6 digits) -> 422 Unprocessable Entity
    inv_res = await client.post(
        "/users/me/addresses",
        json={
            "full_name": "Address User",
            "phone_number": "+91 9999988888",
            "address_line1": "123 Test Street",
            "city": "Mumbai",
            "state": "Maharashtra",
            "postal_code": "123",  # Invalid
            "country": "India",
        },
        headers=headers,
    )
    assert inv_res.status_code == 422

    # 2. Create Valid Address
    create_res = await client.post(
        "/users/me/addresses",
        json={
            "full_name": "Address User",
            "phone_number": "+91 9999988888",
            "address_line1": "Flat 101, Sunshine Heights",
            "address_line2": "Bandra West",
            "locality": "Pali Hill",
            "city": "Mumbai",
            "state": "Maharashtra",
            "postal_code": "400050",
            "country": "India",
            "address_type": "HOME",
            "is_default": True,
            "is_default_shipping": True,
        },
        headers=headers,
    )
    assert create_res.status_code == 201
    addr_data = create_res.json()
    addr_id = addr_data["id"]
    assert addr_data["postal_code"] == "400050"
    assert addr_data["is_default_shipping"] is True

    # 3. List Addresses
    list_res = await client.get("/users/me/addresses", headers=headers)
    assert list_res.status_code == 200
    assert len(list_res.json()) == 1

    # 4. Update Address
    update_res = await client.put(
        f"/users/me/addresses/{addr_id}",
        json={"locality": "Hill Road Bandra"},
        headers=headers,
    )
    assert update_res.status_code == 200
    assert update_res.json()["locality"] == "Hill Road Bandra"

    # 5. Delete Address
    del_res = await client.delete(f"/users/me/addresses/{addr_id}", headers=headers)
    assert del_res.status_code == 200

    # 6. Verify List Empty
    empty_res = await client.get("/users/me/addresses", headers=headers)
    assert empty_res.status_code == 200
    assert len(empty_res.json()) == 0
