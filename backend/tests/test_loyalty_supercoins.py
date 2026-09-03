from decimal import Decimal
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.loyalty_promotions import LoyaltyTierLevel
from app.models.order_payment import Order
from app.models.user import Address
from app.services.loyalty_service import (
    award_coins_for_order,
    get_or_create_loyalty_profile,
    redeem_supercoins,
)


@pytest.mark.asyncio
async def test_supercoins_earn_and_redeem(db_session: AsyncSession):
    """Test SuperCoin welcome bonus, order rewards, and redemption."""
    user_id = 777
    profile = await get_or_create_loyalty_profile(db_session, user_id)
    assert profile.supercoin_balance == 50  # Welcome bonus

    # Seed an address
    addr = Address(
        user_id=user_id,
        full_name="Test User",
        phone_number="9876543210",
        address_line1="123 Market Road",
        city="Bengaluru",
        state="Karnataka",
        postal_code="560001",
    )
    db_session.add(addr)
    await db_session.flush()

    # Simulate Order of ₹2,500
    mock_order = Order(
        order_number="ORD-TEST-99",
        user_id=user_id,
        address_id=addr.id,
        subtotal=Decimal("2500.00"),
        grand_total=Decimal("2500.00"),
    )
    db_session.add(mock_order)
    await db_session.flush()

    coins_awarded = await award_coins_for_order(db_session, user_id, mock_order)
    assert coins_awarded == 50  # Standard non-plus user earns 2 coins per ₹100, max 50
    assert profile.supercoin_balance == 100

    # Redeem 40 coins for ₹40 discount
    ok, msg, discount = await redeem_supercoins(db_session, user_id, coins_to_spend=40, order_id=mock_order.id)
    assert ok is True
    assert discount == Decimal("40")
    assert profile.supercoin_balance == 60
