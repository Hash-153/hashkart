from typing import List, Dict, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.catalog import Category
from app.core.exceptions import HashKartException


class CategoryService:
    """Category hierarchy business logic & validation service."""

    @staticmethod
    async def get_category_tree(db: AsyncSession) -> List[Category]:
        """Fetch full hierarchical category tree starting from root categories (parent_id is None)."""
        result = await db.execute(
            select(Category)
            .options(
                selectinload(Category.subcategories).selectinload(Category.subcategories)
            )
            .where(Category.parent_id.is_(None), Category.is_active == True)
            .order_by(Category.display_order.asc(), Category.name.asc())
        )
        return list(result.scalars().unique().all())

    @staticmethod
    async def validate_no_circular_parent(
        db: AsyncSession, category_id: int, proposed_parent_id: Optional[int]
    ):
        """
        Validate that proposed_parent_id does not create a circular ancestry loop.
        A category can never be its own parent or a descendant of itself.
        """
        if proposed_parent_id is None:
            return

        if proposed_parent_id == category_id:
            raise HashKartException(
                "A category cannot be set as its own parent.",
                code="CIRCULAR_CATEGORY_RELATIONSHIP",
                status_code=400,
            )

        current_id = proposed_parent_id
        visited = {category_id}

        while current_id is not None:
            if current_id in visited:
                raise HashKartException(
                    "Invalid circular parent category relationship detected.",
                    code="CIRCULAR_CATEGORY_RELATIONSHIP",
                    status_code=400,
                )
            visited.add(current_id)

            res = await db.execute(select(Category.parent_id).where(Category.id == current_id))
            current_id = res.scalar_one_or_none()
