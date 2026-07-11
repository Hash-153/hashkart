import asyncio
import logging
import random
from datetime import datetime, timedelta, timezone
from sqlalchemy import select, delete
from app.database import AsyncSessionLocal, init_db, Base
from app.models.user import User, Role, Permission, Address
from app.models.catalog import (
    Category,
    Brand,
    Product,
    ProductVariant,
    ProductImage,
    ProductAttribute,
    AttributeDefinition,
    AttributeValue,
)
from app.models.promotion_review import Coupon, Review
from app.models.inventory import Inventory, InventoryTransaction
from app.models.discovery import SearchQueryAnalytics, UserSearchHistory
from app.core.security import get_password_hash

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hashkart.seeder")

CATEGORIES_DATA = [
    # Top-level categories with subcategories
    {
        "name": "Electronics",
        "slug": "electronics",
        "display_order": 1,
        "image_url": "https://images.unsplash.com/photo-1498049794561-7780e7231661?auto=format&fit=crop&w=300&q=80",
        "subcategories": [
            {"name": "Mobiles & Smartphones", "slug": "mobiles", "display_order": 1, "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=300&q=80"},
            {"name": "Laptops & Computers", "slug": "laptops", "display_order": 2, "image_url": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=300&q=80"},
            {"name": "Audio & Headphones", "slug": "audio", "display_order": 3, "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=300&q=80"},
            {"name": "Smartwatches & Bands", "slug": "wearables", "display_order": 4, "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=300&q=80"},
            {"name": "Cameras & Photography", "slug": "cameras", "display_order": 5, "image_url": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=300&q=80"},
        ],
    },
    {
        "name": "Fashion",
        "slug": "fashion",
        "display_order": 2,
        "image_url": "https://images.unsplash.com/photo-1445205170230-053b83016050?auto=format&fit=crop&w=300&q=80",
        "subcategories": [
            {"name": "Men's Clothing", "slug": "mens-clothing", "display_order": 1, "image_url": "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=300&q=80"},
            {"name": "Women's Ethnic & Western", "slug": "womens-clothing", "display_order": 2, "image_url": "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=300&q=80"},
            {"name": "Footwear & Sneakers", "slug": "footwear", "display_order": 3, "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=300&q=80"},
        ],
    },
    {
        "name": "Home & Kitchen",
        "slug": "home-kitchen",
        "display_order": 3,
        "image_url": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=300&q=80",
        "subcategories": [
            {"name": "Kitchenware & Cookware", "slug": "kitchenware", "display_order": 1, "image_url": "https://images.unsplash.com/photo-1584990347449-a3597c4146a8?auto=format&fit=crop&w=300&q=80"},
            {"name": "Home Furniture", "slug": "furniture", "display_order": 2, "image_url": "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=300&q=80"},
            {"name": "Decor & Lighting", "slug": "decor-lighting", "display_order": 3, "image_url": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=300&q=80"},
        ],
    },
    {
        "name": "Beauty & Personal Care",
        "slug": "beauty-care",
        "display_order": 4,
        "image_url": "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=300&q=80",
        "subcategories": [
            {"name": "Skincare & Hygiene", "slug": "skincare", "display_order": 1, "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=300&q=80"},
            {"name": "Personal Grooming", "slug": "grooming", "display_order": 2, "image_url": "https://images.unsplash.com/photo-1621607512214-68297480165e?auto=format&fit=crop&w=300&q=80"},
        ],
    },
    {
        "name": "Large Appliances",
        "slug": "large-appliances",
        "display_order": 5,
        "image_url": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=300&q=80",
        "subcategories": [
            {"name": "Televisions", "slug": "televisions", "display_order": 1, "image_url": "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=300&q=80"},
            {"name": "Refrigerators", "slug": "refrigerators", "display_order": 2, "image_url": "https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?auto=format&fit=crop&w=300&q=80"},
            {"name": "Air Conditioners", "slug": "air-conditioners", "display_order": 3, "image_url": "https://images.unsplash.com/photo-1614633833026-072049d59392?auto=format&fit=crop&w=300&q=80"},
        ],
    },
]

BRANDS_DATA = [
    {"name": "HashTech", "slug": "hashtech", "description": "Next-generation smartphones and connected devices", "is_featured": True},
    {"name": "Aura Audio", "slug": "aura-audio", "description": "High-fidelity acoustic audio and studio headphones", "is_featured": True},
    {"name": "Titan Compute", "slug": "titan-compute", "description": "High-performance enterprise and creator computing", "is_featured": True},
    {"name": "Zenith Electronics", "slug": "zenith-elec", "description": "Premium 4K Smart displays, QLED panels and home theater", "is_featured": True},
    {"name": "UrbanFit", "slug": "urbanfit", "description": "Contemporary urban apparel and denim wear", "is_featured": True},
    {"name": "Kraft Home", "slug": "kraft-home", "description": "Chef-grade cookware, smart fryers and kitchen essentials", "is_featured": True},
    {"name": "Stellar Time", "slug": "stellar-time", "description": "Precision smartwatches and luxury sports chronographs", "is_featured": True},
    {"name": "Apex Wear", "slug": "apex-wear", "description": "High-performance athletic running footwear and sports shoes", "is_featured": True},
    {"name": "Volt Appliances", "slug": "volt-appliances", "description": "Energy-efficient smart cooling and climate control", "is_featured": False},
    {"name": "Chroma Vision", "slug": "chroma-vision", "description": "Professional 4K mirrorless cameras and vlogging kits", "is_featured": True},
    {"name": "Saffron Touch", "slug": "saffron-touch", "description": "Clean herbal skincare, active serums and botanicals", "is_featured": True},
    {"name": "PureBlend", "slug": "pureblend", "description": "Heavy-duty Indian kitchen mixer grinders and blenders", "is_featured": False},
    {"name": "Velocity Gear", "slug": "velocity-gear", "description": "Esports-grade gaming laptops and accessories", "is_featured": True},
    {"name": "Nordic Living", "slug": "nordic-living", "description": "Scandinavian ergonomic furniture and living room decor", "is_featured": True},
    {"name": "Royal Weave", "slug": "royal-weave", "description": "Handcrafted Indian festive kurtas and silk sets", "is_featured": True},
    {"name": "EvoSound", "slug": "evosound", "description": "Wireless Dolby Atmos soundbars and home audio", "is_featured": False},
    {"name": "FrostTech", "slug": "frosttech", "description": "Smart inverter frost-free refrigerators", "is_featured": True},
    {"name": "GroomPro", "slug": "groompro", "description": "Precision cordless beard trimmers and grooming sets", "is_featured": True},
    {"name": "Lumina Light", "slug": "lumina-light", "description": "Smart ambient WiFi RGB lighting and floor lamps", "is_featured": True},
    {"name": "EcoBreeze", "slug": "ecobreeze", "description": "5-Star AI inverter air conditioners", "is_featured": True},
]

PRODUCTS_CATALOG = [
    # 1. HashTech (Mobiles & Electronics)
    {
        "brand": "hashtech",
        "category": "mobiles",
        "name": "HashTech Ultra 5G Smartphone (256 GB, Titanium Black)",
        "slug": "hashtech-ultra-5g",
        "description": "Flagship 5G smartphone powered by Snapdragon 8 Gen 3, 200MP OIS camera, 6.8-inch 120Hz AMOLED display, and 5000mAh battery with 100W SuperVOOC fast charging.",
        "short_description": "Flagship 200MP 5G phone with Snapdragon 8 Gen 3.",
        "highlight_features": "Snapdragon 8 Gen 3\n200MP OIS Camera\n5000mAh + 100W Fast Charge\n120Hz LTPO AMOLED",
        "price": 64999.0,
        "discount_price": 54999.0,
        "sku_prefix": "HT-U5G",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.8,
        "review_count": 342,
        "images": [
            "https://images.unsplash.com/photo-1592750475338-74b7b21085ab?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1510557880182-3d4d3cba35a5?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Processor": "Snapdragon 8 Gen 3", "RAM": "12 GB", "Storage": "256 GB", "Display": "6.8-inch AMOLED 120Hz", "Battery": "5000 mAh"}
    },
    {
        "brand": "hashtech",
        "category": "mobiles",
        "name": "HashTech Vision Max 5G (128 GB, Emerald Green)",
        "slug": "hashtech-vision-max-5g",
        "description": "Premium 5G smartphone with 50MP Sony sensor with optical image stabilization, 1.5K curved AMOLED screen, and all-day intelligent battery life.",
        "short_description": "50MP Sony OIS Camera with 1.5K Curved Display.",
        "highlight_features": "50MP Sony OIS Sensor\n1.5K Curved AMOLED 120Hz\n67W Flash Charge\nDual Stereo Speakers",
        "price": 54999.0,
        "discount_price": 42999.0,
        "sku_prefix": "HT-VIS-MAX",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.6,
        "review_count": 188,
        "images": [
            "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1580910051074-3eb694886505?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Processor": "MediaTek Dimensity 8300", "RAM": "8 GB", "Storage": "128 GB", "Display": "6.7-inch 120Hz AMOLED", "Battery": "5000 mAh"}
    },
    {
        "brand": "hashtech",
        "category": "mobiles",
        "name": "HashTech Edge Lite 5G (128 GB, Frost Blue)",
        "slug": "hashtech-edge-lite-5g",
        "description": "Ultra-slim lightweight 5G smartphone with bright 120Hz HDR10+ display, clean software experience, and fast dual SIM 5G connectivity.",
        "short_description": "Slim lightweight 5G smartphone with 120Hz screen.",
        "highlight_features": "Ultra-Slim 7.4mm Design\n120Hz Eye-Care Display\n33W Fast Charging\n50MP AI Dual Camera",
        "price": 24999.0,
        "discount_price": 19999.0,
        "sku_prefix": "HT-EDGE-LITE",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.5,
        "review_count": 512,
        "images": [
            "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1585060544812-6b45742d762f?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Processor": "Snapdragon 7s Gen 2", "RAM": "8 GB", "Storage": "128 GB", "Display": "6.67-inch FHD+ 120Hz", "Battery": "5000 mAh"}
    },
    {
        "brand": "hashtech",
        "category": "mobiles",
        "name": "HashTech Pro Gaming 5G (512 GB, Obsidian Black)",
        "slug": "hashtech-pro-gaming-5g",
        "description": "Heavy-duty gaming & multitasking phone with 6000mAh monster battery, liquid cooling chamber, and 108MP high-resolution camera.",
        "short_description": "Performance powerhouse with 6000mAh battery.",
        "highlight_features": "6000mAh Mega Battery\n108MP Studio Camera\nVapor Chamber Cooling\nDual 5G VoNR Support",
        "price": 39999.0,
        "discount_price": 32999.0,
        "sku_prefix": "HT-PROG5G",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.7,
        "review_count": 215,
        "images": [
            "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1565849904461-04a58ad377e0?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Processor": "Snapdragon 8+ Gen 1", "RAM": "12 GB", "Storage": "256 GB", "Display": "6.78-inch AMOLED 144Hz", "Battery": "6000 mAh"}
    },

    # 2. Aura Audio (Audio & Headphones)
    {
        "brand": "aura-audio",
        "category": "audio",
        "name": "Aura Audio Pulse Wireless ANC Over-Ear Headphones",
        "slug": "aura-pulse-anc",
        "description": "Acoustic studio clarity with hybrid active noise cancellation (42dB), 40mm titanium drivers, LDAC high-res audio codec, and 50-hour playback.",
        "short_description": "42dB Hybrid ANC, High-Res LDAC Audio, 50h Playback.",
        "highlight_features": "42dB Hybrid Active Noise Cancellation\n40mm Custom Titanium Drivers\n50-Hour Playback with Fast Charge\nMultipoint Bluetooth 5.3 Pairing",
        "price": 14999.0,
        "discount_price": 11999.0,
        "sku_prefix": "AA-PULSE",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.8,
        "review_count": 430,
        "images": [
            "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Driver": "40mm Titanium Dynamic", "Battery": "50 Hours (ANC Off)", "Noise Cancelling": "Hybrid ANC 42dB", "Connectivity": "Bluetooth 5.3 + 3.5mm Aux"}
    },
    {
        "brand": "aura-audio",
        "category": "audio",
        "name": "Aura Audio Studio ANC Max Professional Studio Headphones",
        "slug": "aura-studio-anc-max",
        "description": "Flagship studio monitor headphones with memory foam ear cushions, balanced acoustic chamber, transparency mode, and crystal clear call quality.",
        "short_description": "Flagship studio sound with plush memory foam earcups.",
        "highlight_features": "Audiophile Sound Tuning\nUltra-Soft Memory Foam\nENC Dual Mics for Calls\nFoldable Travel Case Included",
        "price": 18999.0,
        "discount_price": 14999.0,
        "sku_prefix": "AA-STUDIO-MAX",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.7,
        "review_count": 210,
        "images": [
            "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1583394838336-acd977736f90?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Driver": "45mm Neodymium Driver", "Battery": "40 Hours", "Weight": "260g", "Impedance": "32 Ohms"}
    },
    {
        "brand": "aura-audio",
        "category": "audio",
        "name": "Aura Audio Pods Pro Active Noise Cancelling TWS Earbuds",
        "slug": "aura-pods-pro",
        "description": "Compact true wireless earbuds with 35dB smart ANC, spatial 3D audio, IPX5 sweat resistance, and 36 hours total battery with wireless charging case.",
        "short_description": "Smart 35dB ANC, Spatial Audio & IPX5 Water Resistance.",
        "highlight_features": "35dB Smart Active Noise Cancellation\nSpatial Audio with Head Tracking\nIPX5 Splash & Sweat Resistant\nQi Wireless Charging Case",
        "price": 6999.0,
        "discount_price": 4999.0,
        "sku_prefix": "AA-PODS-PRO",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 680,
        "images": [
            "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Noise Cancellation": "35dB ANC", "Battery Life": "8h buds + 28h case", "Bluetooth": "v5.3", "Latency": "45ms Gaming Mode"}
    },
    {
        "brand": "aura-audio",
        "category": "audio",
        "name": "Aura Audio BassBoom 40W Portable Waterproof Bluetooth Speaker",
        "slug": "aura-bassboom-40w-speaker",
        "description": "Rugged outdoor 40W stereo speaker with deep bass radiators, RGB beat lighting, IPX7 waterproofing, and 24-hour party battery life.",
        "short_description": "40W IPX7 waterproof portable Bluetooth party speaker.",
        "highlight_features": "40W Powerful Stereo Sound\nIPX7 Submersible Waterproof\nRGB Beat-Synced LED Lights\n24 Hours Extended Battery",
        "price": 5499.0,
        "discount_price": 3799.0,
        "sku_prefix": "AA-SPK40W",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.6,
        "review_count": 185,
        "images": [
            "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1545454675-3531b543be5d?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Power": "40W RMS", "Battery": "24 Hours (7500mAh)", "Waterproof": "IPX7", "Bluetooth": "v5.3"}
    },

    # 3. Titan Compute (Laptops & Computers)
    {
        "brand": "titan-compute",
        "category": "laptops",
        "name": "Titan Compute Book Pro 16 (Core i9, 32GB RAM, 1TB SSD)",
        "slug": "titan-compute-book-16",
        "description": "Powerhouse creator laptop with 16-inch 3.2K 165Hz mini-LED display, Intel Core i9 14th Gen processor, NVIDIA GeForce RTX 4070 8GB GPU, and 32GB DDR5 memory.",
        "short_description": "Intel Core i9 14th Gen, RTX 4070, 3.2K Mini-LED Display.",
        "highlight_features": "Intel Core i9-14900HX\nNVIDIA RTX 4070 8GB\n32GB DDR5 + 1TB Gen4 SSD\n16-inch 3.2K 165Hz 100% DCI-P3",
        "price": 149999.0,
        "discount_price": 134999.0,
        "sku_prefix": "TC-B16",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.9,
        "review_count": 120,
        "images": [
            "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Processor": "Intel Core i9-14900HX", "Graphics": "RTX 4070 8GB", "RAM": "32 GB DDR5", "Storage": "1 TB NVMe SSD", "Display": "16-inch 3.2K Mini-LED"}
    },
    {
        "brand": "titan-compute",
        "category": "laptops",
        "name": "Titan Compute Creator 15 OLED Laptop (16GB RAM, 512GB SSD)",
        "slug": "titan-creator-15",
        "description": "Color-calibrated OLED laptop for photographers, UI designers, and creators with Intel Core Ultra 7 processor and all-day 14-hour battery life.",
        "short_description": "15.6-inch 2.8K OLED creator laptop with Core Ultra 7.",
        "highlight_features": "15.6-inch 2.8K 120Hz OLED\nIntel Core Ultra 7 155H\n16GB LPDDR5X RAM\n1.4kg Ultralight Aluminum Chassis",
        "price": 94999.0,
        "discount_price": 82999.0,
        "sku_prefix": "TC-CR15",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.7,
        "review_count": 85,
        "images": [
            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Processor": "Intel Core Ultra 7 155H", "RAM": "16 GB", "Storage": "512 GB SSD", "Display": "15.6-inch 2.8K OLED", "Weight": "1.42 kg"}
    },
    {
        "brand": "titan-compute",
        "category": "laptops",
        "name": "Titan Compute Air Slim 14 Magnesium Laptop (Intel Core i5, 16GB RAM)",
        "slug": "titan-air-slim-14",
        "description": "Ultra-thin 1.1kg magnesium-alloy laptop with 16-hour battery life, backlit keyboard, fingerprint sensor, and crisp anti-glare IPS display.",
        "short_description": "1.1kg Ultra-thin magnesium laptop with 16-hour battery.",
        "highlight_features": "1.19kg Magnesium-Alloy Body\nIntel Core i5 13th Gen\n16GB LPDDR5 RAM\nThunderbolt 4 Fast Charging",
        "price": 79999.0,
        "discount_price": 69999.0,
        "sku_prefix": "TC-AIR14",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.6,
        "review_count": 98,
        "images": [
            "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Processor": "Intel Core i5-1335U", "RAM": "16 GB", "Storage": "512 GB SSD", "Display": "14-inch FHD+ IPS", "Weight": "1.19 kg"}
    },
    {
        "brand": "titan-compute",
        "category": "laptops",
        "name": "Titan Compute 27-inch 4K UHD IPS Frameless Monitor",
        "slug": "titan-27-4k-monitor",
        "description": "Professional 27-inch 4K UHD color-accurate monitor with 99% sRGB, HDR400, USB-C 90W Power Delivery, and ergonomic height-adjustable stand.",
        "short_description": "27-inch 4K UHD IPS monitor with 90W USB-C PD.",
        "highlight_features": "27-inch 4K UHD (3840x2160) IPS\nType-C 90W Single Cable Setup\n99% sRGB & Delta E < 2 Accuracy\nHeight, Pivot & Swivel Stand",
        "price": 32999.0,
        "discount_price": 26999.0,
        "sku_prefix": "TC-MON27",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.8,
        "review_count": 140,
        "images": [
            "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Display": "27-inch 4K IPS", "Resolution": "3840 x 2160", "Ports": "USB-C 90W, 2x HDMI 2.0, DisplayPort", "Warranty": "3 Years"}
    },

    # 4. Zenith Electronics (Televisions & Large Appliances)
    {
        "brand": "zenith-elec",
        "category": "televisions",
        "name": "Zenith Electronics 55-inch 4K Ultra HD Smart QLED TV",
        "slug": "zenith-55-4k-qled",
        "description": "55-inch Quantum Dot 4K QLED television with Dolby Vision Atmos, Google TV OS, hands-free voice control, 120Hz refresh rate, and bezel-less metallic design.",
        "short_description": "55-inch 4K QLED with Dolby Vision, 120Hz & Google TV.",
        "highlight_features": "Quantum Dot 4K Ultra HD (3840 x 2160)\nDolby Vision & Dolby Atmos 40W Speakers\nGoogle TV with Hands-Free Voice Mic\n3x HDMI 2.1 Ports + eARC for Gaming",
        "price": 59999.0,
        "discount_price": 47999.0,
        "sku_prefix": "ZN-TV55-QLED",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.8,
        "review_count": 290,
        "images": [
            "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1461151304267-38535e780c79?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Screen Size": "55 inches", "Resolution": "4K Ultra HD (3840x2160)", "Sound": "40W Dolby Atmos", "Smart OS": "Google TV"}
    },
    {
        "brand": "zenith-elec",
        "category": "televisions",
        "name": "Zenith Electronics 65-inch 4K OLED Cinema TV",
        "slug": "zenith-65-4k-oled",
        "description": "Flagship 65-inch 4K OLED TV with self-lit pixels, infinite contrast ratio, 120Hz VRR G-Sync support, and 60W front-firing Dolby Atmos speakers.",
        "short_description": "65-inch Cinema 4K OLED with self-lit pixels & 120Hz VRR.",
        "highlight_features": "Self-Emitting 4K OLED Display Panel\n120Hz VRR, ALLM & G-Sync Compatible\n60W 4.2ch Dolby Atmos Built-in Soundbar\nUltra-Slim 3.8mm Blade Profile",
        "price": 149999.0,
        "discount_price": 124999.0,
        "sku_prefix": "ZN-TV65-OLED",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.9,
        "review_count": 88,
        "images": [
            "https://images.unsplash.com/photo-1577979749830-f1d742b96791?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Screen Size": "65 inches", "Resolution": "4K OLED (3840x2160)", "Sound": "60W 4.2 Channel", "Gaming": "120Hz VRR, ALLM"}
    },
    {
        "brand": "zenith-elec",
        "category": "televisions",
        "name": "Zenith Electronics 43-inch 4K Frameless Google Smart LED TV",
        "slug": "zenith-43-4k-smart-tv",
        "description": "43-inch 4K Smart TV with HDR10+, vivid color engine, Chromecast built-in, 24W box speakers, and access to 10,000+ streaming apps.",
        "short_description": "43-inch 4K Smart TV with HDR10+ and 24W Stereo Speakers.",
        "highlight_features": "4K Ultra HD Frameless Panel\nHDR10+ Dynamic Color Enhancer\nBuilt-in Chromecast & Dual-Band WiFi\n24W High-Fidelity Box Speakers",
        "price": 39999.0,
        "discount_price": 29999.0,
        "sku_prefix": "ZN-TV43-4K",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.5,
        "review_count": 180,
        "images": [
            "https://images.unsplash.com/photo-1461151304267-38535e780c79?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Screen Size": "43 inches", "Resolution": "4K Ultra HD", "Sound": "24W Stereo", "Refresh Rate": "60Hz"}
    },
    {
        "brand": "zenith-elec",
        "category": "televisions",
        "name": "Zenith Electronics 32-inch HD Ready Smart Android TV",
        "slug": "zenith-32-hd-smart-tv",
        "description": "Compact 32-inch bezel-less Smart TV with Android 11 OS, Dolby Audio, Google Assistant voice remote, and dual HDMI ports.",
        "short_description": "32-inch Bezel-less HD Smart TV with Dolby Audio.",
        "highlight_features": "Bezel-less HD Ready A+ Grade Panel\nAndroid 11 with Play Store Support\n20W Dolby Audio Stereo\nQuad Core Processor with 1GB RAM",
        "price": 18999.0,
        "discount_price": 12999.0,
        "sku_prefix": "ZN-TV32-HD",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.4,
        "review_count": 210,
        "images": [
            "https://images.unsplash.com/photo-1509281373149-e957c6296406?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1461151304267-38535e780c79?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Screen Size": "32 inches", "Resolution": "HD Ready (1366x768)", "Sound": "20W Dolby Audio", "OS": "Android TV"}
    },

    # 5. UrbanFit (Men's & Women's Fashion)
    {
        "brand": "urbanfit",
        "category": "mens-clothing",
        "name": "UrbanFit Pure Cotton Oxford Casual Shirt (Sky Blue)",
        "slug": "urbanfit-oxford-comfort-shirt",
        "description": "Tailored regular-fit long-sleeve casual shirt woven from 100% combed Oxford cotton. Features button-down collar and breathable all-day comfort.",
        "short_description": "100% Combed Oxford Cotton, Regular Fit, Button-down Collar.",
        "highlight_features": "100% Breathable Combed Cotton\nPre-shrunk Fabric\nClassic Oxford Texture\nMachine Wash Friendly",
        "price": 1999.0,
        "discount_price": 1199.0,
        "sku_prefix": "UF-OXF-SHT",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.4,
        "review_count": 410,
        "images": [
            "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Fabric": "100% Combed Cotton", "Fit": "Regular Fit", "Sleeve": "Full Sleeve", "Occasion": "Casual / Smart Casual"}
    },
    {
        "brand": "urbanfit",
        "category": "mens-clothing",
        "name": "UrbanFit Slim-Fit Dark Wash Stretch Denim Jeans",
        "slug": "urbanfit-slim-denim",
        "description": "Modern slim-fit stretchable jeans made from heavy-duty 12oz cotton-elastane denim. Finished in deep indigo with gentle whiskering.",
        "short_description": "Stretchable 12oz cotton denim with vintage indigo wash.",
        "highlight_features": "98% Cotton, 2% Elastane Stretch\nMid-Rise Waist with Zip Fly\nReinforced Rivets and Bar-tacking\nDurable Color-lock Dyeing",
        "price": 2499.0,
        "discount_price": 1499.0,
        "sku_prefix": "UF-JEANS-STR",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.5,
        "review_count": 520,
        "images": [
            "https://images.unsplash.com/photo-1542272604-780c96856453?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Material": "98% Cotton, 2% Elastane", "Fit": "Slim Fit", "Waist": "Mid-Rise", "Wash": "Dark Indigo Wash"}
    },
    {
        "brand": "urbanfit",
        "category": "womens-clothing",
        "name": "UrbanFit Floral Print Summer Tiered Maxi Dress",
        "slug": "urbanfit-summer-maxi-dress",
        "description": "Flattering A-line tiered maxi dress in soft viscose fabric with vibrant floral print, adjustable waist belt, and breathable lining.",
        "short_description": "Breathable viscose tiered maxi dress with floral print.",
        "highlight_features": "100% Breathable Rayon Viscose\nA-Line Tiered Silhouette\nV-Neckline with Elasticated Waist\nMachine Washable",
        "price": 2499.0,
        "discount_price": 1499.0,
        "sku_prefix": "UF-MAXI-DRS",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.5,
        "review_count": 180,
        "images": [
            "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Fabric": "100% Rayon Viscose", "Length": "Maxi (Ankle Length)", "Neck": "V-Neck", "Sleeve": "Flutter Sleeves"}
    },
    {
        "brand": "urbanfit",
        "category": "mens-clothing",
        "name": "UrbanFit Heavyweight Oversized Cotton T-Shirt (Charcoal)",
        "slug": "urbanfit-oversized-tee",
        "description": "Streetwear oversized drop-shoulder t-shirt crafted from 240 GSM bio-washed French terry cotton with ribbed crew neck.",
        "short_description": "240 GSM heavy cotton drop-shoulder streetwear tee.",
        "highlight_features": "240 GSM 100% Bio-Washed Combed Cotton\nDrop-Shoulder Relaxed Oversized Cut\nThick Non-Sagging Lycra Ribbed Collar\nFade-Resistant Reactive Pigment Dye",
        "price": 1499.0,
        "discount_price": 799.0,
        "sku_prefix": "UF-TEE-OVS",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 310,
        "images": [
            "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Fabric": "100% French Terry Cotton", "GSM": "240 GSM", "Fit": "Oversized Fit", "Style": "Streetwear"}
    },

    # 6. Kraft Home (Kitchenware & Cookware)
    {
        "brand": "kraft-home",
        "category": "kitchenware",
        "name": "Kraft Home Hard Anodized 5-Piece Non-Stick Cookware Set",
        "slug": "kraft-cookware-set",
        "description": "Heavy-gauge 5-piece hard anodized cookware set with 3-layer German granite non-stick coating, stay-cool bakelite handles, and induction base.",
        "short_description": "Hard Anodized 3-Layer Granite Cookware with Induction Base.",
        "highlight_features": "Hard-Anodized Aluminum Construction\n3-Layer PFOA-Free Granite Non-Stick\nCompatible with Gas, Induction & Radiant\nIncludes Kadhai, Fry Pan, Dosa Tawa & 2 Lids",
        "price": 8999.0,
        "discount_price": 5999.0,
        "sku_prefix": "KH-COOK5",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 320,
        "images": [
            "https://images.unsplash.com/photo-1584990347449-a3597c4146a8?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1583778176476-4a8b02a64c01?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Pieces": "5 Pieces", "Coating": "German 3-Layer Granite", "Base": "Induction Compatible", "Warranty": "2 Years"}
    },
    {
        "brand": "kraft-home",
        "category": "kitchenware",
        "name": "Kraft Home Smart Touch Digital Air Fryer (5.5 Litres)",
        "slug": "kraft-smart-air-fryer",
        "description": "1700W Rapid 360° Air Circulation fryer with 8 one-touch digital cooking presets, non-stick dishwasher-safe basket, and 90% less oil cooking.",
        "short_description": "5.5L Digital Touch Air Fryer with 8 Cooking Presets.",
        "highlight_features": "1700W 360-Degree Rapid Heat Circulation\nLarge 5.5L Family Capacity Basket\n8 One-Touch Preset Cooking Modes\nAuto-Shutoff & Overheat Protection",
        "price": 9999.0,
        "discount_price": 6999.0,
        "sku_prefix": "KH-AF55L",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.7,
        "review_count": 285,
        "images": [
            "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1588854337236-6889d631faa8?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Capacity": "5.5 Litres", "Power": "1700 Watts", "Temperature": "80°C - 200°C", "Timer": "60 Minutes"}
    },
    {
        "brand": "kraft-home",
        "category": "kitchenware",
        "name": "Kraft Home Tri-Ply Stainless Steel Heavy Bottom Kadhai (3.5L)",
        "slug": "kraft-triply-kadai",
        "description": "Heavy tri-ply construction with food-grade 304 stainless steel interior, heat-radiating aluminum core, and magnetic induction base.",
        "short_description": "Tri-ply 304 stainless steel 3.5L kadhai with tempered glass lid.",
        "highlight_features": "Tri-Ply 3-Layer Heavy Base 2.5mm Thick\nFood Grade SAS 304 Rust-Proof Steel\nStay-Cool Cast Steel Handles\nGas and Induction Stove Friendly",
        "price": 3499.0,
        "discount_price": 2499.0,
        "sku_prefix": "KH-KAD35L",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.6,
        "review_count": 160,
        "images": [
            "https://images.unsplash.com/photo-1583778176476-4a8b02a64c01?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584990347449-a3597c4146a8?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Material": "Tri-Ply Stainless Steel", "Capacity": "3.5 Litres", "Base": "Induction & Gas", "Warranty": "5 Years"}
    },

    # 7. Stellar Time (Smartwatches & Bands)
    {
        "brand": "stellar-time",
        "category": "wearables",
        "name": "Stellar Time Health Pro AMOLED Smartwatch",
        "slug": "stellar-health-pro",
        "description": "Premium stainless steel smartwatch with vibrant 1.43-inch AMOLED Always-On Display, dual-band GPS, 24/7 heart rate, SpO2 sensor, and 12-day battery life.",
        "short_description": "1.43-inch AMOLED display, GPS tracking & 12-day battery.",
        "highlight_features": "1.43-inch HD AMOLED 466x466\nBuilt-in Dual Frequency GPS\nSpO2, Heart Rate & Sleep Health Suite\n5ATM 50-Meter Water Resistance",
        "price": 7999.0,
        "discount_price": 5499.0,
        "sku_prefix": "ST-HLTH-PRO",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.7,
        "review_count": 310,
        "images": [
            "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Display": "1.43-inch AMOLED Always-On", "Battery": "Up to 12 Days", "Sensors": "Optical Heart Rate, SpO2, Accelerometer, GPS", "Water Resistance": "5ATM"}
    },
    {
        "brand": "stellar-time",
        "category": "wearables",
        "name": "Stellar Time Watch Active 3 Rugged Sports Watch",
        "slug": "stellar-watch-active-3",
        "description": "Military-grade shock resistant smartwatch with Bluetooth calling, AI voice assistant, 120+ sports workout modes, and rugged silicone strap.",
        "short_description": "Rugged military-grade sports smartwatch with Bluetooth calling.",
        "highlight_features": "HD Bluetooth Calling with Speaker & Mic\nMIL-STD-810H Drop Tested\n120+ Workout & Sports Modes\nComprehensive Sleep & Stress Tracking",
        "price": 4999.0,
        "discount_price": 2999.0,
        "sku_prefix": "ST-ACT3",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.5,
        "review_count": 489,
        "images": [
            "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Display": "1.39-inch HD TFT 360x360", "Battery": "7 Days Active Use", "Calling": "Bluetooth v5.2 Calling", "Protection": "IP68 Waterproof"}
    },
    {
        "brand": "stellar-time",
        "category": "wearables",
        "name": "Stellar Time Luxe Automatic Chronograph Leather Watch",
        "slug": "stellar-luxe-chronograph",
        "description": "Crafted analog-digital chronograph timepiece with sapphire crystal glass, 24-jewel automatic winding movement, and Italian top-grain leather strap.",
        "short_description": "Automatic chronograph with sapphire crystal and genuine leather.",
        "highlight_features": "Automatic Self-Winding 24-Jewel Movement\nScratch-Resistant Sapphire Crystal\nItalian Full-Grain Leather Strap\n100M Water Resistance",
        "price": 14999.0,
        "discount_price": 11499.0,
        "sku_prefix": "ST-CHRONO",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.8,
        "review_count": 78,
        "images": [
            "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Movement": "24-Jewel Automatic", "Glass": "Sapphire Crystal", "Strap": "Italian Leather", "Water Resistance": "100M"}
    },

    # 8. Apex Wear (Footwear & Sneakers)
    {
        "brand": "apex-wear",
        "category": "footwear",
        "name": "Apex Wear Air Velocity Retro High-Top Sneakers",
        "slug": "apex-air-velocity-retro",
        "description": "Iconic retro high-top basketball sneakers crafted with full-grain leather, padded collar, high-grip rubber cupsole, and air cushion unit.",
        "short_description": "Retro full-grain leather basketball sneakers with Air cushioning.",
        "highlight_features": "Full-Grain Synthetic Leather Upper\nAir-Cushioned Shock Absorbing Sole\nHigh-Traction Solid Rubber Outsole\nClassic High-Top Silhouette",
        "price": 6999.0,
        "discount_price": 4999.0,
        "sku_prefix": "AW-AIR-VEL",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.8,
        "review_count": 540,
        "images": [
            "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1552346154-21d32810aba3?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Sole": "Rubber with Air Unit", "Upper": "Full Grain Leather & Mesh", "Closure": "Lace-Up", "Weight": "380g"}
    },
    {
        "brand": "apex-wear",
        "category": "footwear",
        "name": "Apex Wear Sprint Runner Lightweight Running Shoes",
        "slug": "apex-sprint-runner",
        "description": "Engineered mesh running shoes with responsive foam midsole, breathable knit upper, ergonomic heel support, and anti-slip grooved sole.",
        "short_description": "Breathable engineered mesh running shoes with foam bounce.",
        "highlight_features": "Breathable Fly-Knit Mesh\nResponsive Ultra-Bounce Foam Sole\nReinforced Heel Counter\nLightweight Under 240g",
        "price": 4999.0,
        "discount_price": 3299.0,
        "sku_prefix": "APEX-SPRINT",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 390,
        "images": [
            "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Shoe Type": "Running / Training", "Sole": "High Density EVA + Rubber", "Upper": "Engineered Flyknit", "Weight": "235g"}
    },
    {
        "brand": "apex-wear",
        "category": "footwear",
        "name": "Apex Wear Handcrafted Leather Oxford Formal Shoes",
        "slug": "apex-leather-oxford-formal",
        "description": "Classic closed-lacing Oxford shoes handcrafted from premium genuine leather with cushioned memory foam footbed and anti-skid TPR sole.",
        "short_description": "Genuine leather handcrafted formal Oxford shoes.",
        "highlight_features": "100% Genuine Grain Leather\nOrthopedic Memory Foam Insole\nHand-Burnished Gloss Finish\nDurable TPR Anti-Skid Sole",
        "price": 3999.0,
        "discount_price": 2799.0,
        "sku_prefix": "AW-OXF-FORM",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.5,
        "review_count": 160,
        "images": [
            "https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1533867617858-e7b97e060509?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Upper": "Genuine Leather", "Sole": "Anti-Skid TPR", "Insole": "Memory Foam", "Color": "Tan Brown"}
    },
    {
        "brand": "apex-wear",
        "category": "footwear",
        "name": "Apex Wear Streetstyle Classic Canvas Low-Top Sneakers",
        "slug": "apex-canvas-sneakers",
        "description": "All-day comfort vulcanized canvas low-top sneakers in clean optic white with cushioned insole and signature waffle outsole.",
        "short_description": "Clean white classic low-top vulcanized canvas sneakers.",
        "highlight_features": "Heavy-Duty 10oz Canvas Fabric\nVulcanized Gum Rubber Waffle Sole\nDie-Cut EVA Cushioned Sockliner\nReinforced Brass Eyelets",
        "price": 2499.0,
        "discount_price": 1699.0,
        "sku_prefix": "AW-CNV-WHT",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.5,
        "review_count": 280,
        "images": [
            "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Material": "100% Cotton Canvas", "Sole": "Vulcanized Rubber", "Style": "Low-Top Casual", "Color": "Optic White"}
    },

    # 9. Volt Appliances (Air Conditioners & Large Appliances)
    {
        "brand": "volt-appliances",
        "category": "air-conditioners",
        "name": "Volt Appliances 1 Ton 3-Star Fast Cooling Split Air Conditioner",
        "slug": "volt-1t-split-ac",
        "description": "High-ambient cooling split AC capable of fast cooling even at 52°C outdoor temperatures, equipped with turbo mode and self-diagnosis.",
        "short_description": "1 Ton Fast Turbo Cooling AC for Bedrooms & Offices.",
        "highlight_features": "High Ambient Cooling up to 52°C\nTurbo Cool Mode for Instant Relief\nSelf-Clean & Auto-Diagnosis Function\n100% Copper Condenser Coil",
        "price": 35999.0,
        "discount_price": 28999.0,
        "sku_prefix": "VT-AC1T",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.4,
        "review_count": 125,
        "images": [
            "https://images.unsplash.com/photo-1585338107529-13afc5f02586?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1614633833026-072049d59392?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Tonnage": "1.0 Ton", "Star Rating": "3 Star", "Cooling": "Turbo High Ambient", "Warranty": "1 Year Comprehensive + 5 Years Compressor"}
    },
    {
        "brand": "volt-appliances",
        "category": "air-conditioners",
        "name": "Volt Appliances 1.5 Ton 5-Star Dual Inverter Split AC",
        "slug": "volt-15t-5star-ac",
        "description": "Super energy-efficient dual inverter split AC with 100% grooved copper tubes, active humidity controller, and 4-way air swing.",
        "short_description": "1.5 Ton 5-Star Dual Inverter with 100% Copper Coils.",
        "highlight_features": "5-Star Energy Rating with High ISEER 5.2\nDual Rotary Inverter Compressor\nActive Dehumidifier for Monsoons\nAnti-Corrosive Gold Fin Coating",
        "price": 47999.0,
        "discount_price": 38999.0,
        "sku_prefix": "VT-AC15T5S",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.7,
        "review_count": 210,
        "images": [
            "https://images.unsplash.com/photo-1614633833026-072049d59392?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1585338107529-13afc5f02586?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Tonnage": "1.5 Ton", "Star Rating": "5 Star", "Condenser": "100% Copper", "Refrigerant": "Eco-Friendly R32"}
    },
    {
        "brand": "volt-appliances",
        "category": "air-conditioners",
        "name": "Volt Appliances BLDC 1200mm Smart Ceiling Fan with Remote",
        "slug": "volt-bldc-smart-fan",
        "description": "Brushless DC 28W energy-saving ceiling fan with smart remote control, sleep timer, boost mode, and rust-proof aluminum aerodynamic blades.",
        "short_description": "28W BLDC Motor Energy Saving Ceiling Fan with Remote.",
        "highlight_features": "65% Power Saving (Only 28 Watts)\nSmart Remote with Speed Control & Timer\nHigh Air Delivery 230 CMM\nSilent Operation Even at Top Speed",
        "price": 3999.0,
        "discount_price": 2799.0,
        "sku_prefix": "VT-FAN-BLDC",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 340,
        "images": [
            "https://images.unsplash.com/photo-1595846519845-68e298c2edd8?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1585338107529-13afc5f02586?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Sweep": "1200 mm", "Power": "28 Watts", "Air Delivery": "230 CMM", "Warranty": "3 Years"}
    },

    # 10. Chroma Vision (Cameras & Photography)
    {
        "brand": "chroma-vision",
        "category": "cameras",
        "name": "Chroma Vision Alpha 4K Mirrorless Digital Camera",
        "slug": "chroma-vision-alpha-4k",
        "description": "Professional 24.2MP full-frame mirrorless camera with 4K 60fps video recording, 5-axis in-body image stabilization, and lightning fast eye-autofocus.",
        "short_description": "24.2MP Full-Frame sensor, 4K 60fps, 5-Axis In-Body Stabilization.",
        "highlight_features": "24.2MP Full-Frame CMOS Sensor\n4K 60p 10-bit 4:2:2 Video\nReal-time Eye & Animal Tracking AF\nDual SD Card Slots with USB-C Streaming",
        "price": 124999.0,
        "discount_price": 109999.0,
        "sku_prefix": "CV-ALPH4K",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.9,
        "review_count": 56,
        "images": [
            "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Sensor": "24.2MP Full-Frame Exmor CMOS", "Video": "4K 60p HDR", "ISO Range": "100-51200", "Weight": "509g"}
    },
    {
        "brand": "chroma-vision",
        "category": "cameras",
        "name": "Chroma Vision Travel 4K Creator Vlog Camera",
        "slug": "chroma-travel-4k",
        "description": "Ultra-compact vlog and travel camera with flip-out selfie touch screen, directional 3-capsule microphone with windscreen, and 4K recording.",
        "short_description": "Compact 4K vlogging camera with flip screen.",
        "highlight_features": "Vari-Angle Selfie LCD Touchscreen\nDirectional 3-Capsule Microphone\nProduct Showcase & Background Defocus Modes\nOne-Click Live Streaming via USB-C",
        "price": 44999.0,
        "discount_price": 38999.0,
        "sku_prefix": "CV-TRV4K",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 94,
        "images": [
            "https://images.unsplash.com/photo-1502920917128-1aa500764cbd?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Sensor": "1.0-inch 20.1MP Sensor", "Lens": "24-70mm f/1.8-2.8 ZEISS", "Video": "4K 30p / FHD 120p", "Weight": "294g"}
    },
    {
        "brand": "chroma-vision",
        "category": "cameras",
        "name": "Chroma Vision 50mm f/1.4 Prime Portrait Lens",
        "slug": "chroma-50mm-lens",
        "description": "Large aperture f/1.4 prime lens with ultra-quiet linear stepping motor, multi-layer nano coating, and circular 9-blade diaphragm for creamy bokeh.",
        "short_description": "50mm f/1.4 Large Aperture Prime Lens with Nano Coating.",
        "highlight_features": "Fast f/1.4 Maximum Aperture\nUltra-Quiet Stepping AF Motor\n9 Circular Aperture Blades for Bokeh\nDust & Splash Sealed Mount",
        "price": 28999.0,
        "discount_price": 23499.0,
        "sku_prefix": "CV-LENS50",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.8,
        "review_count": 65,
        "images": [
            "https://images.unsplash.com/photo-1617005082133-548c4dd27f35?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Focal Length": "50mm", "Aperture": "f/1.4 - f/16", "Filter Size": "67mm", "Weight": "420g"}
    },

    # 11. Saffron Touch (Skincare & Hygiene)
    {
        "brand": "saffron-touch",
        "category": "skincare",
        "name": "Saffron Touch 10% Niacinamide & Vitamin C Radiance Face Serum",
        "slug": "saffron-radiance-serum",
        "description": "Dermatologist-tested face serum formulated with pure 10% Niacinamide, Vitamin C, and Kakadu Plum extracts to fade blemishes and brighten skin tone.",
        "short_description": "10% Niacinamide + Vitamin C brightening facial serum.",
        "highlight_features": "10% Niacinamide (Vitamin B3) + 2% Zinc PCA\nLightweight Water-Based Non-Greasy Formula\nFragrance-Free, Paraben-Free, Cruelty-Free\nSuitable for All Skin Types",
        "price": 699.0,
        "discount_price": 499.0,
        "sku_prefix": "ST-SERUM-30M",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.7,
        "review_count": 620,
        "images": [
            "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1608248597359-052445fb846b?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Volume": "30 ml", "Key Actives": "10% Niacinamide, Vitamin C, Zinc", "Skin Type": "All Skin Types", "Format": "Dropper Bottle"}
    },
    {
        "brand": "saffron-touch",
        "category": "skincare",
        "name": "Saffron Touch Daily Hydrating Face Cleanser & Moisturizer Kit",
        "slug": "saffron-daily-care-kit",
        "description": "Complete 3-step daily skincare routine including gentle foaming face wash, hyaluronic acid moisturizer, and lightweight SPF 50 sun defense.",
        "short_description": "3-in-1 Daily Cleanser, Moisturizer and Sunscreen Kit.",
        "highlight_features": "Gentle Cleanser with Aloe & Centella\nCeramide & Hyaluronic Acid Moisturizer\nSPF 50 PA++++ Invisible Sunscreen\nClinically Proven 72-Hour Hydration",
        "price": 1799.0,
        "discount_price": 1299.0,
        "sku_prefix": "ST-KIT-3IN1",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.6,
        "review_count": 215,
        "images": [
            "https://images.unsplash.com/photo-1556228720-195a672e8a03?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Items Included": "Cleanser (100ml), Cream (50g), Sunscreen (50g)", "Formulation": "Chemical-Free Herbal", "Target": "Hydration & UV Protection"}
    },
    {
        "brand": "saffron-touch",
        "category": "skincare",
        "name": "Saffron Touch Kumkumadi Ayurvedic Night Radiance Facial Oil",
        "slug": "saffron-kumkumadi-oil",
        "description": "100% pure Ayurvedic facial oil infused with Kashmiri Saffron, Sandalwood, and 26 precious botanical herbs to rejuvenate skin overnight.",
        "short_description": "100% Pure Kashmiri Saffron & Herbal Night Glow Oil.",
        "highlight_features": "Pure Saffron (Kesar) & Sandalwood Extract\nCold-Pressed Organic Sesame Base\nRestores Skin Elasticity & Radiance\nFree from Mineral Oil & Synthetic Preservatives",
        "price": 1299.0,
        "discount_price": 899.0,
        "sku_prefix": "ST-KUMK-OIL",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.8,
        "review_count": 340,
        "images": [
            "https://images.unsplash.com/photo-1608248597359-052445fb846b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Volume": "30 ml", "Ingredients": "Kashmiri Saffron, Sandalwood, Lotus", "Usage": "Nightly Routine", "Certification": "Ayush Certified"}
    },

    # 12. PureBlend (Mixer Grinders & Kitchen Appliances)
    {
        "brand": "pureblend",
        "category": "kitchenware",
        "name": "PureBlend 1000W Heavy Duty 4-Jar Mixer Grinder",
        "slug": "pureblend-power-mixer",
        "description": "1000W copper motor mixer grinder with 4 stainless steel jars for heavy Indian wet/dry grinding, chutney making, and fruit juicing with pulp filter.",
        "short_description": "1000W 100% Copper Motor with 4 Heavy Duty Steel Jars.",
        "highlight_features": "1000W Pure Copper High-Torque Motor\n4 Food-Grade 304 Stainless Steel Jars\nAir-Cooling Ventilation Technology\nOverload Protector Switch",
        "price": 5999.0,
        "discount_price": 3999.0,
        "sku_prefix": "PB-MIX1000",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.5,
        "review_count": 195,
        "images": [
            "https://images.unsplash.com/photo-1570222094114-d054a817e56b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584990347449-a3597c4146a8?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Motor": "1000W Copper Motor", "Jars": "4 (1.5L, 1.25L, 0.8L, 0.4L)", "Speed": "3 Speeds + Pulse", "Warranty": "5 Years Motor Warranty"}
    },
    {
        "brand": "pureblend",
        "category": "kitchenware",
        "name": "PureBlend Nutri-Pro High-Speed 900W Smoothie Blender",
        "slug": "pureblend-nutri-blender",
        "description": "Compact high-speed bullet blender with 24,000 RPM stainless steel extractor blades, 2 Tritan travel cups with flip-top lids, and one-touch pulse.",
        "short_description": "900W 24,000 RPM Nutri Blender with 2 Travel Cups.",
        "highlight_features": "900W High-Torque Nutrient Extractor Motor\n2x BPA-Free Tritan Cups (700ml & 500ml)\n6-Leaf Hardened Stainless Steel Blades\nDishwasher Safe Parts",
        "price": 4499.0,
        "discount_price": 2999.0,
        "sku_prefix": "PB-NUTRI900",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.7,
        "review_count": 140,
        "images": [
            "https://images.unsplash.com/photo-1584990347449-a3597c4146a8?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1570222094114-d054a817e56b?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Power": "900 Watts", "RPM": "24,000 RPM", "Jars": "2 Tritan Cups", "Warranty": "2 Years"}
    },
    {
        "brand": "pureblend",
        "category": "kitchenware",
        "name": "PureBlend Hand Immersion Blender 400W with Whisk & Chopper",
        "slug": "pureblend-hand-blender",
        "description": "Ergonomic 400W multi-function stick blender with detachable stainless steel shaft, 500ml chopper bowl, balloon whisk, and 600ml measuring beaker.",
        "short_description": "4-in-1 Hand Blender with Chopper and Whisk Attachment.",
        "highlight_features": "400W Silent DC Motor with Turbo Boost\nFood Grade Stainless Steel Splash-Proof Guard\n500ml Quick-Chopping Bowl\nLightweight Ergonomic Soft-Grip Handle",
        "price": 2499.0,
        "discount_price": 1699.0,
        "sku_prefix": "PB-HAND400",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.4,
        "review_count": 95,
        "images": [
            "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1570222094114-d054a817e56b?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Power": "400 Watts", "Attachments": "Whisk, Chopper, Beaker", "Speed": "Variable + Turbo", "Warranty": "1 Year"}
    },

    # 13. Velocity Gear (Gaming Laptops & Accessories)
    {
        "brand": "velocity-gear",
        "category": "laptops",
        "name": "Velocity Gear Playbook 16 Gaming Laptop (RTX 4060, 240Hz)",
        "slug": "velocity-playbook-16",
        "description": "Dedicated gaming laptop with high-airflow dual fan cooling, RGB per-key mechanical keyboard, AMD Ryzen 7 7840HS, and 240Hz esports display.",
        "short_description": "AMD Ryzen 7, RTX 4060 8GB, 240Hz Esports Display.",
        "highlight_features": "AMD Ryzen 7 7840HS\nNVIDIA RTX 4060 140W TGP\n16-inch QHD+ 240Hz IPS\nDual Fan FrostCool V4",
        "price": 109999.0,
        "discount_price": 94999.0,
        "sku_prefix": "VG-PLAY16",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.8,
        "review_count": 164,
        "images": [
            "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Processor": "AMD Ryzen 7 7840HS", "Graphics": "RTX 4060 8GB", "RAM": "16 GB DDR5", "Storage": "1 TB SSD", "Display": "16-inch QHD+ 240Hz"}
    },
    {
        "brand": "velocity-gear",
        "category": "laptops",
        "name": "Velocity Gear RGB Hot-Swappable Mechanical Gaming Keyboard",
        "slug": "velocity-mechanical-keyboard",
        "description": "Tenkeyless 87-key mechanical gaming keyboard with hot-swappable linear red switches, per-key customizable RGB lighting, and braided USB-C cable.",
        "short_description": "Hot-swappable red switch mechanical keyboard with per-key RGB.",
        "highlight_features": "Factory Lubed Red Linear Mechanical Switches\nHot-Swappable 5-Pin PCB\nDouble-Shot PBT Shine-Through Keycaps\n100% Anti-Ghosting N-Key Rollover",
        "price": 4999.0,
        "discount_price": 3499.0,
        "sku_prefix": "VG-KEY87",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.7,
        "review_count": 230,
        "images": [
            "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Switches": "Linear Red", "Layout": "TKL 87 Keys", "RGB": "16.8M Colors", "Connectivity": "Detachable Type-C"}
    },
    {
        "brand": "velocity-gear",
        "category": "laptops",
        "name": "Velocity Gear 26K DPI Ultra-Lightweight Wireless Gaming Mouse",
        "slug": "velocity-gaming-mouse",
        "description": "54-gram lightweight wireless esports mouse with 26,000 DPI optical sensor, optical switches (80M clicks), and 90-hour battery life.",
        "short_description": "54g Ultra-lightweight 26K DPI wireless gaming mouse.",
        "highlight_features": "54g Honeycomb-Free Solid Lightweight Shell\nPixArt 26,000 DPI Optical Sensor\n1ms Ultra-Low Latency 2.4GHz + Bluetooth\n100% Virgin Grade PTFE Glides",
        "price": 3499.0,
        "discount_price": 2499.0,
        "sku_prefix": "VG-MOUSE54",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.6,
        "review_count": 115,
        "images": [
            "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"DPI": "26,000 DPI", "Weight": "54 grams", "Battery": "90 Hours", "Switches": "Optical 80M Clicks"}
    },

    # 14. Nordic Living (Furniture)
    {
        "brand": "nordic-living",
        "category": "furniture",
        "name": "Nordic Living Solid Engineered Wood Ergonomic Study Desk",
        "slug": "nordic-living-work-desk",
        "description": "Minimalist Scandinavian work desk with integrated cable organizer tray, drawer storage, water-resistant matte tabletop, and steel frame.",
        "short_description": "Minimalist study/office desk with cable management & drawer.",
        "highlight_features": "Thick Engineered Wood with Scratch-Proof Laminate\nHeavy-Duty Powder-Coated Steel Legs\nIntegrated Cable Management Grommets\nEasy 20-Minute Tool-Free Assembly",
        "price": 12999.0,
        "discount_price": 8999.0,
        "sku_prefix": "NL-DESK-WD",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 175,
        "images": [
            "https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Dimensions": "120 x 60 x 75 cm", "Material": "Engineered Wood + Steel", "Weight Capacity": "100 kg", "Color": "Natural Teak & Black"}
    },
    {
        "brand": "nordic-living",
        "category": "furniture",
        "name": "Nordic Living 3-Seater Premium Fabric Sofa (Forest Green)",
        "slug": "nordic-living-3s-sofa",
        "description": "Contemporary 3-seater sofa with high-density foam cushioning, soft breathable velvet fabric upholstery, solid Sheesham wood legs, and lumbar cushions.",
        "short_description": "Comfortable 3-seater living room sofa in forest green fabric.",
        "highlight_features": "High-Resilience 32-Density Foam Seating\nStain-Resistant Breathable Fabric\nSolid Kiln-Dried Hardwood Internal Frame\nIncludes 2 Plush Lumbar Cushions",
        "price": 34999.0,
        "discount_price": 24999.0,
        "sku_prefix": "NL-SOFA3S",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.8,
        "review_count": 92,
        "images": [
            "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Dimensions": "198 x 85 x 82 cm", "Seating": "3 Persons", "Frame": "Solid Hardwood", "Warranty": "3 Years Warranty"}
    },
    {
        "brand": "nordic-living",
        "category": "furniture",
        "name": "Nordic Living High-Back Ergonomic Mesh Office Chair",
        "slug": "nordic-ergonomic-chair",
        "description": "Ergonomic executive chair with breathable Korean mesh back, 3D adjustable armrests, synchronized tilt mechanism, and Class-4 hydraulic gas lift.",
        "short_description": "High-back mesh ergonomic desk chair with lumbar support.",
        "highlight_features": "Adaptive Dynamic Lumbar Support\n3D Multi-Directional Padded Armrests\nHeavy-Duty Metal Base (150kg Rated)\nBreathable High-Tension Mesh",
        "price": 14999.0,
        "discount_price": 10499.0,
        "sku_prefix": "NL-CHAIR-ERGO",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.7,
        "review_count": 210,
        "images": [
            "https://images.unsplash.com/photo-1580481077198-c8478623d217?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1518455027359-f3f8164ba6bd?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Gas Lift": "Class 4 BIFMA Certified", "Mechanism": "Multi-Lock Synchro Tilt", "Weight Capacity": "150 kg", "Warranty": "3 Years"}
    },

    # 15. Royal Weave (Ethnic Fashion)
    {
        "brand": "royal-weave",
        "category": "womens-clothing",
        "name": "Royal Weave Handloom Silk Kurta & Dupatta Set",
        "slug": "royal-weave-handloom-kurta",
        "description": "Authentic handloom-inspired women's Anarkali kurta set with zari border, lightweight organza dupatta, and comfortable palazzo pants.",
        "short_description": "Handloom silk kurta with zari border & organza dupatta.",
        "highlight_features": "Pure Handloom Silk Blend Fabric\nIntricate Gold Zari Weave Borders\n3-Piece Set: Kurta, Dupatta, Palazzo\nComfortable All-Day Festive Fit",
        "price": 3499.0,
        "discount_price": 2299.0,
        "sku_prefix": "RW-WKURT-SET",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.7,
        "review_count": 270,
        "images": [
            "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Fabric": "Chanderi Silk Blend", "Style": "Straight Kurta Set", "Dupatta": "Organza with Zari", "Occasion": "Festive / Ethnic"}
    },
    {
        "brand": "royal-weave",
        "category": "mens-clothing",
        "name": "Royal Weave Silk Blend Embroidered Kurta Pajama Set",
        "slug": "royal-weave-men-kurta-set",
        "description": "Intricately designed festive men's kurta set in raw silk blend with floral thread work on the mandarin collar and matching churidar pants.",
        "short_description": "Festive embroidered silk blend kurta with churidar.",
        "highlight_features": "Art Silk Blend with Jacquard Weave\nMandarin Collar with Resham Embroidery\nIncludes Kurta + Drawstring Churidar\nIdeal for Weddings & Festive Celebrations",
        "price": 4999.0,
        "discount_price": 3199.0,
        "sku_prefix": "RW-MKURT",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.7,
        "review_count": 135,
        "images": [
            "https://images.unsplash.com/photo-1617137984095-74e4e5e3613f?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Fabric": "Silk Blend", "Pattern": "Embroidered", "Includes": "Kurta & Churidar", "Care": "Dry Clean Recommended"}
    },
    {
        "brand": "royal-weave",
        "category": "womens-clothing",
        "name": "Royal Weave Banarasi Pure Katan Silk Saree (Royal Crimson)",
        "slug": "royal-weave-banarasi-saree",
        "description": "Handwoven Banarasi Katan silk saree featuring rich golden zari floral jaal work, heavy meenakari pallu, and matching running blouse piece.",
        "short_description": "Handwoven Banarasi Katan silk saree with golden zari jaal.",
        "highlight_features": "100% Pure Katan Silk Weave\nRich Gold Zari Kadwa Floral Jaal\nIncludes 80cm Unstitched Blouse Piece\nComes with Silk Mark Authentication",
        "price": 8999.0,
        "discount_price": 5999.0,
        "sku_prefix": "RW-SAR-BAN",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.9,
        "review_count": 190,
        "images": [
            "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Fabric": "Pure Katan Silk", "Length": "6.3 Meters with Blouse", "Zari": "Gold Zari", "Occasion": "Bridal / Wedding"}
    },

    # 16. EvoSound (Audio & Soundbars)
    {
        "brand": "evosound",
        "category": "audio",
        "name": "EvoSound Cinematic 120W Dolby Atmos Bluetooth Soundbar",
        "slug": "evosound-mini-soundbar",
        "description": "Compact 120W soundbar with built-in dual subwoofers, HDMI ARC, optical input, Bluetooth 5.0, and cinema dialogue enhancement mode.",
        "short_description": "120W Dolby Atmos Soundbar with Built-in Subwoofers.",
        "highlight_features": "120W Peak Power Output\nDolby Digital & Atmos Audio\nHDMI ARC, Optical, Aux & Bluetooth\nDedicated Cinema, Music & News EQ",
        "price": 7999.0,
        "discount_price": 5999.0,
        "sku_prefix": "EVO-BAR120",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.5,
        "review_count": 145,
        "images": [
            "https://images.unsplash.com/photo-1545454675-3531b543be5d?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Output": "120 Watts", "Channels": "2.1 Channel", "Inputs": "HDMI ARC, Optical, USB, Bluetooth", "Warranty": "1 Year"}
    },
    {
        "brand": "evosound",
        "category": "audio",
        "name": "EvoSound Theater 240W 5.1ch Surround Soundbar with Wireless Subwoofer",
        "slug": "evosound-theater-51-soundbar",
        "description": "Full home theater 240W system with wireless active subwoofer, two rear satellite speakers, Dolby Atmos 3D audio, and HDMI eARC.",
        "short_description": "240W 5.1 Channel Home Theater with Wireless Subwoofer.",
        "highlight_features": "240W Cinematic Surround Power\nWireless Down-Firing 6.5-inch Subwoofer\n2x Wireless Rear Surround Satellites\nDolby Atmos & DTS Virtual:X Decoding",
        "price": 16999.0,
        "discount_price": 12999.0,
        "sku_prefix": "EVO-BAR240",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.7,
        "review_count": 82,
        "images": [
            "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1545454675-3531b543be5d?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Output": "240 Watts RMS", "Channels": "5.1 Channel", "Subwoofer": "6.5-inch Wireless", "Warranty": "1 Year"}
    },

    # 17. FrostTech (Refrigerators & Large Appliances)
    {
        "brand": "frosttech",
        "category": "refrigerators",
        "name": "FrostTech 340L Double Door Frost-Free Smart Inverter Refrigerator",
        "slug": "frosttech-260l-frost-free",
        "description": "340L 3-star smart inverter double door refrigerator with multi-airflow cooling, convertible vegetable box, stabilizer-free operation, and toughened glass shelves.",
        "short_description": "340L Frost-Free Double Door with Multi Air-Flow Cooling.",
        "highlight_features": "340L Frost-Free Multi Air-Flow System\nDigital Smart Inverter Compressor\nConvertible Veg Box with Humidity Control\n10-Year Compressor Warranty",
        "price": 36999.0,
        "discount_price": 29999.0,
        "sku_prefix": "FT-REF340L",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 210,
        "images": [
            "https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Capacity": "340 Litres", "Energy Rating": "3 Star", "Cooling Technology": "Frost-Free Multi-Airflow", "Warranty": "1 Year Product + 10 Years Compressor"}
    },
    {
        "brand": "frosttech",
        "category": "refrigerators",
        "name": "FrostTech 580L Side-by-Side Inverter Refrigerator with Water Dispenser",
        "slug": "frosttech-580l-sbs-refrigerator",
        "description": "Luxury 580L side-by-side refrigerator in matte black steel with exterior digital touch LED display, auto-ice maker, and dual cooling zones.",
        "short_description": "580L Side-by-Side Refrigerator with Water Dispenser.",
        "highlight_features": "580L Massive Side-by-Side Storage\nBuilt-in Cold Water Dispenser\nTwin Inverter Dual-Fan Cooling\nSuper Freeze & Holiday Smart Modes",
        "price": 74999.0,
        "discount_price": 62999.0,
        "sku_prefix": "FT-REF580SBS",
        "is_featured": True,
        "is_bestseller": False,
        "rating_avg": 4.9,
        "review_count": 75,
        "images": [
            "https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Capacity": "580 Litres", "Door Style": "Side by Side", "Dispenser": "Water Dispenser", "Finish": "Matte Black Steel"}
    },
    {
        "brand": "frosttech",
        "category": "refrigerators",
        "name": "FrostTech 190L Direct-Cool Single Door Refrigerator (5-Star Inverter)",
        "slug": "frosttech-190l-single-door",
        "description": "Compact 190L 5-star single door refrigerator with fast ice making technology, base drawer for vegetables, and floral blue toughened door finish.",
        "short_description": "190L 5-Star Energy Saver Single Door Refrigerator.",
        "highlight_features": "5-Star Energy Efficiency (Consumes < 110 Units/Year)\n1-Hour Fast Ice Making Zone\nBase Stand Drawer for Onions & Potatoes\nStabilizer Free 90V - 300V",
        "price": 19999.0,
        "discount_price": 14999.0,
        "sku_prefix": "FT-REF190L",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.5,
        "review_count": 310,
        "images": [
            "https://images.unsplash.com/photo-1571175443880-49e1d25b2bc5?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1584568694244-14fbdf83bd30?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Capacity": "190 Litres", "Rating": "5 Star Inverter", "Defrosting": "Direct Cool", "Warranty": "10 Years Compressor"}
    },

    # 18. GroomPro (Grooming & Personal Care)
    {
        "brand": "groompro",
        "category": "grooming",
        "name": "GroomPro Precision Pro Cordless Beard Trimmer",
        "slug": "groompro-precision-trimmer",
        "description": "Self-sharpening titanium ceramic blade trimmer with 40 length settings (0.5mm - 20mm), digital LED battery display, and 120-minute cordless runtime.",
        "short_description": "Cordless trimmer with 40 length settings & LED battery screen.",
        "highlight_features": "Self-Sharpening Titanium-Coated Blades\n40 Precision Length Settings (0.5mm steps)\n120-Minute Runtime with Fast USB-C Charging\n100% IPX7 Fully Washable Body",
        "price": 2499.0,
        "discount_price": 1699.0,
        "sku_prefix": "GP-TRIM40",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 450,
        "images": [
            "https://images.unsplash.com/photo-1621607512214-68297480165e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1599351431202-1e0f0137899a?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Blade": "Titanium-Ceramic", "Length Settings": "40 (0.5 - 20mm)", "Battery": "120 Mins Lithium-Ion", "Waterproof": "IPX7"}
    },
    {
        "brand": "groompro",
        "category": "grooming",
        "name": "GroomPro 5-in-1 Multi-Grooming Styling Kit",
        "slug": "groompro-5in1-kit",
        "description": "All-in-one grooming set with full-size trimmer, precision detailer, nose & ear trimmer, body groomer, micro foil shaver, and 5 comb guards.",
        "short_description": "5-in-1 Complete Beard, Hair & Body Grooming Set.",
        "highlight_features": "5 Interchangeable Stainless Steel Heads\nUp to 90 Minutes Cordless Runtime\nSelf-Sharpening Rust-Proof Steel Blades\nIncludes Storage Stand & Travel Pouch",
        "price": 3499.0,
        "discount_price": 2299.0,
        "sku_prefix": "GP-KIT5IN1",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.5,
        "review_count": 180,
        "images": [
            "https://images.unsplash.com/photo-1599351431202-1e0f0137899a?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1621607512214-68297480165e?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Heads": "5 Attachments", "Battery": "90 Mins Fast Charge", "Body": "Washable Attachments", "Warranty": "2 Years"}
    },
    {
        "brand": "groompro",
        "category": "grooming",
        "name": "GroomPro Salon Ionic Professional 2000W Hair Dryer",
        "slug": "groompro-hair-dryer",
        "description": "Salon-grade 2000W AC motor hair dryer with tourmaline ionic conditioning, 3 heat / 2 speed settings, and cool-shot button for frizz-free hair.",
        "short_description": "2000W Ionic AC Motor Professional Hair Dryer.",
        "highlight_features": "2000W High-Velocity Long-Life AC Motor\nTourmaline Ionic Technology for Zero Frizz\nIncludes Concentrator & Diffuser Nozzles\n3 Heat / 2 Speed with Cold Shot Lock",
        "price": 2999.0,
        "discount_price": 1899.0,
        "sku_prefix": "GP-DRY2000",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 210,
        "images": [
            "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1621607512214-68297480165e?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Power": "2000 Watts", "Technology": "Ionic Conditioning", "Cord": "2.5 Meter Salon Cord", "Warranty": "2 Years"}
    },

    # 19. Lumina Light (Decor & Lighting)
    {
        "brand": "lumina-light",
        "category": "decor-lighting",
        "name": "Lumina Smart Ambient RGB Floor Lamp with WiFi & App Control",
        "slug": "lumina-smart-ambient-lamp",
        "description": "Corner ambient mood lighting floor lamp with 16 million colors, music sync rhythm mode, Alexa & Google Assistant voice control, and timer schedule.",
        "short_description": "16 Million Colors RGB Corner Floor Lamp with Alexa Control.",
        "highlight_features": "16 Million RGB Colors + Warm/Cool White\nMusic Reactive Rhythm Mode\nVoice Control (Works with Alexa & Google Home)\nSleek 140cm Aluminum Alloy Pillar",
        "price": 2999.0,
        "discount_price": 1999.0,
        "sku_prefix": "LL-RGB-LMP",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.6,
        "review_count": 340,
        "images": [
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Height": "140 cm", "Connectivity": "WiFi 2.4GHz + Bluetooth", "Power": "20 Watts LED", "Lifespan": "50,000 Hours"}
    },
    {
        "brand": "lumina-light",
        "category": "decor-lighting",
        "name": "Lumina Smart WiFi LED Strip Lights (5 Meters, Music Sync)",
        "slug": "lumina-led-strip-5m",
        "description": "5-meter flexible adhesive RGBIC LED light strip with segmented color control, built-in mic for music sync, and smart app scheduling.",
        "short_description": "5M Segmented RGBIC Smart LED Strip with Music Sync.",
        "highlight_features": "RGBIC Individual Segment Color Control\nBuilt-in High Sensitivity Music Mic\n3M Heavy-Duty Adhesive Backing\nApp & Alexa Voice Controllable",
        "price": 1999.0,
        "discount_price": 1199.0,
        "sku_prefix": "LL-STRIP-5M",
        "is_featured": False,
        "is_bestseller": True,
        "rating_avg": 4.5,
        "review_count": 480,
        "images": [
            "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Length": "5 Meters (16.4 ft)", "LED Count": "150 LEDs", "Control": "WiFi + App + Remote", "Voltage": "12V DC"}
    },
    {
        "brand": "lumina-light",
        "category": "decor-lighting",
        "name": "Lumina Modern Minimalist Pendant Ceiling Chandelier Light",
        "slug": "lumina-pendant-light",
        "description": "Nordic matte black geometric pendant ceiling hanging lamp with warm white LED filament bulb for dining tables, bedrooms, and cafes.",
        "short_description": "Matte black geometric ceiling pendant lamp fixture.",
        "highlight_features": "Industrial Powder-Coated Metal Cage\nAdjustable 1.2M Fabric Hanging Cord\nStandard E27 Lamp Holder (Bulb Included)\nEasy Ceiling Rosette Mounting",
        "price": 2499.0,
        "discount_price": 1499.0,
        "sku_prefix": "LL-PEND-BLK",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.6,
        "review_count": 92,
        "images": [
            "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Material": "Metal & Iron", "Base": "E27", "Cord Length": "120 cm Adjustable", "Color": "Matte Black"}
    },

    # 20. EcoBreeze (Air Conditioners & Large Appliances)
    {
        "brand": "ecobreeze",
        "category": "air-conditioners",
        "name": "EcoBreeze 1.5 Ton 5-Star AI Inverter Split AC (100% Copper)",
        "slug": "ecobreeze-15t-inverter-ac",
        "description": "5-Star energy-saving AI inverter split air conditioner with 100% copper condenser, 4-in-1 convertible cooling, PM 2.5 air filter, and 4-way swing.",
        "short_description": "1.5 Ton 5-Star AI Inverter Split AC with PM2.5 Air Filter.",
        "highlight_features": "5-Star Energy Efficiency (ISEER 5.2)\n100% Grooved Copper Tubes with Blue Fin Coating\n4-in-1 Convertible Flexi-Cooling\nPM 2.5 Anti-Bacterial Micro Filter",
        "price": 45999.0,
        "discount_price": 36999.0,
        "sku_prefix": "EB-AC15T",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.7,
        "review_count": 310,
        "images": [
            "https://images.unsplash.com/photo-1614633833026-072049d59392?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1585338107529-13afc5f02586?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Tonnage": "1.5 Ton", "Star Rating": "5 Star", "Condenser": "100% Copper", "Refrigerant": "Eco-Friendly R32"}
    },
    {
        "brand": "ecobreeze",
        "category": "air-conditioners",
        "name": "EcoBreeze 1 Ton 3-Star Rapid Inverter Split Air Conditioner",
        "slug": "ecobreeze-1t-inverter-ac",
        "description": "Compact and quiet inverter split AC designed for bedrooms up to 120 sq.ft, with 100% copper condenser and sleep eco-mode.",
        "short_description": "1 Ton 3-Star Silent Inverter AC with Sleep Eco-Mode.",
        "highlight_features": "Fast Cooling for Rooms up to 120 sq ft\nUltra-Quiet 24dB Sleep Operation\nAnti-Corrosive Hydrophilic Blue Fins\nR32 Zero Ozone Depletion Refrigerant",
        "price": 34999.0,
        "discount_price": 27999.0,
        "sku_prefix": "EB-AC1T3S",
        "is_featured": False,
        "is_bestseller": False,
        "rating_avg": 4.5,
        "review_count": 140,
        "images": [
            "https://images.unsplash.com/photo-1585338107529-13afc5f02586?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1614633833026-072049d59392?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"Tonnage": "1.0 Ton", "Star Rating": "3 Star", "Condenser": "100% Copper", "Sound Level": "24 dB"}
    },
    {
        "brand": "ecobreeze",
        "category": "air-conditioners",
        "name": "EcoBreeze True HEPA Smart Room Air Purifier (PM2.5 Real-Time Display)",
        "slug": "ecobreeze-hepa-air-purifier",
        "description": "Smart air purifier with H13 True HEPA filter, activated carbon filter for odors, real-time laser PM2.5 AQI digital screen, and app control.",
        "short_description": "H13 True HEPA Air Purifier with Real-time PM2.5 AQI Display.",
        "highlight_features": "H13 Medical Grade True HEPA 99.97% Filtration\nHigh CADR 380 m3/h for Large Rooms up to 450 sq ft\nLaser Air Quality Sensor with 4-Color AQI Ring\nWhisper-Quiet 22dB Sleep Mode",
        "price": 12999.0,
        "discount_price": 8999.0,
        "sku_prefix": "EB-PUR-H13",
        "is_featured": True,
        "is_bestseller": True,
        "rating_avg": 4.8,
        "review_count": 220,
        "images": [
            "https://images.unsplash.com/photo-1585338107529-13afc5f02586?auto=format&fit=crop&w=800&q=80",
            "https://images.unsplash.com/photo-1614633833026-072049d59392?auto=format&fit=crop&w=800&q=80",
        ],
        "specs": {"CADR": "380 m3/h", "Filter Type": "H13 True HEPA + Carbon", "Room Coverage": "Up to 450 sq ft", "Noise": "22 dB - 52 dB"}
    },
]


async def seed_data():
    logger.info("Initializing database schemas...")
    await init_db()

    async with AsyncSessionLocal() as session:
        logger.info("Refreshing catalog and product images...")
        await session.execute(delete(ProductAttribute))
        await session.execute(delete(ProductImage))
        await session.execute(delete(ProductVariant))
        await session.execute(delete(Product))
        await session.execute(delete(Category))
        await session.execute(delete(Brand))
        await session.flush()

        p_cat_read = Permission(code="catalog:read", name="View Catalog", description="View products & categories")
        p_cat_write = Permission(code="catalog:write", name="Manage Catalog", description="Add, edit, delete products & categories")
        p_ord_read = Permission(code="orders:read", name="View Orders", description="View customer orders")
        p_ord_manage = Permission(code="orders:manage", name="Manage Orders", description="Update order status & refunds")
        p_usr_manage = Permission(code="users:manage", name="Manage Users", description="Manage user accounts & permissions")
        p_aud_read = Permission(code="audit:read", name="View Audit Logs", description="Access security audit logs")
        p_rev_write = Permission(code="reviews:write", name="Write Reviews", description="Post product reviews")

        p_res = await session.execute(select(Permission))
        if not p_res.scalars().all():
            session.add_all([p_cat_read, p_cat_write, p_ord_read, p_ord_manage, p_usr_manage, p_aud_read, p_rev_write])
            await session.flush()

        r_check = await session.execute(select(Role).where(Role.name == "ADMIN"))
        admin_role = r_check.scalar_one_or_none()
        if not admin_role:
            admin_role = Role(
                name="ADMIN",
                description="Super Administrator",
                permissions=[p_cat_read, p_cat_write, p_ord_read, p_ord_manage, p_usr_manage, p_aud_read, p_rev_write],
            )
            manager_role = Role(
                name="MANAGER",
                description="Catalog & Store Manager",
                permissions=[p_cat_read, p_cat_write, p_ord_read, p_ord_manage, p_aud_read],
            )
            support_role = Role(
                name="SUPPORT",
                description="Customer Support Specialist",
                permissions=[p_cat_read, p_ord_read, p_ord_manage],
            )
            customer_role = Role(
                name="CUSTOMER",
                description="Registered Customer",
                permissions=[p_cat_read, p_ord_read, p_rev_write],
            )
            session.add_all([admin_role, manager_role, support_role, customer_role])
            await session.flush()
        else:
            customer_role = (await session.execute(select(Role).where(Role.name == "CUSTOMER"))).scalar_one()

        u_check = await session.execute(select(User).where(User.email == "admin@hashkart.demo"))
        if not u_check.scalar_one_or_none():
            admin_user = User(
                email="admin@hashkart.demo",
                password_hash=get_password_hash("AdminPass123!"),
                full_name="Rajesh Sharma (Admin)",
                first_name="Rajesh",
                last_name="Sharma",
                phone_number="+91 9876543210",
                account_status="ACTIVE",
                is_active=True,
                is_verified=True,
                roles=[admin_role],
            )
            customer_user = User(
                email="customer@hashkart.demo",
                password_hash=get_password_hash("CustomerPass123!"),
                full_name="Priya Patel",
                first_name="Priya",
                last_name="Patel",
                phone_number="+91 9876543211",
                account_status="ACTIVE",
                is_active=True,
                is_verified=True,
                roles=[customer_role],
            )
            session.add_all([admin_user, customer_user])
            await session.flush()

        logger.info("Seeding hierarchical categories with high-res category icons...")
        category_map = {}
        for cat_data in CATEGORIES_DATA:
            top_cat = Category(
                name=cat_data["name"],
                slug=cat_data["slug"],
                display_order=cat_data["display_order"],
                image_url=cat_data["image_url"],
                is_active=True,
            )
            session.add(top_cat)
            await session.flush()
            category_map[cat_data["slug"]] = top_cat

            for sub_data in cat_data.get("subcategories", []):
                sub_cat = Category(
                    name=sub_data["name"],
                    slug=sub_data["slug"],
                    display_order=sub_data["display_order"],
                    image_url=sub_data["image_url"],
                    parent_id=top_cat.id,
                    is_active=True,
                )
                session.add(sub_cat)
                await session.flush()
                category_map[sub_data["slug"]] = sub_cat

        logger.info("Seeding 20 brands...")
        brand_map = {}
        for b_data in BRANDS_DATA:
            brand = Brand(
                name=b_data["name"],
                slug=b_data["slug"],
                description=b_data["description"],
                is_featured=b_data.get("is_featured", False),
                is_active=True,
            )
            session.add(brand)
            await session.flush()
            brand_map[b_data["slug"]] = brand

        logger.info("Seeding curated catalog products with matching high-definition images...")
        for item in PRODUCTS_CATALOG:
            cat = category_map[item["category"]]
            br = brand_map[item["brand"]]

            prod = Product(
                category_id=cat.id,
                brand_id=br.id,
                name=item["name"],
                slug=item["slug"],
                description=item["description"],
                short_description=item["short_description"],
                highlight_features=item["highlight_features"],
                status="ACTIVE",
                visibility="SEARCH_CATALOG",
                is_active=True,
                is_featured=item.get("is_featured", False),
                is_bestseller=item.get("is_bestseller", False),
                rating_avg=item.get("rating_avg", 4.5),
                review_count=item.get("review_count", 120),
            )
            session.add(prod)
            await session.flush()

            v1 = ProductVariant(
                product_id=prod.id,
                sku=f"{item['sku_prefix']}-V1",
                title="Standard Edition / Default Color",
                price=item["price"],
                discount_price=item["discount_price"],
                stock_quantity=random.randint(25, 80),
            )
            v2 = ProductVariant(
                product_id=prod.id,
                sku=f"{item['sku_prefix']}-V2",
                title="Pro Edition / Deluxe",
                price=item["price"] + 4000.0,
                discount_price=item["discount_price"] + 3200.0,
                stock_quantity=random.randint(15, 50),
            )
            session.add_all([v1, v2])
            await session.flush()

            imgs = item.get("images", [])
            for idx, img_url in enumerate(imgs):
                p_img = ProductImage(
                    product_id=prod.id,
                    variant_id=v1.id if idx == 0 else v2.id,
                    image_url=img_url,
                    is_primary=(idx == 0),
                    display_order=idx + 1,
                    alt_text=f"{prod.name} - View {idx + 1}",
                )
                session.add(p_img)

            for k, v in item.get("specs", {}).items():
                p_attr = ProductAttribute(
                    product_id=prod.id,
                    attribute_name=k,
                    attribute_value=str(v),
                )
                session.add(p_attr)

        logger.info("Seeding coupons...")
        c_check = await session.execute(select(Coupon))
        if not c_check.scalars().all():
            now = datetime.now(timezone.utc)
            c1 = Coupon(code="WELCOME10", discount_type="PERCENTAGE", discount_value=10.0, min_order_value=1000.0, max_discount_amount=1500.0, usage_limit=1000, usage_per_user=1, valid_from=now - timedelta(days=1), valid_to=now + timedelta(days=365), is_active=True)
            c2 = Coupon(code="FESTIVE500", discount_type="FIXED", discount_value=500.0, min_order_value=3000.0, usage_limit=500, usage_per_user=1, valid_from=now - timedelta(days=1), valid_to=now + timedelta(days=90), is_active=True)
            c3 = Coupon(code="FLASH20", discount_type="PERCENTAGE", discount_value=20.0, min_order_value=2000.0, max_discount_amount=2000.0, usage_limit=200, usage_per_user=2, valid_from=now - timedelta(days=1), valid_to=now + timedelta(days=180), is_active=True)
            session.add_all([c1, c2, c3])

        logger.info("Seeding trending search queries...")
        sqa_check = await session.execute(select(SearchQueryAnalytics))
        if not sqa_check.scalars().all():
            sqa_list = [
                SearchQueryAnalytics(query="5G Smartphone", normalized_query="5g smartphone", search_count=1420),
                SearchQueryAnalytics(query="Wireless Headphones", normalized_query="wireless headphones", search_count=1280),
                SearchQueryAnalytics(query="4K QLED Smart TV", normalized_query="4k qled smart tv", search_count=980),
                SearchQueryAnalytics(query="Gaming Laptop RTX 4070", normalized_query="gaming laptop rtx 4070", search_count=850),
                SearchQueryAnalytics(query="AMOLED Smartwatch", normalized_query="amoled smartwatch", search_count=710),
                SearchQueryAnalytics(query="Non-Stick Cookware Set", normalized_query="non-stick cookware set", search_count=520),
                SearchQueryAnalytics(query="Air Fryer Digital", normalized_query="air fryer digital", search_count=490),
                SearchQueryAnalytics(query="Inverter AC 1.5 Ton", normalized_query="inverter ac 1.5 ton", search_count=650),
            ]
            session.add_all(sqa_list)

        await session.commit()
        logger.info("Database seeded successfully with accurately matched products and images across all brands!")

if __name__ == "__main__":
    asyncio.run(seed_data())
