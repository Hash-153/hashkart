"""
Locust Performance & Distributed Stress Testing Suite for NovaMart
===================================================================
Simulates high-concurrency e-commerce user behavior:
1. Product Discovery & Full-Text Search Queries
2. Product Detail Page (PDP) views with Q&A and Specification fetching
3. Pincode Serviceability & Delivery SLA checks
4. Flash Sale Lightning Deal reservation attempts
5. Add to Cart, Coupon validation, and Idempotent Checkout transactions
"""

import json
import random
from locust import HttpUser, task, between, tag


INDIAN_PINCODES = ["560001", "110001", "400001", "500001", "600001", "700001", "411001", "380001"]
SEARCH_QUERIES = ["iphone 15", "samsung galaxy s24", "sony headphones", "dell laptop", "oled tv", "running shoes"]


class ShopperBehavior(HttpUser):
    wait_time = between(1, 4)

    def on_start(self):
        """Simulate user login or guest session initialization."""
        self.session_id = f"locust_sess_{random.randint(100000, 999999)}"
        self.headers = {
            "Content-Type": "application/json",
            "X-Session-ID": self.session_id,
        }

    @tag("browse")
    @task(5)
    def browse_homepage_and_discovery(self):
        """Browse landing page discovery feeds and recommendation widgets."""
        self.client.get("/api/v1/discovery/recommended", headers=self.headers, name="Discovery - Recommended")
        self.client.get("/api/v1/discovery/deals", headers=self.headers, name="Discovery - Flash Deals")

    @tag("search")
    @task(4)
    def search_catalog(self):
        """Execute full-text multi-facet search queries."""
        q = random.choice(SEARCH_QUERIES)
        self.client.get(f"/api/v1/search?q={q}", headers=self.headers, name="Search - FullText Query")
        self.client.get(f"/api/v1/search/autocomplete?q={q[:3]}", headers=self.headers, name="Search - Autocomplete")

    @tag("pdp")
    @task(3)
    def view_product_detail(self):
        """View product details, technical specs and Q&A."""
        p_id = random.randint(1, 10)
        self.client.get(f"/api/v1/catalog/products/{p_id}", headers=self.headers, name="PDP - Product View")
        self.client.get(f"/api/v1/qa/products/{p_id}", headers=self.headers, name="PDP - QA List")

    @tag("logistics")
    @task(2)
    def check_pincode_serviceability(self):
        """Check delivery SLA for Indian pincodes."""
        pin = random.choice(INDIAN_PINCODES)
        self.client.get(
            f"/api/v1/logistics/serviceability/check?pincode={pin}&cart_total=24999",
            headers=self.headers,
            name="Logistics - Pincode SLA Check"
        )

    @tag("flash_sale")
    @task(2)
    def attempt_flash_sale_claim(self):
        """High-concurrency flash sale inventory reservation."""
        self.client.get("/api/v1/flash-sales/active", headers=self.headers, name="FlashSale - Active Events")
        self.client.post(
            "/api/v1/flash-sales/1/reserve?product_id=1&quantity=1",
            headers=self.headers,
            name="FlashSale - Reserve Deal"
        )

    @tag("cart_checkout")
    @task(1)
    def cart_and_checkout_flow(self):
        """Add product to cart and simulate preview."""
        v_id = random.randint(1, 5)
        self.client.post(
            "/api/v1/cart/items",
            headers=self.headers,
            json={"variant_id": v_id, "quantity": 1},
            name="Cart - Add Item"
        )
        self.client.get("/api/v1/cart", headers=self.headers, name="Cart - View Cart")
