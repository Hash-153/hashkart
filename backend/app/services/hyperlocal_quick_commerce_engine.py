"""
NovaMart QuickCommerce & Hyperlocal 15-Minute Dark Store Subsystem
==================================================================
Sub-hour order dispatch and micro-fulfillment center (MFC) management:
- Dark Store Geofence Polygon matching & Pin code serviceability
- Dynamic Rider Batching (consolidates multiple nearby deliveries on 1 rider trip)
- Surge pricing multiplier based on rainy weather, festival demand, and available rider capacity
- Live GPS telemetry estimation (Haversine ETA calculations)
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
import math
import uuid
from typing import Dict, List, Optional, Tuple


class DarkStoreStatus(str, Enum):
    OPERATIONAL = "OPERATIONAL"
    HIGH_CONGESTION = "HIGH_CONGESTION"
    RAIN_SURGE = "RAIN_SURGE"
    CLOSED = "CLOSED"


@dataclass
class DarkStoreFacility:
    dark_store_id: str
    store_name: str
    city: str
    pincode: str
    latitude: float
    longitude: float
    max_service_radius_km: float
    active_riders_count: int
    pending_orders_count: int
    status: DarkStoreStatus


@dataclass
class QuickCommerceDispatchPlan:
    dispatch_id: str
    dark_store_id: str
    assigned_rider_id: str
    order_numbers: List[str]
    total_stops: int
    estimated_trip_duration_minutes: int
    surge_fee_inr: Decimal
    is_15_minute_express_guaranteed: bool


class HyperlocalQuickCommerceEngine:
    DARK_STORES: List[DarkStoreFacility] = [
        DarkStoreFacility(dark_store_id="DS-BLR-KOR", store_name="Koramangala Dark Store 1", city="Bengaluru", pincode="560034", latitude=12.9352, longitude=77.6245, max_service_radius_km=3.5, active_riders_count=14, pending_orders_count=6, status=DarkStoreStatus.OPERATIONAL),
        DarkStoreFacility(dark_store_id="DS-BLR-IND", store_name="Indiranagar Dark Store 2", city="Bengaluru", pincode="560038", latitude=12.9719, longitude=77.6412, max_service_radius_km=4.0, active_riders_count=18, pending_orders_count=12, status=DarkStoreStatus.OPERATIONAL),
        DarkStoreFacility(dark_store_id="DS-MUM-BND", store_name="Bandra West Dark Store 1", city="Mumbai", pincode="400050", latitude=19.0596, longitude=72.8295, max_service_radius_km=3.0, active_riders_count=10, pending_orders_count=4, status=DarkStoreStatus.OPERATIONAL),
    ]

    @staticmethod
    def calculate_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Haversine distance in kilometers."""
        r_km = 6371.0
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = math.sin(dlat / 2.0)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2.0)**2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return round(r_km * c, 2)

    @classmethod
    def find_nearest_dark_store(
        cls,
        customer_lat: float,
        customer_lon: float,
    ) -> Optional[Tuple[DarkStoreFacility, float]]:
        """Identify closest operational micro-fulfillment center within service radius."""
        best_store = None
        min_dist = float("inf")

        for store in cls.DARK_STORES:
            if store.status == DarkStoreStatus.CLOSED:
                continue
            dist = cls.calculate_distance_km(customer_lat, customer_lon, store.latitude, store.longitude)
            if dist <= store.max_service_radius_km and dist < min_dist:
                min_dist = dist
                best_store = store

        if best_store:
            return best_store, min_dist
        return None

    @classmethod
    def calculate_surge_fee(
        cls,
        store: DarkStoreFacility,
        is_raining: bool = False,
    ) -> Decimal:
        """Compute surge fee when dark store rider capacity is constrained."""
        surge = Decimal("0.00")
        if is_raining:
            surge += Decimal("25.00") # Rain surge
        if store.active_riders_count > 0:
            load_factor = store.pending_orders_count / store.active_riders_count
            if load_factor > 1.5:
                surge += Decimal("15.00") # High demand surge
        return surge

    @classmethod
    def generate_rider_dispatch(
        cls,
        store_id: str,
        orders: List[Dict[str, Any]], # list of {order_number, lat, lon}
    ) -> QuickCommerceDispatchPlan:
        """Consolidate orders into an optimized 15-minute quick commerce delivery batch."""
        rider_id = f"RIDER-{uuid.uuid4().hex[:5].upper()}"
        dispatch_id = f"QC-{datetime.now().strftime('%Y%m%d%H%M')}-{uuid.uuid4().hex[:4].upper()}"

        return QuickCommerceDispatchPlan(
            dispatch_id=dispatch_id,
            dark_store_id=store_id,
            assigned_rider_id=rider_id,
            order_numbers=[o.get("order_number", "ORD") for o in orders],
            total_stops=len(orders),
            estimated_trip_duration_minutes=max(12, len(orders) * 6),
            surge_fee_inr=Decimal("0.00"),
            is_15_minute_express_guaranteed=len(orders) <= 2,
        )
