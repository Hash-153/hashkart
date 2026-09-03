from decimal import Decimal
import pytest

from app.services.pricing_engine import (
    BuyBoxPricingEngine,
    SellerListingOffer,
)


def test_buybox_winner_evaluation():
    # Seller 1: Slightly higher price but NovaMart Assured, fast 1-day delivery, 4.9 rating, Gold tier
    s1 = SellerListingOffer(
        seller_id=101,
        seller_name="Official Apple Store",
        seller_rating=4.9,
        seller_tier="GOLD",
        selling_price=Decimal("69999.00"),
        mrp=Decimal("79900.00"),
        shipping_charge=Decimal("0.00"),
        estimated_delivery_days=1,
        stock_quantity=50,
        return_rate_percentage=1.0,
        cancellation_rate_percentage=0.1,
        is_fbf_fulfilled=True,
    )

    # Seller 2: Cheaper by ₹100, but 5-day delivery, 3.8 rating, Bronze tier, high returns
    s2 = SellerListingOffer(
        seller_id=102,
        seller_name="Discount Traders",
        seller_rating=3.8,
        seller_tier="BRONZE",
        selling_price=Decimal("69899.00"),
        mrp=Decimal("79900.00"),
        shipping_charge=Decimal("150.00"), # Landed price is actually higher
        estimated_delivery_days=5,
        stock_quantity=10,
        return_rate_percentage=8.5,
        cancellation_rate_percentage=3.0,
        is_fbf_fulfilled=False,
    )

    eval_result = BuyBoxPricingEngine.evaluate_buybox_winner([s1, s2])
    assert eval_result is not None
    assert eval_result.winner_seller_id == 101
    assert eval_result.winning_price == Decimal("69999.00")
    assert eval_result.buybox_composite_score > 0.8


def test_automated_reprice_target_with_floor_protection():
    # Competitor is at ₹950. Target without floor = ₹945
    target_1 = BuyBoxPricingEngine.calculate_automated_reprice_target(
        current_price=Decimal("1000.00"),
        competitor_winning_price=Decimal("950.00"),
        floor_price_limit=Decimal("900.00"),
        undercut_amount=Decimal("5.00"),
    )
    assert target_1 == Decimal("945.00")

    # Competitor is below our floor limit of ₹900. Target must stick to floor limit ₹900
    target_2 = BuyBoxPricingEngine.calculate_automated_reprice_target(
        current_price=Decimal("950.00"),
        competitor_winning_price=Decimal("850.00"),
        floor_price_limit=Decimal("900.00"),
        undercut_amount=Decimal("5.00"),
    )
    assert target_2 == Decimal("900.00")
