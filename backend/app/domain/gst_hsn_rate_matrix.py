"""
NovaMart Master GST HSN Code & Central/State Tax Rate Matrix
============================================================
Authoritative schedule of Indian Harmonized System of Nomenclature (HSN) and Service Accounting Codes (SAC):
Provides precise GST slabs (0%, 5%, 12%, 18%, 28%), compensation cess, and statutory descriptions.
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, Optional, Tuple


@dataclass
class HSNEntry:
    hsn_code: str
    chapter: int
    description: str
    gst_rate_percent: Decimal
    cgst_percent: Decimal
    sgst_percent: Decimal
    igst_percent: Decimal
    cess_percent: Decimal = Decimal("0.0")
    is_reverse_charge_applicable: bool = False


# Exhaustive HSN Catalog for Indian E-Commerce
GST_HSN_RATE_MATRIX: Dict[str, HSNEntry] = {
    # --- CHAPTER 85: ELECTRICAL MACHINERY & ELECTRONICS ---
    "85171300": HSNEntry("85171300", 85, "Smartphones and handheld mobile phones", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "85171200": HSNEntry("85171200", 85, "Other mobile cellular telephones and feature phones", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "85183000": HSNEntry("85183000", 85, "Headphones, earphones, and combined microphone sets", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "85182200": HSNEntry("85182200", 85, "Multiple loudspeakers mounted in the same enclosure (Soundbars)", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "85044090": HSNEntry("85044090", 85, "Static converters, power banks, and battery chargers", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "85287217": HSNEntry("85287217", 85, "Television reception apparatus LED/OLED/QLED (up to 32 inch)", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "85287219": HSNEntry("85287219", 85, "Television reception apparatus LED/OLED/QLED (above 32 inch)", Decimal("28.0"), Decimal("14.0"), Decimal("14.0"), Decimal("28.0")),
    "85165000": HSNEntry("85165000", 85, "Microwave ovens", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "85167920": HSNEntry("85167920", 85, "Electric air fryers and convection cookers", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "85094010": HSNEntry("85094010", 85, "Food grinders and mixers / juicers", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),

    # --- CHAPTER 84: NUCLEAR REACTORS, BOILERS, MACHINERY, LAPTOPS ---
    "84713010": HSNEntry("84713010", 84, "Personal computers (laptops/notebooks/ultrabooks)", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "84713020": HSNEntry("84713020", 84, "Tablet computers and handheld micro-computers", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "84717020": HSNEntry("84717020", 84, "Hard disk drives and Solid State Drives (SSD)", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "84151010": HSNEntry("84151010", 84, "Inverter Split Air Conditioners (Domestic)", Decimal("28.0"), Decimal("14.0"), Decimal("14.0"), Decimal("28.0")),
    "84182100": HSNEntry("84182100", 84, "Compression-type household refrigerators (Frost Free)", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "84501100": HSNEntry("84501100", 84, "Fully-automatic front loading washing machines", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "84501200": HSNEntry("84501200", 84, "Semi-automatic top loading washing machines", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),

    # --- CHAPTER 61 & 62: APPAREL & CLOTHING ---
    "61091000": HSNEntry("61091000", 61, "T-shirts, singlets and other vests of cotton", Decimal("5.0"), Decimal("2.5"), Decimal("2.5"), Decimal("5.0")),
    "61051000": HSNEntry("61051000", 61, "Men's or boys' shirts of cotton (Knitted)", Decimal("5.0"), Decimal("2.5"), Decimal("2.5"), Decimal("5.0")),
    "62052000": HSNEntry("62052000", 62, "Men's or boys' shirts of cotton (Woven)", Decimal("5.0"), Decimal("2.5"), Decimal("2.5"), Decimal("5.0")),
    "62034200": HSNEntry("62034200", 62, "Men's or boys' trousers, bib, overalls and shorts of cotton (Jeans)", Decimal("12.0"), Decimal("6.0"), Decimal("6.0"), Decimal("12.0")),
    "62044220": HSNEntry("62044220", 62, "Women's or girls' dresses and ethnic kurtis of cotton", Decimal("5.0"), Decimal("2.5"), Decimal("2.5"), Decimal("5.0")),
    "61046200": HSNEntry("61046200", 61, "Women's or girls' leggings and track pants of cotton", Decimal("5.0"), Decimal("2.5"), Decimal("2.5"), Decimal("5.0")),

    # --- CHAPTER 64: FOOTWEAR ---
    "64041100": HSNEntry("64041100", 64, "Sports footwear, tennis shoes, basketball shoes, running shoes", Decimal("12.0"), Decimal("6.0"), Decimal("6.0"), Decimal("12.0")),
    "64039990": HSNEntry("64039990", 64, "Leather formal shoes and boots", Decimal("12.0"), Decimal("6.0"), Decimal("6.0"), Decimal("12.0")),
    "64029990": HSNEntry("64029990", 64, "Casual slippers and flip flops (Value under Rs. 1000)", Decimal("5.0"), Decimal("2.5"), Decimal("2.5"), Decimal("5.0")),

    # --- CHAPTER 33: COSMETICS & BEAUTY ---
    "33049990": HSNEntry("33049990", 33, "Skincare creams, moisturizers, lotions and serums", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "33051090": HSNEntry("33051090", 33, "Shampoos and hair care preparations", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "33072000": HSNEntry("33072000", 33, "Personal deodorants and anti-perspirants", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "33030010": HSNEntry("33030010", 33, "Perfumes and luxury eau de toilette", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),

    # --- CHAPTER 99: SERVICE ACCOUNTING CODES (SAC) ---
    "996111": HSNEntry("996111", 99, "Online marketplace platform facilitation services", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "996511": HSNEntry("996511", 99, "Road transportation of goods (Courier & Express Logistics)", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
    "998314": HSNEntry("998314", 99, "Information technology storage & cloud hosting services", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0")),
}


def lookup_hsn_tax(hsn_code: str) -> HSNEntry:
    """Lookup HSN entry with fallback to standard 18% general merchandise rate."""
    clean = str(hsn_code).strip()
    return GST_HSN_RATE_MATRIX.get(
        clean,
        HSNEntry(clean, 0, "General Goods & Services", Decimal("18.0"), Decimal("9.0"), Decimal("9.0"), Decimal("18.0"))
    )
