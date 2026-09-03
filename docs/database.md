# Database Design & Schema Specification

## Overview

The database design for NovaMart uses a normalized relational model supporting full ACID compliance, foreign key integrity, cascade options, check constraints, and performance indexes.

---

## Entity Relationship Overview

The schema consists of 25 core entities:

1. **`users`**: Account records for customers, staff, and admins.
2. **`roles`**: System roles (`CUSTOMER`, `STAFF`, `ADMIN`).
3. **`user_roles`**: Junction table mapping users to roles.
4. **`addresses`**: Saved customer delivery and billing addresses.
5. **`categories`**: Hierarchical product categories and subcategories.
6. **`brands`**: Verified manufacturers and brand entities.
7. **`products`**: Parent product catalog items.
8. **`product_variants`**: Specific SKUs (combinations of size, color, storage, model).
9. **`product_images`**: Variant/product image URLs, gallery order, and alt texts.
10. **`product_attributes`**: Key-value product specifications (e.g., RAM, Battery Capacity, Warranty).
11. **`inventory`**: Real-time stock levels, reserved quantities, and warehouse locations.
12. **`inventory_transactions`**: Audit trail of stock adjustments (Restock, Order Reservation, Order Cancellation, Return).
13. **`carts`**: Active and persistent shopping carts per user or session.
14. **`cart_items`**: Items and quantities inside shopping carts.
15. **`wishlists`**: Saved user wishlists.
16. **`wishlist_items`**: Individual items saved in wishlists.
17. **`orders`**: Customer order headers containing totals, status, and shipping info.
18. **`order_items`**: Line items within an order with price snapshots.
19. **`payments`**: Payment transactions with status (`CREATED`, `PROCESSING`, `SUCCESS`, `FAILED`, `REFUNDED`).
20. **`shipments`**: Logistics tracking details, courier identifiers, and estimated delivery dates.
21. **`coupons`**: Discount promo code definitions (Percentage, Fixed Amount, Min Order Value).
22. **`coupon_usage`**: Tracking code redemptions per user to enforce usage limits.
23. **`reviews`**: Customer ratings (1–5 stars), written reviews, and verified purchase flags.
24. **`notifications`**: Customer in-app alert messages.
25. **`audit_logs`**: System security and administrative event records.

---

## Indexing Strategy

- **Primary Keys**: B-tree index on auto-incrementing integer or UUID primary keys.
- **Foreign Keys**: B-tree index on all foreign key columns to optimize `JOIN` operations.
- **Search Indexes**: Indexes on `products.name`, `products.brand_id`, `products.category_id`, `product_variants.sku`, and `orders.order_number`.
- **Unique Constraints**: Unique indexes on `users.email`, `categories.slug`, `brands.slug`, `product_variants.sku`, and `coupons.code`.
