import uuid
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.order_payment import Order, OrderItem
from app.models.catalog import ProductVariant
from app.models.inventory import InventoryTransaction
from app.models.order_refund import OrderRefund
from app.models.user import User
from app.schemas.order_payment import OrderResponse
from app.schemas.checkout_enhanced import OrderRefundRequest, OrderRefundResponse
from app.schemas.fulfillment import ReturnRequestCreate, ReturnRequestResponse
from app.services.fulfillment_service import create_return_request, list_returns
from app.services.checkout_service import CheckoutService
from app.core.deps import get_current_user

router = APIRouter()


@router.get("/returns", response_model=List[ReturnRequestResponse])
async def list_user_returns(
    current_user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):
    return await list_returns(db, current_user.id)


@router.post("/returns", response_model=ReturnRequestResponse, status_code=status.HTTP_201_CREATED)
async def request_return(
    payload: ReturnRequestCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await create_return_request(db, current_user.id, payload)


@router.get("", response_model=List[OrderResponse])
async def list_user_orders(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List order history for authenticated customer."""
    result = await db.execute(
        select(Order)
        .options(
            selectinload(Order.items),
            selectinload(Order.payment),
            selectinload(Order.shipment),
            selectinload(Order.address),
        )
        .where(Order.user_id == current_user.id)
        .order_by(Order.created_at.desc())
    )
    return result.scalars().all()


@router.get("/{order_number}", response_model=OrderResponse)
async def get_order_by_number(
    order_number: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Fetch detailed order status, line items, and tracking info."""
    result = await db.execute(
        select(Order)
        .options(
            selectinload(Order.items),
            selectinload(Order.payment),
            selectinload(Order.shipment),
            selectinload(Order.address),
        )
        .where(Order.order_number == order_number, Order.user_id == current_user.id)
    )
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found.")
    return order


@router.post("/{order_number}/cancel", response_model=OrderResponse)
async def cancel_order(
    order_number: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Cancel order and restore stock if order hasn't shipped."""
    result = await db.execute(
        select(Order).where(Order.order_number == order_number, Order.user_id == current_user.id)
    )
    order_hdr = result.scalar_one_or_none()
    if not order_hdr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found.")

    try:
        await CheckoutService.cancel_order(db=db, order_id=order_hdr.id, user_id=current_user.id)
        res = await db.execute(
            select(Order)
            .options(
                selectinload(Order.items),
                selectinload(Order.payment),
                selectinload(Order.shipment),
                selectinload(Order.address),
            )
            .where(Order.id == order_hdr.id)
        )
        return res.scalar_one()
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/{order_number}/refund", response_model=OrderRefundResponse)
async def request_order_refund(
    order_number: str,
    refund_in: OrderRefundRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Request mock refund for cancelled or eligible order."""
    result = await db.execute(
        select(Order).where(Order.order_number == order_number, Order.user_id == current_user.id)
    )
    order = result.scalar_one_or_none()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found.")

    ref_amount = refund_in.amount if refund_in.amount else float(order.grand_total)

    refund = OrderRefund(
        order_id=order.id,
        refund_reference=f"REF-{uuid.uuid4().hex[:10].upper()}",
        amount=ref_amount,
        reason=refund_in.reason,
        refund_status="COMPLETED",
    )
    order.payment_status = "REFUNDED"
    db.add(refund)
    await db.commit()
    await db.refresh(refund)
    return refund
