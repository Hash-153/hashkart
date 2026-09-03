from decimal import Decimal
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.deps import get_current_user, get_db
from app.models.loyalty_promotions import BankDiscountOffer, CardNetwork, SuperCoinTransaction, UserLoyaltyProfile
from app.models.user import User
from app.schemas.loyalty_promotions import (
    BankOfferResponse,
    SuperCoinRedemptionQuoteRequest,
    SuperCoinRedemptionQuoteResponse,
    SuperCoinTransactionResponse,
    UserLoyaltyProfileResponse,
)
from app.services.loyalty_service import (
    calculate_best_bank_offer,
    get_or_create_loyalty_profile,
    redeem_supercoins,
)

router = APIRouter()


@router.get("/profile", response_model=UserLoyaltyProfileResponse)
async def get_loyalty_profile(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve user's SuperCoins balance, loyalty tier status, and coin transactions history."""
    profile = await get_or_create_loyalty_profile(db, current_user.id)

    # Fetch recent transactions
    tx_stmt = (
        select(SuperCoinTransaction)
        .where(SuperCoinTransaction.profile_id == profile.id)
        .order_by(SuperCoinTransaction.created_at.desc())
        .limit(20)
    )
    tx_res = await db.execute(tx_stmt)
    txns = tx_res.scalars().all()

    return UserLoyaltyProfileResponse(
        id=profile.id,
        user_id=profile.user_id,
        tier=profile.tier,
        supercoin_balance=profile.supercoin_balance,
        lifetime_coins_earned=profile.lifetime_coins_earned,
        lifetime_coins_spent=profile.lifetime_coins_spent,
        tier_points=profile.tier_points,
        is_flipkart_plus_member=profile.is_flipkart_plus_member,
        plus_membership_expires_at=profile.plus_membership_expires_at,
        recent_transactions=[SuperCoinTransactionResponse.model_validate(t) for t in txns],
    )


@router.post("/quote", response_model=SuperCoinRedemptionQuoteResponse)
async def quote_supercoin_redemption(
    payload: SuperCoinRedemptionQuoteRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Calculate maximum usable SuperCoins for a checkout cart."""
    profile = await get_or_create_loyalty_profile(db, current_user.id)

    # Max coins usable is up to 50% of cart total or full user balance
    max_allowed = min(int(payload.cart_total * Decimal("0.50")), profile.supercoin_balance)
    usable = min(payload.requested_coins, max_allowed)
    discount_val = Decimal(str(usable))
    remaining = max(Decimal("0.00"), payload.cart_total - discount_val)

    return SuperCoinRedemptionQuoteResponse(
        requested_coins=payload.requested_coins,
        usable_coins=usable,
        coin_discount_value_inr=discount_val,
        remaining_payable_inr=remaining,
        conversion_rate=Decimal("1.00"),
    )


@router.get("/bank-offers", response_model=List[BankOfferResponse])
async def list_active_bank_offers(
    db: AsyncSession = Depends(get_db),
):
    """List all active bank card discount offers available across the marketplace."""
    stmt = select(BankDiscountOffer).where(BankDiscountOffer.is_active == True).order_by(BankDiscountOffer.discount_percentage.desc().nullslast())
    res = await db.execute(stmt)
    return res.scalars().all()
