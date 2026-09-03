import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User, Role, Permission
from app.core.security import get_password_hash


@pytest.mark.asyncio
async def test_rbac_permission_guards(client: AsyncClient, db_session: AsyncSession):
    """Test RBAC role and permission guards across CUSTOMER and ADMIN roles."""
    # Seed roles if needed
    r_res = await db_session.execute(select(Role).where(Role.name == "CUSTOMER"))
    cust_role = r_res.scalar_one()

    a_res = await db_session.execute(select(Role).where(Role.name == "ADMIN"))
    admin_role = a_res.scalar_one()

    cust_user = User(
        email="ordinarycust@example.com",
        password_hash=get_password_hash("CustPass123!"),
        full_name="Ordinary Customer",
        account_status="ACTIVE",
        is_active=True,
        roles=[cust_role],
    )
    admin_user = User(
        email="superadmin@example.com",
        password_hash=get_password_hash("AdminPass123!"),
        full_name="Super Admin User",
        account_status="ACTIVE",
        is_active=True,
        roles=[admin_role],
    )
    db_session.add_all([cust_user, admin_user])
    await db_session.commit()

    # Login Customer
    c_login = await client.post(
        "/auth/login",
        json={"email": "ordinarycust@example.com", "password": "CustPass123!"},
    )
    c_token = c_login.json()["access_token"]
    c_headers = {"Authorization": f"Bearer {c_token}"}

    # Customer trying to access Admin dashboard endpoint -> 403 Forbidden
    admin_dashboard_res = await client.get("/admin/dashboard/stats", headers=c_headers)
    assert admin_dashboard_res.status_code == 403

    # Login Admin
    a_login = await client.post(
        "/auth/login",
        json={"email": "superadmin@example.com", "password": "AdminPass123!"},
    )
    a_token = a_login.json()["access_token"]
    a_headers = {"Authorization": f"Bearer {a_token}"}

    # Admin accessing Admin dashboard endpoint -> 200 OK
    admin_ok_res = await client.get("/admin/dashboard/stats", headers=a_headers)
    assert admin_ok_res.status_code == 200
