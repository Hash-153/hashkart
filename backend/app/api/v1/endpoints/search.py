from typing import List, Optional
from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, desc

from app.database import get_db
from app.models.user import User
from app.models.discovery import UserSearchHistory, SearchQueryAnalytics
from app.schemas.search import (
    SearchResponse,
    AutocompleteSuggestion,
    UserSearchHistoryResponse,
    TrendingSearchResponse,
)
from app.services.catalog_service import CatalogService
from app.services.autocomplete_service import AutocompleteService
from app.services.search_service import SearchService
from app.core.deps import get_current_user_optional, get_current_user as get_current_active_user

router = APIRouter()


@router.get("", response_model=SearchResponse)
async def execute_search(
    q: Optional[str] = Query(None, description="Search query keyword"),
    category_id: Optional[int] = Query(None),
    category_slug: Optional[str] = Query(None),
    brand_id: Optional[List[int]] = Query(None),
    min_price: Optional[float] = Query(None),
    max_price: Optional[float] = Query(None),
    min_rating: Optional[float] = Query(None),
    in_stock_only: bool = Query(False),
    min_discount_percent: Optional[int] = Query(None),
    sort: str = Query("relevance"),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user_optional),
):
    """Unified Search & Composable Filter API with autocomplete, dynamic facets, and spelling suggestions."""
    results = await CatalogService.filter_and_search_products(
        db=db,
        query=q,
        category_id=category_id,
        category_slug=category_slug,
        brand_ids=brand_id,
        min_price=min_price,
        max_price=max_price,
        min_rating=min_rating,
        in_stock_only=in_stock_only,
        min_discount_percent=min_discount_percent,
        sort_by=sort,
        page=page,
        limit=limit,
    )

    # Record search history & analytics if query is present
    if q and q.strip():
        norm_q = SearchService.normalize_query(q)
        if norm_q:
            # 1. User search history
            if current_user:
                history_item = UserSearchHistory(
                    user_id=current_user.id,
                    query=q.strip(),
                    normalized_query=norm_q,
                    result_count=results["total"],
                )
                db.add(history_item)

            # 2. Aggregated analytics update
            sqa_res = await db.execute(
                select(SearchQueryAnalytics).where(SearchQueryAnalytics.normalized_query == norm_q)
            )
            sqa = sqa_res.scalar_one_or_none()
            if sqa:
                sqa.search_count += 1
            else:
                sqa = SearchQueryAnalytics(query=q.strip(), normalized_query=norm_q, search_count=1)
                db.add(sqa)

            await db.commit()

    return results


@router.get("/autocomplete", response_model=List[AutocompleteSuggestion])
async def get_autocomplete_suggestions(
    q: str = Query(..., min_length=2, description="Prefix search query"),
    limit: int = Query(8, ge=1, le=20),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve non-blocking search autocomplete suggestions."""
    return await AutocompleteService.get_suggestions(db, query_raw=q, limit=limit)


@router.get("/trending", response_model=List[TrendingSearchResponse])
async def get_trending_searches(
    limit: int = Query(10, ge=1, le=20),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve top trending search queries."""
    res = await db.execute(
        select(SearchQueryAnalytics)
        .order_by(desc(SearchQueryAnalytics.search_count))
        .limit(limit)
    )
    return res.scalars().all()


@router.get("/history", response_model=List[UserSearchHistoryResponse])
async def get_search_history(
    limit: int = Query(10, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """Get authenticated user search history."""
    res = await db.execute(
        select(UserSearchHistory)
        .where(UserSearchHistory.user_id == current_user.id)
        .order_by(desc(UserSearchHistory.created_at))
        .limit(limit)
    )
    return res.scalars().all()


@router.delete("/history/{history_id}")
async def delete_search_history_item(
    history_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """Delete specific search history entry for current user."""
    res = await db.execute(
        delete(UserSearchHistory).where(
            UserSearchHistory.id == history_id,
            UserSearchHistory.user_id == current_user.id,
        )
    )
    await db.commit()
    if res.rowcount == 0:
        raise HTTPException(status_code=404, detail="Search history item not found or unauthorized.")
    return {"message": "Search history item deleted."}


@router.delete("/history")
async def clear_all_search_history(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """Clear all search history entries for current user."""
    await db.execute(delete(UserSearchHistory).where(UserSearchHistory.user_id == current_user.id))
    await db.commit()
    return {"message": "All search history cleared."}
