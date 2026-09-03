import pytest
from decimal import Decimal
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.logistics import (
    CarrierProviderType,
    NDRActionType,
    PincodeServiceability,
    ServiceabilityZone,
)
from app.services.logistics_engine import (
    check_pincode_serviceability,
    handle_ndr_delivery_attempt,
    resolve_ndr_ticket,
)


@pytest.mark.asyncio
async def test_pincode_serviceability_check(db_session: AsyncSession):
    """Test pincode SLA, COD availability and shipping calculations."""
    # Seed a metro pincode (Bengaluru 560001)
    pin = PincodeServiceability(
        pincode="560001",
        city="Bengaluru",
        state="Karnataka",
        zone=ServiceabilityZone.METRO,
        is_cod_available=True,
        is_prepaid_available=True,
        is_return_pickup_available=True,
        standard_sla_days=2,
        express_sla_days=1,
        primary_carrier=CarrierProviderType.EKART,
    )
    db_session.add(pin)
    await db_session.flush()

    res = await check_pincode_serviceability(db_session, "560001", cart_total=Decimal("899.00"))
    assert res.city == "Bengaluru"
    assert res.is_serviceable is True
    assert res.is_cod_available is True
    assert res.standard_sla_days == 2
    assert res.shipping_charge == Decimal("0.00")  # Free above ₹500

    # Low value order shipping fee test
    res_low = await check_pincode_serviceability(db_session, "560001", cart_total=Decimal("299.00"))
    assert res_low.shipping_charge == Decimal("40.00")


@pytest.mark.asyncio
async def test_ndr_workflow(db_session: AsyncSession):
    """Test Non-Delivery Report creation and customer resolution."""
    ndr = await handle_ndr_delivery_attempt(
        db_session,
        shipment_id=101,
        carrier_failure_reason="Customer unavailable at address",
        carrier_remark="Door bell unanswered at 3 PM",
    )
    assert ndr.shipment_id == 101
    assert ndr.attempt_count == 1
    assert ndr.resolution_status == "OPEN"

    # Customer reschedules delivery
    resolved = await resolve_ndr_ticket(
        db_session,
        ndr_id=ndr.id,
        action=NDRActionType.RE_ATTEMPT,
        updated_address="Flat 402, Green Glen Layout, Bengaluru",
    )
    assert resolved is True
    assert ndr.resolution_status == "RESOLVED"
    assert ndr.customer_action == NDRActionType.RE_ATTEMPT
