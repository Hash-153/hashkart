import pytest
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User, Role
from app.core.security import get_password_hash


@pytest.mark.asyncio
async def test_password_strength_validation(client: AsyncClient):
    """Test registration rejecting weak passwords."""
    res = await client.post(
        "/auth/register",
        json={
            "email": "weakpw@example.com",
            "password": "simplepassword123",  # Lacks uppercase & special char
            "full_name": "Weak Password User",
        },
    )
    assert res.status_code == 400
    assert "Password must contain at least one uppercase letter" in res.json()["detail"]


@pytest.mark.asyncio
async def test_account_lockout_after_five_failed_attempts(
    client: AsyncClient, db_session: AsyncSession
):
    """Test locking account after 5 consecutive incorrect passwords."""
    role_res = await db_session.execute(select(Role).where(Role.name == "CUSTOMER"))
    cust_role = role_res.scalar_one()

    user = User(
        email="lockoutuser@example.com",
        password_hash=get_password_hash("ValidPass123!"),
        full_name="Lockout Test User",
        account_status="ACTIVE",
        is_active=True,
        roles=[cust_role],
    )
    db_session.add(user)
    await db_session.commit()

    # 5 Failed Attempts
    for i in range(5):
        fail_res = await client.post(
            "/auth/login",
            json={"email": "lockoutuser@example.com", "password": "WrongPassword123!"},
        )
        assert fail_res.status_code == 401

    # 6th Attempt should trigger 403 Account Locked
    locked_res = await client.post(
        "/auth/login",
        json={"email": "lockoutuser@example.com", "password": "ValidPass123!"},
    )
    assert locked_res.status_code == 403
    assert "Account is locked" in locked_res.json()["detail"]


@pytest.mark.asyncio
async def test_token_rotation_and_session_revocation(
    client: AsyncClient, db_session: AsyncSession
):
    """Test refresh token rotation and active session revocation."""
    role_res = await db_session.execute(select(Role).where(Role.name == "CUSTOMER"))
    cust_role = role_res.scalar_one()

    user = User(
        email="sessionuser@example.com",
        password_hash=get_password_hash("SessionPass123!"),
        full_name="Session User",
        account_status="ACTIVE",
        is_active=True,
        roles=[cust_role],
    )
    db_session.add(user)
    await db_session.commit()

    # 1. Login
    login_res = await client.post(
        "/auth/login",
        json={"email": "sessionuser@example.com", "password": "SessionPass123!"},
    )
    assert login_res.status_code == 200
    data = login_res.json()
    token = data["access_token"]
    ref_token = data["refresh_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. List Active Sessions
    sess_res = await client.get("/auth/sessions", headers=headers)
    assert sess_res.status_code == 200
    sessions = sess_res.json()
    assert len(sessions) == 1
    assert sessions[0]["is_current"] is True

    # 3. Refresh Tokens
    ref_res = await client.post(f"/auth/refresh?refresh_token={ref_token}")
    assert ref_res.status_code == 200
    new_data = ref_res.json()
    new_ref_token = new_data["refresh_token"]

    # Re-using old refresh token must fail
    reuse_res = await client.post(f"/auth/refresh?refresh_token={ref_token}")
    assert reuse_res.status_code == 401

    # 4. Logout
    logout_res = await client.post("/auth/logout", headers={"Authorization": f"Bearer {new_data['access_token']}"})
    assert logout_res.status_code == 200


@pytest.mark.asyncio
async def test_password_forgot_and_reset_flow(
    client: AsyncClient, db_session: AsyncSession
):
    """Test requesting password reset and confirming new password with simulation token."""
    role_res = await db_session.execute(select(Role).where(Role.name == "CUSTOMER"))
    cust_role = role_res.scalar_one()

    user = User(
        email="resetuser@example.com",
        password_hash=get_password_hash("OldPassword123!"),
        full_name="Reset Test User",
        account_status="ACTIVE",
        is_active=True,
        roles=[cust_role],
    )
    db_session.add(user)
    await db_session.commit()

    # 1. Forgot Password Request
    forgot_res = await client.post("/auth/forgot-password", json={"email": "resetuser@example.com"})
    assert forgot_res.status_code == 200
    forgot_data = forgot_res.json()
    reset_token = forgot_data["dev_simulation_reset_token"]
    assert reset_token is not None

    # 2. Reset Password Execution
    reset_res = await client.post(
        "/auth/reset-password",
        json={"reset_token": reset_token, "new_password": "NewStrongPass123!"},
    )
    assert reset_res.status_code == 200

    # 3. Login with New Password
    login_new = await client.post(
        "/auth/login",
        json={"email": "resetuser@example.com", "password": "NewStrongPass123!"},
    )
    assert login_new.status_code == 200
