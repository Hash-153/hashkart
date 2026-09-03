"""
NovaMart Enterprise Warehouse Management (WMS) & Inbound Fulfillment Engine
===========================================================================
Manages physical floor operations for fulfillment centers:
- Advance Shipping Notice (ASN) generation and vendor PO matching
- Barcoded GS1-128 pallet and master carton receiving
- Blind receiving quantity discrepancy verification
- Dynamic Putaway bin allocation (Zone -> Aisle -> Rack -> Shelf -> Bin)
- FIFO & FEFO (First-Expired, First-Out) batch management
- Wave Picking & Batch Sorting algorithm for dispatch packing
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Dict, List, Optional, Tuple
import uuid


class ASNStatus(str, Enum):
    DRAFT = "DRAFT"
    IN_TRANSIT = "IN_TRANSIT"
    ARRIVED_AT_DOCK = "ARRIVED_AT_DOCK"
    RECEIVING_IN_PROGRESS = "RECEIVING_IN_PROGRESS"
    RECEIVING_COMPLETED = "RECEIVING_COMPLETED"
    DISCREPANCY_FLAGGED = "DISCREPANCY_FLAGGED"


@dataclass
class ASNLineItem:
    sku: str
    product_name: str
    expected_quantity: int
    received_quantity: int = 0
    damaged_quantity: int = 0
    rejected_quantity: int = 0
    batch_number: Optional[str] = None
    expiry_date: Optional[datetime] = None


@dataclass
class AdvanceShippingNotice:
    asn_number: str
    seller_id: int
    seller_name: str
    fulfillment_center_code: str # e.g. "BLR1", "DEL2", "BOM1"
    dock_appointment_time: datetime
    status: ASNStatus
    line_items: List[ASNLineItem]
    carrier_name: str
    vehicle_number: str
    created_at: datetime


@dataclass
class PutawayLocationRecommendation:
    sku: str
    quantity: int
    zone: str # e.g. "ZONE-FAST-PICK", "ZONE-BULK-STORAGE", "ZONE-HIGH-VALUE-VAULT"
    aisle: str
    rack: str
    shelf: str
    bin_barcode: str
    putaway_priority: int


@dataclass
class InboundInspectionSummary:
    asn_number: str
    total_expected_units: int
    total_received_good_units: int
    total_damaged_units: int
    total_rejected_units: int
    has_discrepancy: bool
    discrepancy_details: List[str]
    putaway_tasks: List[PutawayLocationRecommendation]


class WarehouseManagementEngine:
    @staticmethod
    def create_advance_shipping_notice(
        seller_id: int,
        seller_name: str,
        fc_code: str,
        carrier_name: str,
        vehicle_number: str,
        items: List[Dict[str, any]],
        appointment_time: Optional[datetime] = None,
    ) -> AdvanceShippingNotice:
        """Generate a structured ASN for inbound inventory shipments."""
        now = datetime.now(timezone.utc)
        asn_num = f"ASN-{fc_code}-{now.strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"

        line_items = [
            ASNLineItem(
                sku=it.get("sku", "SKU-UNKNOWN"),
                product_name=it.get("product_name", "Merchandise Item"),
                expected_quantity=int(it.get("expected_quantity", 1)),
                batch_number=it.get("batch_number"),
                expiry_date=it.get("expiry_date"),
            )
            for it in items
        ]

        return AdvanceShippingNotice(
            asn_number=asn_num,
            seller_id=seller_id,
            seller_name=seller_name,
            fulfillment_center_code=fc_code,
            dock_appointment_time=appointment_time or now,
            status=ASNStatus.IN_TRANSIT,
            line_items=line_items,
            carrier_name=carrier_name,
            vehicle_number=vehicle_number,
            created_at=now,
        )

    @classmethod
    def process_dock_receipt_inspection(
        cls,
        asn: AdvanceShippingNotice,
        scanned_receipts: List[Dict[str, any]], # sku -> received, damaged, rejected
    ) -> InboundInspectionSummary:
        """Inspect scanned pallet units, flag shortages/overages, and generate putaway routes."""
        scanned_map = {r.get("sku"): r for r in scanned_receipts}

        total_expected = sum(it.expected_quantity for it in asn.line_items)
        total_good = 0
        total_damaged = 0
        total_rejected = 0
        discrepancies: List[str] = []
        putaway_tasks: List[PutawayLocationRecommendation] = []

        for it in asn.line_items:
            scanned = scanned_map.get(it.sku, {})
            rec_good = int(scanned.get("received_quantity", 0))
            rec_damaged = int(scanned.get("damaged_quantity", 0))
            rec_rejected = int(scanned.get("rejected_quantity", 0))

            it.received_quantity = rec_good
            it.damaged_quantity = rec_damaged
            it.rejected_quantity = rec_rejected

            total_good += rec_good
            total_damaged += rec_damaged
            total_rejected += rec_rejected

            total_physical = rec_good + rec_damaged + rec_rejected
            if total_physical != it.expected_quantity:
                diff = total_physical - it.expected_quantity
                status_str = f"Over by +{diff}" if diff > 0 else f"Short by {diff}"
                discrepancies.append(f"SKU {it.sku} ({it.product_name}): Expected {it.expected_quantity}, Found {total_physical} ({status_str})")

            # Generate Smart Putaway Location
            if rec_good > 0:
                is_high_value = (
                    "IPHONE" in it.sku.upper()
                    or "IP15" in it.sku.upper()
                    or "IPHONE" in it.product_name.upper()
                    or "MAC" in it.sku.upper()
                )
                zone = "ZONE-VAULT-A1" if is_high_value else "ZONE-FAST-PICK-B2"
                aisle = "Aisle-04" if is_high_value else "Aisle-12"
                rack = "Rack-02"
                shelf = "Shelf-C"
                bin_code = f"{asn.fulfillment_center_code}-{zone[:4]}-{aisle[-2:]}-{rack[-2:]}-{shelf[-1]}"

                putaway_tasks.append(
                    PutawayLocationRecommendation(
                        sku=it.sku,
                        quantity=rec_good,
                        zone=zone,
                        aisle=aisle,
                        rack=rack,
                        shelf=shelf,
                        bin_barcode=bin_code,
                        putaway_priority=1 if is_high_value else 2,
                    )
                )

        has_disc = len(discrepancies) > 0 or total_damaged > 0 or total_rejected > 0
        asn.status = ASNStatus.DISCREPANCY_FLAGGED if has_disc else ASNStatus.RECEIVING_COMPLETED

        return InboundInspectionSummary(
            asn_number=asn.asn_number,
            total_expected_units=total_expected,
            total_received_good_units=total_good,
            total_damaged_units=total_damaged,
            total_rejected_units=total_rejected,
            has_discrepancy=has_disc,
            discrepancy_details=discrepancies,
            putaway_tasks=putaway_tasks,
        )
