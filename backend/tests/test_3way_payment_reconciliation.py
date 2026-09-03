from datetime import datetime, timezone
from decimal import Decimal
import pytest

from app.services.reconciliation_engine import (
    GatewaySettlementRow,
    InternalPaymentRecord,
    PaymentReconciliationEngine,
)


def test_payment_reconciliation_exact_and_discrepancies():
    now = datetime.now(timezone.utc)

    # 1. Exact match record
    r1 = InternalPaymentRecord(order_number="HK-001", gateway_transaction_id="pay_1", captured_amount=Decimal("1500.00"), status="CAPTURED", created_at=now)
    g1 = GatewaySettlementRow(gateway_transaction_id="pay_1", settlement_utr="UTR001", gross_amount=Decimal("1500.00"), gateway_fee=Decimal("30.00"), gateway_gst=Decimal("5.40"), net_settled_amount=Decimal("1464.60"), settlement_date=now)

    # 2. Missing in gateway record
    r2 = InternalPaymentRecord(order_number="HK-002", gateway_transaction_id="pay_2", captured_amount=Decimal("2500.00"), status="CAPTURED", created_at=now)

    # 3. Missing in internal DB record
    g3 = GatewaySettlementRow(gateway_transaction_id="pay_3", settlement_utr="UTR003", gross_amount=Decimal("999.00"), gateway_fee=Decimal("20.00"), gateway_gst=Decimal("3.60"), net_settled_amount=Decimal("975.40"), settlement_date=now)

    # 4. Amount mismatch record
    r4 = InternalPaymentRecord(order_number="HK-004", gateway_transaction_id="pay_4", captured_amount=Decimal("5000.00"), status="CAPTURED", created_at=now)
    g4 = GatewaySettlementRow(gateway_transaction_id="pay_4", settlement_utr="UTR004", gross_amount=Decimal("4500.00"), gateway_fee=Decimal("90.00"), gateway_gst=Decimal("16.20"), net_settled_amount=Decimal("4393.80"), settlement_date=now)

    report = PaymentReconciliationEngine.execute_reconciliation(
        internal_records=[r1, r2, r4],
        gateway_settlement=[g1, g3, g4],
    )

    assert report.total_internal_records == 3
    assert report.total_gateway_records == 3
    assert report.matched_records_count == 1 # pay_1
    assert report.discrepant_records_count == 3 # pay_2, pay_3, pay_4
    assert len(report.discrepancies) == 3
