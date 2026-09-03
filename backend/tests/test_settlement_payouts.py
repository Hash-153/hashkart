import pytest
from decimal import Decimal
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.settlement import (
    CommissionTierType,
    LedgerEntryType,
    SellerCommissionRate,
    SellerEscrowAccount,
    SettlementStatus,
)
from app.services.settlement_service import (
    calculate_seller_item_commission,
    create_seller_payout_batch,
    get_or_create_escrow_account,
    mark_payout_batch_settled,
)


@pytest.mark.asyncio
async def test_seller_escrow_lifecycle(db_session: AsyncSession):
    """Test escrow account balance creation and payout lifecycle."""
    seller_id = 999
    escrow = await get_or_create_escrow_account(db_session, seller_id)
    assert escrow.seller_id == seller_id
    assert escrow.available_balance == Decimal("0.00")
    assert escrow.held_balance == Decimal("0.00")

    # Simulate available funds after orders
    escrow.available_balance = Decimal("2500.00")
    await db_session.flush()

    # Create payout batch
    batch, msg = await create_seller_payout_batch(db_session, seller_id, payout_method="NEFT")
    assert batch is not None
    assert batch.status == SettlementStatus.PROCESSING
    assert batch.net_payout == Decimal("2500.00")
    assert escrow.available_balance == Decimal("0.00")
    assert escrow.pending_payout_balance == Decimal("2500.00")

    # Settle payout batch
    settled = await mark_payout_batch_settled(db_session, batch.id, "NEFT-UTR-12345678", admin_user_id=1)
    assert settled is True
    assert batch.status == SettlementStatus.SETTLED
    assert escrow.pending_payout_balance == Decimal("0.00")
    assert escrow.total_lifetime_settled == Decimal("2500.00")


@pytest.mark.asyncio
async def test_commission_calculation(db_session: AsyncSession):
    """Verify tier commission and minimum marketplace fee enforcement."""
    # Test fallback 5% commission on ₹1,000 item
    comm = await calculate_seller_item_commission(db_session, seller_id=1, category_id=None, gross_amount=Decimal("1000.00"))
    assert comm == Decimal("50.00")

    # Test minimum ₹10 commission on ₹50 item
    comm_small = await calculate_seller_item_commission(db_session, seller_id=1, category_id=None, gross_amount=Decimal("50.00"))
    assert comm_small == Decimal("10.00")
