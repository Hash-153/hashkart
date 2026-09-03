from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Header, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.cart_wishlist import Cart, CartItem, Wishlist, WishlistItem
from app.models.catalog import ProductVariant
from app.models.user import User
from app.schemas.cart_wishlist import (
    CartItemCreate,
    CartItemUpdate,
    CartResponse,
)
from app.services.pricing_service import PricingService
from app.services.inventory_service import InventoryService
from app.core.deps import get_current_user_optional, get_current_user

router = APIRouter()


async def get_or_create_cart(
    db: AsyncSession, user: Optional[User], session_id: Optional[str] = None
) -> Cart:
    """Retrieve or create active cart for authenticated user or guest session."""
    cart = None
    if user:
        result = await db.execute(
            select(Cart).options(selectinload(Cart.items).selectinload(CartItem.variant)).where(Cart.user_id == user.id)
        )
        cart = result.scalar_one_or_none()
        if not cart:
            cart = Cart(user_id=user.id, items=[])
            db.add(cart)
            await db.flush()
    elif session_id:
        result = await db.execute(
            select(Cart).options(selectinload(Cart.items).selectinload(CartItem.variant)).where(Cart.session_id == session_id)
        )
        cart = result.scalar_one_or_none()
        if not cart:
            cart = Cart(session_id=session_id, items=[])
            db.add(cart)
            await db.flush()
    else:
        cart = Cart(items=[])
        db.add(cart)
        await db.flush()
    return cart


async def build_cart_response(db: AsyncSession, cart: Cart) -> CartResponse:
    """Calculate authoritative real-time cart subtotal, tax, shipping, and price warnings using Decimal engine."""
    line_items_data = []
    items_response = []
    price_warnings = []
    stock_warnings = []
    item_count = 0

    for item in cart.items:
        variant = item.variant
        if not variant or not variant.is_active:
            stock_warnings.append(f"Variant SKU '{item.variant_id}' is no longer active.")
            continue

        # Check stock availability
        avail_stock = await InventoryService.get_available_stock(db, variant.id)
        if avail_stock < item.quantity:
            stock_warnings.append(f"Only {avail_stock} units available for '{variant.title}'.")

        unit_p = PricingService.to_decimal(variant.discount_price if variant.discount_price else variant.price)
        line_items_data.append({"price": float(unit_p), "quantity": item.quantity})
        item_count += item.quantity
        items_response.append(item)

    totals = PricingService.calculate_order_totals(line_items_data)

    return CartResponse(
        id=cart.id,
        user_id=cart.user_id,
        session_id=cart.session_id,
        items=items_response,
        subtotal=totals["subtotal"],
        estimated_tax=totals["tax_amount"],
        estimated_shipping=totals["shipping_fee"],
        discount_amount=totals["discount_amount"],
        grand_total=totals["grand_total"],
        item_count=item_count,
        price_change_warnings=price_warnings,
        stock_warnings=stock_warnings,
    )


@router.get("", response_model=CartResponse)
async def get_cart(
    x_session_id: Optional[str] = Header(None),
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db),
):
    """Retrieve active cart and real-time total calculations."""
    cart = await get_or_create_cart(db, current_user, x_session_id)
    return await build_cart_response(db, cart)


@router.post("/items", response_model=CartResponse)
async def add_item_to_cart(
    item_in: CartItemCreate,
    x_session_id: Optional[str] = Header(None),
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db),
):
    """Add a product variant to active cart after validating available inventory."""
    var_res = await db.execute(select(ProductVariant).where(ProductVariant.id == item_in.variant_id))
    variant = var_res.scalar_one_or_none()

    if not variant or not variant.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product variant is unavailable.",
        )

    avail_stock = await InventoryService.get_available_stock(db, variant.id)
    if avail_stock < item_in.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Only {avail_stock} items available in stock.",
        )

    cart = await get_or_create_cart(db, current_user, x_session_id)

    existing_item = next((i for i in cart.items if i.variant_id == item_in.variant_id), None)
    if existing_item:
        new_qty = existing_item.quantity + item_in.quantity
        if avail_stock < new_qty:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Cannot add {item_in.quantity} more. Stock limit of {avail_stock} reached.",
            )
        existing_item.quantity = new_qty
    else:
        new_item = CartItem(cart_id=cart.id, variant_id=item_in.variant_id, quantity=item_in.quantity)
        db.add(new_item)

    await db.commit()
    await db.refresh(cart)
    return await build_cart_response(db, cart)


@router.put("/items/{item_id}", response_model=CartResponse)
async def update_cart_item(
    item_id: int,
    item_in: CartItemUpdate,
    x_session_id: Optional[str] = Header(None),
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db),
):
    """Update item quantity in cart."""
    cart = await get_or_create_cart(db, current_user, x_session_id)
    item = next((i for i in cart.items if i.id == item_id), None)

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart item not found.")

    avail_stock = await InventoryService.get_available_stock(db, item.variant_id)
    if avail_stock < item_in.quantity:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Requested quantity exceeds available stock of {avail_stock}.",
        )

    item.quantity = item_in.quantity
    await db.commit()
    await db.refresh(cart)
    return await build_cart_response(db, cart)


@router.delete("/items/{item_id}", response_model=CartResponse)
async def remove_cart_item(
    item_id: int,
    x_session_id: Optional[str] = Header(None),
    current_user: Optional[User] = Depends(get_current_user_optional),
    db: AsyncSession = Depends(get_db),
):
    """Remove item from cart."""
    cart = await get_or_create_cart(db, current_user, x_session_id)
    item = next((i for i in cart.items if i.id == item_id), None)

    if item:
        await db.delete(item)
        await db.commit()
        await db.refresh(cart)

    return await build_cart_response(db, cart)


@router.post("/items/{item_id}/move-to-wishlist", response_model=CartResponse)
async def move_cart_item_to_wishlist(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Move an item from Cart to authenticated User's Wishlist."""
    cart = await get_or_create_cart(db, current_user)
    item = next((i for i in cart.items if i.id == item_id), None)

    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cart item not found.")

    # Fetch user wishlist
    w_res = await db.execute(
        select(Wishlist).options(selectinload(Wishlist.items)).where(Wishlist.user_id == current_user.id)
    )
    wishlist = w_res.scalar_one_or_none()
    if not wishlist:
        wishlist = Wishlist(user_id=current_user.id, items=[])
        db.add(wishlist)
        await db.flush()

    # Add to wishlist if not present
    existing_witem = next((w for w in wishlist.items if w.variant_id == item.variant_id), None)
    if not existing_witem:
        new_witem = WishlistItem(wishlist_id=wishlist.id, variant_id=item.variant_id)
        db.add(new_witem)

    await db.delete(item)
    await db.commit()
    await db.refresh(cart)
    return await build_cart_response(db, cart)


@router.post("/merge", response_model=CartResponse)
async def merge_guest_cart(
    x_session_id: str = Header(...),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Merge guest cart items into authenticated user cart upon login."""
    guest_res = await db.execute(
        select(Cart).options(selectinload(Cart.items)).where(Cart.session_id == x_session_id)
    )
    guest_cart = guest_res.scalar_one_or_none()

    user_cart = await get_or_create_cart(db, current_user)

    if guest_cart and guest_cart.items:
        for gitem in list(guest_cart.items):
            uitem = next((i for i in user_cart.items if i.variant_id == gitem.variant_id), None)
            if uitem:
                uitem.quantity += gitem.quantity
            else:
                new_item = CartItem(cart_id=user_cart.id, variant_id=gitem.variant_id, quantity=gitem.quantity)
                db.add(new_item)
            await db.delete(gitem)

        await db.delete(guest_cart)
        await db.commit()
        await db.refresh(user_cart)

    return await build_cart_response(db, user_cart)
