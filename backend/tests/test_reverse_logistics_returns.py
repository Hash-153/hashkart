from decimal import Decimal
import pytest

from app.services.returns_engine import (
    QualityInspectionChecklist,
    ReturnDisposition,
    ReverseLogisticsEngine,
)


def test_qc_inspection_approved_restock():
    qc = QualityInspectionChecklist(
        serial_number_matched=True,
        brand_packaging_intact=True,
        all_accessories_included=True,
        no_physical_customer_damage=True,
        power_on_test_passed=True,
        factory_reset_completed=True,
    )

    res = ReverseLogisticsEngine.evaluate_qc_inspection(
        return_id="RET-001",
        order_number="HK-001",
        original_price=Decimal("15000.00"),
        qc=qc,
    )

    assert res.is_approved is True
    assert res.disposition == ReturnDisposition.RESTOCK_AS_NEW
    assert res.refund_eligible_amount == Decimal("15000.00")
    assert res.restocking_fee == Decimal("0.00")


def test_qc_inspection_serial_mismatch_fraud():
    qc = QualityInspectionChecklist(
        serial_number_matched=False, # Swapped device fraud
        brand_packaging_intact=True,
        all_accessories_included=True,
        no_physical_customer_damage=True,
        power_on_test_passed=True,
        factory_reset_completed=True,
    )

    res = ReverseLogisticsEngine.evaluate_qc_inspection(
        return_id="RET-002",
        order_number="HK-002",
        original_price=Decimal("65000.00"),
        qc=qc,
    )

    assert res.is_approved is False
    assert res.disposition == ReturnDisposition.CUSTOMER_FRAUD_REJECTED
    assert res.refund_eligible_amount == Decimal("0.00")
    assert len(res.qc_failure_reasons) >= 1
