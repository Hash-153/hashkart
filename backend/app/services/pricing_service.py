from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, Optional


TWOPLACES = Decimal("0.01")


class PricingService:
    """
    Authoritative monetary calculation engine enforcing strict Python Decimal precision.
    Prevents floating-point rounding errors across Cart, Checkout, Pricing, and Orders.
    """

    @staticmethod
    def to_decimal(val: Any) -> Decimal:
        """Convert float/int/str/Decimal to quantized Decimal(0.01)."""
        if val is None:
            return Decimal("0.00")
        d = Decimal(str(val))
        return d.quantize(TWOPLACES, rounding=ROUND_HALF_UP)

    @staticmethod
    def calculate_discount_details(
        base_price_raw: Any, discount_price_raw: Optional[Any] = None
    ) -> Dict[str, Any]:
        """Calculate sale price, savings amount, and integer discount percentage."""
        base_price = PricingService.to_decimal(base_price_raw)
        if base_price <= Decimal("0.00"):
            return {
                "original_price": 0.0,
                "sale_price": 0.0,
                "discount_amount": 0.0,
                "discount_percentage": 0,
                "has_discount": False,
            }

        if discount_price_raw is not None and Decimal(str(discount_price_raw)) < base_price:
            sale_price = PricingService.to_decimal(discount_price_raw)
            savings = (base_price - sale_price).quantize(TWOPLACES, rounding=ROUND_HALF_UP)
            disc_pct = int(round(float((savings / base_price) * Decimal("100"))))
            return {
                "original_price": float(base_price),
                "sale_price": float(sale_price),
                "discount_amount": float(savings),
                "discount_percentage": disc_pct,
                "has_discount": True,
            }

        return {
            "original_price": float(base_price),
            "sale_price": float(base_price),
            "discount_amount": 0.0,
            "discount_percentage": 0,
            "has_discount": False,
        }

    @staticmethod
    def calculate_tax(taxable_amount: Decimal, tax_rate_percent: Decimal = Decimal("18.00")) -> Decimal:
        """Calculate GST tax amount (default 18%)."""
        if taxable_amount <= Decimal("0.00"):
            return Decimal("0.00")
        tax = (taxable_amount * (tax_rate_percent / Decimal("100.00"))).quantize(
            TWOPLACES, rounding=ROUND_HALF_UP
        )
        return tax

    @staticmethod
    def calculate_shipping(subtotal: Decimal, free_threshold: Decimal = Decimal("500.00"), standard_fee: Decimal = Decimal("49.00")) -> Decimal:
        """Calculate shipping fee based on subtotal threshold."""
        if subtotal <= Decimal("0.00") or subtotal >= free_threshold:
            return Decimal("0.00")
        return standard_fee.quantize(TWOPLACES, rounding=ROUND_HALF_UP)

    @staticmethod
    def calculate_coupon_discount(
        subtotal: Decimal,
        discount_type: str,
        discount_value: Any,
        min_order_value: Any = 0.0,
        max_discount_amount: Optional[Any] = None,
    ) -> Decimal:
        """Calculate authoritative coupon discount amount."""
        subtotal_d = PricingService.to_decimal(subtotal)
        min_order_d = PricingService.to_decimal(min_order_value)
        val_d = PricingService.to_decimal(discount_value)

        if subtotal_d < min_order_d:
            return Decimal("0.00")

        if discount_type == "PERCENTAGE":
            disc = (subtotal_d * (val_d / Decimal("100.00"))).quantize(TWOPLACES, rounding=ROUND_HALF_UP)
            if max_discount_amount is not None:
                max_d = PricingService.to_decimal(max_discount_amount)
                if disc > max_d:
                    disc = max_d
        else:
            disc = val_d

        return min(disc, subtotal_d).quantize(TWOPLACES, rounding=ROUND_HALF_UP)

    @staticmethod
    def calculate_order_totals(
        line_items: list,
        coupon_discount_raw: Any = 0.0,
        tax_rate: Decimal = Decimal("18.00"),
    ) -> Dict[str, Any]:
        """
        Execute full authoritative pricing pipeline for Cart / Checkout:
        Returns subtotal, discount_amount, taxable_amount, tax_amount, shipping_fee, grand_total.
        """
        subtotal = Decimal("0.00")
        for item in line_items:
            unit_p = PricingService.to_decimal(item.get("price"))
            qty = Decimal(str(item.get("quantity", 1)))
            subtotal += (unit_p * qty).quantize(TWOPLACES, rounding=ROUND_HALF_UP)

        coupon_disc = PricingService.to_decimal(coupon_discount_raw)
        coupon_disc = min(coupon_disc, subtotal)

        taxable_amount = subtotal - coupon_disc
        tax_amount = PricingService.calculate_tax(taxable_amount, tax_rate)
        shipping_fee = PricingService.calculate_shipping(subtotal)
        grand_total = (taxable_amount + tax_amount + shipping_fee).quantize(TWOPLACES, rounding=ROUND_HALF_UP)

        return {
            "subtotal": float(subtotal),
            "discount_amount": float(coupon_disc),
            "taxable_amount": float(taxable_amount),
            "tax_amount": float(tax_amount),
            "shipping_fee": float(shipping_fee),
            "grand_total": float(grand_total),
        }
