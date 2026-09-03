"""
NovaMart Customer Price Drop & Stock Restock Alerting Subsystem
===============================================================
Monitors wishlist items and price drops across catalog SKUs:
- Detects price reductions > threshold percentage (e.g. 5% or ₹500 off)
- Enqueues batch transactional push and email notifications
- Tracks alert conversion attribution (click -> order within 48 hours)
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from typing import Dict, List, Optional


@dataclass
class WishlistPriceAlertSubscription:
    user_id: int
    product_id: int
    product_name: str
    target_price_alert_threshold: Decimal
    subscribed_price: Decimal
    user_email: str
    user_phone: str


@dataclass
class TriggeredPriceDropAlert:
    user_id: int
    product_id: int
    product_name: str
    previous_price: Decimal
    new_price: Decimal
    savings_amount: Decimal
    discount_percentage: float
    user_email: str
    triggered_at: datetime


class PriceDropAlertEngine:
    @staticmethod
    def evaluate_price_drop_triggers(
        subscriptions: List[WishlistPriceAlertSubscription],
        current_prices_by_product_id: Dict[int, Decimal],
        min_discount_percentage: float = 3.0,
    ) -> List[TriggeredPriceDropAlert]:
        """Detect qualifying price drops and generate notification queue payloads."""
        triggered: List[TriggeredPriceDropAlert] = []
        now = datetime.now(timezone.utc)

        for sub in subscriptions:
            current_p = current_prices_by_product_id.get(sub.product_id)
            if not current_p:
                continue

            if current_p < sub.subscribed_price:
                savings = sub.subscribed_price - current_p
                pct = float((savings / sub.subscribed_price) * 100)

                if pct >= min_discount_percentage or current_p <= sub.target_price_alert_threshold:
                    triggered.append(
                        TriggeredPriceDropAlert(
                            user_id=sub.user_id,
                            product_id=sub.product_id,
                            product_name=sub.product_name,
                            previous_price=sub.subscribed_price,
                            new_price=current_p,
                            savings_amount=savings,
                            discount_percentage=round(pct, 1),
                            user_email=sub.user_email,
                            triggered_at=now,
                        )
                    )

        return triggered
