# NovaMart REST API Specification & Endpoint Reference

Base URL: `/api/v1`  
Authentication: HTTP Bearer Token (`Authorization: Bearer <jwt_token>`) or `X-Session-ID` header for guest operations.

---

## 1. Authentication & Security

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `POST` | `/auth/register` | Register new customer account | No |
| `POST` | `/auth/login` | Password authentication returning access & refresh tokens | No |
| `POST` | `/auth/refresh` | Rotate access token using valid refresh token | No |
| `POST` | `/auth/logout` | Revoke active session token | Yes |
| `GET` | `/auth/me` | Retrieve authenticated user profile | Yes |
| `PUT` | `/auth/profile` | Update personal profile details | Yes |
| `POST` | `/auth/change-password` | Change user password with current verification | Yes |
| `POST` | `/auth/forgot-password` | Request password reset token via email | No |
| `POST` | `/auth/reset-password` | Reset password using one-time token | No |
| `GET` | `/auth/sessions` | List all active logged-in device sessions | Yes |
| `DELETE` | `/auth/sessions/{id}` | Revoke a specific device session | Yes |
| `DELETE` | `/auth/sessions/other/all` | Revoke all other sessions except current | Yes |

---

## 2. Catalog, Search & Recommendations

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/catalog/categories` | List all catalog categories | No |
| `GET` | `/catalog/categories/tree` | Retrieve nested multi-tier category tree | No |
| `GET` | `/catalog/brands` | List brands with `featured_only` filter | No |
| `GET` | `/catalog/attributes` | Fetch attribute definitions for a category | No |
| `GET` | `/catalog/products/{idOrSlug}` | Get detailed product specification card | No |
| `GET` | `/search` | Full-text search with filtering, facets, and sorting | No |
| `GET` | `/search/autocomplete` | Fast typeahead autocomplete suggestions | No |
| `GET` | `/search/trending` | List trending popular search terms | No |
| `GET` | `/search/history` | Get user search history | Yes |
| `DELETE` | `/search/history/{id}` | Remove a search history item | Yes |
| `DELETE` | `/search/history` | Clear entire search history | Yes |
| `GET` | `/discovery/recommended` | Personalized collaborative recommendation feed | No |
| `GET` | `/discovery/best-selling` | Top selling products feed | No |
| `GET` | `/discovery/deals` | Active discount deals feed | No |
| `GET` | `/discovery/new-arrivals` | Newly launched products feed | No |
| `GET` | `/discovery/recently-viewed` | User recently viewed products | No |
| `POST` | `/discovery/recently-viewed/{id}` | Record product view activity | No |
| `DELETE` | `/discovery/recently-viewed` | Clear recently viewed items | No |

---

## 3. Cart, Checkout & Orders

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/cart` | View current user / guest cart | No |
| `POST` | `/cart/items` | Add product variant to cart | No |
| `PUT` | `/cart/items/{id}` | Update quantity of cart line item | No |
| `DELETE` | `/cart/items/{id}` | Remove item from cart | No |
| `POST` | `/cart/items/{id}/move-to-wishlist` | Move line item to saved wishlist | Yes |
| `POST` | `/cart/merge` | Merge guest cart items into user account | Yes |
| `GET` | `/wishlist` | View saved wishlist items | Yes |
| `POST` | `/wishlist/items` | Add variant to wishlist | Yes |
| `DELETE` | `/wishlist/items/{id}` | Remove item from wishlist | Yes |
| `POST` | `/checkout/coupons/validate` | Verify coupon code eligibility | No |
| `POST` | `/checkout/preview` | Generate order financial preview & tax calculation | Yes |
| `POST` | `/checkout/process` | Place order with idempotent transaction locking | Yes |
| `GET` | `/orders` | List user order history | Yes |
| `GET` | `/orders/{orderNumber}` | Get complete order invoice & tracking snapshot | Yes |
| `POST` | `/orders/{orderNumber}/cancel` | Cancel order prior to dispatch | Yes |
| `POST` | `/orders/{orderNumber}/refund` | Request refund or item return | Yes |

---

## 4. Enterprise Domain APIs

| Method | Endpoint | Description | Auth Required |
| :--- | :--- | :--- | :--- |
| `GET` | `/logistics/serviceability/check` | Check 6-digit Indian PIN code SLA & COD eligibility | No |
| `GET` | `/loyalty/profile` | View SuperCoin balance, tier & coin ledger | Yes |
| `POST` | `/loyalty/redeem` | Burn SuperCoins for checkout order discount | Yes |
| `GET` | `/flash-sales/active` | List live and upcoming lightning flash sales | No |
| `POST` | `/flash-sales/{id}/reserve` | Reserve flash sale unit with atomic lock | Yes |
| `GET` | `/compare` | Side-by-side technical spec comparison matrix | No |
| `GET` | `/qa/products/{id}` | List verified questions & answers for PDP | No |
| `POST` | `/qa/products/{id}/questions` | Post a customer question | Yes |
| `POST` | `/qa/questions/{id}/answers` | Post an answer to a question | Yes |
| `POST` | `/qa/questions/{id}/upvote` | Upvote a helpful question | No |
| `GET` | `/seller/settlement/escrow` | View seller escrow balances & deductions | Seller |
| `POST` | `/seller/settlement/payout/request` | Submit NEFT/RTGS payout transfer request | Seller |
| `GET` | `/risk/scores/{orderId}` | View order multi-factor fraud risk score | Admin |
| `POST` | `/webhooks/subscriptions` | Register third-party outbound webhook endpoint | Admin |
| `GET` | `/telemetry/summary` | Prometheus telemetry operational metrics | Admin |
