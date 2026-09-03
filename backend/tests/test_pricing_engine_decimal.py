from decimal import Decimal
import pytest
from app.services.pricing_service import PricingService


def test_decimal_conversion_and_quantization():
    assert PricingService.to_decimal(1999.99) == Decimal("1999.99")
    assert PricingService.to_decimal("149.995") == Decimal("150.00")
    assert PricingService.to_decimal(None) == Decimal("0.00")


def test_tax_and_shipping_calculation():
    taxable = Decimal("1000.00")
    tax = PricingService.calculate_tax(taxable, Decimal("18.00"))
    assert tax == Decimal("180.00")

    shipping_free = PricingService.calculate_shipping(Decimal("550.00"))
    assert shipping_free == Decimal("0.00")

    shipping_paid = PricingService.calculate_shipping(Decimal("450.00"))
    assert shipping_paid == Decimal("49.00")


def test_coupon_discount_calculation():
    # Percentage coupon with max cap
    disc_pct = PricingService.calculate_coupon_discount(
        subtotal=Decimal("3000.00"),
        discount_type="PERCENTAGE",
        discount_value=20.0,
        min_order_value=1000.0,
        max_discount_amount=500.0,
    )
    assert disc_pct == Decimal("500.00")

    # Fixed coupon
    disc_fixed = PricingService.calculate_coupon_discount(
        subtotal=Decimal("2000.00"),
        discount_type="FIXED",
        discount_value=300.0,
        min_order_value=500.0,
    )
    assert disc_fixed == Decimal("300.00")


def test_order_totals_pipeline():
    line_items = [
        {"price": 1499.00, "quantity": 2},  # 2998.00
        {"price": 499.00, "quantity": 1},   # 499.00 -> total 3497.00
    ]
    totals = PricingService.calculate_order_totals(line_items, coupon_discount_raw=200.0)

    assert totals["subtotal"] == 3497.00
    assert totals["discount_amount"] == 200.00
    assert totals["taxable_amount"] == 3297.00
    assert totals["tax_amount"] == 593.46  # 18% of 3297.00
    assert totals["shipping_fee"] == 0.00  # Subtotal > 500
    assert totals["grand_total"] == 3890.46
