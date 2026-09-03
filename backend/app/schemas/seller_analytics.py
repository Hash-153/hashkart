from pydantic import BaseModel, Field


class SellerDashboardResponse(BaseModel):
    seller_id: int | None
    period_days: int = Field(ge=1, le=365)
    active_listings: int
    orders: int
    revenue: float
    pending_payout: float
