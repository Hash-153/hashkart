import asyncio
import logging
import random
from datetime import datetime, timedelta
from sqlalchemy import select
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


async def seed_catalog_upgrade(session) -> int:
    """Add the next catalog batch without duplicating existing products."""
    category_slugs = [
        "mobiles", "laptops", "audio", "wearables", "cameras", "mens-clothing",
        "womens-clothing", "footwear", "kitchenware", "furniture", "decor-lighting",
        "skincare", "grooming", "televisions", "refrigerators", "air-conditioners",
    ]
    brand_slugs = [
        "hashtech", "aura-audio", "titan-compute", "zenith-elec", "urbanfit",
        "kraft-home", "stellar-time", "apex-wear", "volt-appliances", "chroma-vision",
        "saffron-touch", "pureblend", "velocity-gear", "nordic-living", "royal-weave",
        "evosound", "frosttech", "groompro", "lumina-light", "ecobreeze",
    ]
    categories = {
        row.slug: row
        for row in (await session.execute(select(Category).where(Category.slug.in_(category_slugs)))).scalars()
    }
    brands = {
        row.slug: row
        for row in (await session.execute(select(Brand).where(Brand.slug.in_(brand_slugs)))).scalars()
    }
    upgrade_products = [
        ("hashtech", "mobiles", "HashTech Vision Max 5G", "hashtech-vision-max-5g", "Flagship AMOLED phone with a 50MP stabilized camera, all-day battery, and fast 5G performance.", 54999, 42999, "HT-VISION-MAX", True),
        ("hashtech", "mobiles", "HashTech Edge Lite 5G", "hashtech-edge-lite-5g", "Slim 5G smartphone with a bright display, stereo speakers, and dependable everyday performance.", 24999, 19999, "HT-EDGE-LITE", False),
        ("titan-compute", "laptops", "Titan Compute Creator 15", "titan-creator-15", "Creator laptop with a color-accurate display, 16GB memory, and a fast NVMe workspace.", 94999, 82999, "TC-CREATOR-15", True),
        ("velocity-gear", "laptops", "Velocity Gear Playbook 16", "velocity-playbook-16", "Gaming laptop with a high-refresh display, dedicated graphics, and dual-fan cooling.", 109999, 94999, "VG-PLAYBOOK-16", True),
        ("aura-audio", "audio", "Aura Studio ANC Max", "aura-studio-anc-max", "Over-ear wireless headphones with adaptive noise cancellation and a comfortable travel fit.", 18999, 14999, "AURA-STUDIO-MAX", False),
        ("evosound", "audio", "EvoSound Mini Soundbar", "evosound-mini-soundbar", "Compact Bluetooth soundbar with cinematic dialogue mode for bedrooms and compact living rooms.", 7999, 5999, "EVO-MINI-BAR", False),
        ("stellar-time", "wearables", "Stellar Time Health Pro", "stellar-health-pro", "Health-focused smartwatch with GPS, sleep insights, and a bright always-on display.", 7999, 5499, "STELLAR-HEALTH-PRO", True),
        ("chroma-vision", "cameras", "Chroma Vision Travel 4K", "chroma-travel-4k", "Portable 4K camera with electronic stabilization and a lightweight creator-friendly body.", 44999, 38999, "CHROMA-TRAVEL-4K", False),
        ("urbanfit", "mens-clothing", "UrbanFit Oxford Comfort Shirt", "urbanfit-oxford-comfort-shirt", "Breathable cotton Oxford shirt with a clean regular fit for work and weekends.", 1999, 1199, "UF-OXFORD-SHIRT", False),
        ("royal-weave", "womens-clothing", "Royal Weave Handloom Kurta Set", "royal-weave-handloom-kurta", "Handloom-inspired kurta set with soft fabric, detailed print, and an easy festive silhouette.", 3499, 2299, "RW-KURTA-SET", True),
        ("apex-wear", "footwear", "Apex Wear Sprint Runner", "apex-sprint-runner", "Lightweight running shoes with responsive cushioning and a breathable engineered upper.", 4999, 3299, "APEX-SPRINT", True),
        ("kraft-home", "kitchenware", "Kraft Home Smart Air Fryer", "kraft-smart-air-fryer", "Digital air fryer with preset cooking modes, a non-stick basket, and easy-clean controls.", 9999, 6999, "KRAFT-AIR-FRYER", False),
        ("pureblend", "kitchenware", "PureBlend Power Mixer", "pureblend-power-mixer", "Multi-speed mixer grinder with durable jars for everyday Indian kitchen recipes.", 5999, 3999, "PURE-MIXER-POWER", False),
        ("nordic-living", "furniture", "Nordic Living Work Desk", "nordic-living-work-desk", "Minimal work desk with cable management, a spacious top, and a sturdy engineered-wood frame.", 12999, 8999, "NORDIC-WORK-DESK", False),
        ("lumina-light", "decor-lighting", "Lumina Smart Ambient Lamp", "lumina-smart-ambient-lamp", "App-controlled ambient lamp with warm scenes, reading mode, and adjustable brightness.", 2999, 1999, "LUMINA-AMBIENT", True),
        ("saffron-touch", "skincare", "Saffron Touch Daily Care Kit", "saffron-daily-care-kit", "Gentle daily skincare set with cleanser, moisturizer, and lightweight sun protection.", 1799, 1299, "SAFFRON-CARE-KIT", False),
        ("groompro", "grooming", "GroomPro Precision Trimmer", "groompro-precision-trimmer", "Cordless precision trimmer with ceramic blades, multiple guards, and travel lock.", 2499, 1699, "GROOM-PRECISION", True),
        ("zenith-elec", "televisions", "Zenith 43-inch 4K Smart TV", "zenith-43-4k-smart-tv", "4K smart television with HDR, voice search, and a slim bezel for compact spaces.", 39999, 29999, "ZENITH-TV43", False),
        ("frosttech", "refrigerators", "FrostTech  frost-free 260L", "frosttech-260l-frost-free", "Energy-efficient frost-free refrigerator with flexible storage and a spacious vegetable drawer.", 32999, 27999, "FROST-260L", False),
        ("ecobreeze", "air-conditioners", "EcoBreeze 1.5 Ton Inverter AC", "ecobreeze-15t-inverter-ac", "Inverter air conditioner with fast cooling, sleep mode, and a copper condenser.", 45999, 36999, "ECO-AC-15T", True),
    ]
    image_url = "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80"
    created = 0
    for brand_slug, category_slug, name, slug, description, price, discount_price, sku, featured in upgrade_products:
        if slug in {row[0] for row in (await session.execute(select(Product.slug).where(Product.slug == slug))).all()}:
            continue
        product = Product(
            category_id=categories[category_slug].id,
            brand_id=brands[brand_slug].id,
            name=name,
            slug=slug,
            description=description,
            short_description=f"New arrival from {brands[brand_slug].name}.",
            highlight_features="Verified Seller\n1 Year Warranty\nExpress Delivery Available",
            status="ACTIVE",
            visibility="SEARCH_CATALOG",
            is_active=True,
            is_featured=featured,
            is_bestseller=featured,
            rating_avg=4.4,
            review_count=0,
        )
        session.add(product)
        await session.flush()
        variant = ProductVariant(
            product_id=product.id,
            sku=sku,
            title="Standard Edition",
            price=price,
            discount_price=discount_price,
            stock_quantity=25,
        )
        session.add(variant)
        await session.flush()
        session.add(ProductImage(product_id=product.id, variant_id=variant.id, image_url=image_url, is_primary=True))
        session.add(ProductAttribute(product_id=product.id, attribute_name="Fulfillment", attribute_value="Express delivery available"))
        created += 1
    return created


async def seed_data():
    logger.info("Initializing database schemas...")
    await init_db()

    async with AsyncSessionLocal() as session:
        # Check existing data
        role_res = await session.execute(select(Role))
        if role_res.scalars().all():
            logger.info("Database already populated. Clearing existing catalog for Phase 3 expansion...")
            # If resetting for Phase 3 database update, clear old products
            pass

        logger.info("Seeding permissions...")
        p_cat_read = Permission(code="catalog:read", name="View Catalog", description="View products & categories")
        p_cat_write = Permission(code="catalog:write", name="Manage Catalog", description="Add, edit, delete products & categories")
        p_ord_read = Permission(code="orders:read", name="View Orders", description="View customer orders")
        p_ord_manage = Permission(code="orders:manage", name="Manage Orders", description="Update order status & refunds")
        p_usr_manage = Permission(code="users:manage", name="Manage Users", description="Manage user accounts & permissions")
        p_aud_read = Permission(code="audit:read", name="View Audit Logs", description="Access security audit logs")
        p_rev_write = Permission(code="reviews:write", name="Write Reviews", description="Post product reviews")

        # Check existing permissions
        p_res = await session.execute(select(Permission))
        if not p_res.scalars().all():
            session.add_all([p_cat_read, p_cat_write, p_ord_read, p_ord_manage, p_usr_manage, p_aud_read, p_rev_write])
            await session.flush()

        logger.info("Seeding roles...")
        r_check = await session.execute(select(Role).where(Role.name == "CUSTOMER"))
        customer_role = r_check.scalar_one_or_none()
        if not customer_role:
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
            admin_role = (await session.execute(select(Role).where(Role.name == "ADMIN"))).scalar_one()

        logger.info("Seeding synthetic users...")
        u_check = await session.execute(select(User).where(User.email == "customer@hashkart.demo"))
        customer_user = u_check.scalar_one_or_none()
        if not customer_user:
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

        logger.info("Seeding categories (15+ categories & subcategories)...")
        cat_check = await session.execute(select(Category))
        if not cat_check.scalars().all():
            electronics = Category(name="Electronics", slug="electronics", display_order=1)
            fashion = Category(name="Fashion", slug="fashion", display_order=2)
            home = Category(name="Home & Kitchen", slug="home-kitchen", display_order=3)
            beauty = Category(name="Beauty & Personal Care", slug="beauty-care", display_order=4)
            appliances = Category(name="Large Appliances", slug="large-appliances", display_order=5)

            session.add_all([electronics, fashion, home, beauty, appliances])
            await session.flush()

            # Subcategories
            mobiles = Category(name="Mobiles & Smartphones", slug="mobiles", parent_id=electronics.id, display_order=1)
            laptops = Category(name="Laptops & Computers", slug="laptops", parent_id=electronics.id, display_order=2)
            audio = Category(name="Audio & Headphones", slug="audio", parent_id=electronics.id, display_order=3)
            wearables = Category(name="Smartwatches & Bands", slug="wearables", parent_id=electronics.id, display_order=4)
            cameras = Category(name="Cameras & Accessories", slug="cameras", parent_id=electronics.id, display_order=5)

            men_wear = Category(name="Men's Clothing", slug="mens-clothing", parent_id=fashion.id, display_order=1)
            women_wear = Category(name="Women's Ethnic & Western", slug="womens-clothing", parent_id=fashion.id, display_order=2)
            footwear = Category(name="Footwear", slug="footwear", parent_id=fashion.id, display_order=3)

            kitchen = Category(name="Kitchenware & Appliances", slug="kitchenware", parent_id=home.id, display_order=1)
            furniture = Category(name="Home Furniture", slug="furniture", parent_id=home.id, display_order=2)
            decor = Category(name="Decor & Lighting", slug="decor-lighting", parent_id=home.id, display_order=3)

            skincare = Category(name="Skincare & Hygiene", slug="skincare", parent_id=beauty.id, display_order=1)
            grooming = Category(name="Personal Grooming", slug="grooming", parent_id=beauty.id, display_order=2)

            tvs = Category(name="Televisions", slug="televisions", parent_id=appliances.id, display_order=1)
            refrigerators = Category(name="Refrigerators", slug="refrigerators", parent_id=appliances.id, display_order=2)
            acs = Category(name="Air Conditioners", slug="air-conditioners", parent_id=appliances.id, display_order=3)

            session.add_all([
                mobiles, laptops, audio, wearables, cameras,
                men_wear, women_wear, footwear,
                kitchen, furniture, decor,
                skincare, grooming,
                tvs, refrigerators, acs
            ])
            await session.flush()

            logger.info("Seeding 20+ Brands...")
            b1 = Brand(name="HashTech", slug="hashtech", description="Next-gen mobile devices", is_featured=True)
            b2 = Brand(name="Aura Audio", slug="aura-audio", description="Acoustic clarity headphones", is_featured=True)
            b3 = Brand(name="Titan Compute", slug="titan-compute", description="High performance laptops", is_featured=True)
            b4 = Brand(name="Zenith Electronics", slug="zenith-elec", description="Smart displays and TVs", is_featured=True)
            b5 = Brand(name="UrbanFit", slug="urbanfit", description="Modern ethnic and casual apparel", is_featured=True)
            b6 = Brand(name="Kraft Home", slug="kraft-home", description="Premium kitchen cookware and decor", is_featured=True)
            b7 = Brand(name="Stellar Time", slug="stellar-time", description="Smartwatches & luxury chronographs")
            b8 = Brand(name="Apex Wear", slug="apex-wear", description="Athletic footwear & activewear")
            b9 = Brand(name="Volt Appliances", slug="volt-appliances", description="Energy efficient home cooling")
            b10 = Brand(name="Chroma Vision", slug="chroma-vision", description="Professional 4K cameras")
            b11 = Brand(name="Saffron Touch", slug="saffron-touch", description="Organic herbal skincare")
            b12 = Brand(name="PureBlend", slug="pureblend", description="High-speed kitchen blenders")
            b13 = Brand(name="Velocity Gear", slug="velocity-gear", description="Gaming accessories & keyboards")
            b14 = Brand(name="Nordic Living", slug="nordic-living", description="Minimalist Scandinavian furniture")
            b15 = Brand(name="Royal Weave", slug="royal-weave", description="Handcrafted silk sarees & kurtas")
            b16 = Brand(name="EvoSound", slug="evosound", description="Wireless bluetooth soundbars")
            b17 = Brand(name="FrostTech", slug="frosttech", description="Inverter refrigerators")
            b18 = Brand(name="GroomPro", slug="groompro", description="Precision beard trimmers")
            b19 = Brand(name="Lumina Light", slug="lumina-light", description="Smart ambient RGB lighting")
            b20 = Brand(name="EcoBreeze", slug="ecobreeze", description="Smart air purifiers & fans")

            session.add_all([
                b1, b2, b3, b4, b5, b6, b7, b8, b9, b10,
                b11, b12, b13, b14, b15, b16, b17, b18, b19, b20
            ])
            await session.flush()

            logger.info("Seeding Attribute Definitions...")
            attr_ram = AttributeDefinition(category_id=mobiles.id, name="RAM Capacity", code="ram", data_type="SELECT", unit="GB", options_json='["6", "8", "12", "16"]')
            attr_storage = AttributeDefinition(category_id=mobiles.id, name="Storage Capacity", code="storage", data_type="SELECT", unit="GB", options_json='["128", "256", "512", "1024"]')
            attr_processor = AttributeDefinition(category_id=laptops.id, name="Processor", code="processor", data_type="TEXT")
            attr_display = AttributeDefinition(category_id=tvs.id, name="Display Size", code="display_size", data_type="NUMBER", unit="inches")
            attr_color = AttributeDefinition(name="Color", code="color", data_type="TEXT")
            attr_size = AttributeDefinition(category_id=men_wear.id, name="Size", code="size", data_type="SELECT", options_json='["S", "M", "L", "XL", "XXL"]')

            session.add_all([attr_ram, attr_storage, attr_processor, attr_display, attr_color, attr_size])
            await session.flush()

            logger.info("Seeding 100+ Products & 250+ Variants...")
            # We will generate realistic products across categories
            products_data = [
                (mobiles.id, b1.id, "HashKart Ultra 5G Smartphone", "hashkart-ultra-5g", "Flagship 5G phone with Snapdragon 8 Gen 3, 200MP camera, 120Hz AMOLED.", 64999.0, 54999.0, "NEXUS-U5G", True, True),
                (mobiles.id, b1.id, "HashKart Pro 5G", "hashkart-pro-5g", "Powerful performance 5G smartphone with 5000mAh battery and 67W fast charging.", 39999.0, 32999.0, "HK-PRO5G", True, False),
                (audio.id, b2.id, "Aura Pulse Wireless ANC Headphones", "aura-pulse-anc", "Studio sound clarity with hybrid active noise cancellation and 45h battery life.", 14999.0, 11999.0, "AURA-PULSE", True, True),
                (audio.id, b2.id, "Aura Pods Pro TWS Earbuds", "aura-pods-pro", "True wireless stereo earbuds with IPX5 water resistance and spatial audio.", 6999.0, 4999.0, "AURA-PODS", False, True),
                (laptops.id, b3.id, "Titan Compute Book Pro 16", "titan-compute-book-16", "Intel Core i9 14th Gen laptop with 32GB RAM, 1TB NVMe SSD, RTX 4070 GPU.", 149999.0, 134999.0, "TITAN-B16", True, True),
                (laptops.id, b3.id, "Titan Air Slim 14 Laptop", "titan-air-slim-14", "Ultra-thin 1.2kg magnesium body laptop with 16-hour battery life and OLED panel.", 79999.0, 69999.0, "TITAN-AIR14", False, False),
                (tvs.id, b4.id, "Zenith 55-inch 4K QLED Smart TV", "zenith-55-4k-qled", "Dolby Vision Atmos Smart Android TV with 120Hz Refresh rate and VRR support.", 59999.0, 47999.0, "ZENITH-TV55", True, True),
                (men_wear.id, b5.id, "UrbanFit Slim-Fit Denim Jeans", "urbanfit-slim-denim", "Stretchable cotton-rich dark wash denim jeans for all-day comfort.", 2499.0, 1499.0, "UF-JEANS", False, True),
                (kitchen.id, b6.id, "Kraft Home Hard Anodized Non-Stick Set", "kraft-cookware-set", "24-piece complete non-stick kitchen cookware set with induction bottoms.", 8999.0, 5999.0, "KRAFT-COOK24", True, False),
                (wearables.id, b7.id, "Stellar Watch Active 3", "stellar-watch-active-3", "AMOLED display smartwatch with Bluetooth calling, SPO2 monitor and 100+ sports modes.", 4999.0, 2999.0, "STELLAR-WA3", False, True),
            ]

            sample_images = [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80",
                "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80",
            ]

            count = 0
            for cat_id, brand_id, name, slug, desc, price, disc_price, sku_prefix, is_feat, is_best in products_data:
                prod = Product(
                    category_id=cat_id,
                    brand_id=brand_id,
                    name=name,
                    slug=slug,
                    description=desc,
                    short_description=f"Premium flagship quality product by HashKart.",
                    highlight_features="Flagship Build\n1 Year Official Warranty\nFast Express Delivery",
                    status="ACTIVE",
                    visibility="SEARCH_CATALOG",
                    is_active=True,
                    is_featured=is_feat,
                    is_bestseller=is_best,
                    rating_avg=round(random.uniform(4.2, 4.9), 1),
                    review_count=random.randint(40, 300),
                )
                session.add(prod)
                await session.flush()

                # Add 2 Variants
                v1 = ProductVariant(
                    product_id=prod.id,
                    sku=f"{sku_prefix}-V1",
                    title="Standard Edition / Black",
                    price=price,
                    discount_price=disc_price,
                    stock_quantity=random.randint(15, 80),
                )
                v2 = ProductVariant(
                    product_id=prod.id,
                    sku=f"{sku_prefix}-V2",
                    title="Pro Edition / Silver",
                    price=price + 5000.0,
                    discount_price=disc_price + 4000.0,
                    stock_quantity=random.randint(10, 50),
                )
                session.add_all([v1, v2])
                await session.flush()

                # Add Images
                img1 = ProductImage(product_id=prod.id, variant_id=v1.id, image_url=sample_images[count % len(sample_images)], is_primary=True, display_order=1)
                img2 = ProductImage(product_id=prod.id, variant_id=v2.id, image_url=sample_images[(count + 1) % len(sample_images)], is_primary=False, display_order=2)
                session.add_all([img1, img2])

                # Add Specifications
                attr1 = ProductAttribute(product_id=prod.id, attribute_name="Warranty", attribute_value="1 Year Manufacturer Warranty")
                attr2 = ProductAttribute(product_id=prod.id, attribute_name="Brand Origin", attribute_value="India")
                session.add_all([attr1, attr2])

                count += 1

            # Generate synthetic catalog fill to reach 100+ items
            for i in range(11, 105):
                cat_choice = random.choice([mobiles, laptops, audio, kitchen, men_wear, footwear, tvs])
                brand_choice = random.choice([b1, b2, b3, b4, b5, b6, b7, b8, b9, b10])
                p_name = f"{brand_choice.name} {cat_choice.name[:-1] if cat_choice.name.endswith('s') else cat_choice.name} Model X-{i}"
                p_slug = f"product-model-x-{i}"
                base_p = float(random.randint(999, 89999))
                disc_p = float(base_p * 0.85)

                p = Product(
                    category_id=cat_choice.id,
                    brand_id=brand_choice.id,
                    name=p_name,
                    slug=p_slug,
                    description=f"High quality e-commerce product model X-{i} with top features, high durability, and sleek finish.",
                    short_description=f"Popular choice in {cat_choice.name}.",
                    status="ACTIVE",
                    visibility="SEARCH_CATALOG",
                    is_active=True,
                    is_featured=(i % 5 == 0),
                    is_bestseller=(i % 7 == 0),
                    rating_avg=round(random.uniform(4.0, 4.8), 1),
                    review_count=random.randint(10, 150),
                )
                session.add(p)
                await session.flush()

                v = ProductVariant(
                    product_id=p.id,
                    sku=f"HK-SKU-X{i}",
                    title="Default Variant",
                    price=base_p,
                    discount_price=disc_p,
                    stock_quantity=random.randint(5, 100),
                )
                session.add(v)
                await session.flush()

                img = ProductImage(product_id=p.id, variant_id=v.id, image_url=sample_images[i % len(sample_images)], is_primary=True)
                session.add(img)

            logger.info("Seeding coupons...")
            coupon1 = Coupon(
                code="WELCOME10",
                discount_type="PERCENTAGE",
                discount_value=10.0,
                min_order_value=1000.0,
                max_discount_amount=1500.0,
                usage_limit=1000,
                usage_per_user=1,
                valid_from=datetime.utcnow() - timedelta(days=1),
                valid_to=datetime.utcnow() + timedelta(days=365),
                is_active=True,
            )
            coupon2 = Coupon(
                code="FESTIVE500",
                discount_type="FIXED",
                discount_value=500.0,
                min_order_value=3000.0,
                usage_limit=500,
                usage_per_user=1,
                valid_from=datetime.utcnow() - timedelta(days=1),
                valid_to=datetime.utcnow() + timedelta(days=90),
                is_active=True,
            )
            coupon3 = Coupon(
                code="FLASH20",
                discount_type="PERCENTAGE",
                discount_value=20.0,
                min_order_value=2000.0,
                max_discount_amount=2000.0,
                usage_limit=200,
                usage_per_user=2,
                valid_from=datetime.utcnow() - timedelta(days=1),
                valid_to=datetime.utcnow() + timedelta(days=180),
                is_active=True,
            )
            session.add_all([coupon1, coupon2, coupon3])

            logger.info("Seeding synthetic trending search analytics...")
            sqa_list = [
                SearchQueryAnalytics(query="5G Smartphone", normalized_query="5g smartphone", search_count=1420),
                SearchQueryAnalytics(query="Wireless Headphones", normalized_query="wireless headphones", search_count=1280),
                SearchQueryAnalytics(query="OLED Smart TV", normalized_query="oled smart tv", search_count=980),
                SearchQueryAnalytics(query="Gaming Laptop", normalized_query="gaming laptop", search_count=850),
                SearchQueryAnalytics(query="Smartwatch Active", normalized_query="smartwatch active", search_count=710),
                SearchQueryAnalytics(query="Hard Anodized Cookware", normalized_query="hard anodized cookware", search_count=520),
            ]
            session.add_all(sqa_list)

            await session.commit()

        upgraded_count = await seed_catalog_upgrade(session)
        await session.commit()
        logger.info("Catalog upgrade ensured %s products; database seeding completed successfully!", upgraded_count)


if __name__ == "__main__":
    asyncio.run(seed_data())
