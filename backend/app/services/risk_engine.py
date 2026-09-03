import json
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import List, Tuple
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order_payment import Order
from app.models.risk_fraud import (
    BlacklistRegistry,
    FraudFlagType,
    OrderRiskScore,
    RiskLevel,
    UserSecurityMetric,
)
from app.schemas.risk_fraud import RiskAssessmentRequest, RiskAssessmentResponse


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


async def evaluate_order_risk(
    db: AsyncSession, req: RiskAssessmentRequest
) -> RiskAssessmentResponse:
    """Multi-factor fraud risk evaluation engine for Indian E-commerce orders."""
    risk_score = 10  # Base nominal score
    risk_factors: List[str] = []
    is_cod_allowed = True
    requires_otp = False

    # 1. Blacklist Registry Check
    bl_stmt = select(BlacklistRegistry).where(
        BlacklistRegistry.is_active == True,
        (
            (BlacklistRegistry.entity_type == "PINCODE") & (BlacklistRegistry.entity_value == req.delivery_pincode)
            | (BlacklistRegistry.entity_type == "PHONE") & (BlacklistRegistry.entity_value == (req.customer_phone or ""))
            | (BlacklistRegistry.entity_type == "EMAIL") & (BlacklistRegistry.entity_value == (req.customer_email or ""))
            | (BlacklistRegistry.entity_type == "IP_ADDRESS") & (BlacklistRegistry.entity_value == (req.ip_address or ""))
        ),
    )
    bl_res = await db.execute(bl_stmt)
    blacklisted_entries = bl_res.scalars().all()

    if blacklisted_entries:
        for b in blacklisted_entries:
            risk_score += 60
            risk_factors.append(f"Blacklist match: {b.entity_type} ({b.reason.value})")

    # 2. COD High-Value Risk Check (COD > ₹5,000 in India is high RTO risk)
    if req.payment_method.upper() == "COD":
        if req.cart_total > Decimal("10000.00"):
            risk_score += 35
            risk_factors.append("High value Cash-on-Delivery order (> ₹10,000)")
            is_cod_allowed = False
        elif req.cart_total > Decimal("3000.00"):
            risk_score += 15
            risk_factors.append("Moderate value COD (> ₹3,000) - OTP verification required")
            requires_otp = True

    # 3. User Order Velocity Check (More than 3 orders in past 1 hour)
    one_hour_ago = utcnow() - timedelta(hours=1)
    velocity_stmt = select(func.count(Order.id)).where(
        Order.user_id == req.user_id,
        Order.created_at >= one_hour_ago,
    )
    vel_res = await db.execute(velocity_stmt)
    recent_order_count = vel_res.scalar() or 0

    if recent_order_count >= 3:
        risk_score += 30
        risk_factors.append(f"Abnormal order velocity ({recent_order_count} orders in last 60 mins)")

    # 4. User Historical Security Metrics
    sec_stmt = select(UserSecurityMetric).where(UserSecurityMetric.user_id == req.user_id)
    sec_res = await db.execute(sec_stmt)
    metric = sec_res.scalar_one_or_none()

    if metric:
        if metric.total_rto_orders_count >= 2:
            risk_score += 25
            risk_factors.append(f"Customer has {metric.total_rto_orders_count} past Return-To-Origin (RTO) incidents")
            is_cod_allowed = False
        if metric.account_trust_score < 40:
            risk_score += 20
            risk_factors.append("Low account trust score")

    # Cap risk score between 0 and 100
    risk_score = min(100, max(0, risk_score))

    if risk_score >= 70:
        risk_level = RiskLevel.CRITICAL_BLOCK
        decision = "BLOCKED"
        is_cod_allowed = False
        recommendation = "Order rejected due to multiple high-confidence fraud risk indicators"
    elif risk_score >= 40:
        risk_level = RiskLevel.HIGH
        decision = "FLAGGED"
        requires_otp = True
        recommendation = "Order flagged for secondary phone verification before warehouse dispatch"
    elif risk_score >= 25:
        risk_level = RiskLevel.MEDIUM
        decision = "APPROVED"
        recommendation = "Low-medium risk, proceed with standard automated dispatch"
    else:
        risk_level = RiskLevel.LOW
        decision = "APPROVED"
        recommendation = "Order passed all automated security checks"

    # Persist Risk Score Audit
    risk_record = OrderRiskScore(
        order_id=req.order_id,
        user_id=req.user_id,
        risk_score=risk_score,
        risk_level=risk_level,
        is_cod_restricted=not is_cod_allowed,
        requires_manual_verification=(decision == "FLAGGED"),
        ip_address=req.ip_address,
        device_fingerprint=req.device_fingerprint,
        risk_factors_json=json.dumps(risk_factors),
        decision_action=decision,
    )
    db.add(risk_record)
    await db.flush()

    return RiskAssessmentResponse(
        order_id=req.order_id,
        user_id=req.user_id,
        risk_score=risk_score,
        risk_level=risk_level,
        decision_action=decision,
        is_cod_allowed=is_cod_allowed,
        requires_otp_verification=requires_otp,
        risk_factors=risk_factors,
        recommendation=recommendation,
        evaluated_at=utcnow(),
    )
