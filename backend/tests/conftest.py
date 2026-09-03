import pytest
import pytest_asyncio
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.database import Base, get_db
from app.main import app
from app.models.user import User, Role
from app.core.security import get_password_hash

# In-memory Async SQLite for isolated tests
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

test_engine = create_async_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = async_sessionmaker(
    bind=test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with TestingSessionLocal() as session:
        # Seed required system roles
        r_admin = Role(name="ADMIN", description="Super Admin")
        r_staff = Role(name="STAFF", description="Staff")
        r_cust = Role(name="CUSTOMER", description="Customer")
        session.add_all([r_admin, r_staff, r_cust])
        await session.commit()

        yield session

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    async def _override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = _override_get_db
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver/api/v1") as ac:
        yield ac
    app.dependency_overrides.clear()


@pytest_asyncio.fixture(scope="function")
async def customer_token(client: AsyncClient, db_session: AsyncSession) -> str:
    role_res = await db_session.execute(select(Role).where(Role.name == "CUSTOMER"))
    cust_role = role_res.scalar_one()
    user = User(
        email="testcust@hashkart.demo",
        password_hash=get_password_hash("CustPass123!"),
        full_name="Test Customer",
        account_status="ACTIVE",
        is_active=True,
        roles=[cust_role],
    )
    db_session.add(user)
    await db_session.commit()

    res = await client.post("/auth/login", json={"email": "testcust@hashkart.demo", "password": "CustPass123!"})
    return res.json()["access_token"]


@pytest_asyncio.fixture(scope="function")
async def admin_token(client: AsyncClient, db_session: AsyncSession) -> str:
    role_res = await db_session.execute(select(Role).where(Role.name == "ADMIN"))
    admin_role = role_res.scalar_one()
    user = User(
        email="testadmin@hashkart.demo",
        password_hash=get_password_hash("AdminPass123!"),
        full_name="Test Admin",
        account_status="ACTIVE",
        is_active=True,
        roles=[admin_role],
    )
    db_session.add(user)
    await db_session.commit()

    res = await client.post("/auth/login", json={"email": "testadmin@hashkart.demo", "password": "AdminPass123!"})
    return res.json()["access_token"]
