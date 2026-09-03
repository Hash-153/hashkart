from datetime import datetime, timedelta
from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.database import get_db
from app.models.order_payment import Order
from app.schemas.system import AnalyticsSalesResponse, SalesAnalyticsPoint
from app.models.user import User
from app.core.deps import require_staff

router = APIRouter()


@router.get("/sales", response_model=AnalyticsSalesResponse)
async def get_sales_analytics(
    days: int = Query(7, ge=1, le=90),
    admin_user: User = Depends(require_staff),
    db: AsyncSession = Depends(get_db),
):
    """Fetch daily sales revenue and order counts for analytics charts."""
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=days - 1)

    points: List[SalesAnalyticsPoint] = []
    curr = start_date

    while curr <= end_date:
        curr_str = curr.strftime("%Y-%m-%d")
        next_day = curr + timedelta(days=1)

        stmt = select(
            func.sum(Order.grand_total), func.count(Order.id)
        ).where(
            Order.created_at >= datetime.combine(curr, datetime.min.time()),
            Order.created_at < datetime.combine(next_day, datetime.min.time()),
            Order.payment_status.in_(["PAID", "PENDING"]),
        )
        res = await db.execute(stmt)
        total_sum, count = res.first()

        points.append(
            SalesAnalyticsPoint(
                date=curr_str,
                sales_amount=round(float(total_sum or 0.0), 2),
                orders_count=count or 0,
            )
        )
        curr += timedelta(days=1)

    return AnalyticsSalesResponse(timeframe=f"Last {days} Days", data_points=points)
