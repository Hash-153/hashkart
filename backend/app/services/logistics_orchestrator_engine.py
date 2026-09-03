"""
NovaMart Hyperscale Logistics Orchestration & 3PL Carrier Routing Engine
========================================================================
Comprehensive supply-chain and transportation management:
- Multi-Carrier Rate Card Engine (Surface, Air Express, Volumetric Weight, Fuel Surcharge, COD collection fee)
- Hub-and-Spoke Transport Graph (Source FC -> Sort Center -> Mother Hub -> Delivery Hub -> Final Mile)
- Real-time Non-Delivery Report (NDR) Management (Automated Customer WhatsApp / IVR confirmation, Address correction)
- Dynamic Return-to-Origin (RTO) Prediction Score based on Buyer History and Pin Code defect rate
- Secure Geofenced Delivery Verification (Customer OTP challenge & GPS radius check)
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
import math
import random
from typing import Any, Dict, List, Optional, Tuple


class LogisticsCarrier(str, Enum):
    EKART = "EKART"
    DELHIVERY = "DELHIVERY"
    BLUEDART = "BLUEDART"
    ECOM_EXPRESS = "ECOM_EXPRESS"
    SHADOWFAX = "SHADOWFAX"


class ShippingMode(str, Enum):
    STANDARD_SURFACE = "STANDARD_SURFACE"
    AIR_EXPRESS = "AIR_EXPRESS"
    SAME_DAY_HYPERLOCAL = "SAME_DAY_HYPERLOCAL"
    HEAVY_BULK_CARGO = "HEAVY_BULK_CARGO"


class NDRReasonCode(str, Enum):
    CUSTOMER_UNAVAILABLE = "CUSTOMER_UNAVAILABLE"
    INCORRECT_ADDRESS = "INCORRECT_ADDRESS"
    CUSTOMER_REFUSED_DELIVERY = "CUSTOMER_REFUSED_DELIVERY"
    COD_CASH_NOT_READY = "COD_CASH_NOT_READY"
    DOOR_STEP_QC_FAILED = "DOOR_STEP_QC_FAILED"
    DELIVERY_AREA_RESTRICTED = "DELIVERY_AREA_RESTRICTED"


@dataclass
class PackageDimensions:
    length_cm: float
    width_cm: float
    height_cm: float
    dead_weight_kg: float

    @property
    def volumetric_weight_kg(self) -> float:
        """Calculate volumetric weight using industry standard 5000 divisor."""
        return (self.length_cm * self.width_cm * self.height_cm) / 5000.0

    @property
    def chargeable_weight_kg(self) -> float:
        """Chargeable weight is maximum of dead weight and volumetric weight."""
        return max(self.dead_weight_kg, self.volumetric_weight_kg)


@dataclass
class CarrierShippingRateQuote:
    carrier: LogisticsCarrier
    shipping_mode: ShippingMode
    chargeable_weight_kg: float
    base_freight_charge: Decimal
    fuel_surcharge: Decimal
    cod_collection_fee: Decimal
    gst_on_freight: Decimal
    total_shipping_cost: Decimal
    estimated_transit_hours: int
    promised_delivery_date: datetime


@dataclass
class NDRIncidentRecord:
    ndr_id: str
    waybill_number: str
    order_number: str
    carrier: LogisticsCarrier
    attempt_number: int # 1, 2, 3
    reason_code: NDRReasonCode
    recorded_at: datetime
    customer_response: Optional[str] = None # 'RESCHEDULE', 'CANCEL', 'UPDATED_ADDRESS'
    rescheduled_delivery_date: Optional[datetime] = None
    action_taken: str = "PENDING_CUSTOMER_ACTION"


@dataclass
class DeliveryOTPVerificationResult:
    is_verified: bool
    waybill_number: str
    carrier: LogisticsCarrier
    delivery_timestamp: datetime
    delivered_latitude: float
    delivered_longitude: float
    distance_to_customer_address_meters: float
    is_within_geofence: bool
    status_message: str


class LogisticsOrchestrator:
    # Base Freight Rates per 500g slab across Indian Delivery Zones (Zone A: Local, Zone B: Regional, Zone C: Metro-Metro, Zone D: National, Zone E: North East & Special)
    ZONE_RATES: Dict[str, Dict[LogisticsCarrier, Decimal]] = {
        "LOCAL": {LogisticsCarrier.EKART: Decimal("35.00"), LogisticsCarrier.DELHIVERY: Decimal("38.00"), LogisticsCarrier.BLUEDART: Decimal("55.00")},
        "REGIONAL": {LogisticsCarrier.EKART: Decimal("45.00"), LogisticsCarrier.DELHIVERY: Decimal("48.00"), LogisticsCarrier.BLUEDART: Decimal("68.00")},
        "METRO_METRO": {LogisticsCarrier.EKART: Decimal("52.00"), LogisticsCarrier.DELHIVERY: Decimal("54.00"), LogisticsCarrier.BLUEDART: Decimal("75.00")},
        "NATIONAL": {LogisticsCarrier.EKART: Decimal("65.00"), LogisticsCarrier.DELHIVERY: Decimal("68.00"), LogisticsCarrier.BLUEDART: Decimal("92.00")},
        "SPECIAL": {LogisticsCarrier.EKART: Decimal("85.00"), LogisticsCarrier.DELHIVERY: Decimal("90.00"), LogisticsCarrier.BLUEDART: Decimal("125.00")},
    }

    @classmethod
    def calculate_carrier_rates(
        cls,
        origin_pincode: str,
        destination_pincode: str,
        package: PackageDimensions,
        is_cod: bool = False,
        order_value: Decimal = Decimal("1000.00"),
    ) -> List[CarrierShippingRateQuote]:
        """Compute shipping freight quotes across 3PL carriers."""
        # Determine Delivery Zone
        zone_type = "NATIONAL"
        if origin_pincode == destination_pincode:
            zone_type = "LOCAL"
        elif origin_pincode[:2] == destination_pincode[:2]:
            zone_type = "REGIONAL"
        elif destination_pincode.startswith("7") or destination_pincode.startswith("19"):
            zone_type = "SPECIAL"

        ch_weight = package.chargeable_weight_kg
        slabs_500g = math.ceil(ch_weight / 0.5)

        quotes: List[CarrierShippingRateQuote] = []
        now = datetime.now(timezone.utc)

        for carrier, base_slab in cls.ZONE_RATES.get(zone_type, {}).items():
            base_freight = base_slab * Decimal(str(slabs_500g))
            fuel_surcharge = (base_freight * Decimal("0.12")).quantize(Decimal("0.01")) # 12% fuel index

            # COD handling fee (₹30 or 1.5% of order value, whichever is higher)
            cod_fee = Decimal("0.00")
            if is_cod:
                cod_fee = max(Decimal("30.00"), (order_value * Decimal("0.015")).quantize(Decimal("0.01")))

            subtotal_freight = base_freight + fuel_surcharge + cod_fee
            gst_freight = (subtotal_freight * Decimal("0.18")).quantize(Decimal("0.01")) # 18% GST on Logistics
            total_cost = subtotal_freight + gst_freight

            transit_hrs = 24 if zone_type == "LOCAL" else (48 if zone_type == "REGIONAL" else 72)
            if carrier == LogisticsCarrier.BLUEDART:
                transit_hrs = max(24, transit_hrs - 24) # Air express speed advantage

            delivery_dt = datetime.fromtimestamp(now.timestamp() + (transit_hrs * 3600), tz=timezone.utc)

            quotes.append(
                CarrierShippingRateQuote(
                    carrier=carrier,
                    shipping_mode=ShippingMode.AIR_EXPRESS if carrier == LogisticsCarrier.BLUEDART else ShippingMode.STANDARD_SURFACE,
                    chargeable_weight_kg=round(ch_weight, 2),
                    base_freight_charge=base_freight,
                    fuel_surcharge=fuel_surcharge,
                    cod_collection_fee=cod_fee,
                    gst_on_freight=gst_freight,
                    total_shipping_cost=total_cost,
                    estimated_transit_hours=transit_hrs,
                    promised_delivery_date=delivery_dt,
                )
            )

        quotes.sort(key=lambda q: q.total_shipping_cost)
        return quotes

    @staticmethod
    def calculate_rto_risk_score(
        buyer_past_cancellations: int,
        buyer_past_returns: int,
        buyer_total_orders: int,
        is_cod_payment: bool,
        destination_tier: str, # 'METRO', 'TIER_1', 'TIER_2', 'TIER_3'
    ) -> float:
        """Predict probability of Return-To-Origin (RTO) on a scale of 0.0 to 1.0."""
        base_risk = 0.05

        if is_cod_payment:
            base_risk += 0.15

        if destination_tier in ("TIER_2", "TIER_3"):
            base_risk += 0.08

        if buyer_total_orders > 0:
            defect_rate = (buyer_past_cancellations + buyer_past_returns) / buyer_total_orders
            base_risk += defect_rate * 0.40
        else:
            # First-time buyer COD risk
            if is_cod_payment:
                base_risk += 0.10

        return round(min(0.95, base_risk), 3)

    @staticmethod
    def verify_delivery_geofenced_otp(
        waybill_number: str,
        carrier: LogisticsCarrier,
        entered_otp: str,
        expected_otp: str,
        driver_lat: float,
        driver_lon: float,
        customer_address_lat: float,
        customer_address_lon: float,
        max_geofence_meters: float = 300.0,
    ) -> DeliveryOTPVerificationResult:
        """Validate 6-digit delivery OTP and GPS proximity to the delivery address."""
        now = datetime.now(timezone.utc)

        # Haversine distance formula
        r_earth = 6371000.0 # meters
        phi1 = math.radians(driver_lat)
        phi2 = math.radians(customer_address_lat)
        dphi = math.radians(customer_address_lat - driver_lat)
        dlambda = math.radians(customer_address_lon - driver_lon)

        a = math.sin(dphi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0)**2
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        distance_meters = round(r_earth * c, 1)

        is_geofence_ok = distance_meters <= max_geofence_meters
        is_otp_ok = entered_otp == expected_otp

        if not is_otp_ok:
            msg = "Delivery OTP mismatch. Please ask customer for correct 6-digit OTP."
            success = False
        elif not is_geofence_ok:
            msg = f"Delivery scanned outside geofence boundary ({distance_meters}m away from customer address)."
            success = True # Allowed with audit warning
        else:
            msg = f"Delivery confirmed via OTP within {distance_meters}m of customer address."
            success = True

        return DeliveryOTPVerificationResult(
            is_verified=success and is_otp_ok,
            waybill_number=waybill_number,
            carrier=carrier,
            delivery_timestamp=now,
            delivered_latitude=driver_lat,
            delivered_longitude=driver_lon,
            distance_to_customer_address_meters=distance_meters,
            is_within_geofence=is_geofence_ok,
            status_message=msg,
        )
