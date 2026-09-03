from decimal import Decimal
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.deps import get_current_user, get_db, require_role
from app.models.seller import SellerProfile
from app.models.settlement import (
    CommissionTierType,
    SellerCommissionRate,
    SellerEscrowAccount,
    SellerFinancialLedger,
    SellerPayoutBatch,
    SettlementStatus,
)
from app.models.user import User
from app.schemas.settlement import (
    CommissionRateCreate,
    CommissionRateResponse,
    EscrowAccountResponse,
    LedgerEntryResponse,
    PayoutBatchCreate,
    PayoutBatchResponse,
    SellerSettlementSummary,
)
from app.services.settlement_service import (
    create_seller_payout_batch,
    get_or_create_escrow_account,
    mark_payout_batch_settled,
)

router = APIRouter()


@router.get("/escrow/summary", response_model=SellerSettlementSummary)
async def get_seller_escrow_summary(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve current escrow financial balances, lifetime earnings, and recent payout batches."""
    stmt = select(SellerProfile).where(SellerProfile.user_id == current_user.id)
    res = await db.execute(stmt)
    seller = res.scalar_one_or_none()

    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Seller profile not found",
        )

    escrow = await get_or_create_escrow_account(db, seller.id)

    # Fetch recent batches
    batch_stmt = (
        select(SellerPayoutBatch)
        .options(selectinload(SellerPayoutBatch.items))
        .where(SellerPayoutBatch.seller_id == seller.id)
        .order_by(SellerPayoutBatch.created_at.desc())
        .limit(10)
    )
    batch_res = await db.execute(batch_stmt)
    batches = batch_res.scalars().all()

    # Calculate total commission and tax paid from ledger
    ledger_agg_stmt = select(
        func.sum(SellerFinancialLedger.fee_deductions),
        func.sum(SellerFinancialLedger.tax_deductions),
        func.count(SellerFinancialLedger.id),
    ).where(SellerFinancialLedger.seller_id == seller.id)
    agg_res = await db.execute(ledger_agg_stmt)
    comm_sum, tax_sum, order_cnt = agg_res.one()

    return SellerSettlementSummary(
        seller_id=seller.id,
        available_balance=escrow.available_balance,
        held_balance=escrow.held_balance,
        pending_payout_balance=escrow.pending_payout_balance,
        total_lifetime_settled=escrow.total_lifetime_settled,
        total_orders_settled=order_cnt or 0,
        total_commission_paid=comm_sum or Decimal("0.00"),
        total_tax_withheld=tax_sum or Decimal("0.00"),
        recent_batches=[PayoutBatchResponse.model_validate(b) for b in batches],
    )


@router.get("/ledger", response_model=List[LedgerEntryResponse])
async def get_seller_ledger_entries(
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Retrieve detailed financial ledger audit entries for the authenticated seller."""
    stmt = select(SellerProfile).where(SellerProfile.user_id == current_user.id)
    res = await db.execute(stmt)
    seller = res.scalar_one_or_none()

    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Seller profile not found",
        )

    ledger_stmt = (
        select(SellerFinancialLedger)
        .where(SellerFinancialLedger.seller_id == seller.id)
        .order_by(SellerFinancialLedger.created_at.desc())
        .offset(offset)
        .limit(limit)
    )
    l_res = await db.execute(ledger_stmt)
    entries = l_res.scalars().all()
    return entries


@router.post("/payouts/request", response_model=PayoutBatchResponse)
async def request_payout_batch(
    payload: PayoutBatchCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Initiate a payout transfer batch from available escrow balance."""
    stmt = select(SellerProfile).where(SellerProfile.user_id == current_user.id)
    res = await db.execute(stmt)
    seller = res.scalar_one_or_none()

    if not seller or seller.id != payload.seller_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Cannot request payout for another seller",
        )

    batch, msg = await create_seller_payout_batch(db, seller.id, payload.payout_method)
    if not batch:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg,
        )
    await db.commit()
    await db.refresh(batch)
    return batch


@router.post("/admin/payouts/{batch_id}/settle", response_model=PayoutBatchResponse)
async def settle_payout_batch(
    batch_id: int,
    gateway_txn_id: str = Query(..., min_length=5),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_role(["ADMIN", "FINANCE"])),
):
    """Admin endpoint to finalize bank settlement transfer."""
    success = await mark_payout_batch_settled(db, batch_id, gateway_txn_id, current_user.id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Payout batch could not be settled (invalid ID or already settled)",
        )
    await db.commit()

    stmt = select(SellerPayoutBatch).options(selectinload(SellerPayoutBatch.items)).where(SellerPayoutBatch.id == batch_id)
    res = await db.execute(stmt)
    batch = res.scalar_one()
    return batch
