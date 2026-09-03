import pytest
from decimal import Decimal

from app.services.catalog_importer import (
    CatalogBatchImporter,
    validate_ean13_checksum,
    validate_image_url,
)


def test_validate_ean13_checksum():
    assert validate_ean13_checksum("8901030384486") is True # Valid Indian product EAN (check digit 6)
    assert validate_ean13_checksum("8901030384480") is False # Invalid check digit
    assert validate_ean13_checksum("123") is False


def test_validate_image_url():
    assert validate_image_url("https://cdn.novamart.in/images/products/phone.webp") is True
    assert validate_image_url("https://cdn.novamart.in/images/products/phone.jpg?v=1") is True
    assert validate_image_url("ftp://invalid.com/pic.png") is False
    assert validate_image_url("https://cdn.novamart.in/file.exe") is False


def test_catalog_batch_import_parsing():
    raw_csv = [
        {
            "title": "Realme GT 6T 5G Smartphone",
            "category": "mobiles",
            "brand": "Realme",
            "sku": "RME-GT6T-128",
            "price": "24999",
            "mrp": "30999",
            "stock": "50",
            "images": "https://img.novamart.in/gt6t.jpg",
            "attr_ram": "8 GB",
            "attr_storage": "128 GB",
        },
        {
            "title": "Bad", # Too short title
            "category": "audio",
            "brand": "Sony",
            "sku": "INVALID SKU!@#$",
            "price": "-500", # Negative price
            "mrp": "100",
            "stock": "-5",
        },
    ]

    items, summary = CatalogBatchImporter.parse_and_validate_rows(raw_csv)
    assert summary.total_rows_processed == 2
    assert summary.valid_rows_count == 1
    assert summary.invalid_rows_count == 1
    assert "RME-GT6T-128" in summary.created_skus
    assert len(summary.errors_by_row[2]) >= 3
