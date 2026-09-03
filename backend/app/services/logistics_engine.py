import uuid
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import Dict, List, Optional, Tuple
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.logistics import (
    CarrierAccount,
    CarrierProviderType,
    DispatchManifest,
    DispatchManifestStatus,
    ManifestPackageItem,
    NDRActionType,
    NDRTicket,
    PincodeServiceability,
    ServiceabilityZone,
)
from app.models.order_payment import Order, Shipment
from app.schemas.logistics import PincodeServiceabilityResponse


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


# Indian Pincode Prefix Map for fallback geo-resolution
PINCODE_ZONE_MAP: Dict[str, Tuple[str, str, ServiceabilityZone, int]] = {
    "11": ("New Delhi", "Delhi", ServiceabilityZone.METRO, 2),
    "12": ("Gurgaon", "Haryana", ServiceabilityZone.METRO, 2),
    "20": ("Noida", "Uttar Pradesh", ServiceabilityZone.METRO, 2),
    "40": ("Mumbai", "Maharashtra", ServiceabilityZone.METRO, 2),
    "41": ("Pune", "Maharashtra", ServiceabilityZone.METRO, 2),
    "56": ("Bengaluru", "Karnataka", ServiceabilityZone.METRO, 2),
    "60": ("Chennai", "Tamil Nadu", ServiceabilityZone.METRO, 2),
    "50": ("Hyderabad", "Telangana", ServiceabilityZone.METRO, 2),
    "70": ("Kolkata", "West Bengal", ServiceabilityZone.METRO, 2),
    "38": ("Ahmedabad", "Gujarat", ServiceabilityZone.METRO, 2),
    "30": ("Jaipur", "Rajasthan", ServiceabilityZone.REGIONAL, 3),
    "68": ("Kochi", "Kerala", ServiceabilityZone.REGIONAL, 3),
    "75": ("Bhubaneswar", "Odisha", ServiceabilityZone.REGIONAL, 3),
    "80": ("Patna", "Bihar", ServiceabilityZone.REST_OF_INDIA, 4),
    "78": ("Guwahati", "Assam", ServiceabilityZone.SPECIAL_ZONE, 5),
    "19": ("Srinagar", "Jammu and Kashmir", ServiceabilityZone.SPECIAL_ZONE, 6),
}


async def check_pincode_serviceability(
    db: AsyncSession,
    pincode: str,
    cart_total: Optional[Decimal] = None,
    weight_kg: Decimal = Decimal("0.5"),
) -> PincodeServiceabilityResponse:
    """Evaluate destination delivery SLA, COD eligibility, and shipping charge."""
    stmt = select(PincodeServiceability).where(
        PincodeServiceability.pincode == pincode,
        PincodeServiceability.is_active == True,
    )
    res = await db.execute(stmt)
    pin_record = res.scalar_one_or_none()

    if pin_record:
        city = pin_record.city
        state = pin_record.state
        district = pin_record.district
        zone = pin_record.zone
        is_cod = pin_record.is_cod_available
        is_prepaid = pin_record.is_prepaid_available
        std_sla = pin_record.standard_sla_days
        exp_sla = pin_record.express_sla_days
        carrier = pin_record.primary_carrier
    else:
        # Fallback to 2-digit prefix geo-zone estimation
        prefix = pincode[:2]
        if prefix in PINCODE_ZONE_MAP:
            city, state, zone, std_sla = PINCODE_ZONE_MAP[prefix]
        else:
            city, state, zone, std_sla = ("India", "India", ServiceabilityZone.REST_OF_INDIA, 4)
        
        district = city
        is_cod = True
        is_prepaid = True
        exp_sla = max(1, std_sla - 1)
        carrier = CarrierProviderType.EKART

    # Calculate Flipkart-style shipping charge (Free above ₹500)
    shipping_charge = Decimal("0.00")
    if cart_total is not None and cart_total < Decimal("500.00"):
        if zone == ServiceabilityZone.LOCAL:
            shipping_charge = Decimal("30.00")
        elif zone in (ServiceabilityZone.METRO, ServiceabilityZone.REGIONAL):
            shipping_charge = Decimal("40.00")
        else:
            shipping_charge = Decimal("60.00")

    now = datetime.now()
    std_date = (now + timedelta(days=std_sla)).strftime("%A, %d %b")
    exp_date = (now + timedelta(days=exp_sla)).strftime("%A, %d %b")

    return PincodeServiceabilityResponse(
        pincode=pincode,
        city=city,
        state=state,
        district=district,
        zone=zone,
        is_serviceable=True,
        is_cod_available=is_cod,
        is_prepaid_available=is_prepaid,
        is_return_pickup_available=True,
        standard_sla_days=std_sla,
        express_sla_days=exp_sla,
        estimated_delivery_date=std_date,
        express_delivery_date=exp_date,
        shipping_charge=shipping_charge,
        primary_carrier=carrier,
    )


async def create_dispatch_manifest(
    db: AsyncSession,
    warehouse_id: int,
    carrier_code: CarrierProviderType,
    shipment_ids: List[int],
    driver_name: Optional[str] = None,
    driver_phone: Optional[str] = None,
    vehicle_number: Optional[str] = None,
    user_id: Optional[int] = None,
) -> DispatchManifest:
    """Generate official daily carrier handover manifest with barcoded package items."""
    manifest_no = f"MNF-{carrier_code.value[:3]}-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
    manifest = DispatchManifest(
        manifest_number=manifest_no,
        warehouse_id=warehouse_id,
        carrier_code=carrier_code,
        status=DispatchManifestStatus.READY_FOR_PICKUP,
        driver_name=driver_name,
        driver_phone=driver_phone,
        vehicle_number=vehicle_number,
        created_by_user_id=user_id,
        scheduled_pickup_time=utcnow() + timedelta(hours=2),
    )
    db.add(manifest)
    await db.flush()

    total_weight = Decimal("0.00")
    total_packages = 0

    if shipment_ids:
        stmt = (
            select(Shipment)
            .options(selectinload(Shipment.order))
            .where(Shipment.id.in_(shipment_ids))
        )
        res = await db.execute(stmt)
        shipments = res.scalars().all()

        for s in shipments:
            weight = Decimal("0.50")
            pkg = ManifestPackageItem(
                manifest_id=manifest.id,
                shipment_id=s.id,
                tracking_number=s.tracking_number or f"TRK-{s.id}",
                order_number=s.order.order_number if s.order else f"ORD-{s.order_id}",
                destination_pincode="560001",
                weight_kg=weight,
                is_scanned=True,
                scanned_at=utcnow(),
            )
            db.add(pkg)
            total_packages += 1
            total_weight += weight

    manifest.total_packages = total_packages
    manifest.total_weight_kg = total_weight
    await db.flush()
    return manifest


async def handle_ndr_delivery_attempt(
    db: AsyncSession,
    shipment_id: int,
    carrier_failure_reason: str,
    carrier_remark: Optional[str] = None,
) -> NDRTicket:
    """Create or increment Non-Delivery Report (NDR) ticket for automated customer resolution."""
    stmt = select(NDRTicket).where(
        NDRTicket.shipment_id == shipment_id,
        NDRTicket.resolution_status == "OPEN",
    )
    res = await db.execute(stmt)
    ndr = res.scalar_one_or_none()

    if ndr:
        ndr.attempt_count += 1
        ndr.carrier_failure_reason = carrier_failure_reason
        ndr.carrier_remark = carrier_remark
    else:
        shipment_stmt = select(Shipment).where(Shipment.id == shipment_id)
        s_res = await db.execute(shipment_stmt)
        shipment = s_res.scalar_one_or_none()
        order_id = shipment.order_id if shipment else 0
        tracking_no = shipment.tracking_number if shipment else f"TRK-{shipment_id}"

        ndr = NDRTicket(
            shipment_id=shipment_id,
            tracking_number=tracking_no,
            order_id=order_id,
            attempt_count=1,
            carrier_failure_reason=carrier_failure_reason,
            carrier_remark=carrier_remark,
            resolution_status="OPEN",
        )
        db.add(ndr)

    await db.flush()
    return ndr


async def resolve_ndr_ticket(
    db: AsyncSession,
    ndr_id: int,
    action: NDRActionType,
    rescheduled_date: Optional[datetime] = None,
    updated_address: Optional[str] = None,
) -> bool:
    """Record customer preference for NDR re-attempt or Return-To-Origin (RTO)."""
    stmt = select(NDRTicket).where(NDRTicket.id == ndr_id)
    res = await db.execute(stmt)
    ndr = res.scalar_one_or_none()

    if not ndr:
        return False

    ndr.customer_action = action
    ndr.rescheduled_delivery_date = rescheduled_date
    ndr.updated_address_line = updated_address
    ndr.resolution_status = "RESOLVED"
    ndr.resolved_at = utcnow()

    await db.flush()
    return True
