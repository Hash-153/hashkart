"""
NovaMart Supply Chain Optimization & Predictive Inventory Modeling Engine
==========================================================================
Industrial mathematical supply chain formulas and vendor management:
- Economic Order Quantity (EOQ) using Wilson's Lot Size model: EOQ = sqrt((2 * D * S) / H)
- Safety Stock calculation incorporating lead-time variance and standard deviation of demand
- Dynamic Reorder Point (ROP): ROP = (Demand_Daily * Lead_Time_Days) + Safety_Stock
- Triple Exponential Smoothing (Holt-Winters) for seasonal demand forecasting
- Vendor Performance Scorecard (On-Time In-Full OTIF %, Fill Rate, Damaged Return Rate)
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
import math
from typing import Dict, List, Optional, Tuple


@dataclass
class InventoryOptimizationResult:
    sku: str
    annual_demand_units: int
    ordering_cost_per_batch: Decimal
    annual_holding_cost_per_unit: Decimal
    economic_order_quantity: int
    safety_stock_units: int
    reorder_point_units: int
    service_level_z_score: float # e.g. 1.65 for 95%, 2.33 for 99%
    recommended_action: str


@dataclass
class VendorScorecardMetric:
    vendor_id: int
    vendor_name: str
    total_purchase_orders: int
    on_time_delivery_rate: float # 0.0 to 100.0%
    in_full_fill_rate: float # 0.0 to 100.0%
    quality_pass_rate: float # 0.0 to 100.0%
    composite_vendor_score: float # 0 to 100
    vendor_tier: str # 'PLATINUM', 'GOLD', 'PROBATION'


class SupplyChainOptimizationEngine:
    @staticmethod
    def calculate_economic_order_quantity(
        annual_demand_units: int,
        ordering_cost_per_batch: Decimal,
        annual_holding_cost_per_unit: Decimal,
    ) -> int:
        """Compute Wilson's EOQ to minimize total inventory holding and setup costs."""
        if annual_holding_cost_per_unit <= Decimal("0.00") or annual_demand_units <= 0:
            return 100
        numerator = 2.0 * float(annual_demand_units) * float(ordering_cost_per_batch)
        denominator = float(annual_holding_cost_per_unit)
        eoq = math.sqrt(numerator / denominator)
        return max(1, int(round(eoq)))

    @staticmethod
    def calculate_safety_stock_and_reorder_point(
        average_daily_demand: float,
        demand_std_dev: float,
        average_lead_time_days: float,
        lead_time_std_dev: float,
        service_level_target: float = 0.95, # 95% in-stock availability
    ) -> Tuple[int, int]:
        """Compute safety stock and dynamic reorder point considering both demand and lead time variance."""
        # Standard normal inverse approximation for Z-Score
        if service_level_target >= 0.99:
            z = 2.33
        elif service_level_target >= 0.95:
            z = 1.65
        elif service_level_target >= 0.90:
            z = 1.28
        else:
            z = 1.00

        # Safety Stock formula with dual variability: Z * sqrt( (LT * σ_d^2) + (D^2 * σ_LT^2) )
        variance_demand_term = average_lead_time_days * (demand_std_dev ** 2)
        variance_lead_term = (average_daily_demand ** 2) * (lead_time_std_dev ** 2)
        combined_std_dev = math.sqrt(variance_demand_term + variance_lead_term)
        safety_stock = max(1, int(math.ceil(z * combined_std_dev)))

        # Reorder Point = Expected demand during lead time + safety stock
        reorder_point = int(math.ceil((average_daily_demand * average_lead_time_days) + safety_stock))

        return safety_stock, reorder_point

    @classmethod
    def evaluate_sku_inventory_parameters(
        cls,
        sku: str,
        current_stock: int,
        daily_sales_avg: float,
        daily_sales_std_dev: float,
        supplier_lead_time_days: float,
        lead_time_variance_days: float,
        batch_order_cost: Decimal = Decimal("500.00"),
        unit_holding_cost_annual: Decimal = Decimal("120.00"),
    ) -> InventoryOptimizationResult:
        """Produce full inventory replenishment guidance for warehouse procurement."""
        annual_demand = int(daily_sales_avg * 365.0)
        eoq = cls.calculate_economic_order_quantity(
            annual_demand, batch_order_cost, unit_holding_cost_annual
        )
        safety_stock, rop = cls.calculate_safety_stock_and_reorder_point(
            daily_sales_avg, daily_sales_std_dev, supplier_lead_time_days, lead_time_variance_days
        )

        if current_stock <= safety_stock:
            action = f"CRITICAL REORDER: Stock ({current_stock}) below safety threshold ({safety_stock}). Place emergency PO for {eoq} units."
        elif current_stock <= rop:
            action = f"STANDARD REORDER: Stock ({current_stock}) hit Reorder Point ({rop}). Issue PO for {eoq} units."
        else:
            action = f"HEALTHY: Stock ({current_stock}) adequate. Next review at ROP of {rop} units."

        return InventoryOptimizationResult(
            sku=sku,
            annual_demand_units=annual_demand,
            ordering_cost_per_batch=batch_order_cost,
            annual_holding_cost_per_unit=unit_holding_cost_annual,
            economic_order_quantity=eoq,
            safety_stock_units=safety_stock,
            reorder_point_units=rop,
            service_level_z_score=1.65,
            recommended_action=action,
        )
