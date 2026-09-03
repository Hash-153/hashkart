from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict


class NotificationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    title: str
    message: str
    notification_type: str
    is_read: bool
    link: Optional[str] = None
    created_at: datetime


class AuditLogResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: Optional[int] = None
    action: str
    entity_type: Optional[str] = None
    entity_id: Optional[str] = None
    ip_address: Optional[str] = None
    details: Optional[str] = None
    created_at: datetime


class DashboardStatsResponse(BaseModel):
    total_sales_revenue: float
    total_orders_count: int
    total_customers_count: int
    total_products_count: int
    low_stock_products_count: int
    pending_orders_count: int
    average_order_value: float


class SalesAnalyticsPoint(BaseModel):
    date: str
    sales_amount: float
    orders_count: int


class AnalyticsSalesResponse(BaseModel):
    timeframe: str
    data_points: List[SalesAnalyticsPoint]
