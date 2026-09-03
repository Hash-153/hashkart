"""
NovaMart Dynamic Pricing & Multi-Armed Bandit Reinforcement Learning Engine
===========================================================================
Algorithmic price elasticity optimization for high-velocity marketplace listings:
- Upper Confidence Bound (UCB1) multi-armed bandit price selection
- Thompson Sampling with Beta-Bernoulli conjugate priors for conversion exploration vs exploitation
- Price Elasticity of Demand curve estimation: E_d = (% Δ Quantity) / (% Δ Price)
- Dynamic Competitor Undercutting with hard-floor gross margin guards
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
import math
import random
from typing import Dict, List, Optional, Tuple


@dataclass
class PriceArmStatistics:
    price_point: Decimal
    impressions_count: int
    conversions_count: int
    total_revenue_generated: Decimal
    total_profit_generated: Decimal
    alpha_prior: float = 1.0 # Beta distribution successes
    beta_prior: float = 1.0  # Beta distribution failures

    @property
    def empirical_conversion_rate(self) -> float:
        if self.impressions_count == 0:
            return 0.0
        return self.conversions_count / self.impressions_count

    @property
    def expected_revenue_per_impression(self) -> float:
        return self.empirical_conversion_rate * float(self.price_point)


class DynamicPricingMABEngine:
    def __init__(self, sku: str, cost_price: Decimal, min_margin_percent: Decimal = Decimal("8.0")):
        self.sku = sku
        self.cost_price = cost_price
        self.min_margin_percent = min_margin_percent
        self.hard_floor_price = (cost_price * (Decimal("1.0") + min_margin_percent / Decimal("100.0"))).quantize(Decimal("0.01"))
        self.price_arms: Dict[Decimal, PriceArmStatistics] = {}

    def register_price_point(self, price: Decimal):
        """Register candidate price point arm."""
        if price >= self.hard_floor_price:
            self.price_arms[price] = PriceArmStatistics(
                price_point=price,
                impressions_count=0,
                conversions_count=0,
                total_revenue_generated=Decimal("0.00"),
                total_profit_generated=Decimal("0.00"),
            )

    def select_price_ucb1(self, total_experiment_impressions: int) -> Decimal:
        """Select price arm using Upper Confidence Bound (UCB1) exploration formula."""
        if not self.price_arms:
            return self.hard_floor_price

        # Check unvisited arms first
        for price, arm in self.price_arms.items():
            if arm.impressions_count == 0:
                return price

        best_price = None
        highest_ucb = -1.0

        for price, arm in self.price_arms.items():
            # Expected reward = Revenue per impression
            avg_reward = arm.expected_revenue_per_impression
            # UCB exploration bonus
            bonus = math.sqrt((2.0 * math.log(max(1, total_experiment_impressions))) / arm.impressions_count)
            ucb_value = avg_reward + (bonus * float(price) * 0.1)

            if ucb_value > highest_ucb:
                highest_ucb = ucb_value
                best_price = price

        return best_price or self.hard_floor_price

    def select_price_thompson_sampling(self) -> Decimal:
        """Select price arm using Bayesian Thompson Sampling from Beta posterior."""
        if not self.price_arms:
            return self.hard_floor_price

        best_price = None
        highest_sample = -1.0

        for price, arm in self.price_arms.items():
            # Sample conversion probability from Beta(alpha, beta)
            sampled_cvr = random.betavariate(arm.alpha_prior, arm.beta_prior)
            sampled_expected_revenue = sampled_cvr * float(price)

            if sampled_expected_revenue > highest_sample:
                highest_sample = sampled_expected_revenue
                best_price = price

        return best_price or self.hard_floor_price

    def record_feedback(self, price: Decimal, converted: bool, quantity: int = 1):
        """Update posterior statistics with purchase or bounce feedback."""
        arm = self.price_arms.get(price)
        if not arm:
            return

        arm.impressions_count += 1
        if converted:
            arm.conversions_count += quantity
            arm.alpha_prior += float(quantity)
            rev = price * Decimal(str(quantity))
            profit = (price - self.cost_price) * Decimal(str(quantity))
            arm.total_revenue_generated += rev
            arm.total_profit_generated += profit
        else:
            arm.beta_prior += 1.0

    @staticmethod
    def calculate_price_elasticity(
        price_old: Decimal, qty_old: int,
        price_new: Decimal, qty_new: int,
    ) -> float:
        """Compute point price elasticity of demand."""
        if qty_old == 0 or price_old == Decimal("0.00"):
            return 0.0
        pct_delta_qty = (qty_new - qty_old) / qty_old
        pct_delta_price = float(price_new - price_old) / float(price_old)
        if pct_delta_price == 0.0:
            return 0.0
        return round(pct_delta_qty / pct_delta_price, 2)
