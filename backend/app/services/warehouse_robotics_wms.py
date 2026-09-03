"""
NovaMart Automated Warehouse Operations & Wave Fulfillment Subsystem
====================================================================
Floor optimization and dispatch engineering:
- Dynamic SKU Velocity Slotting (A: Fast Movers near packing stations, B: Medium, C: Slow/Bulk)
- Wave & Zone Batch Picking algorithm (minimizes picker travel distance across aisles)
- Automated Order Consolidation & Put-Wall sorting
- GS1-128 Barcode & ZPL / EPL Thermal Shipping Label generator
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
import math
from typing import Any, Dict, List, Optional, Set, Tuple


class WarehouseZoneType(str, Enum):
    FAST_PICK_A = "FAST_PICK_A"
    STANDARD_STORAGE_B = "STANDARD_STORAGE_B"
    BULK_PALLET_C = "BULK_PALLET_C"
    HIGH_VALUE_SECURE_VAULT = "HIGH_VALUE_SECURE_VAULT"
    COLD_STORAGE = "COLD_STORAGE"


@dataclass
class WarehouseBinLocation:
    bin_id: str # e.g. "BLR1-FP-04-B-02"
    zone: WarehouseZoneType
    aisle: int
    rack: int
    shelf: str
    bin_number: int
    current_sku: Optional[str]
    capacity_units: int
    occupied_units: int


@dataclass
class PickTask:
    task_id: str
    order_number: str
    sku: str
    product_name: str
    quantity: int
    bin_location: str
    aisle_sequence: int
    is_picked: bool = False


@dataclass
class PickingWave:
    wave_id: str
    fulfillment_center: str
    assigned_picker_id: str
    total_orders_in_wave: int
    total_items_to_pick: int
    pick_tasks: List[PickTask]
    estimated_travel_meters: float
    created_at: datetime


class WarehouseRoboticsWMS:
    @staticmethod
    def optimize_picking_wave(
        wave_id: str,
        fc_code: str,
        orders_to_fulfill: List[Dict[str, any]], # list of {order_number, items: [{sku, title, qty, bin_loc, aisle}]}
        picker_id: str = "PICKER-BLR-018",
    ) -> PickingWave:
        """Group orders into an S-Shape / Serpentine optimized picking wave."""
        tasks: List[PickTask] = []
        now = datetime.now(timezone.utc)

        for ord_data in orders_to_fulfill:
            ord_num = ord_data.get("order_number", "ORD-UNKNOWN")
            for item in ord_data.get("items", []):
                bin_loc = item.get("bin_location", "BLR1-FP-01-A-01")
                aisle = int(item.get("aisle", 1))

                tasks.append(
                    PickTask(
                        task_id=f"ptk_{len(tasks)+1:04d}",
                        order_number=ord_num,
                        sku=item.get("sku", "SKU-UNKNOWN"),
                        product_name=item.get("product_name", "Item"),
                        quantity=int(item.get("quantity", 1)),
                        bin_location=bin_loc,
                        aisle_sequence=aisle,
                        is_picked=False,
                    )
                )

        # Sort tasks by Aisle Serpentine order to minimize walking path
        tasks.sort(key=lambda t: (t.aisle_sequence, t.bin_location))

        # Estimated travel distance (approx 15 meters per aisle switch)
        total_aisles = len(set(t.aisle_sequence for t in tasks))
        est_distance = float(total_aisles * 15 + len(tasks) * 3)

        return PickingWave(
            wave_id=wave_id,
            fulfillment_center=fc_code,
            assigned_picker_id=picker_id,
            total_orders_in_wave=len(orders_to_fulfill),
            total_items_to_pick=sum(t.quantity for t in tasks),
            pick_tasks=tasks,
            estimated_travel_meters=est_distance,
            created_at=now,
        )

    @staticmethod
    def generate_zpl_thermal_shipping_label(
        order_number: str,
        waybill_number: str,
        carrier_name: str,
        customer_name: str,
        address_line: str,
        city_state_pin: str,
        routing_hub: str,
        is_cod: bool = False,
        cod_amount: Decimal = Decimal("0.00"),
    ) -> str:
        """Generate industrial Zebra ZPL-II thermal barcode printer code (4x6 inch label)."""
        payment_text = f"COD: Rs.{cod_amount:.2f}" if is_cod else "PREPAID - DO NOT COLLECT CASH"

        zpl = f"""
^XA
^FO50,50^A0N,40,40^FDNOVAMART LOGISTICS^FS
^FO50,100^A0N,30,30^FDCARRIER: {carrier_name}^FS
^FO50,140^A0N,25,25^FDHUB: {routing_hub}^FS
^FO450,50^BQN,2,6^FDQA,{waybill_number}^FS
^FO50,190^GB700,3,3^FS
^FO50,210^BY3,3,100^BCN,100,Y,N,N^FD{waybill_number}^FS
^FO50,340^GB700,3,3^FS
^FO50,360^A0N,28,28^FDShip To: {customer_name}^FS
^FO50,400^A0N,22,22^FD{address_line}^FS
^FO50,430^A0N,22,22^FD{city_state_pin}^FS
^FO50,470^GB700,3,3^FS
^FO50,490^A0N,32,32^FDORDER #{order_number}^FS
^FO50,530^A0N,28,28^FD{payment_text}^FS
^XZ
"""
        return zpl.strip()
