# HashKart — Production-Grade Indian E-Commerce Marketplace Platform

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/Hash-153/hashkart)
[![Repository Scale](https://img.shields.io/badge/Lines%20of%20Code-555K%2B-blue.svg)](https://github.com/Hash-153/hashkart)
[![Live Products](https://img.shields.io/badge/Catalog%20Products-1%2C200%2B-orange.svg)](https://github.com/Hash-153/hashkart)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI%20%7C%20Async%20SQLAlchemy-009688.svg)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/Frontend-React%2018%20%7C%20TypeScript%20%7C%20Vite-61DAFB.svg)](https://react.dev)

**HashKart** is a full-stack, enterprise-grade, high-performance Indian e-commerce marketplace platform inspired by Flipkart. Built with a modern React + TypeScript frontend, an asynchronous Python FastAPI backend, SQLAlchemy 2.0 ORM, and high-concurrency inventory protection.

---

## 🌟 Key Features

### 🛍️ Storefront & Interactive Experience
- **16 Curated Catalog Verticals**: 75+ products per category (1,200+ total active items) across Mobiles, Laptops, Audio, Smartwatches, Cameras, Men's & Women's Fashion, Footwear, Kitchenware, Furniture, Decor, Skincare, Grooming, TVs, Refrigerators, and Air Conditioners.
- **100% Real Product Photography**: High-definition, authentic product images matching exact specifications and brand models.
- **Modern UI & Micro-interactions**: Flipkart-style yellow-blue design system, 3D product card elevation on hover, logo glow, search bar highlight glow, and interactive wishlist heart pop animation.
- **Search & Filter Engine**: Full-text fuzzy keyword matching, trending search queries autocomplete, price sliders, brand filters, and star ratings.
- **Dynamic Routing & Policy Pages**: 4-column e-commerce footer linked to dynamic static info views (`/info/:pageKey`) with automatic scroll restoration (`ScrollToTop`).

### 🛒 Cart, Wishlist & Checkout
- **Persistent Cart & Guest Sessions**: Seamless shopping cart with real-time tax (18% GST) and delivery SLA estimation.
- **Guest & User Wishlists**: Instant toggle wishlist with toast notifications and persistent guest session storage.
- **Coupons & Promotions**: Dynamic discount engine supporting percentage & fixed vouchers (`WELCOME10`, `FESTIVE500`, `FLASH20`).
- **Pincode Logistics Matrix**: Real-time serviceability check across 3,500+ Indian postal hubs with courier partner allocations (Ekart, Delhivery, BlueDart).

### 🔒 Security, Orders & Operations
- **Enterprise Authentication**: JWT access and refresh token rotation, bcrypt password hashing, and role-based access control (`CUSTOMER`, `STAFF`, `ADMIN`).
- **Inventory Concurrency Protection**: Multi-warehouse stock tracking with atomic row reservation locks (`SELECT FOR UPDATE`).
- **Order Lifecycle & Invoicing**: State machine from order placement to delivery with automated GST-compliant tax invoices.
- **Seller & Admin Operations Portal**: Real-time KPI analytics dashboards, revenue metrics, and inventory editors.

---

## 🏗️ Architecture & Tech Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend** | React 18, TypeScript, Vite, CSS Design System (Custom Tokens), Lucide Icons |
| **Backend** | Python 3.11+, FastAPI, SQLAlchemy 2.0 (Async), Pydantic v2, Uvicorn |
| **Database** | SQLite (Fast Local Async) / PostgreSQL / Redis |
| **Data Scale** | 555,000+ Lines of Code across 364 files, 1,200 Catalog SKUs, 3,500 Orders |
| **Testing** | Pytest (Backend API & ORM suite), TypeScript typecheck |
| **DevOps** | Docker, Docker Compose, GitHub Actions CI/CD |

---

## 📁 Repository Directory Structure

```text
hashkart/
├── backend/
│   ├── app/
│   │   ├── api/v1/endpoints/   # Modular API routes (auth, catalog, cart, wishlist, orders, admin)
│   │   ├── core/               # Security, JWT tokens, config & lifespan
│   │   ├── fixtures/           # Master Enterprise JSON datasets (5.55L+ LOC)
│   │   ├── models/             # SQLAlchemy 2.0 declarative ORM models
│   │   ├── schemas/            # Pydantic v2 validation & response schemas
│   │   └── services/           # Business logic & payment simulators
│   └── tests/                  # Pytest test suite
├── frontend/
│   ├── src/
│   │   ├── components/         # Reusable UI components (Header, Footer, ProductCard, FilterSidebar)
│   │   ├── pages/              # Views (Home, ProductListing, ProductDetail, Cart, Wishlist, Admin)
│   │   ├── services/           # Axios API client & backend connection
│   │   └── index.css           # Design tokens, hover effects & responsive layout
│   └── package.json            # Vite + React dependencies
├── scripts/                    # Catalog generators, database seeders & PR automators
└── README.md                   # Project documentation
```

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.11+
- Node.js 18+ and npm

---

### 1. Start the Backend API Server

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server with auto-reload
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
- **Backend API**: `http://127.0.0.1:8000`
- **Swagger Interactive Docs**: `http://127.0.0.1:8000/docs`

---

### 2. Start the Frontend Storefront

```bash
# Navigate to frontend directory
cd frontend

# Install node dependencies
npm install

# Start Vite dev server
npm run dev -- --host 127.0.0.1 --port 5173
```
- **Frontend Storefront**: `http://127.0.0.1:5173/`

---

### 3. Seed Database & Master Catalog

To seed the database with 1,200 products across all 16 categories with verified real photography:

```bash
python scripts/verify_and_update_real_product_images.py
```

---

## 🧪 Verification & Quality Checks

```bash
# Frontend Typecheck
cd frontend
npm run typecheck

# Backend API Tests
cd ../backend
pytest
```

---

## 📄 License & Attribution

Developed for **HashKart Marketplace Platform** ([GitHub Repo](https://github.com/Hash-153/hashkart)).
All rights reserved.
