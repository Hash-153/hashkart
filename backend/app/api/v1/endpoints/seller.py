from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user, require_admin
from app.database import get_db
from app.models.seller import SellerProfile
from app.models.user import User
from app.schemas.seller import (
    SellerApprovalRequest,
    SellerListingCreate,
    SellerListingResponse,
    SellerOnboardingCreate,
    SellerProfileResponse,
)
from app.services.seller_service import (
    approve_seller,
    create_listing,
    get_seller_for_user,
    list_seller_listings,
    require_approved_seller,
    submit_onboarding,
)

router = APIRouter()
admin_router = APIRouter()


@router.post("/onboarding", response_model=SellerProfileResponse, status_code=status.HTTP_201_CREATED)
async def onboard_seller(
    payload: SellerOnboardingCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await submit_onboarding(db, user.id, payload)


@router.get("/profile", response_model=SellerProfileResponse)
async def seller_profile(
    user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):
    seller = await get_seller_for_user(db, user.id)
    if not seller:
        from fastapi import HTTPException

        raise HTTPException(status_code=404, detail="Seller profile not found")
    return seller


@router.post("/listings", response_model=SellerListingResponse, status_code=status.HTTP_201_CREATED)
async def add_listing(
    payload: SellerListingCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    seller = await require_approved_seller(db, user.id)
    return await create_listing(db, seller.id, payload)


@router.get("/listings", response_model=list[SellerListingResponse])
async def seller_listings(
    user: User = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):
    seller = await require_approved_seller(db, user.id)
    return await list_seller_listings(db, seller.id)


@admin_router.patch(
    "/sellers/{seller_id}/approval", response_model=SellerProfileResponse
)
async def review_seller(
    seller_id: int,
    payload: SellerApprovalRequest,
    _: User = Depends(require_admin),
    db: AsyncSession = Depends(get_db),
):
    return await approve_seller(db, seller_id, payload.status, payload.rejection_reason)
