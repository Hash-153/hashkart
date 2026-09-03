from typing import List, Optional
from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas.catalog import ProductDetailResponse
from app.schemas.discovery import DiscoverySection
from app.services.recommendation_service import RecommendationService
from app.services.recently_viewed_service import RecentlyViewedService
from app.core.deps import get_current_user_optional, get_current_user as get_current_active_user

router = APIRouter()


@router.get("/recommended", response_model=DiscoverySection)
async def get_personalized_recommendations(
    limit: int = Query(10, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user_optional),
):
    """Retrieve personalized product recommendations based on user signals or fallback bestsellers."""
    user_id = current_user.id if current_user else None
    products = await RecommendationService.get_personalized_recommendations(db, user_id=user_id, limit=limit)
    return {
        "section_key": "recommended_for_you",
        "title": "Recommended For You",
        "subtitle": "Handpicked selections based on your browsing & shopping preferences",
        "layout_type": "carousel",
        "products": products,
    }


@router.get("/best-selling", response_model=DiscoverySection)
async def get_best_selling_products(
    limit: int = Query(10, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve top best-selling products ranked by total sales quantity."""
    products = await RecommendationService.get_best_selling_products(db, limit=limit)
    return {
        "section_key": "best_selling",
        "title": "Best-Selling Products",
        "subtitle": "Top customer favorites across HashKart",
        "layout_type": "carousel",
        "products": products,
    }


@router.get("/deals", response_model=DiscoverySection)
async def get_top_deals(
    limit: int = Query(10, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve top discounted deal products."""
    products = await RecommendationService.get_top_deals(db, limit=limit)
    return {
        "section_key": "top_deals",
        "title": "Top Deals & Discounts",
        "subtitle": "Unbeatable price cuts on high-rated products",
        "layout_type": "carousel",
        "products": products,
    }


@router.get("/new-arrivals", response_model=DiscoverySection)
async def get_new_arrivals(
    limit: int = Query(10, ge=1, le=50),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve latest new arrival products."""
    products = await RecommendationService.get_new_arrivals(db, limit=limit)
    return {
        "section_key": "new_arrivals",
        "title": "New Arrivals",
        "subtitle": "Freshly launched tech, fashion, and home products",
        "layout_type": "carousel",
        "products": products,
    }


@router.get("/recently-viewed", response_model=List[ProductDetailResponse])
async def get_recently_viewed(
    limit: int = Query(12, ge=1, le=30),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """Retrieve authenticated user recently viewed products."""
    return await RecentlyViewedService.get_user_recently_viewed(db, user_id=current_user.id, limit=limit)


@router.post("/recently-viewed/{product_id}")
async def record_recently_viewed(
    product_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """Record product view for authenticated user."""
    await RecentlyViewedService.record_product_view(db, user_id=current_user.id, product_id=product_id)
    return {"message": "Product view recorded."}


@router.delete("/recently-viewed")
async def clear_recently_viewed(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
):
    """Clear all recently viewed items for authenticated user."""
    await RecentlyViewedService.clear_recently_viewed(db, user_id=current_user.id)
    return {"message": "Recently viewed history cleared."}
