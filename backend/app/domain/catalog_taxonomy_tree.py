"""
NovaMart Comprehensive Indian E-Commerce Category Taxonomy & Attribute Schema Tree
===================================================================================
Authoritative 4-tier category taxonomy matrix (Mobiles, Electronics, Fashion, Appliances, Home, Beauty):
Defines hierarchical slugs, mandatory specification attributes, variation axes, and validation patterns.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set


@dataclass
class CategorySpecDefinition:
    attribute_key: str
    display_name: str
    data_type: str # 'STRING', 'NUMBER', 'BOOLEAN', 'ENUM', 'MULTI_SELECT'
    is_mandatory: bool
    is_filterable: bool
    is_variant_axis: bool
    allowed_values: Optional[List[str]] = None
    validation_regex: Optional[str] = None


@dataclass
class CategoryTaxonomyNode:
    category_id: int
    name: str
    slug: str
    parent_slug: Optional[str]
    level: int # 1: Root, 2: Department, 3: Shelf, 4: Product Type
    commission_rate_percent: float
    gst_rate_percent: float
    hsn_default: str
    specs: List[CategorySpecDefinition] = field(default_factory=list)


# Authoritative Taxonomy Dictionary
CATEGORY_TAXONOMY_TREE: Dict[str, CategoryTaxonomyNode] = {
    # --- LEVEL 1: ROOT DEPARTMENTS ---
    "mobiles": CategoryTaxonomyNode(
        category_id=100, name="Mobiles & Accessories", slug="mobiles", parent_slug=None, level=1,
        commission_rate_percent=6.5, gst_rate_percent=18.0, hsn_default="85171300",
    ),
    "electronics": CategoryTaxonomyNode(
        category_id=200, name="Electronics & Computers", slug="electronics", parent_slug=None, level=1,
        commission_rate_percent=7.0, gst_rate_percent=18.0, hsn_default="84713010",
    ),
    "appliances": CategoryTaxonomyNode(
        category_id=300, name="TVs & Large Appliances", slug="appliances", parent_slug=None, level=1,
        commission_rate_percent=8.5, gst_rate_percent=28.0, hsn_default="85287217",
    ),
    "fashion": CategoryTaxonomyNode(
        category_id=400, name="Fashion & Lifestyle", slug="fashion", parent_slug=None, level=1,
        commission_rate_percent=12.0, gst_rate_percent=12.0, hsn_default="61091000",
    ),
    "home": CategoryTaxonomyNode(
        category_id=500, name="Home & Kitchen", slug="home", parent_slug=None, level=1,
        commission_rate_percent=10.0, gst_rate_percent=18.0, hsn_default="94036000",
    ),
    "beauty": CategoryTaxonomyNode(
        category_id=600, name="Beauty, Toys & More", slug="beauty", parent_slug=None, level=1,
        commission_rate_percent=9.0, gst_rate_percent=18.0, hsn_default="33049990",
    ),

    # --- LEVEL 2 & 3: MOBILES SUB-CATEGORIES ---
    "smartphones": CategoryTaxonomyNode(
        category_id=101, name="Smartphones", slug="smartphones", parent_slug="mobiles", level=2,
        commission_rate_percent=5.5, gst_rate_percent=18.0, hsn_default="85171300",
        specs=[
            CategorySpecDefinition("ram_gb", "RAM", "ENUM", True, True, True, ["4 GB", "6 GB", "8 GB", "12 GB", "16 GB"]),
            CategorySpecDefinition("storage_gb", "Internal Storage", "ENUM", True, True, True, ["64 GB", "128 GB", "256 GB", "512 GB", "1 TB"]),
            CategorySpecDefinition("color", "Color", "STRING", True, True, True),
            CategorySpecDefinition("network_type", "Network Generation", "ENUM", True, True, False, ["5G", "4G VoLTE", "3G", "2G"]),
            CategorySpecDefinition("primary_camera_mp", "Primary Rear Camera", "NUMBER", False, True, False),
            CategorySpecDefinition("battery_mah", "Battery Capacity", "NUMBER", True, True, False),
            CategorySpecDefinition("screen_size_inch", "Display Size", "NUMBER", True, True, False),
            CategorySpecDefinition("processor_brand", "Processor Brand", "ENUM", False, True, False, ["Apple A-Series", "Qualcomm Snapdragon", "MediaTek Dimensity", "Google Tensor"]),
        ]
    ),
    "feature-phones": CategoryTaxonomyNode(
        category_id=102, name="Feature Phones", slug="feature-phones", parent_slug="mobiles", level=2,
        commission_rate_percent=6.0, gst_rate_percent=18.0, hsn_default="85171200",
        specs=[
            CategorySpecDefinition("sim_type", "SIM Type", "ENUM", True, True, False, ["Dual SIM", "Single SIM"]),
            CategorySpecDefinition("battery_mah", "Battery Capacity", "NUMBER", True, True, False),
            CategorySpecDefinition("expandable_memory", "Expandable Memory", "BOOLEAN", False, True, False),
        ]
    ),
    "mobile-cases": CategoryTaxonomyNode(
        category_id=103, name="Mobile Cases & Covers", slug="mobile-cases", parent_slug="mobiles", level=2,
        commission_rate_percent=15.0, gst_rate_percent=18.0, hsn_default="39269099",
        specs=[
            CategorySpecDefinition("compatible_model", "Compatible Phone Model", "STRING", True, True, False),
            CategorySpecDefinition("material", "Material", "ENUM", True, True, False, ["Silicone", "Leather", "Polycarbonate", "TPU", "Glass"]),
            CategorySpecDefinition("theme", "Theme / Pattern", "STRING", False, True, False),
        ]
    ),
    "power-banks": CategoryTaxonomyNode(
        category_id=104, name="Power Banks", slug="power-banks", parent_slug="mobiles", level=2,
        commission_rate_percent=8.0, gst_rate_percent=18.0, hsn_default="85044090",
        specs=[
            CategorySpecDefinition("capacity_mah", "Capacity", "ENUM", True, True, True, ["10000 mAh", "20000 mAh", "30000 mAh"]),
            CategorySpecDefinition("fast_charging_watt", "Fast Charging Wattage", "NUMBER", True, True, False),
            CategorySpecDefinition("output_ports", "Number of Output Ports", "NUMBER", True, True, False),
            CategorySpecDefinition("wireless_charging", "Supports Wireless Charging", "BOOLEAN", False, True, False),
        ]
    ),

    # --- ELECTRONICS: LAPTOPS, AUDIO, TABLETS ---
    "laptops": CategoryTaxonomyNode(
        category_id=201, name="Laptops", slug="laptops", parent_slug="electronics", level=2,
        commission_rate_percent=6.0, gst_rate_percent=18.0, hsn_default="84713010",
        specs=[
            CategorySpecDefinition("processor", "Processor", "ENUM", True, True, False, ["Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9", "AMD Ryzen 5", "AMD Ryzen 7", "Apple M2", "Apple M3", "Apple M3 Pro", "Apple M3 Max"]),
            CategorySpecDefinition("ram_gb", "RAM", "ENUM", True, True, True, ["8 GB", "16 GB", "32 GB", "64 GB"]),
            CategorySpecDefinition("ssd_capacity_gb", "SSD Capacity", "ENUM", True, True, True, ["256 GB", "512 GB", "1 TB", "2 TB"]),
            CategorySpecDefinition("graphic_processor", "Dedicated Graphics", "STRING", False, True, False),
            CategorySpecDefinition("screen_size_inch", "Screen Size", "NUMBER", True, True, False),
            CategorySpecDefinition("operating_system", "Operating System", "ENUM", True, True, False, ["Windows 11 Home", "macOS Sonoma", "Ubuntu / Linux", "DOS"]),
            CategorySpecDefinition("weight_kg", "Weight", "NUMBER", False, True, False),
        ]
    ),
    "audio-headphones": CategoryTaxonomyNode(
        category_id=202, name="Headphones & Earphones", slug="audio-headphones", parent_slug="electronics", level=2,
        commission_rate_percent=9.0, gst_rate_percent=18.0, hsn_default="85183000",
        specs=[
            CategorySpecDefinition("form_factor", "Headphone Type", "ENUM", True, True, False, ["True Wireless (TWS)", "In Ear Neckband", "On Ear", "Over Ear"]),
            CategorySpecDefinition("connectivity", "Connectivity", "ENUM", True, True, False, ["Bluetooth Wireless", "Wired 3.5mm", "Type-C"]),
            CategorySpecDefinition("anc_support", "Active Noise Cancellation (ANC)", "BOOLEAN", True, True, False),
            CategorySpecDefinition("battery_life_hours", "Playtime (Hours)", "NUMBER", True, True, False),
            CategorySpecDefinition("ip_rating", "Water Resistance IP Rating", "STRING", False, True, False),
        ]
    ),
    "smartwatches": CategoryTaxonomyNode(
        category_id=203, name="Smart Watches", slug="smartwatches", parent_slug="electronics", level=2,
        commission_rate_percent=8.5, gst_rate_percent=18.0, hsn_default="85176290",
        specs=[
            CategorySpecDefinition("display_type", "Display Type", "ENUM", True, True, False, ["AMOLED", "HD LCD", "Retina OLED"]),
            CategorySpecDefinition("dial_shape", "Dial Shape", "ENUM", True, True, False, ["Round", "Square", "Rectangle"]),
            CategorySpecDefinition("bluetooth_calling", "Bluetooth Calling", "BOOLEAN", True, True, False),
            CategorySpecDefinition("battery_days", "Battery Runtime (Days)", "NUMBER", False, True, False),
            CategorySpecDefinition("strap_color", "Strap Color", "STRING", True, True, True),
        ]
    ),

    # --- APPLIANCES: TELEVISIONS, REFRIGERATORS, AIR CONDITIONERS ---
    "televisions": CategoryTaxonomyNode(
        category_id=301, name="Televisions", slug="televisions", parent_slug="appliances", level=2,
        commission_rate_percent=7.5, gst_rate_percent=28.0, hsn_default="85287217",
        specs=[
            CategorySpecDefinition("screen_size_inch", "Screen Size", "ENUM", True, True, True, ["32 inch", "43 inch", "50 inch", "55 inch", "65 inch", "75 inch", "85 inch"]),
            CategorySpecDefinition("resolution", "Display Resolution", "ENUM", True, True, False, ["HD Ready (1366x768)", "Full HD (1920x1080)", "4K Ultra HD (3840x2160)", "8K Ultra HD"]),
            CategorySpecDefinition("panel_type", "Panel Technology", "ENUM", True, True, False, ["OLED", "QLED", "Mini-LED", "LED IPS"]),
            CategorySpecDefinition("smart_os", "Smart TV OS", "ENUM", True, True, False, ["Google TV", "Android TV", "webOS", "Tizen", "Fire TV OS"]),
            CategorySpecDefinition("refresh_rate_hz", "Refresh Rate", "NUMBER", False, True, False),
            CategorySpecDefinition("sound_output_watts", "Speaker Output (Watts)", "NUMBER", False, True, False),
        ]
    ),
    "refrigerators": CategoryTaxonomyNode(
        category_id=302, name="Refrigerators", slug="refrigerators", parent_slug="appliances", level=2,
        commission_rate_percent=8.0, gst_rate_percent=28.0, hsn_default="84182100",
        specs=[
            CategorySpecDefinition("door_type", "Door Configuration", "ENUM", True, True, False, ["Single Door", "Double Door Frost Free", "Side by Side", "Triple Door", "French Door"]),
            CategorySpecDefinition("capacity_litres", "Capacity (Litres)", "NUMBER", True, True, False),
            CategorySpecDefinition("star_rating", "BEE Star Rating", "ENUM", True, True, False, ["5 Star", "4 Star", "3 Star", "2 Star", "1 Star"]),
            CategorySpecDefinition("inverter_compressor", "Digital Inverter Compressor", "BOOLEAN", True, True, False),
        ]
    ),
    "air-conditioners": CategoryTaxonomyNode(
        category_id=303, name="Air Conditioners", slug="air-conditioners", parent_slug="appliances", level=2,
        commission_rate_percent=8.0, gst_rate_percent=28.0, hsn_default="84151010",
        specs=[
            CategorySpecDefinition("tonnage", "Cooling Capacity (Tons)", "ENUM", True, True, False, ["1.0 Ton", "1.5 Ton", "2.0 Ton"]),
            CategorySpecDefinition("ac_type", "AC Type", "ENUM", True, True, False, ["Inverter Split AC", "Fixed Speed Split AC", "Window AC", "Portable AC"]),
            CategorySpecDefinition("star_rating", "BEE Star Rating", "ENUM", True, True, False, ["5 Star", "4 Star", "3 Star"]),
            CategorySpecDefinition("copper_condenser", "100% Copper Condenser Coil", "BOOLEAN", True, True, False),
        ]
    ),
    "washing-machines": CategoryTaxonomyNode(
        category_id=304, name="Washing Machines", slug="washing-machines", parent_slug="appliances", level=2,
        commission_rate_percent=8.0, gst_rate_percent=28.0, hsn_default="84501100",
        specs=[
            CategorySpecDefinition("function_type", "Function Type", "ENUM", True, True, False, ["Fully Automatic Front Load", "Fully Automatic Top Load", "Semi Automatic Top Load"]),
            CategorySpecDefinition("capacity_kg", "Washing Capacity (kg)", "NUMBER", True, True, False),
            CategorySpecDefinition("inverter_motor", "Inverter Direct Drive Motor", "BOOLEAN", True, True, False),
            CategorySpecDefinition("heater_built_in", "In-built Heater", "BOOLEAN", False, True, False),
        ]
    ),

    # --- FASHION: APPAREL, FOOTWEAR, ACCESSORIES ---
    "men-tshirts": CategoryTaxonomyNode(
        category_id=401, name="Men's T-Shirts", slug="men-tshirts", parent_slug="fashion", level=2,
        commission_rate_percent=14.0, gst_rate_percent=12.0, hsn_default="61091000",
        specs=[
            CategorySpecDefinition("size", "Size", "ENUM", True, True, True, ["XS", "S", "M", "L", "XL", "XXL", "3XL"]),
            CategorySpecDefinition("color", "Color", "STRING", True, True, True),
            CategorySpecDefinition("neck_type", "Neck Type", "ENUM", True, True, False, ["Round Neck", "Polo Neck", "V Neck", "Mandarin Collar", "Hooded"]),
            CategorySpecDefinition("fabric", "Fabric Material", "ENUM", True, True, False, ["100% Cotton", "Cotton Blend", "Polyester", "Dry Fit Lycra", "Linen Blend"]),
            CategorySpecDefinition("pattern", "Pattern / Print", "ENUM", False, True, False, ["Solid", "Striped", "Graphic Print", "Colorblock", "Typographic"]),
            CategorySpecDefinition("fit", "Fit", "ENUM", False, True, False, ["Regular Fit", "Slim Fit", "Oversized Fit", "Relaxed Fit"]),
        ]
    ),
    "men-jeans": CategoryTaxonomyNode(
        category_id=402, name="Men's Jeans", slug="men-jeans", parent_slug="fashion", level=2,
        commission_rate_percent=14.0, gst_rate_percent=12.0, hsn_default="62034200",
        specs=[
            CategorySpecDefinition("waist_size_inch", "Waist Size", "ENUM", True, True, True, ["28", "30", "32", "34", "36", "38", "40"]),
            CategorySpecDefinition("fit", "Fit Type", "ENUM", True, True, False, ["Slim Fit", "Skinny Fit", "Regular Straight", "Tapered", "Baggy Relaxed"]),
            CategorySpecDefinition("stretchable", "Stretchable Denim", "BOOLEAN", True, True, False),
            CategorySpecDefinition("distressed", "Distressed / Ripped", "BOOLEAN", False, True, False),
            CategorySpecDefinition("wash_care", "Denim Wash Shade", "ENUM", False, True, False, ["Light Blue", "Medium Blue", "Dark Indigo", "Black", "Grey"]),
        ]
    ),
    "footwear-sneakers": CategoryTaxonomyNode(
        category_id=403, name="Casual & Sports Sneakers", slug="footwear-sneakers", parent_slug="fashion", level=2,
        commission_rate_percent=13.0, gst_rate_percent=12.0, hsn_default="64041100",
        specs=[
            CategorySpecDefinition("uk_size", "UK/India Shoe Size", "ENUM", True, True, True, ["UK 6", "UK 7", "UK 8", "UK 9", "UK 10", "UK 11", "UK 12"]),
            CategorySpecDefinition("color", "Color", "STRING", True, True, True),
            CategorySpecDefinition("outer_material", "Outer Material", "ENUM", True, True, False, ["Mesh Knit", "Synthetic Leather", "Genuine Leather", "Canvas", "Suede"]),
            CategorySpecDefinition("sole_material", "Sole Material", "ENUM", False, True, False, ["EVA Foam", "Rubber", "TPU Air Cushion", "Phylon"]),
            CategorySpecDefinition("closure", "Closure Type", "ENUM", False, True, False, ["Lace-Up", "Slip-On", "Velcro Strap"]),
        ]
    ),
}
