"""
NovaMart 3PL Courier Rate Card & Logistics Tariff Schedules
===========================================================
Rate cards, fuel surcharge indexes, RTO tariffs, and volumetric multipliers:
Covers Ekart Logistics, Delhivery Express, BlueDart Aviation, Shadowfax Hyperlocal, Ecom Express.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, Optional


@dataclass
class CarrierTariffSlab:
    carrier_name: str
    service_mode: str # 'SURFACE', 'AIR', 'HYPERLOCAL'
    zone: str # 'ZONE_A_LOCAL', 'ZONE_B_REGIONAL', 'ZONE_C_METRO', 'ZONE_D_NATIONAL', 'ZONE_E_SPECIAL'
    base_500g_rate_inr: Decimal
    additional_500g_rate_inr: Decimal
    cod_fixed_fee_inr: Decimal
    cod_percent_fee: Decimal
    rto_rate_multiplier: Decimal # Usually 1.0x to 1.2x of forward shipping
    fuel_surcharge_percent: Decimal


CARRIER_TARIFF_MATRIX: List[CarrierTariffSlab] = [
    # --- EKART LOGISTICS ---
    CarrierTariffSlab("EKART", "SURFACE", "ZONE_A_LOCAL", Decimal("33.00"), Decimal("22.00"), Decimal("30.00"), Decimal("1.2"), Decimal("1.0"), Decimal("10.0")),
    CarrierTariffSlab("EKART", "SURFACE", "ZONE_B_REGIONAL", Decimal("42.00"), Decimal("28.00"), Decimal("30.00"), Decimal("1.2"), Decimal("1.0"), Decimal("10.0")),
    CarrierTariffSlab("EKART", "SURFACE", "ZONE_C_METRO", Decimal("49.00"), Decimal("32.00"), Decimal("30.00"), Decimal("1.2"), Decimal("1.0"), Decimal("10.0")),
    CarrierTariffSlab("EKART", "SURFACE", "ZONE_D_NATIONAL", Decimal("60.00"), Decimal("38.00"), Decimal("30.00"), Decimal("1.2"), Decimal("1.0"), Decimal("10.0")),
    CarrierTariffSlab("EKART", "SURFACE", "ZONE_E_SPECIAL", Decimal("78.00"), Decimal("48.00"), Decimal("35.00"), Decimal("1.5"), Decimal("1.1"), Decimal("12.0")),

    # --- DELHIVERY EXPRESS ---
    CarrierTariffSlab("DELHIVERY", "SURFACE", "ZONE_A_LOCAL", Decimal("36.00"), Decimal("24.00"), Decimal("32.00"), Decimal("1.3"), Decimal("1.0"), Decimal("12.0")),
    CarrierTariffSlab("DELHIVERY", "SURFACE", "ZONE_B_REGIONAL", Decimal("45.00"), Decimal("30.00"), Decimal("32.00"), Decimal("1.3"), Decimal("1.0"), Decimal("12.0")),
    CarrierTariffSlab("DELHIVERY", "SURFACE", "ZONE_C_METRO", Decimal("52.00"), Decimal("35.00"), Decimal("32.00"), Decimal("1.3"), Decimal("1.0"), Decimal("12.0")),
    CarrierTariffSlab("DELHIVERY", "SURFACE", "ZONE_D_NATIONAL", Decimal("65.00"), Decimal("42.00"), Decimal("32.00"), Decimal("1.3"), Decimal("1.0"), Decimal("12.0")),
    CarrierTariffSlab("DELHIVERY", "SURFACE", "ZONE_E_SPECIAL", Decimal("85.00"), Decimal("52.00"), Decimal("40.00"), Decimal("1.5"), Decimal("1.1"), Decimal("14.0")),

    # --- BLUEDART AVIATION ---
    CarrierTariffSlab("BLUEDART", "AIR", "ZONE_A_LOCAL", Decimal("55.00"), Decimal("40.00"), Decimal("45.00"), Decimal("1.5"), Decimal("1.0"), Decimal("15.0")),
    CarrierTariffSlab("BLUEDART", "AIR", "ZONE_B_REGIONAL", Decimal("68.00"), Decimal("48.00"), Decimal("45.00"), Decimal("1.5"), Decimal("1.0"), Decimal("15.0")),
    CarrierTariffSlab("BLUEDART", "AIR", "ZONE_C_METRO", Decimal("78.00"), Decimal("54.00"), Decimal("45.00"), Decimal("1.5"), Decimal("1.0"), Decimal("15.0")),
    CarrierTariffSlab("BLUEDART", "AIR", "ZONE_D_NATIONAL", Decimal("95.00"), Decimal("65.00"), Decimal("45.00"), Decimal("1.5"), Decimal("1.0"), Decimal("15.0")),
    CarrierTariffSlab("BLUEDART", "AIR", "ZONE_E_SPECIAL", Decimal("130.00"), Decimal("85.00"), Decimal("50.00"), Decimal("1.8"), Decimal("1.2"), Decimal("18.0")),
]
