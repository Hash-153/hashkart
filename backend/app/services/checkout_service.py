import uuid
from decimal import Decimal
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_, and_, update
from sqlalchemy.orm import selectinload

from app.models.catalog import ProductVariant
from app.models.cart_wishlist import Cart, CartItem
from app.models.user import User, Address
from app.models.promotion_review import Coupon, CouponUsage
from app.models.order_payment import Order, OrderItem, Payment, Shipment
from app.models.inventory_reservation import InventoryReservation
from app.models.checkout_idempotency import CheckoutIdempotency
from app.models.order_refund import OrderRefund
from app.services.warehouse_task_service import create_order_tasks
from app.models.system import Notification, AuditLog
from app.services.pricing_service import PricingService
from app.services.inventory_service import InventoryService
from app.services.promotion_service import PromotionService


class CheckoutService:
    """Orchestrates checkout preview, idempotency validation, order creation, state transitions, and refunds."""

    @staticmethod
    async def get_checkout_preview(
        db: AsyncSession, user: User, address_id: int, coupon_code: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate checkout preview without placing an order or reserving stock.
        Includes authoritative financial breakdown, price-change alerts, and stock warnings.
        """
        # Validate delivery address
        addr_res = await db.execute(
            select(Address).where(Address.id == address_id, Address.user_id == user.id)
        )
        address = addr_res.scalar_one_or_none()
        if not address:
            raise ValueError("Invalid delivery address selected.")

        # Fetch cart
        cart_res = await db.execute(
            select(Cart).options(selectinload(Cart.items).selectinload(CartItem.variant)).where(Cart.user_id == user.id)
        )
        cart = cart_res.scalar_one_or_none()
        if not cart or not cart.items:
            raise ValueError("Your cart is empty.")

        preview_items: List[Dict[str, Any]] = []
        price_changes: List[str] = []
        stock_warnings: List[str] = []
        raw_subtotal = Decimal("0.00")

        for item in cart.items:
            variant = item.variant
            if not variant or not variant.is_active:
                stock_warnings.append(f"Product SKU '{item.variant.sku}' is unavailable.")
                continue

            # Check available stock
            avail_stock = await InventoryService.get_available_stock(db, variant.id)
            if avail_stock < item.quantity:
                stock_warnings.append(
                    f"'{variant.title}' has only {avail_stock} units available (Requested: {item.quantity})."
                )

            # Authoritative current sale price
            current_unit_price = PricingService.to_decimal(variant.discount_price if variant.discount_price else variant.price)
            line_total = (current_unit_price * Decimal(str(item.quantity))).quantize(Decimal("0.01"))
            raw_subtotal += line_total

            preview_items.append({
                "variant_id": variant.id,
                "product_name": variant.product.name if variant.product else variant.title,
                "variant_title": variant.title,
                "sku": variant.sku,
                "unit_price": float(current_unit_price),
                "quantity": item.quantity,
                "line_total": float(line_total),
            })

        # Evaluate promotions
        promo_discount, applied_promos = PromotionService.evaluate_promotions(preview_items, raw_subtotal)

        # Coupon calculation
        coupon_discount = Decimal("0.00")
        coupon_obj = None
        if coupon_code and coupon_code.strip():
            c_code = coupon_code.strip().upper()
            c_res = await db.execute(
                select(Coupon).where(Coupon.code == c_code, Coupon.is_active == True)
            )
            coupon_obj = c_res.scalar_one_or_none()
            if coupon_obj:
                now = datetime.utcnow()
                if coupon_obj.valid_from <= now <= coupon_obj.valid_to:
                    coupon_discount = PricingService.calculate_coupon_discount(
                        subtotal=raw_subtotal,
                        discount_type=coupon_obj.discount_type,
                        discount_value=coupon_obj.discount_value,
                        min_order_value=coupon_obj.min_order_value,
                        max_discount_amount=coupon_obj.max_discount_amount,
                    )

        total_discount = promo_discount + coupon_discount
        taxable = max(Decimal("0.00"), raw_subtotal - total_discount)
        tax = PricingService.calculate_tax(taxable)
        shipping = PricingService.calculate_shipping(raw_subtotal)
        grand_total = taxable + tax + shipping

        return {
            "address_id": address.id,
            "items": preview_items,
            "subtotal": float(raw_subtotal),
            "promotion_discount": float(promo_discount),
            "coupon_discount": float(coupon_discount),
            "total_discount": float(total_discount),
            "tax": float(tax),
            "shipping": float(shipping),
            "grand_total": float(grand_total),
            "applied_promotions": applied_promos,
            "coupon": coupon_obj,
            "price_changes": price_changes,
            "stock_warnings": stock_warnings,
        }

    @staticmethod
    async def place_order_with_idempotency(
        db: AsyncSession,
        user: User,
        address_id: int,
        payment_method: str,
        idempotency_key: Optional[str] = None,
        coupon_code: Optional[str] = None,
        mock_scenario: str = "SUCCESS",  # SUCCESS, FAILURE, DECLINED, PENDING
    ) -> Tuple[Order, bool]:
        """
        Concurrency-safe order placement with Idempotency Key deduplication & Stock Reservation.
        """
        # 1. Idempotency Check
        if idempotency_key:
            idem_res = await db.execute(
                select(CheckoutIdempotency)
                .options(selectinload(CheckoutIdempotency.order))
                .where(CheckoutIdempotency.idempotency_key == idempotency_key, CheckoutIdempotency.user_id == user.id)
            )
            idem = idem_res.scalar_one_or_none()
            if idem and idem.order:
                return idem.order, True  # Return cached order

        # 2. Get Preview Calculation
        preview = await CheckoutService.get_checkout_preview(db, user, address_id, coupon_code)
        if preview["stock_warnings"]:
            raise ValueError(f"Checkout failed: {'; '.join(preview['stock_warnings'])}")

        # 3. Reserve Stock for all items under transaction lock
        cart_res = await db.execute(
            select(Cart).options(selectinload(Cart.items).selectinload(CartItem.variant)).where(Cart.user_id == user.id)
        )
        cart = cart_res.scalar_one_or_none()
        if not cart or not cart.items:
            raise ValueError("Cart is empty.")

        reservations: List[InventoryReservation] = []
        for item in cart.items:
            success, res_obj, err_msg = await InventoryService.reserve_stock(
                db, variant_id=item.variant_id, quantity=item.quantity, user_id=user.id
            )
            if not success or not res_obj:
                # Rollback previous reservations in this batch
                for prev_r in reservations:
                    await InventoryService.release_reservation(db, prev_r.reservation_key)
                raise ValueError(f"Inventory reservation failed for '{item.variant.title}': {err_msg}")
            reservations.append(res_obj)

        # 4. Handle Mock Payment Gateway Scenarios
        if mock_scenario in ["FAILURE", "DECLINED"]:
            for r in reservations:
                await InventoryService.release_reservation(db, r.reservation_key)
            raise ValueError(f"Mock Payment Failed ({mock_scenario}): Card declined or bank timeout.")

        payment_status = "PAID" if mock_scenario == "SUCCESS" and payment_method != "COD" else "PENDING"
        order_status = "CONFIRMED" if payment_status == "PAID" or payment_method == "COD" else "PENDING"
        order_num = f"HK-{datetime.utcnow().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"

        # 5. Create Order Record
        order = Order(
            order_number=order_num,
            user_id=user.id,
            address_id=address_id,
            coupon_id=preview["coupon"].id if preview["coupon"] else None,
            status=order_status,
            payment_status=payment_status,
            subtotal=preview["subtotal"],
            tax_amount=preview["tax"],
            shipping_fee=preview["shipping"],
            discount_amount=preview["total_discount"],
            grand_total=preview["grand_total"],
        )
        db.add(order)
        await db.flush()

        # 6. Create Line Items & Confirm Stock Reservations
        for item in cart.items:
            unit_p = float(PricingService.to_decimal(item.variant.discount_price or item.variant.price))
            line_tot = float(PricingService.to_decimal(unit_p * item.quantity))

            order_item = OrderItem(
                order_id=order.id,
                variant_id=item.variant_id,
                product_name=item.variant.product.name if item.variant.product else item.variant.title,
                variant_title=item.variant.title,
                sku=item.variant.sku,
                unit_price=float(item.variant.price),
                discount_price=float(item.variant.discount_price) if item.variant.discount_price else None,
                quantity=item.quantity,
                line_subtotal=line_tot,
            )
            db.add(order_item)

        for r in reservations:
            await InventoryService.confirm_reservation(db, r.reservation_key)

        # 7. Record Payment & Shipment
        payment = Payment(
            order_id=order.id,
            payment_method=payment_method,
            transaction_reference=f"TXN-{uuid.uuid4().hex[:12].upper()}",
            amount=preview["grand_total"],
            status="SUCCESS" if payment_status == "PAID" else "CREATED",
            gateway_response=f"Mock Payment Scenario: {mock_scenario}",
        )
        db.add(payment)

        shipment = Shipment(
            order_id=order.id,
            tracking_number=f"TRK-{uuid.uuid4().hex[:10].upper()}",
            carrier_name="HashKart Express",
            shipment_status="MANIFEST_CREATED",
            estimated_delivery=datetime.utcnow() + timedelta(days=4),
        )
        db.add(shipment)
        await db.flush()
        await create_order_tasks(db, order.id, shipment.id)

        # 8. Record Idempotency Key
        if idempotency_key:
            idem_obj = CheckoutIdempotency(idempotency_key=idempotency_key, user_id=user.id, order_id=order.id)
            db.add(idem_obj)

        # 9. Clear Purchased Cart Items
        for citem in list(cart.items):
            await db.delete(citem)

        # 10. Audit Log & In-App Notification
        notif = Notification(
            user_id=user.id,
            title="Order Confirmed!",
            message=f"Order {order_num} for ₹{preview['grand_total']} placed successfully.",
            notification_type="ORDER",
            link=f"/orders/{order_num}",
        )
        db.add(notif)

        audit = AuditLog(
            user_id=user.id,
            action="ORDER_CREATED",
            entity_type="Order",
            entity_id=str(order.id),
            details=f"Placed order {order_num} via {payment_method}",
        )
        db.add(audit)

        await db.commit()

        # Reload complete order
        res_order = await db.execute(
            select(Order)
            .options(
                selectinload(Order.items),
                selectinload(Order.payment),
                selectinload(Order.shipment),
                selectinload(Order.address),
            )
            .where(Order.id == order.id)
        )
        return res_order.scalar_one(), False

    @staticmethod
    async def cancel_order(db: AsyncSession, order_id: int, user_id: int, reason: str = "Customer request") -> Order:
        """Cancel order and restore stock."""
        stmt = (
            select(Order)
            .options(selectinload(Order.items).selectinload(OrderItem.variant))
            .where(Order.id == order_id, Order.user_id == user_id)
            .with_for_update()
        )
        res = await db.execute(stmt)
        order = res.scalar_one_or_none()

        if not order:
            raise ValueError("Order not found.")

        if order.status in ["SHIPPED", "DELIVERED", "CANCELLED"]:
            raise ValueError(f"Order cannot be cancelled in status '{order.status}'.")

        order.status = "CANCELLED"
        order.payment_status = "REFUNDED" if order.payment_status == "PAID" else "CANCELLED"

        # Restore product stock
        for item in order.items:
            if item.variant:
                item.variant.stock_quantity += item.quantity

        audit = AuditLog(
            user_id=user_id,
            action="ORDER_CANCELLED",
            entity_type="Order",
            entity_id=str(order.id),
            details=f"Cancelled order {order.order_number}: {reason}",
        )
        db.add(audit)

        await db.commit()
        return order
