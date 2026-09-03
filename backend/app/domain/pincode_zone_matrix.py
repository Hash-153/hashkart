"""
NovaMart Indian Postal Circle & Logistics Fulfillment Matrix
============================================================
Defines India's 9 Postal Zones (North, West, South, East, North-East, APS),
regional sorting mother hubs, and delivery SLA turn-around-time (TAT) matrix.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple


class PostalCircleRegion(str, Enum):
    NORTH_ZONE = "NORTH_ZONE"
    WEST_ZONE = "WEST_ZONE"
    SOUTH_ZONE = "SOUTH_ZONE"
    EAST_ZONE = "EAST_ZONE"
    NORTH_EAST_ZONE = "NORTH_EAST_ZONE"


@dataclass
class PostalCircleInfo:
    circle_code: int # First digit of PIN (1-8)
    region: PostalCircleRegion
    states_covered: List[str]
    primary_mother_hub: str
    hub_airport_code: str


@dataclass
class PincodeServiceabilityRecord:
    pincode: str
    city: str
    district: str
    state: str
    state_gst_code: int
    circle_zone: PostalCircleRegion
    is_prepaid_serviceable: bool
    is_cod_serviceable: bool
    max_cod_limit_inr: float
    is_next_day_delivery_eligible: bool
    standard_tat_days: int


# Postal Circle Directory
POSTAL_CIRCLES: Dict[int, PostalCircleInfo] = {
    1: PostalCircleInfo(1, PostalCircleRegion.NORTH_ZONE, ["Delhi", "Haryana", "Punjab", "Himachal Pradesh", "Jammu and Kashmir", "Chandigarh"], "Delhi North Hub", "DEL"),
    2: PostalCircleInfo(2, PostalCircleRegion.NORTH_ZONE, ["Uttar Pradesh", "Uttarakhand"], "Lucknow Hub", "LKO"),
    3: PostalCircleInfo(3, PostalCircleRegion.WEST_ZONE, ["Rajasthan", "Gujarat", "Daman and Diu", "Dadra and Nagar Haveli"], "Ahmedabad West Hub", "AMD"),
    4: PostalCircleInfo(4, PostalCircleRegion.WEST_ZONE, ["Maharashtra", "Goa", "Madhya Pradesh", "Chhattisgarh"], "Mumbai Central Hub", "BOM"),
    5: PostalCircleInfo(5, PostalCircleRegion.SOUTH_ZONE, ["Andhra Pradesh", "Telangana", "Karnataka"], "Bengaluru South Hub", "BLR"),
    6: PostalCircleInfo(6, PostalCircleRegion.SOUTH_ZONE, ["Tamil Nadu", "Kerala", "Puducherry", "Lakshadweep"], "Chennai South Hub", "MAA"),
    7: PostalCircleInfo(7, PostalCircleRegion.EAST_ZONE, ["West Bengal", "Odisha", "Arunachal Pradesh", "Nagaland", "Manipur", "Mizoram", "Tripura", "Meghalaya", "Assam", "Sikkim", "Andaman and Nicobar"], "Kolkata East Hub", "CCU"),
    8: PostalCircleInfo(8, PostalCircleRegion.EAST_ZONE, ["Bihar", "Jharkhand"], "Patna Hub", "PAT"),
}


class PincodeZoneRouter:
    @staticmethod
    def get_postal_circle_from_pincode(pincode: str) -> Optional[PostalCircleInfo]:
        """Resolve pin code starting digit to Indian postal circle."""
        if not pincode or len(pincode) != 6 or not pincode.isdigit():
            return None
        first_digit = int(pincode[0])
        return POSTAL_CIRCLES.get(first_digit)

    @staticmethod
    def calculate_transit_tat_days(origin_pincode: str, destination_pincode: str) -> int:
        """Compute estimated ground transit days between two PIN codes."""
        if not origin_pincode or not destination_pincode:
            return 4

        # Intra-city Local (Same first 3 digits)
        if origin_pincode[:3] == destination_pincode[:3]:
            return 1

        # Intra-State Regional (Same first 2 digits)
        if origin_pincode[:2] == destination_pincode[:2]:
            return 2

        # Same Postal Circle
        if origin_pincode[0] == destination_pincode[0]:
            return 3

        # North-East or Remote Islands (Starts with 7 or 19)
        if destination_pincode.startswith("7") or destination_pincode.startswith("19"):
            return 5

        # Standard Inter-Zone Metro-to-Metro
        return 3
