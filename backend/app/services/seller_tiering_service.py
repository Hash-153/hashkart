"""
NovaMart Automated Merchant Tiering & Performance Scorecard Engine
==================================================================
Evaluates seller performance metrics across quarterly cycles:
- Gross Merchandise Value (GMV)
- Order Dispatch SLA Compliance (Breach Rate < 2%)
- Seller Cancellation Rate (Target < 0.5%)
- Product Quality Defect / Customer Return Rate (Target < 5%)
- Average Customer Rating (Target >= 4.3 stars)
Assigns Gold, Silver, or Bronze status with benefits (Reduced commission, prioritized BuyBox).
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import List, Tuple


@dataclass
class SellerPerformanceMetrics:
    seller_id: int
    seller_name: str
    total_gmv: Decimal
    total_orders_fulfilled: int
    dispatch_breach_rate_pct: float
    cancellation_rate_pct: float
    customer_return_rate_pct: float
    average_customer_rating: float
    current_tier: str # 'GOLD', 'SILVER', 'BRONZE'


@dataclass
class TierEvaluationResult:
    seller_id: int
    new_tier: str
    is_tier_upgraded: bool
    is_tier_downgraded: bool
    commission_discount_pct: Decimal
    performance_score: float # 0.0 to 100.0
    qualifying_reasons: List[str]
    improvement_recommendations: List[str]


class SellerTieringEngine:
    @staticmethod
    def calculate_seller_performance_score(metrics: SellerPerformanceMetrics) -> float:
        """Compute holistic performance score out of 100."""
        # 1. Rating component (max 25 pts)
        rating_pts = (metrics.average_customer_rating / 5.0) * 25.0

        # 2. SLA Dispatch component (max 25 pts)
        sla_pts = max(0.0, 25.0 - (metrics.dispatch_breach_rate_pct * 5.0))

        # 3. Low Cancellation component (max 25 pts)
        cancel_pts = max(0.0, 25.0 - (metrics.cancellation_rate_pct * 10.0))

        # 4. Low Returns component (max 25 pts)
        return_pts = max(0.0, 25.0 - (metrics.customer_return_rate_pct * 2.0))

        total = rating_pts + sla_pts + cancel_pts + return_pts
        return round(max(0.0, min(100.0, total)), 2)

    @classmethod
    def evaluate_tier(cls, metrics: SellerPerformanceMetrics) -> TierEvaluationResult:
        """Evaluate quarterly performance to assign new merchant tier."""
        score = cls.calculate_seller_performance_score(metrics)
        qualifying = []
        improvements = []

        # Gold Criteria: Score >= 85, GMV >= ₹5,00,000, Rating >= 4.3, Orders >= 50
        is_gold = (
            score >= 85.0
            and metrics.total_gmv >= Decimal("500000.00")
            and metrics.average_customer_rating >= 4.3
            and metrics.total_orders_fulfilled >= 50
            and metrics.cancellation_rate_pct <= 1.0
        )

        # Silver Criteria: Score >= 70, GMV >= ₹1,00,000, Orders >= 20
        is_silver = (
            score >= 70.0
            and metrics.total_gmv >= Decimal("100000.00")
            and metrics.total_orders_fulfilled >= 20
            and metrics.cancellation_rate_pct <= 2.0
        )

        if is_gold:
            new_tier = "GOLD"
            comm_discount = Decimal("1.50") # 1.5% off commission
            qualifying.append("Exceptional customer rating (>= 4.3 stars)")
            qualifying.append("Flawless dispatch SLA (> 98% on-time)")
            qualifying.append("Exceeded Gold GMV threshold of ₹5,00,000")
        elif is_silver:
            new_tier = "SILVER"
            comm_discount = Decimal("0.75")
            qualifying.append("Solid operational fulfillment consistency")
            qualifying.append("Exceeded Silver GMV threshold of ₹1,00,000")
            if metrics.average_customer_rating < 4.3:
                improvements.append("Increase customer review rating to >= 4.3 for Gold tier")
            if metrics.total_gmv < Decimal("500000.00"):
                improvements.append("Scale sales volume toward ₹5,00,000 Gold threshold")
        else:
            new_tier = "BRONZE"
            comm_discount = Decimal("0.00")
            if metrics.dispatch_breach_rate_pct > 2.0:
                improvements.append("Reduce warehouse dispatch breach delays below 2%")
            if metrics.cancellation_rate_pct > 0.5:
                improvements.append("Eliminate out-of-stock seller cancellations")
            if metrics.customer_return_rate_pct > 5.0:
                improvements.append("Improve product packaging to reduce transit returns")

        tier_ranks = {"BRONZE": 1, "SILVER": 2, "GOLD": 3}
        current_rank = tier_ranks.get(metrics.current_tier.upper(), 1)
        new_rank = tier_ranks[new_tier]

        return TierEvaluationResult(
            seller_id=metrics.seller_id,
            new_tier=new_tier,
            is_tier_upgraded=new_rank > current_rank,
            is_tier_downgraded=new_rank < current_rank,
            commission_discount_pct=comm_discount,
            performance_score=score,
            qualifying_reasons=qualifying,
            improvement_recommendations=improvements,
        )
