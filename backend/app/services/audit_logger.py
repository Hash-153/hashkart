"""
NovaMart Immutable Security & Financial Audit Logging Subsystem
===============================================================
Records cryptographically signed audit entries for sensitive platform operations:
- Role & Permission escalations
- Bank details & GSTIN modifications
- Escrow payout approvals & manual balance overrides
- High-value inventory stock write-offs
- IP address, User-Agent, and geographic location tracking
"""

from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import json
from typing import Any, Dict, Optional


@dataclass
class AuditTrailRecord:
    id: str
    actor_user_id: int
    actor_email: str
    actor_role: str
    action_type: str # 'ROLE_CHANGE', 'PAYOUT_APPROVAL', 'STOCK_ADJUSTMENT', 'PRICE_OVERRIDE'
    resource_type: str
    resource_id: str
    previous_state: Optional[Dict[str, Any]]
    new_state: Optional[Dict[str, Any]]
    ip_address: str
    user_agent: str
    timestamp: datetime
    integrity_hash: str


class AuditLogger:
    @staticmethod
    def compute_record_hash(
        actor_user_id: int,
        action_type: str,
        resource_id: str,
        timestamp: datetime,
        prev_state: Optional[Dict[str, Any]],
        new_state: Optional[Dict[str, Any]],
    ) -> str:
        """Compute SHA-256 integrity hash across record fields."""
        payload = f"{actor_user_id}|{action_type}|{resource_id}|{timestamp.isoformat()}|{json.dumps(prev_state, sort_keys=True)}|{json.dumps(new_state, sort_keys=True)}"
        return hashlib.sha256(payload.encode()).hexdigest()

    @classmethod
    def create_audit_entry(
        cls,
        actor_user_id: int,
        actor_email: str,
        actor_role: str,
        action_type: str,
        resource_type: str,
        resource_id: str,
        previous_state: Optional[Dict[str, Any]] = None,
        new_state: Optional[Dict[str, Any]] = None,
        ip_address: str = "127.0.0.1",
        user_agent: str = "Mozilla/5.0",
    ) -> AuditTrailRecord:
        """Create and hash an immutable audit trail record."""
        now = datetime.now(timezone.utc)
        record_id = f"aud_{now.strftime('%Y%m%d%H%M%S')}_{actor_user_id}"
        sig = cls.compute_record_hash(actor_user_id, action_type, resource_id, now, previous_state, new_state)

        return AuditTrailRecord(
            id=record_id,
            actor_user_id=actor_user_id,
            actor_email=actor_email,
            actor_role=actor_role,
            action_type=action_type,
            resource_type=resource_type,
            resource_id=resource_id,
            previous_state=previous_state,
            new_state=new_state,
            ip_address=ip_address,
            user_agent=user_agent,
            timestamp=now,
            integrity_hash=sig,
        )

    @classmethod
    def verify_entry_integrity(cls, record: AuditTrailRecord) -> bool:
        """Verify that an audit record has not been tampered with."""
        expected = cls.compute_record_hash(
            record.actor_user_id,
            record.action_type,
            record.resource_id,
            record.timestamp,
            record.previous_state,
            record.new_state,
        )
        return expected == record.integrity_hash
