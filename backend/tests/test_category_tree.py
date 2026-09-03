import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.catalog import Category
from app.services.category_service import CategoryService
from app.core.exceptions import HashKartException


@pytest.mark.asyncio
async def test_category_tree_hierarchy_retrieval(client: AsyncClient, db_session: AsyncSession):
    """Test retrieving hierarchical category tree."""
    c_root = Category(name="Electronics Root", slug="electronics-root", display_order=1, is_active=True)
    db_session.add(c_root)
    await db_session.commit()
    await db_session.refresh(c_root)

    c_sub = Category(name="Smartphones Sub", slug="smartphones-sub", parent_id=c_root.id, display_order=1, is_active=True)
    db_session.add(c_sub)
    await db_session.commit()
    await db_session.refresh(c_sub)
    db_session.expire_all()

    # Direct service call check
    direct_tree = await CategoryService.get_category_tree(db_session)
    assert len(direct_tree) >= 1
    d_root = [c for c in direct_tree if c.slug == "electronics-root"][0]
    assert len(d_root.subcategories) == 1
    assert d_root.subcategories[0].slug == "smartphones-sub"

    # API Endpoint check
    res = await client.get("/catalog/categories/tree")
    assert res.status_code == 200
    tree = res.json()
    assert len(tree) >= 1
    root_match = [c for c in tree if c["slug"] == "electronics-root"]
    assert len(root_match) == 1
    assert len(root_match[0]["subcategories"]) == 1
    assert root_match[0]["subcategories"][0]["slug"] == "smartphones-sub"


@pytest.mark.asyncio
async def test_circular_category_parent_validation(db_session: AsyncSession):
    """Test circular hierarchy validation in CategoryService."""
    c1 = Category(name="Cat One", slug="cat-one", is_active=True)
    c2 = Category(name="Cat Two", slug="cat-two", is_active=True)
    db_session.add_all([c1, c2])
    await db_session.flush()

    # Make c2 child of c1
    c2.parent_id = c1.id
    await db_session.commit()

    # Attempting to make c1 child of c2 must trigger HashKartException
    with pytest.raises(HashKartException) as exc_info:
        await CategoryService.validate_no_circular_parent(db_session, category_id=c1.id, proposed_parent_id=c2.id)

    assert "circular" in str(exc_info.value).lower()
