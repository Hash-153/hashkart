# API Documentation & Endpoints Specification

## Overview

All NovaMart REST API endpoints are prefixed with `/api/v1`. The API communicates using JSON payloads and standard HTTP status codes (`200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `422 Unprocessable Entity`, `500 Internal Server Error`).

---

## Endpoint Summary

### Authentication (`/api/v1/auth`)
- `POST /auth/register`: Register new customer account.
- `POST /auth/login`: Authenticate credentials & return JWT tokens.
- `POST /auth/refresh`: Refresh access token using refresh token.
- `GET /auth/me`: Fetch currently authenticated user profile.
- `POST /auth/forgot-password`: Initiate password reset flow.
- `POST /auth/reset-password`: Reset password with token.

### Customer Account & Addresses (`/api/v1/users`)
- `GET /users/profile`: Get detailed profile.
- `PUT /users/profile`: Update profile info.
- `GET /users/addresses`: List saved addresses.
- `POST /users/addresses`: Add new address.
- `PUT /users/addresses/{id}`: Edit address.
- `DELETE /users/addresses/{id}`: Delete address.

### Catalog (`/api/v1/catalog`)
- `GET /catalog/categories`: List hierarchical category tree.
- `GET /catalog/brands`: List all brands.
- `GET /catalog/products`: Browse/Search/Filter products (Query: `q`, `category_id`, `brand_id`, `min_price`, `max_price`, `min_rating`, `sort_by`, `page`, `limit`).
- `GET /catalog/products/{slug}`: Fetch single product details with variants, attributes, images.
- `GET /catalog/featured`: Featured, best seller, and new products.

### Cart & Wishlist (`/api/v1/cart` & `/api/v1/wishlist`)
- `GET /cart`: Fetch active cart items and totals.
- `POST /cart/items`: Add variant to cart.
- `PUT /cart/items/{item_id}`: Update quantity.
- `DELETE /cart/items/{item_id}`: Remove item from cart.
- `DELETE /cart`: Clear cart.
- `GET /wishlist`: Fetch wishlist.
- `POST /wishlist/items`: Add product variant to wishlist.
- `DELETE /wishlist/items/{item_id}`: Remove item from wishlist.

### Checkout & Orders (`/api/v1/checkout` & `/api/v1/orders`)
- `POST /checkout/validate`: Validate cart, address, shipping method, and coupon code.
- `POST /checkout/process`: Execute checkout, process payment, reserve inventory, create order.
- `GET /orders`: List user order history.
- `GET /orders/{order_number}`: Get detailed order status and tracking.
- `POST /orders/{order_number}/cancel`: Request order cancellation.
- `POST /orders/{order_number}/return`: Request order return.

### Reviews & Ratings (`/api/v1/reviews`)
- `GET /reviews/product/{product_id}`: Fetch product reviews and summary rating stats.
- `POST /reviews`: Submit a product review (verifies purchase).

### Notifications (`/api/v1/notifications`)
- `GET /notifications`: Get user notifications.
- `PUT /notifications/{id}/read`: Mark notification as read.

### Admin Operations (`/api/v1/admin`)
- `GET /admin/dashboard/stats`: Get high-level KPI dashboard metrics.
- `GET /admin/analytics/sales`: Fetch daily/monthly sales data.
- `POST /admin/products`: Create catalog product.
- `PUT /admin/products/{id}`: Update catalog product.
- `POST /admin/categories`: Create category.
- `POST /admin/brands`: Create brand.
- `GET /admin/orders`: List all orders across platform.
- `PUT /admin/orders/{id}/status`: Update order status (Packing, Shipping, Delivery).
- `POST /admin/coupons`: Create promo coupon.
- `GET /admin/reviews/pending`: List reviews for moderation.
- `PUT /admin/reviews/{id}/moderation`: Approve or reject review.
- `GET /admin/audit-logs`: View system audit trail.
