from decimal import Decimal
import pytest

from app.services.price_drop_alert_service import (
    PriceDropAlertEngine,
    WishlistPriceAlertSubscription,
)


def test_price_drop_alert_detection():
    subs = [
        WishlistPriceAlertSubscription(
            user_id=1,
            product_id=101,
            product_name="Apple iPhone 15",
            target_price_alert_threshold=Decimal("65000.00"),
            subscribed_price=Decimal("70000.00"),
            user_email="buyer@example.com",
            user_phone="9876543210",
        ),
        WishlistPriceAlertSubscription(
            user_id=2,
            product_id=202,
            product_name="Sony XM5",
            target_price_alert_threshold=Decimal("20000.00"),
            subscribed_price=Decimal("26990.00"),
            user_email="buyer2@example.com",
            user_phone="9876543211",
        ),
    ]

    current_prices = {
        101: Decimal("64999.00"), # Dropped below target
        202: Decimal("26990.00"), # Price unchanged
    }

    triggered = PriceDropAlertEngine.evaluate_price_drop_triggers(subs, current_prices)
    assert len(triggered) == 1
    assert triggered[0].product_id == 101
    assert triggered[0].savings_amount == Decimal("5001.00")
    assert triggered[0].discount_percentage > 7.0
