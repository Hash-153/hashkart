from fastapi import APIRouter
from app.api.v1.endpoints import (
    admin,
    analytics,
    auth,
    cart,
    catalog,
    checkout,
    comparison,
    discovery,
    flash_sales,
    fulfillment,
    helpdesk,
    logistics,
    loyalty,
    notifications,
    operations,
    orders,
    payments,
    qa,
    reviews,
    risk,
    search,
    seller,
    seller_analytics,
    settlement,
    support,
    telemetry,
    users,
    warehouse,
    webhooks,
)

api_router = APIRouter()

# Core Storefront & Auth
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(users.router, prefix="/users", tags=["Users & Account"])
api_router.include_router(catalog.router, prefix="/catalog", tags=["Catalog"])
api_router.include_router(search.router, prefix="/search", tags=["Search Subsystem"])
api_router.include_router(discovery.router, prefix="/discovery", tags=["Discovery & Recommendations"])
api_router.include_router(cart.router, prefix="/cart", tags=["Shopping Cart"])
api_router.include_router(wishlist_router := cart.router, prefix="/cart-extra", tags=["Shopping Cart Extra"])
api_router.include_router(checkout.router, prefix="/checkout", tags=["Checkout"])
api_router.include_router(orders.router, prefix="/orders", tags=["Orders"])
api_router.include_router(reviews.router, prefix="/reviews", tags=["Reviews"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])

# Enterprise E-Commerce Features
api_router.include_router(loyalty.router, prefix="/loyalty", tags=["SuperCoins & Loyalty Rewards"])
api_router.include_router(flash_sales.router, prefix="/flash-sales", tags=["Flash Sales & Deals"])
api_router.include_router(logistics.router, prefix="/logistics", tags=["Logistics & Pincode Matrix"])
api_router.include_router(comparison.router, prefix="/compare", tags=["Product Comparison"])
api_router.include_router(qa.router, prefix="/qa", tags=["Community Q&A"])
api_router.include_router(helpdesk.router, prefix="/helpdesk", tags=["Customer Helpdesk & SLA"])
api_router.include_router(risk.router, prefix="/risk", tags=["Fraud & Risk Prevention"])
api_router.include_router(webhooks.router, prefix="/webhooks", tags=["Enterprise Webhooks"])
api_router.include_router(telemetry.router, prefix="/telemetry", tags=["Observability & Metrics"])

# Seller & Marketplace Operations
api_router.include_router(seller.router, prefix="/seller", tags=["Seller Operations"])
api_router.include_router(seller.admin_router, prefix="/admin", tags=["Seller Administration"])
api_router.include_router(seller_analytics.router, prefix="/seller/analytics", tags=["Seller Analytics"])
api_router.include_router(settlement.router, prefix="/seller/settlement", tags=["Seller Settlement & Escrow"])

# Admin & WMS Operations
api_router.include_router(admin.router, prefix="/admin", tags=["Admin Operations"])
api_router.include_router(analytics.router, prefix="/admin/analytics", tags=["Analytics"])
api_router.include_router(fulfillment.router, prefix="/admin/fulfillment", tags=["Fulfillment Operations"])
api_router.include_router(operations.router, prefix="/admin/operations", tags=["Marketplace Operations"])
api_router.include_router(payments.router, prefix="/payments", tags=["Payments & Reconciliation"])
api_router.include_router(support.router, prefix="/support", tags=["Customer Support"])
api_router.include_router(warehouse.router, prefix="/admin/warehouse", tags=["Warehouse Operations"])
