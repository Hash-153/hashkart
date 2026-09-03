from decimal import Decimal
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.deps import get_current_user, get_db, require_role
from app.models.logistics import (
    CarrierAccount,
    CarrierProviderType,
    DispatchManifest,
    NDRActionType,
    NDRTicket,
    PincodeServiceability,
)
from app.models.user import User
from app.schemas.logistics import (
    DispatchManifestCreate,
    DispatchManifestResponse,
    NDRActionRequest,
    NDRTicketResponse,
    PincodeCheckRequest,
    PincodeCreateUpdate,
    PincodeServiceabilityResponse,
)
from app.services.logistics_engine import (
    check_pincode_serviceability,
    create_dispatch_manifest,
    handle_ndr_delivery_attempt,
    resolve_ndr_ticket,
)

router = APIRouter()


@router.post("/pincode/check", response_model=PincodeServiceabilityResponse)
async def check_delivery_pincode(
    payload: PincodeCheckRequest,
    db: AsyncSession = Depends(get_db),
):
    """Public customer endpoint to check delivery SLA, COD eligibility, and shipping cost for any 6-digit Indian pincode."""
    return await check_pincode_serviceability(
        db,
        pincode=payload.pincode,
        cart_total=payload.cart_total,
        weight_kg=payload.weight_kg or Decimal("0.5"),
    )


@router.post("/manifests/create", response_model=DispatchManifestResponse)
async def generate_carrier_manifest(
    payload: DispatchManifestCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "STAFF", "WAREHOUSE"])),
):
    """Warehouse operations endpoint to generate a daily carrier dispatch manifest."""
    manifest = await create_dispatch_manifest(
        db,
        warehouse_id=payload.warehouse_id,
        carrier_code=payload.carrier_code,
        shipment_ids=payload.shipment_ids,
        driver_name=payload.driver_name,
        driver_phone=payload.driver_phone,
        vehicle_number=payload.vehicle_number,
        user_id=current_user.id,
    )
    await db.commit()

    stmt = (
        select(DispatchManifest)
        .options(selectinload(DispatchManifest.packages))
        .where(DispatchManifest.id == manifest.id)
    )
    res = await db.execute(stmt)
    return res.scalar_one()


@router.get("/manifests", response_model=List[DispatchManifestResponse])
async def list_dispatch_manifests(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "STAFF", "WAREHOUSE"])),
):
    """List recent dispatch manifests for warehouse tracking."""
    stmt = (
        select(DispatchManifest)
        .options(selectinload(DispatchManifest.packages))
        .order_by(DispatchManifest.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    res = await db.execute(stmt)
    return res.scalars().all()


@router.get("/ndr/tickets", response_model=List[NDRTicketResponse])
async def list_open_ndr_tickets(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "STAFF", "SUPPORT"])),
):
    """List open non-delivery report (NDR) tickets awaiting customer action or re-attempt."""
    stmt = select(NDRTicket).where(NDRTicket.resolution_status == "OPEN").order_by(NDRTicket.created_at.desc())
    res = await db.execute(stmt)
    return res.scalars().all()


@router.post("/ndr/tickets/{ticket_id}/action", response_model=NDRTicketResponse)
async def act_on_ndr_ticket(
    ticket_id: int,
    payload: NDRActionRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Customer or support staff action on a failed delivery attempt."""
    success = await resolve_ndr_ticket(
        db,
        ndr_id=ticket_id,
        action=payload.action,
        rescheduled_date=payload.rescheduled_delivery_date,
        updated_address=payload.updated_address_line,
    )
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="NDR ticket not found",
        )
    await db.commit()

    stmt = select(NDRTicket).where(NDRTicket.id == ticket_id)
    res = await db.execute(stmt)
    return res.scalar_one()
