"""
NovaMart Reverse Logistics & Doorstep Quality Control (QC) Engine
================================================================
Manages end-to-end customer return lifecycles:
- Doorstep pickup QC verification checklists (IMEI/Serial, Seal, Brand Box, Accessories)
- Return Reason categorization & fraud scoring
- Automated disposition routing (Restock -> Grade-B Refurbished -> Vendor Return -> Liquidation)
- Immediate Escrow debit and instant customer refund disbursement
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Tuple
import uuid


class ReturnDisposition(str, Enum):
    RESTOCK_AS_NEW = "RESTOCK_AS_NEW"
    GRADE_B_REFURBISHED = "GRADE_B_REFURBISHED"
    RETURN_TO_VENDOR = "RETURN_TO_VENDOR"
    LIQUIDATION_SCRAP = "LIQUIDATION_SCRAP"
    CUSTOMER_FRAUD_REJECTED = "CUSTOMER_FRAUD_REJECTED"


@dataclass
class QualityInspectionChecklist:
    serial_number_matched: bool
    brand_packaging_intact: bool
    all_accessories_included: bool
    no_physical_customer_damage: bool
    power_on_test_passed: bool
    factory_reset_completed: bool
    inspector_notes: Optional[str] = None


@dataclass
class ReturnInspectionResult:
    return_id: str
    order_number: str
    is_approved: bool
    disposition: ReturnDisposition
    refund_eligible_amount: Decimal
    restocking_fee: Decimal
    qc_failure_reasons: List[str]
    inspector_badge_id: str
    inspected_at: datetime


class ReverseLogisticsEngine:
    @staticmethod
    def evaluate_qc_inspection(
        return_id: str,
        order_number: str,
        original_price: Decimal,
        qc: QualityInspectionChecklist,
        inspector_badge_id: str = "INSP-BLR-042",
    ) -> ReturnInspectionResult:
        """Evaluate doorstep or hub quality inspection checklist."""
        failures = []

        if not qc.serial_number_matched:
            failures.append("Serial / IMEI number on device does not match outbound order record")

        if not qc.no_physical_customer_damage:
            failures.append("Physical casing crack, deep scratch, or liquid immersion damage detected")

        if not qc.all_accessories_included:
            failures.append("Missing primary power adapter or standard package accessories")

        if not qc.brand_packaging_intact:
            failures.append("Original brand retail box missing or mutilated")

        if not qc.power_on_test_passed:
            failures.append("Device failed basic electrical power-on test")

        is_approved = len(failures) == 0
        now = datetime.now(timezone.utc)

        if is_approved:
            disposition = ReturnDisposition.RESTOCK_AS_NEW
            refund_amount = original_price
            restock_fee = Decimal("0.00")
        elif not qc.serial_number_matched:
            disposition = ReturnDisposition.CUSTOMER_FRAUD_REJECTED
            refund_amount = Decimal("0.00")
            restock_fee = Decimal("0.00")
        elif not qc.all_accessories_included or not qc.brand_packaging_intact:
            # Minor defect: accept with 10% restock fee for Grade-B Refurb
            disposition = ReturnDisposition.GRADE_B_REFURBISHED
            restock_fee = (original_price * Decimal("0.10")).quantize(Decimal("0.01"))
            refund_amount = original_price - restock_fee
            is_approved = True
        else:
            disposition = ReturnDisposition.LIQUIDATION_SCRAP
            refund_amount = Decimal("0.00")
            restock_fee = Decimal("0.00")

        return ReturnInspectionResult(
            return_id=return_id,
            order_number=order_number,
            is_approved=is_approved,
            disposition=disposition,
            refund_eligible_amount=refund_amount,
            restocking_fee=restock_fee,
            qc_failure_reasons=failures,
            inspector_badge_id=inspector_badge_id,
            inspected_at=now,
        )
