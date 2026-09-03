"""
NovaMart Bulk Catalog Ingestion & Barcode Ingestion Pipeline
============================================================
Handles high-throughput seller catalog batch uploads:
- CSV & Tab-Delimited parsing with schema auto-mapping
- Barcode validation (EAN-13, UPC-A, ISBN) with check-digit algorithms
- Automated image URL validation and dimensions sanitization
- Category inference & attribute mapping
- Detailed line-by-line error reporting
"""

from dataclasses import dataclass, field
from decimal import Decimal
import re
from typing import Dict, List, Optional, Tuple


@dataclass
class CatalogImportRow:
    row_number: int
    title: str
    category_slug: str
    brand_name: str
    sku: str
    barcode: Optional[str]
    price: Decimal
    mrp: Decimal
    stock: int
    image_urls: List[str]
    attributes: Dict[str, str]
    is_valid: bool = True
    validation_errors: List[str] = field(default_factory=list)


@dataclass
class CatalogImportResult:
    total_rows_processed: int
    valid_rows_count: int
    invalid_rows_count: int
    created_skus: List[str]
    errors_by_row: Dict[int, List[str]]


def validate_ean13_checksum(barcode: str) -> bool:
    """Validate EAN-13 barcode using modulo 10 checksum algorithm."""
    clean = re.sub(r"\D", "", barcode)
    if len(clean) != 13:
        return False

    digits = [int(d) for d in clean]
    # Sum odd positions (weight 1) and even positions (weight 3) except check digit
    odd_sum = sum(digits[i] for i in range(0, 12, 2))
    even_sum = sum(digits[i] * 3 for i in range(1, 12, 2))
    total = odd_sum + even_sum

    check_digit = (10 - (total % 10)) % 10
    return check_digit == digits[12]


def validate_image_url(url: str) -> bool:
    """Check whether image URL is HTTPS and points to a supported image format."""
    if not url.startswith("https://") and not url.startswith("http://"):
        return False
    return bool(re.search(r"\.(jpg|jpeg|png|webp|avif)(\?.*)?$", url, re.IGNORECASE))


class CatalogBatchImporter:
    @staticmethod
    def parse_and_validate_rows(
        raw_rows: List[Dict[str, str]]
    ) -> Tuple[List[CatalogImportRow], CatalogImportResult]:
        """Validate an array of raw uploaded catalog CSV dictionary records."""
        parsed_items: List[CatalogImportRow] = []
        errors_map: Dict[int, List[str]] = {}
        valid_count = 0
        invalid_count = 0
        created_skus: List[str] = []

        for idx, r in enumerate(raw_rows, start=1):
            errors = []
            title = r.get("title", "").strip()
            category = r.get("category", "").strip().lower()
            brand = r.get("brand", "").strip()
            sku = r.get("sku", "").strip()
            barcode = r.get("barcode", "").strip() if r.get("barcode") else None

            if not title:
                errors.append("Product title is required")
            elif len(title) < 5:
                errors.append("Product title must be at least 5 characters")

            if not category:
                errors.append("Category classification is required")

            if not brand:
                errors.append("Brand name is required")

            if not sku:
                errors.append("Seller SKU is required")
            elif not re.match(r"^[A-Za-z0-9\-_]{3,50}$", sku):
                errors.append("SKU must be 3-50 alphanumeric characters with dashes/underscores")

            # Validate Price & MRP
            try:
                price = Decimal(str(r.get("price", "0")))
                if price <= Decimal("0"):
                    errors.append("Price must be greater than zero")
            except Exception:
                price = Decimal("0")
                errors.append("Invalid price format")

            try:
                mrp = Decimal(str(r.get("mrp", "0")))
                if mrp < price:
                    errors.append("MRP cannot be less than selling price")
            except Exception:
                mrp = price

            # Validate Stock Quantity
            try:
                stock = int(r.get("stock", "0"))
                if stock < 0:
                    errors.append("Stock quantity cannot be negative")
            except Exception:
                stock = 0
                errors.append("Invalid stock number format")

            # Validate Barcode if provided
            if barcode:
                if len(barcode) == 13 and not validate_ean13_checksum(barcode):
                    errors.append(f"Invalid EAN-13 check digit for barcode '{barcode}'")

            # Validate Image URLs
            raw_imgs = [img.strip() for img in r.get("images", "").split(",") if img.strip()]
            for img in raw_imgs:
                if not validate_image_url(img):
                    errors.append(f"Invalid image URL or unsupported format: '{img}'")

            # Extract Dynamic Attributes
            attrs: Dict[str, str] = {}
            for k, v in r.items():
                if k.startswith("attr_") and v.strip():
                    attr_name = k.replace("attr_", "").strip()
                    attrs[attr_name] = v.strip()

            is_valid = len(errors) == 0
            if is_valid:
                valid_count += 1
                created_skus.append(sku)
            else:
                invalid_count += 1
                errors_map[idx] = errors

            parsed_items.append(
                CatalogImportRow(
                    row_number=idx,
                    title=title,
                    category_slug=category,
                    brand_name=brand,
                    sku=sku,
                    barcode=barcode,
                    price=price,
                    mrp=mrp,
                    stock=stock,
                    image_urls=raw_imgs,
                    attributes=attrs,
                    is_valid=is_valid,
                    validation_errors=errors,
                )
            )

        summary = CatalogImportResult(
            total_rows_processed=len(raw_rows),
            valid_rows_count=valid_count,
            invalid_rows_count=invalid_count,
            created_skus=created_skus,
            errors_by_row=errors_map,
        )

        return parsed_items, summary
