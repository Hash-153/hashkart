from datetime import datetime
from decimal import Decimal
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.catalog import Product, ProductVariant
from app.models.seller import SellerListing, SellerProfile
from app.schemas.seller import SellerListingCreate, SellerOnboardingCreate


async def get_seller_for_user(db: AsyncSession, user_id: int) -> Optional[SellerProfile]:
    result = await db.execute(select(SellerProfile).where(SellerProfile.user_id == user_id))
    return result.scalar_one_or_none()


async def submit_onboarding(
    db: AsyncSession, user_id: int, payload: SellerOnboardingCreate
) -> SellerProfile:
    existing = await get_seller_for_user(db, user_id)
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Seller profile already exists")

    duplicate = await db.execute(
        select(SellerProfile).where(SellerProfile.tax_identifier == payload.tax_identifier)
    )
    if duplicate.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Tax identifier already registered")

    seller = SellerProfile(user_id=user_id, **payload.model_dump())
    db.add(seller)
    await db.flush()
    return seller


async def require_approved_seller(db: AsyncSession, user_id: int) -> SellerProfile:
    seller = await get_seller_for_user(db, user_id)
    if not seller or seller.status != "APPROVED":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="An approved seller profile is required for this operation",
        )
    return seller


async def create_listing(
    db: AsyncSession, seller_id: int, payload: SellerListingCreate
) -> SellerListing:
    variant = await db.get(ProductVariant, payload.variant_id)
    product = await db.get(Product, payload.product_id)
    if not variant or not product or variant.product_id != product.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product and variant do not match")

    existing = await db.execute(
        select(SellerListing).where(
            SellerListing.seller_id == seller_id, SellerListing.variant_id == payload.variant_id
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Listing already exists")

    listing = SellerListing(seller_id=seller_id, status="ACTIVE", **payload.model_dump())
    db.add(listing)
    await db.flush()
    return listing


async def list_seller_listings(db: AsyncSession, seller_id: int) -> list[SellerListing]:
    result = await db.execute(
        select(SellerListing)
        .where(SellerListing.seller_id == seller_id)
        .order_by(SellerListing.created_at.desc())
    )
    return list(result.scalars().all())


async def approve_seller(
    db: AsyncSession, seller_id: int, decision: str, rejection_reason: Optional[str]
) -> SellerProfile:
    seller = await db.get(SellerProfile, seller_id)
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller profile not found")
    if decision == "REJECTED" and not rejection_reason:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Rejection reason is required")

    seller.status = decision
    seller.rejection_reason = rejection_reason if decision == "REJECTED" else None
    seller.approved_at = datetime.utcnow() if decision == "APPROVED" else None
    await db.flush()
    return seller
