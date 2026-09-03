from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user, get_db, require_role
from app.models.risk_fraud import BlacklistRegistry, OrderRiskScore, UserSecurityMetric
from app.models.user import User
from app.schemas.risk_fraud import (
    BlacklistEntryCreate,
    BlacklistEntryResponse,
    RiskAssessmentRequest,
    RiskAssessmentResponse,
    UserSecurityMetricResponse,
)
from app.services.risk_engine import evaluate_order_risk

router = APIRouter()


@router.post("/evaluate", response_model=RiskAssessmentResponse)
async def assess_order_risk(
    payload: RiskAssessmentRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Internal/Checkout API to evaluate order fraud risk and enforce payment method gating."""
    assessment = await evaluate_order_risk(db, payload)
    await db.commit()
    return assessment


@router.get("/blacklist", response_model=List[BlacklistEntryResponse])
async def list_blacklist_entries(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "SECURITY", "FRAUD_ANALYST"])),
):
    """List actively blacklisted addresses, phone numbers, IPs, and fraudulent devices."""
    stmt = select(BlacklistRegistry).where(BlacklistRegistry.is_active == True).order_by(BlacklistRegistry.created_at.desc())
    res = await db.execute(stmt)
    return res.scalars().all()


@router.post("/blacklist", response_model=BlacklistEntryResponse)
async def add_blacklist_entry(
    payload: BlacklistEntryCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "SECURITY", "FRAUD_ANALYST"])),
):
    """Add a phone number, email, IP, or pincode to the global marketplace blacklist."""
    entry = BlacklistRegistry(
        entity_type=payload.entity_type.upper(),
        entity_value=payload.entity_value.strip(),
        reason=payload.reason,
        notes=payload.notes,
        created_by_user_id=current_user.id,
        expires_at=payload.expires_at,
    )
    db.add(entry)
    await db.commit()
    await db.refresh(entry)
    return entry


@router.get("/user/{user_id}/metrics", response_model=UserSecurityMetricResponse)
async def get_user_security_metrics(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "SECURITY", "SUPPORT"])),
):
    """Retrieve historical RTO, return rate, and buyer trust score for customer support investigations."""
    stmt = select(UserSecurityMetric).where(UserSecurityMetric.user_id == user_id)
    res = await db.execute(stmt)
    metric = res.scalar_one_or_none()

    if not metric:
        metric = UserSecurityMetric(
            user_id=user_id,
            total_orders_count=0,
            total_cod_orders_count=0,
            total_rto_orders_count=0,
            total_returns_count=0,
            account_trust_score=85,
            is_trusted_buyer=True,
        )
        db.add(metric)
        await db.commit()
        await db.refresh(metric)

    return metric
