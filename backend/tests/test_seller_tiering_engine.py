from decimal import Decimal
import pytest

from app.services.seller_tiering_service import (
    SellerPerformanceMetrics,
    SellerTieringEngine,
)


def test_seller_tier_gold_promotion():
    metrics = SellerPerformanceMetrics(
        seller_id=1,
        seller_name="Elite Retailers",
        total_gmv=Decimal("1250000.00"),
        total_orders_fulfilled=120,
        dispatch_breach_rate_pct=0.5,
        cancellation_rate_pct=0.2,
        customer_return_rate_pct=2.1,
        average_customer_rating=4.8,
        current_tier="SILVER",
    )

    res = SellerTieringEngine.evaluate_tier(metrics)
    assert res.new_tier == "GOLD"
    assert res.is_tier_upgraded is True
    assert res.commission_discount_pct == Decimal("1.50")
    assert res.performance_score > 90.0


def test_seller_tier_bronze_maintenance():
    metrics = SellerPerformanceMetrics(
        seller_id=2,
        seller_name="New Seller Store",
        total_gmv=Decimal("45000.00"),
        total_orders_fulfilled=8,
        dispatch_breach_rate_pct=4.0,
        cancellation_rate_pct=3.5,
        customer_return_rate_pct=6.2,
        average_customer_rating=3.9,
        current_tier="BRONZE",
    )

    res = SellerTieringEngine.evaluate_tier(metrics)
    assert res.new_tier == "BRONZE"
    assert res.is_tier_upgraded is False
    assert len(res.improvement_recommendations) >= 2
