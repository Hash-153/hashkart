import math
import uuid
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import List, Optional, Tuple
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.loyalty_promotions import (
    BankDiscountOffer,
    CardNetwork,
    LoyaltyTierLevel,
    SuperCoinTransaction,
    SuperCoinTransactionType,
    UserLoyaltyProfile,
)
from app.models.order_payment import Order


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


async def get_or_create_loyalty_profile(
    db: AsyncSession, user_id: int
) -> UserLoyaltyProfile:
    """Retrieve or initialize the SuperCoins loyalty profile for a user."""
    stmt = select(UserLoyaltyProfile).where(UserLoyaltyProfile.user_id == user_id)
    res = await db.execute(stmt)
    profile = res.scalar_one_or_none()

    if not profile:
        profile = UserLoyaltyProfile(
            user_id=user_id,
            tier=LoyaltyTierLevel.BRONZE,
            supercoin_balance=50,  # Welcome bonus 50 SuperCoins
            lifetime_coins_earned=50,
            lifetime_coins_spent=0,
            tier_points=50,
            is_flipkart_plus_member=False,
        )
        db.add(profile)
        await db.flush()

        # Add initial welcome credit transaction
        txn = SuperCoinTransaction(
            profile_id=profile.id,
            user_id=user_id,
            transaction_type=SuperCoinTransactionType.EARNED_PROMOTION,
            coins=50,
            running_balance=50,
            description="NovaMart Welcome Bonus SuperCoins",
            reference_id=f"BONUS-{uuid.uuid4().hex[:6].upper()}",
            expires_at=utcnow() + timedelta(days=365),
        )
        db.add(txn)
        await db.flush()
        await db.refresh(profile)

    return profile


async def award_coins_for_order(
    db: AsyncSession, user_id: int, order: Order
) -> int:
    """Award SuperCoins upon successful order delivery.
    Plus Members: 4 coins per ₹100 spent (max 100 per order)
    Regular Members: 2 coins per ₹100 spent (max 50 per order)
    """
    profile = await get_or_create_loyalty_profile(db, user_id)
    order_val = getattr(order, "grand_total", None) or getattr(order, "total_amount", Decimal("0.00"))
    if not isinstance(order_val, Decimal):
        order_val = Decimal(str(order_val))

    if profile.is_flipkart_plus_member:
        coins = int((order_val / Decimal("100.00")) * 4)
        coins = min(coins, 100)
    else:
        coins = int((order_val / Decimal("100.00")) * 2)
        coins = min(coins, 50)

    if coins <= 0:
        return 0

    profile.supercoin_balance += coins
    profile.lifetime_coins_earned += coins
    profile.tier_points += coins

    # Check for tier upgrades
    if profile.tier_points >= 500:
        profile.tier = LoyaltyTierLevel.VIP_PLUS
        profile.is_flipkart_plus_member = True
    elif profile.tier_points >= 250:
        profile.tier = LoyaltyTierLevel.GOLD
    elif profile.tier_points >= 100:
        profile.tier = LoyaltyTierLevel.SILVER

    txn = SuperCoinTransaction(
        profile_id=profile.id,
        user_id=user_id,
        order_id=order.id,
        transaction_type=SuperCoinTransactionType.EARNED_PURCHASE,
        coins=coins,
        running_balance=profile.supercoin_balance,
        description=f"Earned from Order #{order.order_number}",
        reference_id=f"COIN-ORD-{order.id}",
        expires_at=utcnow() + timedelta(days=365),
    )
    db.add(txn)
    await db.flush()
    return coins


async def redeem_supercoins(
    db: AsyncSession, user_id: int, coins_to_spend: int, order_id: Optional[int] = None
) -> Tuple[bool, str, Decimal]:
    """Redeem SuperCoins for checkout discount (1 Coin = ₹1.00)."""
    if coins_to_spend <= 0:
        return False, "Invalid coin amount", Decimal("0.00")

    profile = await get_or_create_loyalty_profile(db, user_id)
    if profile.supercoin_balance < coins_to_spend:
        return False, f"Insufficient SuperCoins. Balance: {profile.supercoin_balance}", Decimal("0.00")

    profile.supercoin_balance -= coins_to_spend
    profile.lifetime_coins_spent += coins_to_spend

    discount_inr = Decimal(str(coins_to_spend))

    txn = SuperCoinTransaction(
        profile_id=profile.id,
        user_id=user_id,
        order_id=order_id,
        transaction_type=SuperCoinTransactionType.SPENT_CHECKOUT,
        coins=-coins_to_spend,
        running_balance=profile.supercoin_balance,
        description=f"Redeemed ₹{discount_inr} discount at checkout",
        reference_id=f"RED-ORD-{order_id}" if order_id else f"RED-{uuid.uuid4().hex[:6].upper()}",
    )
    db.add(txn)
    await db.flush()
    return True, "SuperCoins redeemed successfully", discount_inr


async def calculate_best_bank_offer(
    db: AsyncSession,
    bank_code: CardNetwork,
    cart_total: Decimal,
    category_id: Optional[int] = None,
) -> Tuple[Optional[BankDiscountOffer], Decimal]:
    """Find the most lucrative bank discount offer for the given card and cart amount."""
    now = utcnow()
    stmt = (
        select(BankDiscountOffer)
        .where(
            BankDiscountOffer.is_active == True,
            BankDiscountOffer.starts_at <= now,
            BankDiscountOffer.ends_at >= now,
            BankDiscountOffer.min_order_value <= cart_total,
            (BankDiscountOffer.bank_code == bank_code) | (BankDiscountOffer.bank_code == CardNetwork.ALL_BANKS),
        )
        .order_by(BankDiscountOffer.discount_percentage.desc().nullslast())
    )
    res = await db.execute(stmt)
    offers = res.scalars().all()

    best_offer = None
    max_discount = Decimal("0.00")

    for o in offers:
        if o.flat_discount_amount:
            discount = o.flat_discount_amount
        elif o.discount_percentage:
            discount = (cart_total * (o.discount_percentage / Decimal("100.00"))).quantize(Decimal("0.01"))
            if o.max_discount_cap:
                discount = min(discount, o.max_discount_cap)
        else:
            discount = Decimal("0.00")

        if discount > max_discount:
            max_discount = discount
            best_offer = o

    return best_offer, max_discount
