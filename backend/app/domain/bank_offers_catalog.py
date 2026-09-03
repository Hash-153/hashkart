"""
NovaMart Bank Offer Catalog, BIN Range Matcher & EMI Subvention Matrix
======================================================================
Card-issuer promotions and No-Cost EMI interest subvention schedules:
- Bank Card 6-digit IIN / BIN Range mapping (HDFC, ICICI, SBI, Axis, Kotak, Amex)
- Instant Cart Discount calculation rules (Min cart value, percentage discount, maximum cap)
- 3, 6, 9, 12, 18, 24 Month EMI interest calculations with merchant subvention
"""

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Dict, List, Optional, Tuple


@dataclass
class CardBINRangeDefinition:
    bin_prefix: str # 6-digit Bank Identification Number
    bank_name: str
    card_network: str # 'VISA', 'MASTERCARD', 'RUPAY', 'AMEX'
    card_tier: str # 'PLATINUM', 'SIGNATURE', 'INFINITE', 'MILLENNIA', 'REGALIA'
    is_credit: bool


@dataclass
class EMITenureOption:
    tenure_months: int
    annual_interest_rate_percent: Decimal
    is_no_cost_emi: bool
    monthly_installment_amount: Decimal
    total_interest_amount: Decimal
    merchant_interest_discount: Decimal
    total_effective_payable: Decimal


# Bank BIN Ranges Database
BANK_BIN_RANGES: List[CardBINRangeDefinition] = [
    # HDFC Bank
    CardBINRangeDefinition("405202", "HDFC", "VISA", "REGALIA_GOLD", True),
    CardBINRangeDefinition("462899", "HDFC", "VISA", "MILLENNIA", True),
    CardBINRangeDefinition("524178", "HDFC", "MASTERCARD", "DINERS_CLUB", True),
    CardBINRangeDefinition("607062", "HDFC", "RUPAY", "PLATINUM", False),

    # ICICI Bank
    CardBINRangeDefinition("437551", "ICICI", "VISA", "AMAZON_PAY", True),
    CardBINRangeDefinition("409758", "ICICI", "VISA", "CORAL", True),
    CardBINRangeDefinition("517643", "ICICI", "MASTERCARD", "RUBYXZ", True),
    CardBINRangeDefinition("607212", "ICICI", "RUPAY", "SELECT", True),

    # State Bank of India (SBI Card)
    CardBINRangeDefinition("472642", "SBI", "VISA", "SIMPLYCLICK", True),
    CardBINRangeDefinition("438628", "SBI", "VISA", "PRIME", True),
    CardBINRangeDefinition("522668", "SBI", "MASTERCARD", "AURUM", True),
    CardBINRangeDefinition("607384", "SBI", "RUPAY", "BPCL", True),

    # Axis Bank
    CardBINRangeDefinition("431581", "AXIS", "VISA", "FLIPKART_AXIS", True),
    CardBINRangeDefinition("403848", "AXIS", "VISA", "MAGNUS", True),
    CardBINRangeDefinition("540166", "AXIS", "MASTERCARD", "NEO", True),
]


class BankOffersAndEMICalculator:
    @staticmethod
    def identify_card_issuer_from_bin(first_6_digits: str) -> Optional[CardBINRangeDefinition]:
        """Match card 6-digit prefix against bank BIN database."""
        prefix = str(first_6_digits).strip()[:6]
        for b in BANK_BIN_RANGES:
            if b.bin_prefix == prefix:
                return b
        return None

    @staticmethod
    def calculate_emi_schedules(
        principal_amount: Decimal,
        is_no_cost_eligible: bool = True,
    ) -> List[EMITenureOption]:
        """Compute monthly installments across standard and No-Cost EMI tenures."""
        tenures = [
            (3, Decimal("14.0")),
            (6, Decimal("15.0")),
            (9, Decimal("15.5")),
            (12, Decimal("16.0")),
            (18, Decimal("16.5")),
            (24, Decimal("17.0")),
        ]

        results: List[EMITenureOption] = []
        p = float(principal_amount)

        for n, annual_rate in tenures:
            r = (float(annual_rate) / 100.0) / 12.0 # Monthly interest rate
            # Standard Equated Monthly Installment Formula: E = P * r * (1+r)^n / ((1+r)^n - 1)
            emi = p * (r * math.pow(1.0 + r, n)) / (math.pow(1.0 + r, n) - 1.0)
            total_repaid = emi * n
            total_interest = Decimal(str(round(total_repaid - p, 2)))
            monthly_inst = Decimal(str(round(emi, 2)))

            # If No-Cost EMI: Merchant gives upfront instant discount equal to the total bank interest
            merchant_discount = total_interest if is_no_cost_eligible else Decimal("0.00")
            effective_payable = (principal_amount + total_interest - merchant_discount).quantize(Decimal("0.01"))

            results.append(
                EMITenureOption(
                    tenure_months=n,
                    annual_interest_rate_percent=annual_rate,
                    is_no_cost_emi=is_no_cost_eligible,
                    monthly_installment_amount=monthly_inst,
                    total_interest_amount=total_interest,
                    merchant_interest_discount=merchant_discount,
                    total_effective_payable=effective_payable,
                )
            )

        return results
