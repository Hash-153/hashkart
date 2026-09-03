from decimal import Decimal
import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.risk_fraud import BlacklistRegistry, FraudFlagType, RiskLevel
from app.schemas.risk_fraud import RiskAssessmentRequest
from app.services.risk_engine import evaluate_order_risk


@pytest.mark.asyncio
async def test_fraud_risk_evaluation(db_session: AsyncSession):
    """Test risk evaluation for safe prepaid order vs blacklisted high-value COD order."""
    # 1. Normal safe order
    safe_req = RiskAssessmentRequest(
        order_id=501,
        user_id=1,
        cart_total=Decimal("1299.00"),
        payment_method="UPI",
        delivery_pincode="560001",
        ip_address="192.168.1.1",
    )
    safe_eval = await evaluate_order_risk(db_session, safe_req)
    assert safe_eval.risk_level in (RiskLevel.LOW, RiskLevel.MEDIUM)
    assert safe_eval.decision_action == "APPROVED"
    assert safe_eval.is_cod_allowed is True

    # 2. Blacklist phone number
    bl = BlacklistRegistry(
        entity_type="PHONE",
        entity_value="9999999999",
        reason=FraudFlagType.PROMO_ABUSE,
    )
    db_session.add(bl)
    await db_session.flush()

    fraud_req = RiskAssessmentRequest(
        order_id=502,
        user_id=2,
        cart_total=Decimal("15000.00"),
        payment_method="COD",
        delivery_pincode="110001",
        customer_phone="9999999999",
    )
    fraud_eval = await evaluate_order_risk(db_session, fraud_req)
    assert fraud_eval.risk_level == RiskLevel.CRITICAL_BLOCK
    assert fraud_eval.decision_action == "BLOCKED"
    assert fraud_eval.is_cod_allowed is False
