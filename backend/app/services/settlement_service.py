import uuid
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import List, Optional, Tuple
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.catalog import Product
from app.models.order_payment import Order, OrderItem
from app.models.seller import SellerProfile
from app.models.settlement import (
    CommissionTierType,
    LedgerEntryType,
    SellerCommissionRate,
    SellerEscrowAccount,
    SellerFinancialLedger,
    SellerPayoutBatch,
    SellerPayoutItem,
    SettlementStatus,
)


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


async def get_or_create_escrow_account(
    db: AsyncSession, seller_id: int
) -> SellerEscrowAccount:
    """Retrieve or initialize the escrow ledger account for a seller."""
    stmt = select(SellerEscrowAccount).where(SellerEscrowAccount.seller_id == seller_id)
    res = await db.execute(stmt)
    account = res.scalar_one_or_none()

    if not account:
        account = SellerEscrowAccount(
            seller_id=seller_id,
            available_balance=Decimal("0.00"),
            held_balance=Decimal("0.00"),
            pending_payout_balance=Decimal("0.00"),
            total_lifetime_settled=Decimal("0.00"),
            currency="INR",
            is_locked=False,
        )
        db.add(account)
        await db.flush()
        await db.refresh(account)

    return account


async def calculate_seller_item_commission(
    db: AsyncSession, seller_id: int, category_id: Optional[int], gross_amount: Decimal
) -> Decimal:
    """Calculate platform commission fee based on category and seller rate agreements."""
    # Look for specific seller + category rate
    stmt = (
        select(SellerCommissionRate)
        .where(
            SellerCommissionRate.is_active == True,
            (SellerCommissionRate.seller_id == seller_id) | (SellerCommissionRate.seller_id.is_(None)),
            (SellerCommissionRate.category_id == category_id) | (SellerCommissionRate.category_id.is_(None)),
        )
        .order_by(
            SellerCommissionRate.seller_id.desc().nullslast(),
            SellerCommissionRate.category_id.desc().nullslast(),
        )
        .limit(1)
    )
    res = await db.execute(stmt)
    rate_rule = res.scalar_one_or_none()

    if not rate_rule:
        # Default fallback 5% marketplace commission
        commission = (gross_amount * Decimal("0.05")).quantize(Decimal("0.01"))
        return max(commission, Decimal("10.00"))

    if rate_rule.commission_type == CommissionTierType.PERCENTAGE:
        calculated = (gross_amount * (rate_rule.base_percentage / Decimal("100.00"))).quantize(Decimal("0.01"))
    elif rate_rule.commission_type == CommissionTierType.FIXED:
        calculated = rate_rule.fixed_fee
    else:
        percentage_part = (gross_amount * (rate_rule.base_percentage / Decimal("100.00"))).quantize(Decimal("0.01"))
        calculated = percentage_part + rate_rule.fixed_fee

    if rate_rule.min_commission and calculated < rate_rule.min_commission:
        calculated = rate_rule.min_commission
    if rate_rule.max_commission and calculated > rate_rule.max_commission:
        calculated = rate_rule.max_commission

    return calculated


async def credit_order_to_escrow(
    db: AsyncSession, order: Order, seller_id: int
) -> List[SellerFinancialLedger]:
    """Hold buyer payment funds in escrow upon successful order placement/payment."""
    escrow = await get_or_create_escrow_account(db, seller_id)
    created_entries: List[SellerFinancialLedger] = []

    # Filter items belonging to this seller
    for item in order.items:
        gross_amount = item.price * item.quantity
        commission_fee = await calculate_seller_item_commission(
            db, seller_id, None, gross_amount
        )
        # Indian Marketplace GST/TCS withholding: 1% TCS on net sales
        tcs_withholding = (gross_amount * Decimal("0.01")).quantize(Decimal("0.01"))
        # GST on platform commission: 18% GST on platform fee
        gst_on_commission = (commission_fee * Decimal("0.18")).quantize(Decimal("0.01"))
        total_deductions = commission_fee + tcs_withholding + gst_on_commission
        net_credit = gross_amount - total_deductions

        # Increment escrow held balance
        escrow.held_balance += net_credit

        ref_no = f"TXN-ESC-{order.id}-{item.id}-{uuid.uuid4().hex[:6].upper()}"
        ledger = SellerFinancialLedger(
            escrow_account_id=escrow.id,
            seller_id=seller_id,
            order_id=order.id,
            order_item_id=item.id,
            entry_type=LedgerEntryType.SALE_CREDIT,
            gross_amount=gross_amount,
            net_amount=net_credit,
            fee_deductions=commission_fee,
            tax_deductions=tcs_withholding + gst_on_commission,
            running_balance=escrow.available_balance + escrow.held_balance,
            currency="INR",
            reference_number=ref_no,
            description=f"Escrow hold for Order #{order.order_number} Item #{item.id}",
        )
        db.add(ledger)
        created_entries.append(ledger)

    await db.flush()
    return created_entries


async def release_escrow_to_available(
    db: AsyncSession, order: Order, seller_id: int
) -> bool:
    """Release escrow hold to available balance after return window expires (e.g. 7 days post-delivery)."""
    escrow = await get_or_create_escrow_account(db, seller_id)
    
    # Calculate amount to release for this order
    stmt = (
        select(SellerFinancialLedger)
        .where(
            SellerFinancialLedger.seller_id == seller_id,
            SellerFinancialLedger.order_id == order.id,
            SellerFinancialLedger.entry_type == LedgerEntryType.SALE_CREDIT,
        )
    )
    res = await db.execute(stmt)
    entries = res.scalars().all()

    total_release = sum(e.net_amount for e in entries)
    if total_release <= Decimal("0.00"):
        return False

    if escrow.held_balance >= total_release:
        escrow.held_balance -= total_release
        escrow.available_balance += total_release
    else:
        escrow.available_balance += escrow.held_balance
        escrow.held_balance = Decimal("0.00")

    ref_no = f"TXN-REL-{order.id}-{uuid.uuid4().hex[:6].upper()}"
    release_entry = SellerFinancialLedger(
        escrow_account_id=escrow.id,
        seller_id=seller_id,
        order_id=order.id,
        entry_type=LedgerEntryType.ADJUSTMENT,
        gross_amount=total_release,
        net_amount=total_release,
        fee_deductions=Decimal("0.00"),
        tax_deductions=Decimal("0.00"),
        running_balance=escrow.available_balance + escrow.held_balance,
        currency="INR",
        reference_number=ref_no,
        description=f"Escrow matured and released to available balance for Order #{order.order_number}",
    )
    db.add(release_entry)
    await db.flush()
    return True


async def create_seller_payout_batch(
    db: AsyncSession, seller_id: int, payout_method: str = "NEFT"
) -> Tuple[Optional[SellerPayoutBatch], str]:
    """Compile available balances into an official NEFT/UPI bank payout batch."""
    escrow = await get_or_create_escrow_account(db, seller_id)

    if escrow.is_locked:
        return None, f"Escrow account locked: {escrow.lock_reason}"
    if escrow.available_balance < Decimal("500.00"):
        return None, "Minimum payout threshold is ₹500.00"

    payout_amount = escrow.available_balance
    escrow.available_balance = Decimal("0.00")
    escrow.pending_payout_balance += payout_amount

    batch_ref = f"PAYOUT-{seller_id}-{datetime.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
    batch = SellerPayoutBatch(
        batch_reference=batch_ref,
        seller_id=seller_id,
        status=SettlementStatus.PROCESSING,
        gross_payout=payout_amount,
        total_deductions=Decimal("0.00"),
        net_payout=payout_amount,
        payout_method=payout_method,
        scheduled_date=utcnow() + timedelta(days=1),
    )
    db.add(batch)
    await db.flush()

    ledger_ref = f"TXN-OUT-{batch.id}-{uuid.uuid4().hex[:6].upper()}"
    ledger_entry = SellerFinancialLedger(
        escrow_account_id=escrow.id,
        seller_id=seller_id,
        payout_batch_id=batch.id,
        entry_type=LedgerEntryType.PAYOUT_TRANSFER,
        gross_amount=payout_amount,
        net_amount=payout_amount,
        fee_deductions=Decimal("0.00"),
        tax_deductions=Decimal("0.00"),
        running_balance=escrow.available_balance + escrow.held_balance,
        currency="INR",
        reference_number=ledger_ref,
        description=f"Payout transfer queued in Batch #{batch_ref}",
    )
    db.add(ledger_entry)
    await db.flush()

    return batch, "Payout batch created successfully"


async def mark_payout_batch_settled(
    db: AsyncSession, batch_id: int, gateway_txn_id: str, admin_user_id: int
) -> bool:
    """Mark payout batch as successfully transferred to seller's bank account."""
    stmt = (
        select(SellerPayoutBatch)
        .options(selectinload(SellerPayoutBatch.items))
        .where(SellerPayoutBatch.id == batch_id)
    )
    res = await db.execute(stmt)
    batch = res.scalar_one_or_none()

    if not batch or batch.status == SettlementStatus.SETTLED:
        return False

    escrow = await get_or_create_escrow_account(db, batch.seller_id)
    if escrow.pending_payout_balance >= batch.net_payout:
        escrow.pending_payout_balance -= batch.net_payout
    else:
        escrow.pending_payout_balance = Decimal("0.00")
    escrow.total_lifetime_settled += batch.net_payout

    batch.status = SettlementStatus.SETTLED
    batch.gateway_transaction_id = gateway_txn_id
    batch.processed_by_admin_id = admin_user_id
    batch.settled_at = utcnow()

    await db.flush()
    return True
