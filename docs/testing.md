# Automated Testing Strategy

## Overview

NovaMart utilizes automated testing across all layers to ensure zero-regression releases and verify edge cases.

---

## Test Execution Matrix

### Backend Automated Tests
- **Framework**: Pytest + Pytest-Asyncio + Async HTTPX Client.
- **Database**: Async SQLite in-memory database fixture matching PostgreSQL behavior.
- **Coverage Targets**:
  - Authentication (Registration, Duplicate Email, Password Hashing, JWT Validation)
  - Authorization (RBAC permissions for Customer vs Admin routes)
  - Catalog (Product filtering, category lookups, search engine)
  - Cart & Wishlist (Adding/removing items, price snapshot recalculation)
  - Checkout & Pricing (Discount calculation, coupon limits, tax math)
  - Inventory Race Conditions (Simulated concurrent order reservations)
  - Payment Simulation (Deterministic success, card failure, UPI timeout)
  - Orders (Order state machine status transitions)

---

## Execution Commands

### Running Backend Tests
```bash
cd backend
pytest -v --tb=short
```

---

## Synthetic Test Fixtures

Test fixtures populate isolated in-memory test databases with synthetic customers, catalog items, categories, coupons, and orders, guaranteeing test repeatability without touching production data.
