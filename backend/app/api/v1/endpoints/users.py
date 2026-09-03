from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from app.database import get_db
from app.models.user import User, Address
from app.models.system import AuditLog
from app.schemas.user import (
    AddressCreate,
    AddressUpdate,
    AddressResponse,
    SecurityAuditResponse,
)
from app.core.deps import get_current_user

router = APIRouter()


@router.get("/me/addresses", response_model=List[AddressResponse])
async def list_user_addresses(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Fetch saved delivery addresses for current customer."""
    result = await db.execute(
        select(Address)
        .where(Address.user_id == current_user.id)
        .order_by(Address.is_default.desc(), Address.created_at.desc())
    )
    return result.scalars().all()


@router.post("/me/addresses", response_model=AddressResponse, status_code=status.HTTP_201_CREATED)
async def create_user_address(
    address_in: AddressCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Add a new delivery address to customer address book."""
    if address_in.is_default:
        await db.execute(
            update(Address).where(Address.user_id == current_user.id).values(is_default=False)
        )
    if address_in.is_default_shipping:
        await db.execute(
            update(Address).where(Address.user_id == current_user.id).values(is_default_shipping=False)
        )
    if address_in.is_default_billing:
        await db.execute(
            update(Address).where(Address.user_id == current_user.id).values(is_default_billing=False)
        )

    new_address = Address(
        user_id=current_user.id,
        full_name=address_in.full_name,
        phone_number=address_in.phone_number,
        address_line1=address_in.address_line1,
        address_line2=address_in.address_line2,
        locality=address_in.locality,
        city=address_in.city,
        state=address_in.state,
        postal_code=address_in.postal_code,
        country=address_in.country,
        address_type=address_in.address_type,
        is_default=address_in.is_default,
        is_default_shipping=address_in.is_default_shipping,
        is_default_billing=address_in.is_default_billing,
    )
    db.add(new_address)
    await db.commit()
    await db.refresh(new_address)
    return new_address


@router.put("/me/addresses/{address_id}", response_model=AddressResponse)
async def update_user_address(
    address_id: int,
    address_in: AddressUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Update an existing saved address."""
    addr_res = await db.execute(
        select(Address).where(Address.id == address_id, Address.user_id == current_user.id)
    )
    address = addr_res.scalar_one_or_none()
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found.")

    if address_in.is_default:
        await db.execute(
            update(Address).where(Address.user_id == current_user.id).values(is_default=False)
        )
    if address_in.is_default_shipping:
        await db.execute(
            update(Address).where(Address.user_id == current_user.id).values(is_default_shipping=False)
        )
    if address_in.is_default_billing:
        await db.execute(
            update(Address).where(Address.user_id == current_user.id).values(is_default_billing=False)
        )

    for field, val in address_in.model_dump(exclude_unset=True).items():
        setattr(address, field, val)

    await db.commit()
    await db.refresh(address)
    return address


@router.delete("/me/addresses/{address_id}")
async def delete_user_address(
    address_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Delete an address from customer address book."""
    addr_res = await db.execute(
        select(Address).where(Address.id == address_id, Address.user_id == current_user.id)
    )
    address = addr_res.scalar_one_or_none()
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found.")

    await db.delete(address)
    await db.commit()
    return {"message": "Address deleted successfully."}


@router.post("/me/addresses/{address_id}/default-shipping", response_model=AddressResponse)
async def set_default_shipping_address(
    address_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Set specified address as default shipping address."""
    addr_res = await db.execute(
        select(Address).where(Address.id == address_id, Address.user_id == current_user.id)
    )
    address = addr_res.scalar_one_or_none()
    if not address:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Address not found.")

    await db.execute(
        update(Address).where(Address.user_id == current_user.id).values(is_default_shipping=False)
    )
    address.is_default_shipping = True
    await db.commit()
    await db.refresh(address)
    return address


@router.get("/me/security-events", response_model=List[SecurityAuditResponse])
async def get_my_security_events(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Fetch security audit history log for authenticated user."""
    result = await db.execute(
        select(AuditLog)
        .where(AuditLog.user_id == current_user.id)
        .order_by(AuditLog.created_at.desc())
    )
    return result.scalars().all()
