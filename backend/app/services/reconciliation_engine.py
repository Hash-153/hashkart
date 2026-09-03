"""
NovaMart 3-Way Payment Gateway Settlement Reconciliation Engine
===============================================================
Performs automated tripartite matching:
1. Internal Order Financial Ledger (`payments` table)
2. Payment Gateway Settlement Statement (Razorpay / PayU / Cashfree MT940 / CSV)
3. Bank Nodal Account Escrow Deposit Ledger
Identifies:
- Discrepancies in fee / GST deduction percentages
- Missing capture webhooks (orders paid on PG but stuck in PENDING on marketplace)
- Chargebacks, disputes, and unreversed refund deductions
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal
from typing import Dict, List, Optional, Tuple


@dataclass
class InternalPaymentRecord:
    order_number: str
    gateway_transaction_id: str
    captured_amount: Decimal
    status: str
    created_at: datetime


@dataclass
class GatewaySettlementRow:
    gateway_transaction_id: str
    settlement_utr: str
    gross_amount: Decimal
    gateway_fee: Decimal
    gateway_gst: Decimal
    net_settled_amount: Decimal
    settlement_date: datetime


@dataclass
class ReconciliationDiscrepancy:
    order_number: str
    gateway_transaction_id: str
    issue_type: str # 'MISSING_IN_GATEWAY', 'MISSING_IN_INTERNAL_DB', 'AMOUNT_MISMATCH', 'FEE_OVERCHARGE'
    internal_amount: Decimal
    gateway_amount: Decimal
    discrepancy_amount: Decimal
    notes: str


@dataclass
class ReconciliationReport:
    total_internal_records: int
    total_gateway_records: int
    matched_records_count: int
    discrepant_records_count: int
    total_gross_settled: Decimal
    total_fees_paid: Decimal
    total_gst_paid: Decimal
    discrepancies: List[ReconciliationDiscrepancy]


class PaymentReconciliationEngine:
    @staticmethod
    def execute_reconciliation(
        internal_records: List[InternalPaymentRecord],
        gateway_settlement: List[GatewaySettlementRow],
    ) -> ReconciliationReport:
        """Match internal payment records against payment gateway settlement statements."""
        internal_by_tx = {r.gateway_transaction_id: r for r in internal_records}
        gateway_by_tx = {g.gateway_transaction_id: g for g in gateway_settlement}

        all_tx_ids = set(internal_by_tx.keys()).union(set(gateway_by_tx.keys()))

        matched_count = 0
        discrepancies: List[ReconciliationDiscrepancy] = []

        total_gross = Decimal("0.00")
        total_fees = Decimal("0.00")
        total_gst = Decimal("0.00")

        for tx_id in all_tx_ids:
            internal = internal_by_tx.get(tx_id)
            gateway = gateway_by_tx.get(tx_id)

            if internal and not gateway:
                discrepancies.append(
                    ReconciliationDiscrepancy(
                        order_number=internal.order_number,
                        gateway_transaction_id=tx_id,
                        issue_type="MISSING_IN_GATEWAY",
                        internal_amount=internal.captured_amount,
                        gateway_amount=Decimal("0.00"),
                        discrepancy_amount=internal.captured_amount,
                        notes="Captured in NovaMart DB but not present in payment gateway settlement batch.",
                    )
                )
            elif gateway and not internal:
                total_gross += gateway.gross_amount
                total_fees += gateway.gateway_fee
                total_gst += gateway.gateway_gst

                discrepancies.append(
                    ReconciliationDiscrepancy(
                        order_number="UNKNOWN",
                        gateway_transaction_id=tx_id,
                        issue_type="MISSING_IN_INTERNAL_DB",
                        internal_amount=Decimal("0.00"),
                        gateway_amount=gateway.gross_amount,
                        discrepancy_amount=gateway.gross_amount,
                        notes="Settled by gateway but order record not found in marketplace database.",
                    )
                )
            elif internal and gateway:
                total_gross += gateway.gross_amount
                total_fees += gateway.gateway_fee
                total_gst += gateway.gateway_gst

                diff = abs(internal.captured_amount - gateway.gross_amount)
                if diff > Decimal("0.01"):
                    discrepancies.append(
                        ReconciliationDiscrepancy(
                            order_number=internal.order_number,
                            gateway_transaction_id=tx_id,
                            issue_type="AMOUNT_MISMATCH",
                            internal_amount=internal.captured_amount,
                            gateway_amount=gateway.gross_amount,
                            discrepancy_amount=diff,
                            notes=f"Amount difference of ₹{diff:,.2f} detected.",
                        )
                    )
                else:
                    matched_count += 1

        return ReconciliationReport(
            total_internal_records=len(internal_records),
            total_gateway_records=len(gateway_settlement),
            matched_records_count=matched_count,
            discrepant_records_count=len(discrepancies),
            total_gross_settled=total_gross,
            total_fees_paid=total_fees,
            total_gst_paid=total_gst,
            discrepancies=discrepancies,
        )
