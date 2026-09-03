import pytest
from app.services.wms_engine import WarehouseManagementEngine, ASNStatus


def test_wms_asn_creation_and_discrepancy_inspection():
    items = [
        {"sku": "APL-IP15-128", "product_name": "Apple iPhone 15", "expected_quantity": 50},
        {"sku": "SNY-XM5-BLK", "product_name": "Sony XM5 Headphones", "expected_quantity": 30},
    ]

    asn = WarehouseManagementEngine.create_advance_shipping_notice(
        seller_id=1,
        seller_name="Official Apple Partner",
        fc_code="BLR1",
        carrier_name="EKART",
        vehicle_number="KA-01-E-1234",
        items=items,
    )

    assert asn.status == ASNStatus.IN_TRANSIT
    assert len(asn.line_items) == 2

    # Scanned receipts with 1 unit shortage on iPhones and 2 damaged headphones
    scanned_receipts = [
        {"sku": "APL-IP15-128", "received_quantity": 49, "damaged_quantity": 0, "rejected_quantity": 0},
        {"sku": "SNY-XM5-BLK", "received_quantity": 28, "damaged_quantity": 2, "rejected_quantity": 0},
    ]

    summary = WarehouseManagementEngine.process_dock_receipt_inspection(asn, scanned_receipts)

    assert summary.has_discrepancy is True
    assert summary.total_received_good_units == 77
    assert summary.total_damaged_units == 2
    assert len(summary.discrepancy_details) >= 1
    assert len(summary.putaway_tasks) == 2
    assert summary.putaway_tasks[0].zone == "ZONE-VAULT-A1" # High-value vault for iPhones
