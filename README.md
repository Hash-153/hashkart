# NovaMart — Production-Grade Indian E-Commerce Marketplace Platform

NovaMart is a full-stack, original, high-performance Indian e-commerce marketplace platform built with React, TypeScript, FastAPI, SQLAlchemy 2.0, PostgreSQL, and Uvicorn.

---

## Key Features

- **Storefront & Catalog**: Multi-level categories, brand filtering, variants (size, color, storage, model), interactive search with suggestions, multi-attribute filter sidebar, price sliders, sorting, pagination.
- **Cart & Wishlist**: Persistent cart with stock validation, shipping & tax calculations, real-time total updates, one-click wishlist to cart.
- **Authentication & RBAC**: Secure JWT auth (Access & Refresh tokens), password hashing (Argon2/Bcrypt), role-based permissions (`CUSTOMER`, `STAFF`, `ADMIN`).
- **Checkout & Address Management**: Multi-step checkout pipeline, address validation, coupon verification, order summary calculation.
- **Mock Payment Gateway**: Deterministic payment simulator supporting Mock Card, UPI, NetBanking, Wallets, and Cash on Delivery (COD).
- **Order Management System**: Full order lifecycle status machine (`PENDING` -> `CONFIRMED` -> `PACKED` -> `SHIPPED` -> `DELIVERED`, cancellation, returns, refunds).
- **Inventory & Race Protection**: Stock reservation engine with database row locking (`SELECT FOR UPDATE`), inventory movement history, low stock triggers.
- **Reviews & Moderation**: Verified buyer ratings, detailed reviews, admin moderation approval workflow.
- **Coupons & Discount Engine**: Percentage & fixed discounts, min cart value, usage limits, expiration validation.
- **Admin Operations Dashboard**: Full CRUD for Catalog, Brands, Categories, Customers, Orders, Inventory, Coupons, and Moderation.
- **Analytics & Reporting**: Local DB-driven charts & key performance indicators (sales, revenue, top products, AOV).
- **In-App Notifications**: Real-time order status updates, coupon alerts, price drop notifications.
- **Audit Logging**: Comprehensive admin and sensitive action audit trail.
- **Seller Marketplace Operations**: Seller onboarding, approval, catalog listings, and seller-scoped inventory offers.
- **Fulfillment & Returns**: Shipment event timelines and item-level return requests with controlled state transitions.
- **Platform Infrastructure**: Alembic migrations, optional Redis caching, lifecycle-managed background jobs, metrics, and CI.

---

## Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend** | React 18, TypeScript, Vite, Modern CSS (Design Tokens), Lucide Icons |
| **Backend** | Python 3.11+, FastAPI, SQLAlchemy 2.0 (Async), Pydantic v2, Uvicorn |
| **Database** | PostgreSQL / SQLite (for fast local dev/tests) |
| **Testing** | Pytest (Backend), Vitest (Frontend) |
| **Containerization** | Docker, Docker Compose |

---

## Directory Architecture

```
.
├── backend/            # FastAPI Python backend application
│   ├── app/            # Application logic (models, schemas, routers, services)
│   ├── tests/          # Pytest backend test suite
│   ├── pyproject.toml  # Python project & tool dependencies
│   └── requirements.txt# Backend requirements
├── frontend/           # React TypeScript frontend application
│   ├── src/            # Components, pages, services, styles, assets
│   ├── package.json    # Frontend npm dependencies
│   └── vite.config.ts  # Vite build configuration
├── database/           # Schema migrations and seed scripts
├── docs/               # Technical documentation suite
│   ├── architecture.md
│   ├── database.md
│   ├── security.md
│   ├── testing.md
│   ├── development-log.md
│   ├── dependency-policy.md
│   └── api.md
├── docker/             # Docker configurations
├── scripts/            # Database seeder & synthetic data scripts
├── docker-compose.yml  # Container orchestration
├── .env.example        # Environment variable templates
└── README.md           # Master documentation
```

---

## Quick Start

### 1. Local Setup without Docker

#### Backend
```bash
cd backend
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Backend API will be available at `http://localhost:8000`. OpenAPI interactive docs at `http://localhost:8000/docs`.

#### Frontend
```bash
cd frontend
npm install
npm run dev
```
Frontend application will be available at `http://localhost:5173`.

### 2. Docker Compose Setup

```bash
copy .env.example .env
# Edit .env and replace all placeholder credentials before deployment.
docker-compose up --build
```

For production deployments, set `APP_ENV=production`, keep `DEBUG=false`, provide a
unique JWT secret of at least 32 characters, and restrict `CORS_ORIGINS` and
`TRUSTED_HOSTS` to the real application domains. The backend exposes `/health` for
liveness and `/ready` for database readiness checks. The Compose stack runs the API
without source mounts or hot reload and includes container healthchecks.
Set `AUTO_CREATE_SCHEMA=false` in production; the container runs `alembic upgrade head`
before starting the API. Local development can keep it enabled for convenience.

### Quality Checks

```bash
cd backend
python -m pytest
cd ../frontend
npm run test
npm run typecheck
npm run build
```

Every push and pull request runs these checks through GitHub Actions in
`.github/workflows/ci.yml`.

### Marketplace Operations

Seller onboarding is intentionally separate from account registration. A customer
submits `/api/v1/seller/onboarding`, an administrator approves the profile, and only
approved sellers can create listings. Customer returns are submitted through
`/api/v1/orders/returns`; staff review them through the fulfillment administration
routes. Seller and return state transitions are validated in service code so route
handlers cannot bypass ownership or terminal-state rules.

### Operations API Surface

- Seller analytics: `GET /api/v1/seller/analytics/dashboard`
- Payment webhooks: `POST /api/v1/payments/webhooks/{provider}`
- Payment reconciliation: `GET|POST /api/v1/payments/reconciliation`
- Customer support: `GET|POST /api/v1/support/tickets`
- Warehouse receiving: `GET /api/v1/admin/warehouse/receipts` and `POST /api/v1/admin/warehouse/inspections`
- Pick and pack: `GET|PATCH /api/v1/admin/fulfillment/tasks`
- Shipment dispatch and events: `/api/v1/admin/fulfillment/shipments`

External email, SMS, carrier, and payment providers are isolated behind async
provider interfaces. The default adapters are deterministic logging/mock adapters
for local development; production deployments should supply verified provider
implementations and secrets through environment variables.

---

## Running Tests

### Backend Tests
```bash
cd backend
pytest
```

---

## Documentation

Full architectural specifications, database schemas, security details, and API documentation are available in the [`docs/`](file:///c:/flipkart%20clone/docs) directory.
