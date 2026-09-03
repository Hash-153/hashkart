from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
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
from app.core.deps import get_current_user

router = APIRouter()


async def get_or_create_wishlist(db: AsyncSession, user: User) -> Wishlist:
    """Helper to fetch or create user wishlist."""
    result = await db.execute(
        select(Wishlist).options(selectinload(Wishlist.items).selectinload(WishlistItem.variant)).where(Wishlist.user_id == user.id)
    )
    wishlist = result.scalar_one_or_none()
    if not wishlist:
        wishlist = Wishlist(user_id=user.id, items=[])
        db.add(wishlist)
        await db.flush()
    return wishlist


@router.get("", response_model=WishlistResponse)
async def get_wishlist(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Fetch user wishlist items."""
    wishlist = await get_or_create_wishlist(db, current_user)
    return wishlist


@router.post("/items", response_model=WishlistResponse)
async def add_to_wishlist(
    item_in: WishlistItemCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Add item to wishlist."""
    var_res = await db.execute(select(ProductVariant).where(ProductVariant.id == item_in.variant_id))
    if not var_res.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product variant not found.")

    wishlist = await get_or_create_wishlist(db, current_user)
    existing = next((i for i in wishlist.items if i.variant_id == item_in.variant_id), None)
    if not existing:
        new_item = WishlistItem(wishlist_id=wishlist.id, variant_id=item_in.variant_id)
        db.add(new_item)
        await db.commit()
        await db.refresh(wishlist)

    return wishlist


@router.delete("/items/{item_id}", response_model=WishlistResponse)
async def remove_from_wishlist(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Remove item from wishlist."""
    wishlist = await get_or_create_wishlist(db, current_user)
    item = next((i for i in wishlist.items if i.id == item_id), None)
    if item:
        await db.delete(item)
        await db.commit()
        await db.refresh(wishlist)
    return wishlist


@router.post("/items/{item_id}/move-to-cart", response_model=WishlistResponse)
async def move_wishlist_item_to_cart(
    item_id: int,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Move an item from Wishlist into User's Cart."""
    wishlist = await get_or_create_wishlist(db, current_user)
    witem = next((i for i in wishlist.items if i.id == item_id), None)

    if not witem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Wishlist item not found.")

    # Validate stock
    avail_stock = await InventoryService.get_available_stock(db, witem.variant_id)
    if avail_stock <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item is currently out of stock.")

    # Get user cart
    c_res = await db.execute(
        select(Cart).options(selectinload(Cart.items)).where(Cart.user_id == current_user.id)
    )
    cart = c_res.scalar_one_or_none()
    if not cart:
        cart = Cart(user_id=current_user.id, items=[])
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
    await db.refresh(wishlist)
    return wishlist
