import pytest
from app.services.pricing_service import PricingService


def test_pricing_service_calculations():
    """Test discount details calculation logic."""
    # 1. No discount
    res1 = PricingService.calculate_discount_details(1000.0, None)
    assert res1["original_price"] == 1000.0
    assert res1["sale_price"] == 1000.0
    assert res1["discount_amount"] == 0.0
    assert res1["discount_percentage"] == 0
    assert res1["has_discount"] is False

    # 2. 20% discount (2000 base, 1600 sale)
    res2 = PricingService.calculate_discount_details(2000.0, 1600.0)
    assert res2["original_price"] == 2000.0
    assert res2["sale_price"] == 1600.0
    assert res2["discount_amount"] == 400.0
    assert res2["discount_percentage"] == 20
    assert res2["has_discount"] is True
