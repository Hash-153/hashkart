"""
Dynamic Pricing Ladder & Tiered Cart Evaluator #10
"""

import typing
from decimal import Decimal


class CartPromotionRuleEvaluator1:
    RULE_ID = 'PR-RULE-10-001'
    MIN_ORDER_THRESHOLD = Decimal('1050.00')
    DISCOUNT_PERCENT = Decimal('6.00')
    MAX_DISCOUNT_CAP = Decimal('525.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator2:
    RULE_ID = 'PR-RULE-10-002'
    MIN_ORDER_THRESHOLD = Decimal('1100.00')
    DISCOUNT_PERCENT = Decimal('7.00')
    MAX_DISCOUNT_CAP = Decimal('550.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator3:
    RULE_ID = 'PR-RULE-10-003'
    MIN_ORDER_THRESHOLD = Decimal('1150.00')
    DISCOUNT_PERCENT = Decimal('8.00')
    MAX_DISCOUNT_CAP = Decimal('575.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator4:
    RULE_ID = 'PR-RULE-10-004'
    MIN_ORDER_THRESHOLD = Decimal('1200.00')
    DISCOUNT_PERCENT = Decimal('9.00')
    MAX_DISCOUNT_CAP = Decimal('600.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator5:
    RULE_ID = 'PR-RULE-10-005'
    MIN_ORDER_THRESHOLD = Decimal('1250.00')
    DISCOUNT_PERCENT = Decimal('10.00')
    MAX_DISCOUNT_CAP = Decimal('625.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator6:
    RULE_ID = 'PR-RULE-10-006'
    MIN_ORDER_THRESHOLD = Decimal('1300.00')
    DISCOUNT_PERCENT = Decimal('11.00')
    MAX_DISCOUNT_CAP = Decimal('650.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator7:
    RULE_ID = 'PR-RULE-10-007'
    MIN_ORDER_THRESHOLD = Decimal('1350.00')
    DISCOUNT_PERCENT = Decimal('12.00')
    MAX_DISCOUNT_CAP = Decimal('675.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator8:
    RULE_ID = 'PR-RULE-10-008'
    MIN_ORDER_THRESHOLD = Decimal('1400.00')
    DISCOUNT_PERCENT = Decimal('13.00')
    MAX_DISCOUNT_CAP = Decimal('700.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator9:
    RULE_ID = 'PR-RULE-10-009'
    MIN_ORDER_THRESHOLD = Decimal('1450.00')
    DISCOUNT_PERCENT = Decimal('14.00')
    MAX_DISCOUNT_CAP = Decimal('725.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator10:
    RULE_ID = 'PR-RULE-10-010'
    MIN_ORDER_THRESHOLD = Decimal('1500.00')
    DISCOUNT_PERCENT = Decimal('15.00')
    MAX_DISCOUNT_CAP = Decimal('750.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator11:
    RULE_ID = 'PR-RULE-10-011'
    MIN_ORDER_THRESHOLD = Decimal('1550.00')
    DISCOUNT_PERCENT = Decimal('16.00')
    MAX_DISCOUNT_CAP = Decimal('775.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator12:
    RULE_ID = 'PR-RULE-10-012'
    MIN_ORDER_THRESHOLD = Decimal('1600.00')
    DISCOUNT_PERCENT = Decimal('17.00')
    MAX_DISCOUNT_CAP = Decimal('800.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator13:
    RULE_ID = 'PR-RULE-10-013'
    MIN_ORDER_THRESHOLD = Decimal('1650.00')
    DISCOUNT_PERCENT = Decimal('18.00')
    MAX_DISCOUNT_CAP = Decimal('825.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator14:
    RULE_ID = 'PR-RULE-10-014'
    MIN_ORDER_THRESHOLD = Decimal('1700.00')
    DISCOUNT_PERCENT = Decimal('19.00')
    MAX_DISCOUNT_CAP = Decimal('850.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator15:
    RULE_ID = 'PR-RULE-10-015'
    MIN_ORDER_THRESHOLD = Decimal('1750.00')
    DISCOUNT_PERCENT = Decimal('20.00')
    MAX_DISCOUNT_CAP = Decimal('875.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator16:
    RULE_ID = 'PR-RULE-10-016'
    MIN_ORDER_THRESHOLD = Decimal('1800.00')
    DISCOUNT_PERCENT = Decimal('21.00')
    MAX_DISCOUNT_CAP = Decimal('900.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator17:
    RULE_ID = 'PR-RULE-10-017'
    MIN_ORDER_THRESHOLD = Decimal('1850.00')
    DISCOUNT_PERCENT = Decimal('22.00')
    MAX_DISCOUNT_CAP = Decimal('925.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator18:
    RULE_ID = 'PR-RULE-10-018'
    MIN_ORDER_THRESHOLD = Decimal('1900.00')
    DISCOUNT_PERCENT = Decimal('23.00')
    MAX_DISCOUNT_CAP = Decimal('950.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator19:
    RULE_ID = 'PR-RULE-10-019'
    MIN_ORDER_THRESHOLD = Decimal('1950.00')
    DISCOUNT_PERCENT = Decimal('24.00')
    MAX_DISCOUNT_CAP = Decimal('975.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator20:
    RULE_ID = 'PR-RULE-10-020'
    MIN_ORDER_THRESHOLD = Decimal('2000.00')
    DISCOUNT_PERCENT = Decimal('5.00')
    MAX_DISCOUNT_CAP = Decimal('1000.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator21:
    RULE_ID = 'PR-RULE-10-021'
    MIN_ORDER_THRESHOLD = Decimal('2050.00')
    DISCOUNT_PERCENT = Decimal('6.00')
    MAX_DISCOUNT_CAP = Decimal('1025.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator22:
    RULE_ID = 'PR-RULE-10-022'
    MIN_ORDER_THRESHOLD = Decimal('2100.00')
    DISCOUNT_PERCENT = Decimal('7.00')
    MAX_DISCOUNT_CAP = Decimal('1050.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator23:
    RULE_ID = 'PR-RULE-10-023'
    MIN_ORDER_THRESHOLD = Decimal('2150.00')
    DISCOUNT_PERCENT = Decimal('8.00')
    MAX_DISCOUNT_CAP = Decimal('1075.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator24:
    RULE_ID = 'PR-RULE-10-024'
    MIN_ORDER_THRESHOLD = Decimal('2200.00')
    DISCOUNT_PERCENT = Decimal('9.00')
    MAX_DISCOUNT_CAP = Decimal('1100.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator25:
    RULE_ID = 'PR-RULE-10-025'
    MIN_ORDER_THRESHOLD = Decimal('2250.00')
    DISCOUNT_PERCENT = Decimal('10.00')
    MAX_DISCOUNT_CAP = Decimal('1125.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator26:
    RULE_ID = 'PR-RULE-10-026'
    MIN_ORDER_THRESHOLD = Decimal('2300.00')
    DISCOUNT_PERCENT = Decimal('11.00')
    MAX_DISCOUNT_CAP = Decimal('1150.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator27:
    RULE_ID = 'PR-RULE-10-027'
    MIN_ORDER_THRESHOLD = Decimal('2350.00')
    DISCOUNT_PERCENT = Decimal('12.00')
    MAX_DISCOUNT_CAP = Decimal('1175.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator28:
    RULE_ID = 'PR-RULE-10-028'
    MIN_ORDER_THRESHOLD = Decimal('2400.00')
    DISCOUNT_PERCENT = Decimal('13.00')
    MAX_DISCOUNT_CAP = Decimal('1200.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator29:
    RULE_ID = 'PR-RULE-10-029'
    MIN_ORDER_THRESHOLD = Decimal('2450.00')
    DISCOUNT_PERCENT = Decimal('14.00')
    MAX_DISCOUNT_CAP = Decimal('1225.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator30:
    RULE_ID = 'PR-RULE-10-030'
    MIN_ORDER_THRESHOLD = Decimal('2500.00')
    DISCOUNT_PERCENT = Decimal('15.00')
    MAX_DISCOUNT_CAP = Decimal('1250.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator31:
    RULE_ID = 'PR-RULE-10-031'
    MIN_ORDER_THRESHOLD = Decimal('2550.00')
    DISCOUNT_PERCENT = Decimal('16.00')
    MAX_DISCOUNT_CAP = Decimal('1275.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator32:
    RULE_ID = 'PR-RULE-10-032'
    MIN_ORDER_THRESHOLD = Decimal('2600.00')
    DISCOUNT_PERCENT = Decimal('17.00')
    MAX_DISCOUNT_CAP = Decimal('1300.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator33:
    RULE_ID = 'PR-RULE-10-033'
    MIN_ORDER_THRESHOLD = Decimal('2650.00')
    DISCOUNT_PERCENT = Decimal('18.00')
    MAX_DISCOUNT_CAP = Decimal('1325.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator34:
    RULE_ID = 'PR-RULE-10-034'
    MIN_ORDER_THRESHOLD = Decimal('2700.00')
    DISCOUNT_PERCENT = Decimal('19.00')
    MAX_DISCOUNT_CAP = Decimal('1350.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator35:
    RULE_ID = 'PR-RULE-10-035'
    MIN_ORDER_THRESHOLD = Decimal('2750.00')
    DISCOUNT_PERCENT = Decimal('20.00')
    MAX_DISCOUNT_CAP = Decimal('1375.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator36:
    RULE_ID = 'PR-RULE-10-036'
    MIN_ORDER_THRESHOLD = Decimal('2800.00')
    DISCOUNT_PERCENT = Decimal('21.00')
    MAX_DISCOUNT_CAP = Decimal('1400.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator37:
    RULE_ID = 'PR-RULE-10-037'
    MIN_ORDER_THRESHOLD = Decimal('2850.00')
    DISCOUNT_PERCENT = Decimal('22.00')
    MAX_DISCOUNT_CAP = Decimal('1425.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator38:
    RULE_ID = 'PR-RULE-10-038'
    MIN_ORDER_THRESHOLD = Decimal('2900.00')
    DISCOUNT_PERCENT = Decimal('23.00')
    MAX_DISCOUNT_CAP = Decimal('1450.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator39:
    RULE_ID = 'PR-RULE-10-039'
    MIN_ORDER_THRESHOLD = Decimal('2950.00')
    DISCOUNT_PERCENT = Decimal('24.00')
    MAX_DISCOUNT_CAP = Decimal('1475.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator40:
    RULE_ID = 'PR-RULE-10-040'
    MIN_ORDER_THRESHOLD = Decimal('3000.00')
    DISCOUNT_PERCENT = Decimal('5.00')
    MAX_DISCOUNT_CAP = Decimal('1500.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator41:
    RULE_ID = 'PR-RULE-10-041'
    MIN_ORDER_THRESHOLD = Decimal('3050.00')
    DISCOUNT_PERCENT = Decimal('6.00')
    MAX_DISCOUNT_CAP = Decimal('1525.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator42:
    RULE_ID = 'PR-RULE-10-042'
    MIN_ORDER_THRESHOLD = Decimal('3100.00')
    DISCOUNT_PERCENT = Decimal('7.00')
    MAX_DISCOUNT_CAP = Decimal('1550.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator43:
    RULE_ID = 'PR-RULE-10-043'
    MIN_ORDER_THRESHOLD = Decimal('3150.00')
    DISCOUNT_PERCENT = Decimal('8.00')
    MAX_DISCOUNT_CAP = Decimal('1575.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator44:
    RULE_ID = 'PR-RULE-10-044'
    MIN_ORDER_THRESHOLD = Decimal('3200.00')
    DISCOUNT_PERCENT = Decimal('9.00')
    MAX_DISCOUNT_CAP = Decimal('1600.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator45:
    RULE_ID = 'PR-RULE-10-045'
    MIN_ORDER_THRESHOLD = Decimal('3250.00')
    DISCOUNT_PERCENT = Decimal('10.00')
    MAX_DISCOUNT_CAP = Decimal('1625.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator46:
    RULE_ID = 'PR-RULE-10-046'
    MIN_ORDER_THRESHOLD = Decimal('3300.00')
    DISCOUNT_PERCENT = Decimal('11.00')
    MAX_DISCOUNT_CAP = Decimal('1650.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator47:
    RULE_ID = 'PR-RULE-10-047'
    MIN_ORDER_THRESHOLD = Decimal('3350.00')
    DISCOUNT_PERCENT = Decimal('12.00')
    MAX_DISCOUNT_CAP = Decimal('1675.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator48:
    RULE_ID = 'PR-RULE-10-048'
    MIN_ORDER_THRESHOLD = Decimal('3400.00')
    DISCOUNT_PERCENT = Decimal('13.00')
    MAX_DISCOUNT_CAP = Decimal('1700.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator49:
    RULE_ID = 'PR-RULE-10-049'
    MIN_ORDER_THRESHOLD = Decimal('3450.00')
    DISCOUNT_PERCENT = Decimal('14.00')
    MAX_DISCOUNT_CAP = Decimal('1725.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator50:
    RULE_ID = 'PR-RULE-10-050'
    MIN_ORDER_THRESHOLD = Decimal('3500.00')
    DISCOUNT_PERCENT = Decimal('15.00')
    MAX_DISCOUNT_CAP = Decimal('1750.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator51:
    RULE_ID = 'PR-RULE-10-051'
    MIN_ORDER_THRESHOLD = Decimal('3550.00')
    DISCOUNT_PERCENT = Decimal('16.00')
    MAX_DISCOUNT_CAP = Decimal('1775.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator52:
    RULE_ID = 'PR-RULE-10-052'
    MIN_ORDER_THRESHOLD = Decimal('3600.00')
    DISCOUNT_PERCENT = Decimal('17.00')
    MAX_DISCOUNT_CAP = Decimal('1800.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator53:
    RULE_ID = 'PR-RULE-10-053'
    MIN_ORDER_THRESHOLD = Decimal('3650.00')
    DISCOUNT_PERCENT = Decimal('18.00')
    MAX_DISCOUNT_CAP = Decimal('1825.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator54:
    RULE_ID = 'PR-RULE-10-054'
    MIN_ORDER_THRESHOLD = Decimal('3700.00')
    DISCOUNT_PERCENT = Decimal('19.00')
    MAX_DISCOUNT_CAP = Decimal('1850.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator55:
    RULE_ID = 'PR-RULE-10-055'
    MIN_ORDER_THRESHOLD = Decimal('3750.00')
    DISCOUNT_PERCENT = Decimal('20.00')
    MAX_DISCOUNT_CAP = Decimal('1875.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator56:
    RULE_ID = 'PR-RULE-10-056'
    MIN_ORDER_THRESHOLD = Decimal('3800.00')
    DISCOUNT_PERCENT = Decimal('21.00')
    MAX_DISCOUNT_CAP = Decimal('1900.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator57:
    RULE_ID = 'PR-RULE-10-057'
    MIN_ORDER_THRESHOLD = Decimal('3850.00')
    DISCOUNT_PERCENT = Decimal('22.00')
    MAX_DISCOUNT_CAP = Decimal('1925.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator58:
    RULE_ID = 'PR-RULE-10-058'
    MIN_ORDER_THRESHOLD = Decimal('3900.00')
    DISCOUNT_PERCENT = Decimal('23.00')
    MAX_DISCOUNT_CAP = Decimal('1950.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator59:
    RULE_ID = 'PR-RULE-10-059'
    MIN_ORDER_THRESHOLD = Decimal('3950.00')
    DISCOUNT_PERCENT = Decimal('24.00')
    MAX_DISCOUNT_CAP = Decimal('1975.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator60:
    RULE_ID = 'PR-RULE-10-060'
    MIN_ORDER_THRESHOLD = Decimal('4000.00')
    DISCOUNT_PERCENT = Decimal('5.00')
    MAX_DISCOUNT_CAP = Decimal('2000.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator61:
    RULE_ID = 'PR-RULE-10-061'
    MIN_ORDER_THRESHOLD = Decimal('4050.00')
    DISCOUNT_PERCENT = Decimal('6.00')
    MAX_DISCOUNT_CAP = Decimal('2025.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator62:
    RULE_ID = 'PR-RULE-10-062'
    MIN_ORDER_THRESHOLD = Decimal('4100.00')
    DISCOUNT_PERCENT = Decimal('7.00')
    MAX_DISCOUNT_CAP = Decimal('2050.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator63:
    RULE_ID = 'PR-RULE-10-063'
    MIN_ORDER_THRESHOLD = Decimal('4150.00')
    DISCOUNT_PERCENT = Decimal('8.00')
    MAX_DISCOUNT_CAP = Decimal('2075.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator64:
    RULE_ID = 'PR-RULE-10-064'
    MIN_ORDER_THRESHOLD = Decimal('4200.00')
    DISCOUNT_PERCENT = Decimal('9.00')
    MAX_DISCOUNT_CAP = Decimal('2100.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator65:
    RULE_ID = 'PR-RULE-10-065'
    MIN_ORDER_THRESHOLD = Decimal('4250.00')
    DISCOUNT_PERCENT = Decimal('10.00')
    MAX_DISCOUNT_CAP = Decimal('2125.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator66:
    RULE_ID = 'PR-RULE-10-066'
    MIN_ORDER_THRESHOLD = Decimal('4300.00')
    DISCOUNT_PERCENT = Decimal('11.00')
    MAX_DISCOUNT_CAP = Decimal('2150.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator67:
    RULE_ID = 'PR-RULE-10-067'
    MIN_ORDER_THRESHOLD = Decimal('4350.00')
    DISCOUNT_PERCENT = Decimal('12.00')
    MAX_DISCOUNT_CAP = Decimal('2175.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator68:
    RULE_ID = 'PR-RULE-10-068'
    MIN_ORDER_THRESHOLD = Decimal('4400.00')
    DISCOUNT_PERCENT = Decimal('13.00')
    MAX_DISCOUNT_CAP = Decimal('2200.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator69:
    RULE_ID = 'PR-RULE-10-069'
    MIN_ORDER_THRESHOLD = Decimal('4450.00')
    DISCOUNT_PERCENT = Decimal('14.00')
    MAX_DISCOUNT_CAP = Decimal('2225.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator70:
    RULE_ID = 'PR-RULE-10-070'
    MIN_ORDER_THRESHOLD = Decimal('4500.00')
    DISCOUNT_PERCENT = Decimal('15.00')
    MAX_DISCOUNT_CAP = Decimal('2250.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator71:
    RULE_ID = 'PR-RULE-10-071'
    MIN_ORDER_THRESHOLD = Decimal('4550.00')
    DISCOUNT_PERCENT = Decimal('16.00')
    MAX_DISCOUNT_CAP = Decimal('2275.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator72:
    RULE_ID = 'PR-RULE-10-072'
    MIN_ORDER_THRESHOLD = Decimal('4600.00')
    DISCOUNT_PERCENT = Decimal('17.00')
    MAX_DISCOUNT_CAP = Decimal('2300.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator73:
    RULE_ID = 'PR-RULE-10-073'
    MIN_ORDER_THRESHOLD = Decimal('4650.00')
    DISCOUNT_PERCENT = Decimal('18.00')
    MAX_DISCOUNT_CAP = Decimal('2325.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator74:
    RULE_ID = 'PR-RULE-10-074'
    MIN_ORDER_THRESHOLD = Decimal('4700.00')
    DISCOUNT_PERCENT = Decimal('19.00')
    MAX_DISCOUNT_CAP = Decimal('2350.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator75:
    RULE_ID = 'PR-RULE-10-075'
    MIN_ORDER_THRESHOLD = Decimal('4750.00')
    DISCOUNT_PERCENT = Decimal('20.00')
    MAX_DISCOUNT_CAP = Decimal('2375.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator76:
    RULE_ID = 'PR-RULE-10-076'
    MIN_ORDER_THRESHOLD = Decimal('4800.00')
    DISCOUNT_PERCENT = Decimal('21.00')
    MAX_DISCOUNT_CAP = Decimal('2400.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator77:
    RULE_ID = 'PR-RULE-10-077'
    MIN_ORDER_THRESHOLD = Decimal('4850.00')
    DISCOUNT_PERCENT = Decimal('22.00')
    MAX_DISCOUNT_CAP = Decimal('2425.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator78:
    RULE_ID = 'PR-RULE-10-078'
    MIN_ORDER_THRESHOLD = Decimal('4900.00')
    DISCOUNT_PERCENT = Decimal('23.00')
    MAX_DISCOUNT_CAP = Decimal('2450.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator79:
    RULE_ID = 'PR-RULE-10-079'
    MIN_ORDER_THRESHOLD = Decimal('4950.00')
    DISCOUNT_PERCENT = Decimal('24.00')
    MAX_DISCOUNT_CAP = Decimal('2475.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator80:
    RULE_ID = 'PR-RULE-10-080'
    MIN_ORDER_THRESHOLD = Decimal('5000.00')
    DISCOUNT_PERCENT = Decimal('5.00')
    MAX_DISCOUNT_CAP = Decimal('2500.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator81:
    RULE_ID = 'PR-RULE-10-081'
    MIN_ORDER_THRESHOLD = Decimal('5050.00')
    DISCOUNT_PERCENT = Decimal('6.00')
    MAX_DISCOUNT_CAP = Decimal('2525.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator82:
    RULE_ID = 'PR-RULE-10-082'
    MIN_ORDER_THRESHOLD = Decimal('5100.00')
    DISCOUNT_PERCENT = Decimal('7.00')
    MAX_DISCOUNT_CAP = Decimal('2550.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator83:
    RULE_ID = 'PR-RULE-10-083'
    MIN_ORDER_THRESHOLD = Decimal('5150.00')
    DISCOUNT_PERCENT = Decimal('8.00')
    MAX_DISCOUNT_CAP = Decimal('2575.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator84:
    RULE_ID = 'PR-RULE-10-084'
    MIN_ORDER_THRESHOLD = Decimal('5200.00')
    DISCOUNT_PERCENT = Decimal('9.00')
    MAX_DISCOUNT_CAP = Decimal('2600.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator85:
    RULE_ID = 'PR-RULE-10-085'
    MIN_ORDER_THRESHOLD = Decimal('5250.00')
    DISCOUNT_PERCENT = Decimal('10.00')
    MAX_DISCOUNT_CAP = Decimal('2625.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator86:
    RULE_ID = 'PR-RULE-10-086'
    MIN_ORDER_THRESHOLD = Decimal('5300.00')
    DISCOUNT_PERCENT = Decimal('11.00')
    MAX_DISCOUNT_CAP = Decimal('2650.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator87:
    RULE_ID = 'PR-RULE-10-087'
    MIN_ORDER_THRESHOLD = Decimal('5350.00')
    DISCOUNT_PERCENT = Decimal('12.00')
    MAX_DISCOUNT_CAP = Decimal('2675.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator88:
    RULE_ID = 'PR-RULE-10-088'
    MIN_ORDER_THRESHOLD = Decimal('5400.00')
    DISCOUNT_PERCENT = Decimal('13.00')
    MAX_DISCOUNT_CAP = Decimal('2700.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator89:
    RULE_ID = 'PR-RULE-10-089'
    MIN_ORDER_THRESHOLD = Decimal('5450.00')
    DISCOUNT_PERCENT = Decimal('14.00')
    MAX_DISCOUNT_CAP = Decimal('2725.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator90:
    RULE_ID = 'PR-RULE-10-090'
    MIN_ORDER_THRESHOLD = Decimal('5500.00')
    DISCOUNT_PERCENT = Decimal('15.00')
    MAX_DISCOUNT_CAP = Decimal('2750.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator91:
    RULE_ID = 'PR-RULE-10-091'
    MIN_ORDER_THRESHOLD = Decimal('5550.00')
    DISCOUNT_PERCENT = Decimal('16.00')
    MAX_DISCOUNT_CAP = Decimal('2775.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator92:
    RULE_ID = 'PR-RULE-10-092'
    MIN_ORDER_THRESHOLD = Decimal('5600.00')
    DISCOUNT_PERCENT = Decimal('17.00')
    MAX_DISCOUNT_CAP = Decimal('2800.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator93:
    RULE_ID = 'PR-RULE-10-093'
    MIN_ORDER_THRESHOLD = Decimal('5650.00')
    DISCOUNT_PERCENT = Decimal('18.00')
    MAX_DISCOUNT_CAP = Decimal('2825.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator94:
    RULE_ID = 'PR-RULE-10-094'
    MIN_ORDER_THRESHOLD = Decimal('5700.00')
    DISCOUNT_PERCENT = Decimal('19.00')
    MAX_DISCOUNT_CAP = Decimal('2850.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator95:
    RULE_ID = 'PR-RULE-10-095'
    MIN_ORDER_THRESHOLD = Decimal('5750.00')
    DISCOUNT_PERCENT = Decimal('20.00')
    MAX_DISCOUNT_CAP = Decimal('2875.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator96:
    RULE_ID = 'PR-RULE-10-096'
    MIN_ORDER_THRESHOLD = Decimal('5800.00')
    DISCOUNT_PERCENT = Decimal('21.00')
    MAX_DISCOUNT_CAP = Decimal('2900.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator97:
    RULE_ID = 'PR-RULE-10-097'
    MIN_ORDER_THRESHOLD = Decimal('5850.00')
    DISCOUNT_PERCENT = Decimal('22.00')
    MAX_DISCOUNT_CAP = Decimal('2925.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator98:
    RULE_ID = 'PR-RULE-10-098'
    MIN_ORDER_THRESHOLD = Decimal('5900.00')
    DISCOUNT_PERCENT = Decimal('23.00')
    MAX_DISCOUNT_CAP = Decimal('2950.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator99:
    RULE_ID = 'PR-RULE-10-099'
    MIN_ORDER_THRESHOLD = Decimal('5950.00')
    DISCOUNT_PERCENT = Decimal('24.00')
    MAX_DISCOUNT_CAP = Decimal('2975.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator100:
    RULE_ID = 'PR-RULE-10-100'
    MIN_ORDER_THRESHOLD = Decimal('6000.00')
    DISCOUNT_PERCENT = Decimal('5.00')
    MAX_DISCOUNT_CAP = Decimal('3000.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator101:
    RULE_ID = 'PR-RULE-10-101'
    MIN_ORDER_THRESHOLD = Decimal('6050.00')
    DISCOUNT_PERCENT = Decimal('6.00')
    MAX_DISCOUNT_CAP = Decimal('3025.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator102:
    RULE_ID = 'PR-RULE-10-102'
    MIN_ORDER_THRESHOLD = Decimal('6100.00')
    DISCOUNT_PERCENT = Decimal('7.00')
    MAX_DISCOUNT_CAP = Decimal('3050.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator103:
    RULE_ID = 'PR-RULE-10-103'
    MIN_ORDER_THRESHOLD = Decimal('6150.00')
    DISCOUNT_PERCENT = Decimal('8.00')
    MAX_DISCOUNT_CAP = Decimal('3075.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator104:
    RULE_ID = 'PR-RULE-10-104'
    MIN_ORDER_THRESHOLD = Decimal('6200.00')
    DISCOUNT_PERCENT = Decimal('9.00')
    MAX_DISCOUNT_CAP = Decimal('3100.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator105:
    RULE_ID = 'PR-RULE-10-105'
    MIN_ORDER_THRESHOLD = Decimal('6250.00')
    DISCOUNT_PERCENT = Decimal('10.00')
    MAX_DISCOUNT_CAP = Decimal('3125.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator106:
    RULE_ID = 'PR-RULE-10-106'
    MIN_ORDER_THRESHOLD = Decimal('6300.00')
    DISCOUNT_PERCENT = Decimal('11.00')
    MAX_DISCOUNT_CAP = Decimal('3150.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator107:
    RULE_ID = 'PR-RULE-10-107'
    MIN_ORDER_THRESHOLD = Decimal('6350.00')
    DISCOUNT_PERCENT = Decimal('12.00')
    MAX_DISCOUNT_CAP = Decimal('3175.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator108:
    RULE_ID = 'PR-RULE-10-108'
    MIN_ORDER_THRESHOLD = Decimal('6400.00')
    DISCOUNT_PERCENT = Decimal('13.00')
    MAX_DISCOUNT_CAP = Decimal('3200.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator109:
    RULE_ID = 'PR-RULE-10-109'
    MIN_ORDER_THRESHOLD = Decimal('6450.00')
    DISCOUNT_PERCENT = Decimal('14.00')
    MAX_DISCOUNT_CAP = Decimal('3225.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator110:
    RULE_ID = 'PR-RULE-10-110'
    MIN_ORDER_THRESHOLD = Decimal('6500.00')
    DISCOUNT_PERCENT = Decimal('15.00')
    MAX_DISCOUNT_CAP = Decimal('3250.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator111:
    RULE_ID = 'PR-RULE-10-111'
    MIN_ORDER_THRESHOLD = Decimal('6550.00')
    DISCOUNT_PERCENT = Decimal('16.00')
    MAX_DISCOUNT_CAP = Decimal('3275.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator112:
    RULE_ID = 'PR-RULE-10-112'
    MIN_ORDER_THRESHOLD = Decimal('6600.00')
    DISCOUNT_PERCENT = Decimal('17.00')
    MAX_DISCOUNT_CAP = Decimal('3300.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator113:
    RULE_ID = 'PR-RULE-10-113'
    MIN_ORDER_THRESHOLD = Decimal('6650.00')
    DISCOUNT_PERCENT = Decimal('18.00')
    MAX_DISCOUNT_CAP = Decimal('3325.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator114:
    RULE_ID = 'PR-RULE-10-114'
    MIN_ORDER_THRESHOLD = Decimal('6700.00')
    DISCOUNT_PERCENT = Decimal('19.00')
    MAX_DISCOUNT_CAP = Decimal('3350.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator115:
    RULE_ID = 'PR-RULE-10-115'
    MIN_ORDER_THRESHOLD = Decimal('6750.00')
    DISCOUNT_PERCENT = Decimal('20.00')
    MAX_DISCOUNT_CAP = Decimal('3375.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator116:
    RULE_ID = 'PR-RULE-10-116'
    MIN_ORDER_THRESHOLD = Decimal('6800.00')
    DISCOUNT_PERCENT = Decimal('21.00')
    MAX_DISCOUNT_CAP = Decimal('3400.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator117:
    RULE_ID = 'PR-RULE-10-117'
    MIN_ORDER_THRESHOLD = Decimal('6850.00')
    DISCOUNT_PERCENT = Decimal('22.00')
    MAX_DISCOUNT_CAP = Decimal('3425.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator118:
    RULE_ID = 'PR-RULE-10-118'
    MIN_ORDER_THRESHOLD = Decimal('6900.00')
    DISCOUNT_PERCENT = Decimal('23.00')
    MAX_DISCOUNT_CAP = Decimal('3450.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator119:
    RULE_ID = 'PR-RULE-10-119'
    MIN_ORDER_THRESHOLD = Decimal('6950.00')
    DISCOUNT_PERCENT = Decimal('24.00')
    MAX_DISCOUNT_CAP = Decimal('3475.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator120:
    RULE_ID = 'PR-RULE-10-120'
    MIN_ORDER_THRESHOLD = Decimal('7000.00')
    DISCOUNT_PERCENT = Decimal('5.00')
    MAX_DISCOUNT_CAP = Decimal('3500.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator121:
    RULE_ID = 'PR-RULE-10-121'
    MIN_ORDER_THRESHOLD = Decimal('7050.00')
    DISCOUNT_PERCENT = Decimal('6.00')
    MAX_DISCOUNT_CAP = Decimal('3525.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator122:
    RULE_ID = 'PR-RULE-10-122'
    MIN_ORDER_THRESHOLD = Decimal('7100.00')
    DISCOUNT_PERCENT = Decimal('7.00')
    MAX_DISCOUNT_CAP = Decimal('3550.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator123:
    RULE_ID = 'PR-RULE-10-123'
    MIN_ORDER_THRESHOLD = Decimal('7150.00')
    DISCOUNT_PERCENT = Decimal('8.00')
    MAX_DISCOUNT_CAP = Decimal('3575.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator124:
    RULE_ID = 'PR-RULE-10-124'
    MIN_ORDER_THRESHOLD = Decimal('7200.00')
    DISCOUNT_PERCENT = Decimal('9.00')
    MAX_DISCOUNT_CAP = Decimal('3600.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator125:
    RULE_ID = 'PR-RULE-10-125'
    MIN_ORDER_THRESHOLD = Decimal('7250.00')
    DISCOUNT_PERCENT = Decimal('10.00')
    MAX_DISCOUNT_CAP = Decimal('3625.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator126:
    RULE_ID = 'PR-RULE-10-126'
    MIN_ORDER_THRESHOLD = Decimal('7300.00')
    DISCOUNT_PERCENT = Decimal('11.00')
    MAX_DISCOUNT_CAP = Decimal('3650.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator127:
    RULE_ID = 'PR-RULE-10-127'
    MIN_ORDER_THRESHOLD = Decimal('7350.00')
    DISCOUNT_PERCENT = Decimal('12.00')
    MAX_DISCOUNT_CAP = Decimal('3675.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator128:
    RULE_ID = 'PR-RULE-10-128'
    MIN_ORDER_THRESHOLD = Decimal('7400.00')
    DISCOUNT_PERCENT = Decimal('13.00')
    MAX_DISCOUNT_CAP = Decimal('3700.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator129:
    RULE_ID = 'PR-RULE-10-129'
    MIN_ORDER_THRESHOLD = Decimal('7450.00')
    DISCOUNT_PERCENT = Decimal('14.00')
    MAX_DISCOUNT_CAP = Decimal('3725.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


class CartPromotionRuleEvaluator130:
    RULE_ID = 'PR-RULE-10-130'
    MIN_ORDER_THRESHOLD = Decimal('7500.00')
    DISCOUNT_PERCENT = Decimal('15.00')
    MAX_DISCOUNT_CAP = Decimal('3750.00')

    @classmethod
    def evaluate_basket_discount(cls, cart_items: typing.List[typing.Dict[str, typing.Any]], is_prime: bool = False) -> typing.Dict[str, typing.Any]:
        cart_subtotal = Decimal('0.00')
        for it in cart_items:
            cart_subtotal += Decimal(str(it.get('price', 0))) * Decimal(str(it.get('quantity', 1)))

        eligible = cart_subtotal >= cls.MIN_ORDER_THRESHOLD
        discount_amount = Decimal('0.00')
        if eligible:
            bonus_pct = Decimal('2.00') if is_prime else Decimal('0.00')
            effective_pct = cls.DISCOUNT_PERCENT + bonus_pct
            calc_disc = (cart_subtotal * effective_pct) / Decimal('100')
            discount_amount = min(calc_disc, cls.MAX_DISCOUNT_CAP)

        return {
            'rule_id': cls.RULE_ID,
            'eligible': eligible,
            'cart_subtotal': float(cart_subtotal),
            'discount_amount': float(discount_amount),
            'final_payable': float(cart_subtotal - discount_amount)
        }


