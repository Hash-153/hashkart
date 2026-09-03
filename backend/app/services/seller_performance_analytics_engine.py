"""
NovaMart Merchant Performance Scorecard & BuyBox Competitiveness Engine
========================================================================
Comprehensive seller tiering, defect monitoring, and algorithmic marketplace governance:
- Order Defect Rate (ODR) = (Negative Reviews + A-to-Z Claims + Chargebacks) / Total Orders (Target < 1.0%)
- Late Dispatch Rate (LDR) = Orders dispatched after promised SLA / Total Orders (Target < 4.0%)
- Pre-fulfillment Cancellation Rate (CR) = Seller-initiated cancellations / Total Orders (Target < 2.5%)
- Return Rate (RR) & Quality Discrepancy Monitoring
- Automated Merchant Tiering (PLATINUM, GOLD, SILVER, BRONZE, PROBATION, SUSPENDED)
- Dynamic Commission Rebates: Platinum sellers get 20% discount on marketplace fees
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Tuple


class MerchantTier(str, Enum):
    PLATINUM = "PLATINUM"
    GOLD = "GOLD"
    SILVER = "SILVER"
    BRONZE = "BRONZE"
    PROBATION = "PROBATION"
    SUSPENDED = "SUSPENDED"


@dataclass
class SellerPerformanceMetrics:
    seller_id: int
    seller_name: str
    evaluation_window_days: int
    total_orders_evaluated: int
    gross_merchandise_value: Decimal
    order_defect_count: int
    late_dispatch_count: int
    seller_cancelled_count: int
    customer_return_count: int
    average_customer_rating: float


@dataclass
class SellerScorecardReport:
    seller_id: int
    seller_name: str
    order_defect_rate: float # %
    late_dispatch_rate: float # %
    cancellation_rate: float # %
    return_rate: float # %
    assigned_tier: MerchantTier
    commission_discount_percent: Decimal
    buybox_competitiveness_multiplier: float
    is_fbf_eligible: bool # Fulfilled by NovaMart
    enforcement_warning: Optional[str] = None


class SellerPerformanceAnalyticsEngine:
    @classmethod
    def evaluate_seller_performance(
        cls,
        metrics: SellerPerformanceMetrics,
    ) -> SellerScorecardReport:
        """Compute all defect metrics and calculate quarterly merchant tier."""
        total = max(1, metrics.total_orders_evaluated)

        odr = round((metrics.order_defect_count / total) * 100.0, 2)
        ldr = round((metrics.late_dispatch_count / total) * 100.0, 2)
        cr = round((metrics.seller_cancelled_count / total) * 100.0, 2)
        rr = round((metrics.customer_return_count / total) * 100.0, 2)

        # Tier & Governance Logic
        warning = None
        if odr > 2.0 or cr > 5.0:
            tier = MerchantTier.SUSPENDED
            warning = "Account suspended due to excessive defect rate exceeding 2.0%."
            comm_discount = Decimal("0.0")
            buybox_mult = 0.0
            fbf = False
        elif odr > 1.0 or ldr > 4.0 or cr > 2.5:
            tier = MerchantTier.PROBATION
            warning = "Account placed on 14-day performance probation."
            comm_discount = Decimal("0.0")
            buybox_mult = 0.60
            fbf = False
        elif metrics.gross_merchandise_value >= Decimal("5000000.00") and metrics.average_customer_rating >= 4.7 and ldr <= 1.0:
            tier = MerchantTier.PLATINUM
            comm_discount = Decimal("20.0") # 20% discount on marketplace commission
            buybox_mult = 1.30
            fbf = True
        elif metrics.gross_merchandise_value >= Decimal("1500000.00") and metrics.average_customer_rating >= 4.4:
            tier = MerchantTier.GOLD
            comm_discount = Decimal("10.0")
            buybox_mult = 1.15
            fbf = True
        elif metrics.gross_merchandise_value >= Decimal("300000.00") and metrics.average_customer_rating >= 4.0:
            tier = MerchantTier.SILVER
            comm_discount = Decimal("5.0")
            buybox_mult = 1.0
            fbf = True
        else:
            tier = MerchantTier.BRONZE
            comm_discount = Decimal("0.0")
            buybox_mult = 0.90
            fbf = False

        return SellerScorecardReport(
            seller_id=metrics.seller_id,
            seller_name=metrics.seller_name,
            order_defect_rate=odr,
            late_dispatch_rate=ldr,
            cancellation_rate=cr,
            return_rate=rr,
            assigned_tier=tier,
            commission_discount_percent=comm_discount,
            buybox_competitiveness_multiplier=buybox_mult,
            is_fbf_eligible=fbf,
            enforcement_warning=warning,
        )
