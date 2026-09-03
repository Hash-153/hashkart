from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user
from app.database import get_db
from app.models.user import User
from app.schemas.seller_analytics import SellerDashboardResponse
from app.services.seller_analytics_service import seller_dashboard

router = APIRouter()


@router.get("/dashboard", response_model=SellerDashboardResponse)
async def dashboard(
    days: int = Query(30, ge=1, le=365),
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await seller_dashboard(db, user.id, days)
