"""
NovaMart Dynamic Pricing & BuyBox Winning Algorithm Engine
==========================================================
Implements multi-seller BuyBox competitive ranking and dynamic repricing:
- Weighted scoring of Seller Price, Dispatch SLA, Return Rate, and Seller Rating
- Automated competitive undercut algorithms with floor profit margin guards
- Dynamic discount matching for festive sales & flash deals
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, Optional, Tuple


@dataclass
class SellerListingOffer:
    seller_id: int
    seller_name: str
    seller_rating: float # 0.0 to 5.0
    seller_tier: str # 'GOLD', 'SILVER', 'BRONZE'
    selling_price: Decimal
    mrp: Decimal
    shipping_charge: Decimal
    estimated_delivery_days: int
    stock_quantity: int
    return_rate_percentage: float
    cancellation_rate_percentage: float
    is_fbf_fulfilled: bool # Flipkart Fulfilled equivalent (NovaMart Assured)


@dataclass
class BuyBoxWinnerEvaluation:
    winner_seller_id: int
    winning_price: Decimal
    buybox_composite_score: float
    all_ranked_sellers: List[Tuple[int, float, Decimal]] # (seller_id, composite_score, price)
    price_spread_percentage: float
    recommendations: List[str]


# BuyBox Scoring Weights (Sum = 1.0)
WEIGHT_LANDED_PRICE = 0.45       # Landed price (Price + Shipping)
WEIGHT_FULFILLMENT_SLA = 0.20    # Fast delivery days & NovaMart Assured badge
WEIGHT_SELLER_RATING = 0.15      # Customer satisfaction rating
WEIGHT_RETURN_CANCELLATION = 0.10 # Operational defect rate
WEIGHT_SELLER_TIER = 0.10        # Merchant tier bonus (Gold/Silver)


class BuyBoxPricingEngine:
    @staticmethod
    def calculate_seller_composite_score(
        offer: SellerListingOffer,
        min_landed_price_in_pool: Decimal,
    ) -> float:
        """Compute the multi-factor BuyBox competitiveness score for a merchant offer."""
        landed_price = offer.selling_price + offer.shipping_charge

        # 1. Price Score: (min_price / landed_price)
        price_score = float(min_landed_price_in_pool / landed_price) if landed_price > 0 else 0.0

        # 2. SLA Score: Faster delivery = higher score
        sla_days = max(1, offer.estimated_delivery_days)
        sla_score = 1.0 if sla_days <= 1 else (0.85 if sla_days <= 2 else (0.65 if sla_days <= 4 else 0.4))
        if offer.is_fbf_fulfilled:
            sla_score = min(1.0, sla_score + 0.15) # NovaMart Assured bonus

        # 3. Rating Score: rating / 5.0
        rating_score = max(0.0, min(1.0, offer.seller_rating / 5.0))

        # 4. Operations Defect Score: lower returns/cancels = higher score
        defect_pct = offer.return_rate_percentage + (offer.cancellation_rate_percentage * 2.0)
        ops_score = max(0.0, 1.0 - (defect_pct / 20.0))

        # 5. Tier Score
        tier_scores = {"GOLD": 1.0, "SILVER": 0.8, "BRONZE": 0.5}
        tier_score = tier_scores.get(offer.seller_tier.upper(), 0.5)

        # Weighted Sum
        composite = (
            (price_score * WEIGHT_LANDED_PRICE)
            + (sla_score * WEIGHT_FULFILLMENT_SLA)
            + (rating_score * WEIGHT_SELLER_RATING)
            + (ops_score * WEIGHT_RETURN_CANCELLATION)
            + (tier_score * WEIGHT_SELLER_TIER)
        )

        return round(composite, 4)

    @classmethod
    def evaluate_buybox_winner(
        cls,
        offers: List[SellerListingOffer],
    ) -> Optional[BuyBoxWinnerEvaluation]:
        """Determine which seller wins the primary BuyBox display on the Product Page."""
        valid_offers = [o for o in offers if o.stock_quantity > 0]
        if not valid_offers:
            return None

        # Determine lowest landed price across active pool
        min_landed = min(o.selling_price + o.shipping_charge for o in valid_offers)

        scored_offers: List[Tuple[SellerListingOffer, float]] = []
        for o in valid_offers:
            score = cls.calculate_seller_composite_score(o, min_landed)
            scored_offers.append((o, score))

        # Sort by composite score descending
        scored_offers.sort(key=lambda x: x[1], reverse=True)
        winner, top_score = scored_offers[0]

        max_price = max(o.selling_price for o in valid_offers)
        min_price = min(o.selling_price for o in valid_offers)
        spread_pct = float(((max_price - min_price) / max_price) * 100) if max_price > 0 else 0.0

        recs = []
        if winner.is_fbf_fulfilled:
            recs.append("Won via NovaMart Assured fulfillment speed advantage")
        if winner.selling_price <= min_price:
            recs.append("Lowest competitive marketplace price")
        if winner.seller_tier == "GOLD":
            recs.append("Top-tier Gold merchant reliability score")

        return BuyBoxWinnerEvaluation(
            winner_seller_id=winner.seller_id,
            winning_price=winner.selling_price,
            buybox_composite_score=top_score,
            all_ranked_sellers=[(o.seller_id, s, o.selling_price) for o, s in scored_offers],
            price_spread_percentage=round(spread_pct, 2),
            recommendations=recs,
        )

    @staticmethod
    def calculate_automated_reprice_target(
        current_price: Decimal,
        competitor_winning_price: Decimal,
        floor_price_limit: Decimal,
        undercut_amount: Decimal = Decimal("5.00"),
    ) -> Decimal:
        """Calculate optimal dynamic repricing target with hard profit floor protection."""
        ideal_target = competitor_winning_price - undercut_amount
        return max(floor_price_limit, min(current_price, ideal_target))
