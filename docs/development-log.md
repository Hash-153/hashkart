# Engineering Development Log — HashKart

This document records key implementation decisions, design trade-offs, refactoring, and testing results throughout the development lifecycle of HashKart.

---

## Log Entry: Phase 1 — Foundation Setup
- **Date**: 2026-08-25
- **Feature**: Initial Architecture & Foundation Infrastructure
- **Implementation Decisions**:
  - Selected FastAPI with Async SQLAlchemy 2.0 and Asyncpg for high-throughput asynchronous request handling.
  - Implemented dual database configuration (PostgreSQL for containerized production/development and Async SQLite for fast unit testing).
  - Selected React 18 with TypeScript and Vite for the frontend, incorporating a custom design token system styled in vanilla CSS variables to achieve a rich, modern Flipkart-inspired visual aesthetic without external component library overhead.
  - Enforced zero GPL dependencies in `docs/dependency-policy.md`.
- **Testing Performed**:
  - Created initial Pytest configuration and verified app startup routines.

---

## Log Entry: Phase 2 — Deep Authentication, Authorization, User Account Management & Security
- **Date**: 2026-08-25
- **Feature**: Deep Auth & RBAC Security Engine
- **Implementation Decisions**:
  - Implemented JWT token rotation with JTI revocation tracking and refresh token blacklisting.
  - Implemented account lockout after 5 consecutive failed login attempts.
  - Added Address Book CRUD, Password Reset simulation flow, and Security Audit Logging.
- **Testing Performed**:
  - Built `test_auth_phase2.py` and `test_addresses_crud.py`. Pass rate 100%.

---

## Log Entry: Phase 3 — Advanced Product Catalog & Product Management
- **Date**: 2026-08-25
- **Feature**: Rebranding to HashKart & Advanced Catalog Management
- **Implementation Decisions**:
  - Rebranded application to **HashKart**.
  - Built Category tree with circular parent prevention, Attribute definitions/values, and Pricing calculation service.
  - Built Admin catalog management portal for creating categories, brands, products, and variants.
  - Expanded database seeder script to generate 15+ categories, 20+ brands, 100+ products, and 250+ variants.
- **Testing Performed**:
  - Built catalog test suite (`test_category_tree.py`, `test_product_search_filter.py`, `test_pricing_service.py`). Pass rate 100%.

---

## Log Entry: Phase 4 — Advanced Search, Discovery, Filtering, Sorting & Recommendations
- **Date**: 2026-08-25
- **Feature**: In-Application Search Engine, Dynamic Facets, Autocomplete & Recommendations
- **Implementation Decisions**:
  - Built `SearchService` with query normalization, tokenization, plural stemming, Levenshtein distance typo tolerance ("Did You Mean?"), and weighted match explanations (`SKU_MATCH`, `NAME_EXACT`, `NAME_PREFIX`, `BRAND_MATCH`, `CATEGORY_MATCH`, `ATTRIBUTE_MATCH`, `DESCRIPTION_MATCH`).
  - Built `AutocompleteService` for non-blocking prefix suggestions.
  - Built `FacetService` for calculating category, brand, price min/max, rating distribution, and dynamic attribute facet counts.
  - Built `RecommendationService` & `RecentlyViewedService` for personalized "Recommended For You", best-selling products, top deals, new arrivals, and customer recently viewed tracking.
  - Built frontend components: `SearchBar`, `FilterChips`, `DiscoverySection`, and `RecentlyViewed`. Preserved URL query state in `ProductListing.tsx`.
- **Testing Performed**:
  - Built search & discovery test suites (`test_search_advanced.py`, `test_autocomplete_typo.py`, `test_search_history_privacy.py`, `test_discovery_recommendations.py`).
  - Empirical verification: **28 / 28 Pytest backend tests passed (100% pass rate)**. `npm run build` completed with **0 TypeScript errors**.
