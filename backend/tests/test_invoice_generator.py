from datetime import datetime, timezone
from decimal import Decimal
import pytest

from app.services.invoice_generator import generate_tax_invoice, number_to_indian_rupee_words


def test_number_to_indian_rupee_words():
    assert number_to_indian_rupee_words(Decimal("0")) == "Rupees Zero Only"
    assert "One Lakh" in number_to_indian_rupee_words(Decimal("125000.00"))
    assert "Twenty Five" in number_to_indian_rupee_words(Decimal("125.00"))


def test_generate_gst_tax_invoice_intra_state():
    seller_data = {
        "business_name": "NovaMart Retail Hub Bengaluru",
        "gstin": "29AAACB1234K1Z5",
        "pan": "AAACB1234K",
        "pickup_address": "MG Road, Bengaluru",
        "state": "Karnataka",
    }
    customer_data = {
        "full_name": "Rohit Sharma",
        "phone": "9876543210",
        "address_line1": "Indiranagar",
        "state": "Karnataka",
    }
    order_data = {
        "order_number": "HK-2026-99A1",
        "created_at": datetime.now(timezone.utc),
        "shipping_fee": Decimal("0.00"),
    }
    items_data = [
        {
            "id": 1,
            "product_name": "Sony WH-1000XM5",
            "variant_title": "Black",
            "sku": "SNY-XM5",
            "hsn_code": "85183000",
            "quantity": 1,
            "unit_price": Decimal("26990.00"),
            "discount_amount": Decimal("0.00"),
        }
    ]

    invoice = generate_tax_invoice(order_data, seller_data, customer_data, items_data)

    assert invoice.is_interstate is False
    assert invoice.seller_state_code == "29"
    assert invoice.buyer_state_code == "29"
    assert invoice.total_cgst > Decimal("0.00")
    assert invoice.total_sgst > Decimal("0.00")
    assert invoice.total_igst == Decimal("0.00")
    assert invoice.digital_signature_hash is not None
    assert len(invoice.qr_code_payload) > 20


def test_generate_gst_tax_invoice_inter_state():
    seller_data = {
        "business_name": "NovaMart Retail Hub Bengaluru",
        "gstin": "29AAACB1234K1Z5",
        "state": "Karnataka",
    }
    customer_data = {
        "full_name": "Pooja Hegde",
        "phone": "9876543211",
        "address_line1": "Marine Drive",
        "state": "Maharashtra", # Inter-state
    }
    order_data = {
        "order_number": "HK-2026-99A2",
        "created_at": datetime.now(timezone.utc),
        "shipping_fee": Decimal("49.00"),
    }
    items_data = [
        {
            "id": 2,
            "product_name": "Apple iPhone 15",
            "variant_title": "128GB",
            "sku": "APL-IP15",
            "hsn_code": "85171300",
            "quantity": 1,
            "unit_price": Decimal("69999.00"),
            "discount_amount": Decimal("1000.00"),
        }
    ]

    invoice = generate_tax_invoice(order_data, seller_data, customer_data, items_data)

    assert invoice.is_interstate is True
    assert invoice.seller_state_code == "29"
    assert invoice.buyer_state_code == "27"
    assert invoice.total_cgst == Decimal("0.00")
    assert invoice.total_sgst == Decimal("0.00")
    assert invoice.total_igst > Decimal("0.00")
    assert invoice.shipping_charges == Decimal("49.00")
