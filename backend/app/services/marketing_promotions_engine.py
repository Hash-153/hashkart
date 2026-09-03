"""
NovaMart Targeted Promotions, SuperCoin Minting & Bank Discount Engine
======================================================================
Coordinates complex promotional rules for high-conversion festivals:
- Rule-based Cart Level Discounts (Tiered % off, Free Shipping thresholds)
- Bank Card Instant Discounts (e.g. 10% Instant Discount on HDFC/ICICI Credit Cards, max cap ₹1,500)
- SuperCoins Loyalty Profile (Minting 4 coins / ₹100 for Plus, 2 coins for Non-Plus; Coin burning at ₹1.00/coin)
- Flash Sale inventory claim concurrency locks
- No-Cost EMI interest subvention calculations
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Optional, Tuple


class PromotionType(str, Enum):
    BANK_CARD_INSTANT_DISCOUNT = "BANK_CARD_INSTANT_DISCOUNT"
    CART_THRESHOLD_DISCOUNT = "CART_THRESHOLD_DISCOUNT"
    BUY_X_GET_Y = "BUY_X_GET_Y"
    SUPERCOIN_BONUS_MULTIPLIER = "SUPERCOIN_BONUS_MULTIPLIER"
    NO_COST_EMI_SUBVENTION = "NO_COST_EMI_SUBVENTION"


@dataclass
class BankCardOfferRule:
    offer_id: str
    bank_name: str # e.g. "HDFC", "ICICI", "SBI", "AXIS"
    card_type: str # 'CREDIT_CARD', 'DEBIT_CARD'
    discount_percentage: Decimal
    max_discount_cap: Decimal
    min_cart_value: Decimal
    is_active: bool


@dataclass
class SuperCoinPassbookTransaction:
    transaction_id: str
    user_id: int
    order_number: Optional[str]
    coins_amount: int
    transaction_type: str # 'EARNED_FROM_ORDER', 'REDEEMED_ON_CHECKOUT', 'EXPIRY', 'REFUND_REVERSED'
    running_balance: int
    timestamp: datetime


@dataclass
class CheckoutDiscountBreakdown:
    original_subtotal: Decimal
    coupon_discount: Decimal
    bank_offer_discount: Decimal
    supercoins_redeemed_count: int
    supercoins_cash_discount: Decimal
    final_payable_amount: Decimal
    supercoins_to_be_minted: int
    applied_offer_descriptions: List[str]


class PromotionsAndLoyaltyEngine:
    BANK_OFFERS: List[BankCardOfferRule] = [
        BankCardOfferRule(offer_id="HDFC_CC_10", bank_name="HDFC", card_type="CREDIT_CARD", discount_percentage=Decimal("10.0"), max_discount_cap=Decimal("1500.00"), min_cart_value=Decimal("5000.00"), is_active=True),
        BankCardOfferRule(offer_id="ICICI_CC_10", bank_name="ICICI", card_type="CREDIT_CARD", discount_percentage=Decimal("10.0"), max_discount_cap=Decimal("1250.00"), min_cart_value=Decimal("5000.00"), is_active=True),
        BankCardOfferRule(offer_id="SBI_CC_75", bank_name="SBI", card_type="CREDIT_CARD", discount_percentage=Decimal("7.5"), max_discount_cap=Decimal("1000.00"), min_cart_value=Decimal("4000.00"), is_active=True),
        BankCardOfferRule(offer_id="AXIS_DC_5", bank_name="AXIS", card_type="DEBIT_CARD", discount_percentage=Decimal("5.0"), max_discount_cap=Decimal("500.00"), min_cart_value=Decimal("2500.00"), is_active=True),
    ]

    @classmethod
    def evaluate_checkout_discounts(
        cls,
        subtotal: Decimal,
        is_plus_member: bool,
        applied_coupon_code: Optional[str] = None,
        selected_bank: Optional[str] = None,
        selected_card_type: Optional[str] = None,
        requested_supercoins_to_burn: int = 0,
        user_available_supercoins: int = 0,
    ) -> CheckoutDiscountBreakdown:
        """Compute all stackable discounts, loyalty points, and cash payable total."""
        applied_descriptions: List[str] = []
        coupon_disc = Decimal("0.00")
        bank_disc = Decimal("0.00")

        # 1. Coupon Evaluation
        if applied_coupon_code:
            code = applied_coupon_code.upper().strip()
            if code == "FESTIVE10" and subtotal >= Decimal("1000.00"):
                coupon_disc = min(Decimal("1000.00"), (subtotal * Decimal("0.10")).quantize(Decimal("0.01")))
                applied_descriptions.append("Coupon 'FESTIVE10' applied (10% OFF)")
            elif code == "FLIPKART500" and subtotal >= Decimal("2999.00"):
                coupon_disc = Decimal("500.00")
                applied_descriptions.append("Coupon 'FLIPKART500' applied (Flat ₹500 OFF)")

        current_amount = max(Decimal("0.00"), subtotal - coupon_disc)

        # 2. Bank Card Offer Evaluation
        if selected_bank and selected_card_type:
            for offer in cls.BANK_OFFERS:
                if (
                    offer.is_active
                    and offer.bank_name.upper() == selected_bank.upper()
                    and offer.card_type.upper() == selected_card_type.upper()
                    and current_amount >= offer.min_cart_value
                ):
                    computed = (current_amount * (offer.discount_percentage / Decimal("100.0"))).quantize(Decimal("0.01"))
                    bank_disc = min(offer.max_discount_cap, computed)
                    applied_descriptions.append(
                        f"{offer.bank_name} {offer.card_type} {offer.discount_percentage}% Instant Discount (Saved ₹{bank_disc:,.2f})"
                    )
                    break

        current_amount = max(Decimal("0.00"), current_amount - bank_disc)

        # 3. SuperCoins Burning (1 Coin = ₹1.00 cash discount)
        burnable_coins = min(requested_supercoins_to_burn, user_available_supercoins, int(current_amount))
        supercoins_cash = Decimal(str(burnable_coins))
        if burnable_coins > 0:
            applied_descriptions.append(f"Redeemed {burnable_coins} SuperCoins (Saved ₹{burnable_coins})")

        final_payable = max(Decimal("0.00"), current_amount - supercoins_cash)

        # 4. SuperCoins Minting (Plus: 4 coins / ₹100 up to 100; Regular: 2 coins / ₹100 up to 50)
        hundreds_spent = int(final_payable // Decimal("100.00"))
        rate = 4 if is_plus_member else 2
        cap = 100 if is_plus_member else 50
        minted_coins = min(cap, hundreds_spent * rate)

        return CheckoutDiscountBreakdown(
            original_subtotal=subtotal,
            coupon_discount=coupon_disc,
            bank_offer_discount=bank_disc,
            supercoins_redeemed_count=burnable_coins,
            supercoins_cash_discount=supercoins_cash,
            final_payable_amount=final_payable,
            supercoins_to_be_minted=minted_coins,
            applied_offer_descriptions=applied_descriptions,
        )
