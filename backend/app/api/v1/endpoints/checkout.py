import uuid
from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Header, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.cart_wishlist import Cart
from app.models.user import User, Address
from app.models.promotion_review import Coupon, CouponUsage
from app.models.order_payment import Order
from app.schemas.order_payment import (
    CheckoutProcessRequest,
    OrderResponse,
)
from app.schemas.promotion_review import CouponValidateResponse, CouponResponse
from app.schemas.user import AddressCreate, AddressResponse
from app.schemas.checkout_enhanced import CheckoutPreviewResponse
from app.services.checkout_service import CheckoutService
from app.core.deps import get_current_user

router = APIRouter()


@router.get("/addresses", response_model=List[AddressResponse])
async def get_user_addresses(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Fetch saved delivery addresses for authenticated customer."""
    result = await db.execute(
        select(Address).where(Address.user_id == current_user.id).order_by(Address.is_default.desc())
    )
    return result.scalars().all()


@router.post("/addresses", response_model=AddressResponse, status_code=status.HTTP_201_CREATED)
async def create_user_address(
    address_in: AddressCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Add a new delivery address."""
    if address_in.is_default:
        existing = await db.execute(select(Address).where(Address.user_id == current_user.id))
        for addr in existing.scalars().all():
            addr.is_default = False

    new_address = Address(
        user_id=current_user.id,
        full_name=address_in.full_name,
        phone_number=address_in.phone_number,
        address_line1=address_in.address_line1,
        address_line2=address_in.address_line2,
        city=address_in.city,
        state=address_in.state,
        postal_code=address_in.postal_code,
        country=address_in.country,
        address_type=address_in.address_type,
        is_default=address_in.is_default,
    )
    db.add(new_address)
    await db.commit()
    await db.refresh(new_address)
    return new_address


@router.post("/coupons/validate", response_model=CouponValidateResponse)
async def validate_coupon(
    code: str,
    subtotal: float,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Validate promo coupon code and calculate discount amount."""
    code_upper = code.strip().upper()
    result = await db.execute(select(Coupon).where(Coupon.code == code_upper, Coupon.is_active == True))
    coupon = result.scalar_one_or_none()

    if not coupon:
        return CouponValidateResponse(is_valid=False, message="Invalid coupon code.")

    now = datetime.utcnow()
    if coupon.valid_from > now or coupon.valid_to < now:
        return CouponValidateResponse(is_valid=False, message="Coupon has expired.")

    if subtotal < coupon.min_order_value:
        return CouponValidateResponse(
            is_valid=False,
            message=f"Minimum cart value of ₹{coupon.min_order_value} required for this coupon.",
        )

    if coupon.usage_limit is not None and coupon.times_used >= coupon.usage_limit:
        return CouponValidateResponse(is_valid=False, message="Coupon usage limit reached.")

    usage_res = await db.execute(
        select(CouponUsage).where(CouponUsage.coupon_id == coupon.id, CouponUsage.user_id == current_user.id)
    )
    user_usage_count = len(usage_res.scalars().all())
    if user_usage_count >= coupon.usage_per_user:
        return CouponValidateResponse(is_valid=False, message="You have already redeemed this coupon.")

    if coupon.discount_type == "PERCENTAGE":
        discount = round((subtotal * coupon.discount_value) / 100.0, 2)
        if coupon.max_discount_amount and discount > coupon.max_discount_amount:
            discount = float(coupon.max_discount_amount)
    else:
        discount = float(coupon.discount_value)

    discount = min(discount, subtotal)

    return CouponValidateResponse(
        is_valid=True,
        message="Coupon applied successfully!",
        discount_amount=round(discount, 2),
        coupon=CouponResponse.model_validate(coupon),
    )


@router.post("/preview", response_model=CheckoutPreviewResponse)
async def preview_checkout(
    address_id: int,
    coupon_code: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Generate checkout preview calculation without placing an order or reserving stock."""
    try:
        return await CheckoutService.get_checkout_preview(
            db=db, user=current_user, address_id=address_id, coupon_code=coupon_code
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/process", response_model=OrderResponse)
async def process_checkout(
    checkout_in: CheckoutProcessRequest,
    x_idempotency_key: Optional[str] = Header(None),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Execute Order Placement & Payment Simulation Pipeline.
    Supports idempotency key deduplication, pessimistic inventory row locking, and mock payment gateway scenarios.
    """
    try:
        mock_scenario = "SUCCESS"
        if checkout_in.mock_payment_details and checkout_in.mock_payment_details.get("simulate_failure"):
            mock_scenario = "FAILURE"

        order, cached = await CheckoutService.place_order_with_idempotency(
            db=db,
            user=current_user,
            address_id=checkout_in.address_id,
            payment_method=checkout_in.payment_method,
            idempotency_key=x_idempotency_key,
            coupon_code=checkout_in.coupon_code,
            mock_scenario=mock_scenario,
        )
        return order
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
