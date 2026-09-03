from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user_optional, get_db
from app.models.user import User
from app.schemas.comparison import (
    ProductComparisonMatrixResponse,
    SaveComparisonRequest,
)
from app.services.comparison_service import generate_product_comparison_matrix

router = APIRouter()


@router.get("/matrix", response_model=ProductComparisonMatrixResponse)
async def get_comparison_matrix(
    product_ids: str = Query(..., description="Comma-separated product IDs (e.g. 1,2,3)"),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve side-by-side spec comparison table for up to 4 product IDs."""
    try:
        p_ids = [int(p.strip()) for p in product_ids.split(",") if p.strip().isdigit()]
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid product IDs format",
        )

    if not p_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one valid product ID required",
        )

    return await generate_product_comparison_matrix(db, p_ids)
