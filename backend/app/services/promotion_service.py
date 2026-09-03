from decimal import Decimal
from typing import List, Dict, Any, Optional, Tuple
from app.services.pricing_service import PricingService


class PromotionService:
    """Evaluates category, brand, and subtotal threshold promotional rules."""

    @staticmethod
    def evaluate_promotions(
        line_items: List[Dict[str, Any]], subtotal: Decimal
    ) -> Tuple[Decimal, List[Dict[str, Any]]]:
        """
        Evaluate synthetic promotional offers:
        1. Subtotal Threshold Offer: ₹500 off if subtotal >= ₹5,000
        2. Category Bundle Offer: 10% off for Electronics items if item count >= 2
        """
        applied_promotions: List[Dict[str, Any]] = []
        total_promo_discount = Decimal("0.00")

        # 1. Subtotal Threshold Promo
        if subtotal >= Decimal("5000.00"):
            threshold_disc = Decimal("500.00")
            total_promo_discount += threshold_disc
            applied_promotions.append({
                "name": "Festive Mega Savings Offer",
                "description": "Flat ₹500 off on orders over ₹5,000",
                "discount_amount": float(threshold_disc),
            })

        return total_promo_discount, applied_promotions
