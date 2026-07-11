from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Header, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models.cart_wishlist import Wishlist, WishlistItem, Cart, CartItem
from app.models.catalog import ProductVariant
from app.models.user import User
from app.schemas.cart_wishlist import (
    WishlistResponse,
    WishlistItemCreate,
)
from app.services.inventory_service import InventoryService
from app.core.deps import get_current_user_optional

router = APIRouter()


async def get_or_create_wishlist(
    db: AsyncSession, user: Optional[User] = None, session_id: Optional[str] = None
) -> Wishlist:
    """Helper to fetch or create user or guest session wishlist."""
    wishlist = None
    if user:
        result = await db.execute(select(Wishlist).where(Wishlist.user_id == user.id))
        wishlist = result.scalar_one_or_none()
        if not wishlist:
            if session_id:
                s_res = await db.execute(select(Wishlist).where(Wishlist.session_id == session_id))
                wishlist = s_res.scalar_one_or_none()
                if wishlist:
                    wishlist.user_id = user.id
                    await db.flush()

            if not wishlist:
                wishlist = Wishlist(user_id=user.id)
                db.add(wishlist)
                await db.flush()
    elif session_id:
        result = await db.execute(select(Wishlist).where(Wishlist.session_id == session_id))
        wishlist = result.scalar_one_or_none()
        if not wishlist:
            wishlist = Wishlist(session_id=session_id)
            db.add(wishlist)
            await db.flush()
    else:
        wishlist = Wishlist()
        db.add(wishlist)
        await db.flush()

    return wishlist


async def fetch_wishlist_response(db: AsyncSession, wishlist: Wishlist) -> WishlistResponse:
    """Fetch all items with eager loaded variants and images."""
    stmt = (
        select(WishlistItem)
        .options(
            selectinload(WishlistItem.variant).selectinload(ProductVariant.images),
            selectinload(WishlistItem.variant).selectinload(ProductVariant.product),
        )
        .where(WishlistItem.wishlist_id == wishlist.id)
        .order_by(WishlistItem.added_at.desc())
    )
    res = await db.execute(stmt)
    items = list(res.scalars().all())

    return WishlistResponse(
        id=wishlist.id,
        user_id=wishlist.user_id,
        session_id=wishlist.session_id,
        items=items,
    )


@router.get("", response_model=WishlistResponse)
async def get_wishlist(
    current_user: Optional[User] = Depends(get_current_user_optional),
    session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    db: AsyncSession = Depends(get_db),
):
    """Fetch user or guest wishlist items."""
    wishlist = await get_or_create_wishlist(db, user=current_user, session_id=session_id)
    return await fetch_wishlist_response(db, wishlist)


@router.post("/items", response_model=WishlistResponse)
async def add_to_wishlist(
    item_in: WishlistItemCreate,
    current_user: Optional[User] = Depends(get_current_user_optional),
    session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    db: AsyncSession = Depends(get_db),
):
    """Add item to wishlist for user or guest."""
    var_res = await db.execute(select(ProductVariant).where(ProductVariant.id == item_in.variant_id))
    if not var_res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product variant not found.")

    wishlist = await get_or_create_wishlist(db, user=current_user, session_id=session_id)

    # Check if item already exists
    chk = await db.execute(
        select(WishlistItem).where(
            WishlistItem.wishlist_id == wishlist.id,
            WishlistItem.variant_id == item_in.variant_id,
        )
    )
    existing = chk.scalar_one_or_none()

    if not existing:
        new_item = WishlistItem(wishlist_id=wishlist.id, variant_id=item_in.variant_id)
        db.add(new_item)
        await db.commit()

    return await fetch_wishlist_response(db, wishlist)


@router.delete("/items/{item_id}", response_model=WishlistResponse)
async def remove_from_wishlist(
    item_id: int,
    current_user: Optional[User] = Depends(get_current_user_optional),
    session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    db: AsyncSession = Depends(get_db),
):
    """Remove item from wishlist."""
    wishlist = await get_or_create_wishlist(db, user=current_user, session_id=session_id)

    chk = await db.execute(
        select(WishlistItem).where(
            WishlistItem.id == item_id,
            WishlistItem.wishlist_id == wishlist.id,
        )
    )
    item = chk.scalar_one_or_none()
    if item:
        await db.delete(item)
        await db.commit()

    return await fetch_wishlist_response(db, wishlist)


@router.post("/items/{item_id}/move-to-cart", response_model=WishlistResponse)
async def move_wishlist_item_to_cart(
    item_id: int,
    current_user: Optional[User] = Depends(get_current_user_optional),
    session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    db: AsyncSession = Depends(get_db),
):
    """Move an item from Wishlist into Cart."""
    wishlist = await get_or_create_wishlist(db, user=current_user, session_id=session_id)

    chk = await db.execute(
        select(WishlistItem).where(
            WishlistItem.id == item_id,
            WishlistItem.wishlist_id == wishlist.id,
        )
    )
    witem = chk.scalar_one_or_none()

    if not witem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wishlist item not found.")

    # Validate stock
    avail_stock = await InventoryService.get_available_stock(db, witem.variant_id)
    if avail_stock <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item is currently out of stock.")

    # Get user or guest cart
    cart_stmt = select(Cart).options(selectinload(Cart.items))
    if current_user:
        c_res = await db.execute(cart_stmt.where(Cart.user_id == current_user.id))
        cart = c_res.scalar_one_or_none()
        if not cart:
            cart = Cart(user_id=current_user.id, items=[])
            db.add(cart)
            await db.flush()
    else:
        c_res = await db.execute(cart_stmt.where(Cart.session_id == session_id))
        cart = c_res.scalar_one_or_none()
        if not cart:
            cart = Cart(session_id=session_id, items=[])
            db.add(cart)
            await db.flush()

    existing_citem = next((c for c in cart.items if c.variant_id == witem.variant_id), None)
    if existing_citem:
        existing_citem.quantity += 1
    else:
        new_citem = CartItem(cart_id=cart.id, variant_id=witem.variant_id, quantity=1)
        db.add(new_citem)

    await db.delete(witem)
    await db.commit()

    return await fetch_wishlist_response(db, wishlist)
