from datetime import datetime, timezone
import pytest

from app.services.audit_logger import AuditLogger


def test_audit_trail_entry_creation_and_integrity():
    record = AuditLogger.create_audit_entry(
        actor_user_id=1,
        actor_email="admin@novamart.in",
        actor_role="ADMIN",
        action_type="PAYOUT_APPROVAL",
        resource_type="SELLER_PAYOUT_BATCH",
        resource_id="BATCH-2026-99",
        previous_state={"status": "PENDING_APPROVAL", "amount": 150000},
        new_state={"status": "APPROVED", "amount": 150000},
        ip_address="10.0.12.45",
    )

    assert record.id.startswith("aud_")
    assert record.integrity_hash is not None
    assert AuditLogger.verify_entry_integrity(record) is True

    # Tamper with record state
    record.new_state["amount"] = 9999999
    assert AuditLogger.verify_entry_integrity(record) is False
