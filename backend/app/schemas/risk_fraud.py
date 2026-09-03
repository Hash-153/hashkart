from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict

from app.models.risk_fraud import FraudFlagType, RiskLevel


class RiskAssessmentRequest(BaseModel):
    order_id: int
    user_id: int
    cart_total: Decimal
    payment_method: str  # COD, UPI, CARD, NETBANKING
    delivery_pincode: str
    ip_address: Optional[str] = None
    device_fingerprint: Optional[str] = None
    customer_phone: Optional[str] = None
    customer_email: Optional[str] = None


class RiskAssessmentResponse(BaseModel):
    order_id: int
    user_id: int
    risk_score: int  # 0 to 100 (0=safe, 100=highest risk)
    risk_level: RiskLevel
    decision_action: str  # APPROVED, FLAGGED, BLOCKED
    is_cod_allowed: bool
    requires_otp_verification: bool
    risk_factors: List[str] = []
    recommendation: str
    evaluated_at: datetime


class BlacklistEntryCreate(BaseModel):
    entity_type: str  # PHONE, EMAIL, IP_ADDRESS, DEVICE_ID, PINCODE
    entity_value: str
    reason: FraudFlagType
    notes: Optional[str] = None
    expires_at: Optional[datetime] = None


class BlacklistEntryResponse(BaseModel):
    id: int
    entity_type: str
    entity_value: str
    reason: FraudFlagType
    notes: Optional[str]
    is_active: bool
    created_at: datetime
    expires_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)


class UserSecurityMetricResponse(BaseModel):
    user_id: int
    total_orders_count: int
    total_cod_orders_count: int
    total_rto_orders_count: int
    total_returns_count: int
    total_refund_amount: Decimal
    account_trust_score: int
    is_trusted_buyer: bool
    last_evaluated_at: datetime
    model_config = ConfigDict(from_attributes=True)
