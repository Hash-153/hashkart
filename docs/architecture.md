# NovaMart Enterprise Marketplace Architecture & Engineering Design

NovaMart is an enterprise-grade multi-tenant e-commerce marketplace built to emulate the scale, resiliency, and performance of leading hyperscale marketplaces (such as Flipkart). This document details the end-to-end architecture, domain partitioning, distributed transaction boundaries, caching hierarchy, and fault-tolerance patterns.

---

## 1. High-Level Architecture Overview

NovaMart follows a modular distributed microservices-style monolithic architecture deployed on Kubernetes (Amazon EKS / Google GKE) with multi-AZ Aurora PostgreSQL, Valkey / ElastiCache Redis clustering, and asynchronous Celery worker pools.

```mermaid
graph TD
    Client[Web & Mobile Clients] --> CloudFront[Amazon CloudFront CDN / Cloudflare]
    CloudFront --> WAF[AWS WAFv2 Layer 7 Firewall]
    WAF --> ALB[Application Load Balancer / Nginx Ingress]
    
    subgraph Kubernetes_Cluster["Kubernetes Cluster (EKS Multi-AZ)"]
        ALB --> ReactUI[Frontend React + Vite Pods]
        ALB --> FastAPIPods[FastAPI Backend Pods (8 - 48 HPA)]
        
        FastAPIPods --> RateLimiter[Sliding-Window Token Bucket]
        FastAPIPods --> Telemetry[Prometheus Metrics Exporter]
        
        FastAPIPods --> CatalogService[Catalog & Search Subsystem]
        FastAPIPods --> OrderService[Order & Checkout Engine]
        FastAPIPods --> SettlementService[Seller Escrow & Settlement]
        FastAPIPods --> LogisticsEngine[Pincode & 3PL Logistics]
        FastAPIPods --> LoyaltyService[SuperCoins & Plus Membership]
        FastAPIPods --> RiskEngine[Fraud & COD Risk Engine]
        FastAPIPods --> WebhookDispatcher[HMAC Webhook Dispatcher]
        
        CeleryWorker[Celery Async Workers] --> FastAPIPods
        CeleryBeat[Celery Cron Scheduler] --> CeleryWorker
    end

    subgraph Data_Tier["Distributed Data Tier"]
        FastAPIPods --> AuroraMaster[(Aurora PostgreSQL Primary)]
        FastAPIPods --> AuroraReplicas[(Aurora Read Replicas x3)]
        FastAPIPods --> RedisCluster[(ElastiCache Redis Multi-Shard)]
    end
```

---

## 2. Core Domain Services & Responsibilities

### 2.1 Order & Checkout Engine (`app.services.checkout_service`)
- **Pessimistic Inventory Locking**: Uses `SELECT ... FOR UPDATE` on `ProductVariant` during final order commit to prevent race conditions during flash sales.
- **Idempotent Order Placement**: Enforces `X-Idempotency-Key` headers on `/checkout/process` with Redis TTL-based distributed locks to prevent duplicate credit card or bank debits.
- **Financial Ledger Snapshotting**: Stores immutable snapshots of product price, taxes, coupon discounts, shipping fees, and addresses on `OrderItem` at transaction time.

### 2.2 Seller Escrow & Settlement Engine (`app.services.settlement_service`)
- **Escrow Hold Lifecycle**: When an order is placed and delivered, funds are routed into a dedicated `SellerEscrowAccount` in `HELD` status.
- **Return Period Clearance**: After the 7-day customer return window elapses without return requests, funds automatically transition to `AVAILABLE` balance.
- **Automated Tax & Commission Withholding**:
  - Marketplace Commission (typically 5% - 15% per category tier)
  - 18% GST on Marketplace Commission
  - 1% Tax Collected at Source (TCS) under Section 52 of the CGST Act
  - 0.1% / 1% TDS under Section 194-O of the Income Tax Act
- **NEFT/RTGS Batch Payout Generator**: Groups cleared seller balances into ISO-20022 and NACHA-compatible batch transfer files.

### 2.3 Logistics & Delivery SLA Engine (`app.services.logistics_engine`)
- **Pincode Geo-Matrix**: Maintains a 6-digit Indian postal code matrix mapping serviceability, Cash-on-Delivery (COD) eligibility, and carrier zone classification (Metro, Tier-1, Tier-2, North-East, Remote).
- **3PL Carrier Routing**: Automatically allocates shipments between Ekart, Delhivery, BlueDart, and Ecom Express based on past delivery performance SLAs and cost efficiency.
- **Dispatch Manifests**: Generates standardized barcoded manifests for daily warehouse driver handover.
- **Non-Delivery Report (NDR) Management**: Tracks failed delivery attempts, automated customer IVR/WhatsApp confirmation, and Re-attempt scheduling.

### 2.4 SuperCoins & Loyalty Program (`app.services.loyalty_service`)
- **Flipkart Plus Tier Management**: Plus members earn 4 SuperCoins per ₹100 spent (capped at 100 per order) with 2-hour early access to flash sales. Regular customers earn 2 SuperCoins per ₹100 (capped at 50).
- **Coin Redemption & Burning**: 1 SuperCoin = ₹1.00 direct checkout discount or exchangeable in the Reward Store for OTT subscriptions, dining vouchers, and travel discounts.

### 2.5 Risk & Fraud Engine (`app.services.risk_engine`)
- **Multi-Factor Fraud Evaluation**:
  - IP and device fingerprint velocity checks (e.g. >3 orders placed in 2 minutes)
  - Disposable temporary email domain detection
  - Address sanitization & pincode blacklist matching
  - High-value COD thresholds (>₹25,000 requiring OTP verification or prepaid conversion)
- **Automatic Gating**: Automatically locks high-risk orders in `HELD_FOR_REVIEW` status and flags them on the Admin Security Console.

### 2.6 Webhook & Event Dispatcher (`app.services.webhook_dispatcher`)
- **HMAC-SHA256 Signatures**: Secures outbound webhooks to third-party ERPs and seller systems with timestamped cryptographic hashes in `X-NovaMart-Signature`.
- **Exponential Backoff Retries**: Retries failed delivery attempts at 1m, 5m, 15m, 1h, 6h intervals.
- **Dead-Letter Queue (DLQ)**: Permanently unresolvable events are stored in the DLQ for operator inspection.

---

## 3. Caching & Performance Architecture

| Data Layer | Cache Technology | TTL | Invalidation Strategy |
| :--- | :--- | :--- | :--- |
| Category Tree & Brands | Redis Memory | 24 Hours | Event-driven on Admin catalog edit |
| Product Details & Specs | Redis Memory | 1 Hour | Write-through on SKU price/stock update |
| Pincode Serviceability | Redis Hash | 7 Days | Cache-aside on logistics matrix change |
| User Session & Auth | Redis String | 14 Days | Explicit revocation on Logout/Password Reset |
| Rate Limit Counters | Redis Token Bucket | 60 Seconds | Rolling sliding-window eviction |

---

## 4. Resilience & Fault Tolerance

1. **Database Failover**: Aurora PostgreSQL provides multi-AZ automated failover within <30 seconds without data loss.
2. **Circuit Breakers**: External payment gateways (Razorpay, PayU) and SMS gateways (Twilio, Gupshup) are wrapped with resilience circuit breakers to prevent thread exhaustion.
3. **Graceful Degradation**: If Redis is temporarily unavailable, read queries automatically fall back directly to Aurora PostgreSQL read replicas.
