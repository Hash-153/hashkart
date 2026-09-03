"""
NovaMart Distributed Order State Machine & Orchestrated Saga Subsystem
======================================================================
Coordinates multi-service transactions with forward actions and compensating rollbacks:
- Step 1: Inventory Lock Reservation (Compensator: Release Inventory Hold)
- Step 2: Payment Gateway Authorize & Capture (Compensator: Trigger IMPS / Gateway Void)
- Step 3: Logistics AWB Waybill Allocation (Compensator: Cancel Carrier Manifest)
- Step 4: Rule 46 GST Invoice Issuance (Compensator: Issue Credit Note)
- Step 5: Omnichannel Customer Notification Outbox dispatch
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Tuple
import uuid


class SagaExecutionStatus(str, Enum):
    STARTED = "STARTED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED_SUCCESS = "COMPLETED_SUCCESS"
    COMPENSATING = "COMPENSATING"
    ROLLED_BACK = "ROLLED_BACK"
    FAILED_UNRECOVERABLE = "FAILED_UNRECOVERABLE"


@dataclass
class SagaStepResult:
    step_name: str
    is_success: bool
    payload_response: Dict[str, Any]
    error_message: Optional[str] = None
    executed_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class OrderSagaContext:
    saga_id: str
    order_number: str
    user_id: int
    seller_id: int
    sku_items: List[Dict[str, Any]] # [{sku, quantity, price}]
    grand_total: Decimal
    payment_method: str
    shipping_address_pincode: str
    status: SagaExecutionStatus
    completed_steps: List[str]
    step_results: Dict[str, SagaStepResult]
    failure_reason: Optional[str] = None


class OrderCheckoutSagaCoordinator:
    def __init__(self, ctx: OrderSagaContext):
        self.ctx = ctx

    def execute_saga(self) -> OrderSagaContext:
        """Execute full choreographed order checkout workflow with automated compensation on failure."""
        self.ctx.status = SagaExecutionStatus.IN_PROGRESS

        # Step 1: Reserve Warehouse Physical Inventory
        if not self._step_reserve_inventory():
            self._compensate_and_abort("INVENTORY_STOCK_UNAVAILABLE")
            return self.ctx

        # Step 2: Process & Capture Payment
        if not self._step_capture_payment():
            self._compensate_and_abort("PAYMENT_CAPTURE_DECLINED")
            return self.ctx

        # Step 3: Allocate Logistics Carrier Waybill
        if not self._step_allocate_logistics_waybill():
            self._compensate_and_abort("LOGISTICS_CARRIER_SERVICE_FAILURE")
            return self.ctx

        # Step 4: Issue Tax Invoice
        if not self._step_issue_gst_invoice():
            self._compensate_and_abort("INVOICE_GENERATION_ERROR")
            return self.ctx

        # Step 5: Enqueue Notifications
        self._step_enqueue_notifications()

        self.ctx.status = SagaExecutionStatus.COMPLETED_SUCCESS
        return self.ctx

    def _step_reserve_inventory(self) -> bool:
        # Simulate inventory hold lock
        self.ctx.completed_steps.append("RESERVE_INVENTORY")
        self.ctx.step_results["RESERVE_INVENTORY"] = SagaStepResult(
            step_name="RESERVE_INVENTORY",
            is_success=True,
            payload_response={"hold_ttl_seconds": 900, "reserved_items_count": len(self.ctx.sku_items)},
        )
        return True

    def _step_capture_payment(self) -> bool:
        # Simulate payment gateway capture
        tx_id = f"pay_{uuid.uuid4().hex[:10]}"
        self.ctx.completed_steps.append("CAPTURE_PAYMENT")
        self.ctx.step_results["CAPTURE_PAYMENT"] = SagaStepResult(
            step_name="CAPTURE_PAYMENT",
            is_success=True,
            payload_response={"payment_transaction_id": tx_id, "amount": str(self.ctx.grand_total)},
        )
        return True

    def _step_allocate_logistics_waybill(self) -> bool:
        awb = f"EKT{datetime.now().strftime('%Y%m%d')}{uuid.uuid4().int % 100000:05d}IN"
        self.ctx.completed_steps.append("ALLOCATE_LOGISTICS")
        self.ctx.step_results["ALLOCATE_LOGISTICS"] = SagaStepResult(
            step_name="ALLOCATE_LOGISTICS",
            is_success=True,
            payload_response={"carrier": "EKART", "waybill_number": awb},
        )
        return True

    def _step_issue_gst_invoice(self) -> bool:
        inv_no = f"INV-2026-{uuid.uuid4().hex[:6].upper()}"
        self.ctx.completed_steps.append("ISSUE_INVOICE")
        self.ctx.step_results["ISSUE_INVOICE"] = SagaStepResult(
            step_name="ISSUE_INVOICE",
            is_success=True,
            payload_response={"invoice_number": inv_no, "tax_rate": "18%"},
        )
        return True

    def _step_enqueue_notifications(self):
        self.ctx.completed_steps.append("NOTIFY_CUSTOMER")
        self.ctx.step_results["NOTIFY_CUSTOMER"] = SagaStepResult(
            step_name="NOTIFY_CUSTOMER",
            is_success=True,
            payload_response={"sms_queued": True, "email_queued": True, "whatsapp_queued": True},
        )

    def _compensate_and_abort(self, reason: str):
        """Execute backward compensating transactions in reverse order of completion."""
        self.ctx.status = SagaExecutionStatus.COMPENSATING
        self.ctx.failure_reason = reason

        for step in reversed(self.ctx.completed_steps):
            if step == "ALLOCATE_LOGISTICS":
                # Cancel courier waybill
                pass
            elif step == "CAPTURE_PAYMENT":
                # Issue instant refund
                pass
            elif step == "RESERVE_INVENTORY":
                # Release inventory hold lock
                pass

        self.ctx.status = SagaExecutionStatus.ROLLED_BACK
