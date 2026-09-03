import json
from decimal import Decimal
from typing import Dict, List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.catalog import AttributeDefinition, AttributeValue, Category, Product, ProductAttribute, ProductImage
from app.schemas.comparison import (
    CompareProductCard,
    ProductComparisonMatrixResponse,
    SpecRow,
    SpecSection,
)


async def generate_product_comparison_matrix(
    db: AsyncSession, product_ids: List[int]
) -> ProductComparisonMatrixResponse:
    """Build a Flipkart-style side-by-side spec comparison table for 2 to 4 products."""
    if not product_ids:
        return ProductComparisonMatrixResponse(category_id=0, category_name="General", products=[], spec_sections=[])

    stmt = (
        select(Product)
        .options(
            selectinload(Product.images),
            selectinload(Product.brand),
            selectinload(Product.category),
            selectinload(Product.variants),
            selectinload(Product.attributes),
        )
        .where(Product.id.in_(product_ids[:4]))
    )
    res = await db.execute(stmt)
    products = res.scalars().all()

    if not products:
        return ProductComparisonMatrixResponse(category_id=0, category_name="General", products=[], spec_sections=[])

    category_id = products[0].category_id
    category_name = products[0].category.name if products[0].category else "General"

    # Build Header Cards
    product_cards: List[CompareProductCard] = []
    for p in products:
        price = Decimal(str(p.variants[0].price)) if p.variants else Decimal("999.00")
        mrp = Decimal(str(p.variants[0].discount_price or p.variants[0].price)) if p.variants else price
        if mrp < price:
            mrp = price * Decimal("1.2")
        disc = int(((mrp - price) / mrp) * 100) if mrp > price else 0
        img = p.images[0].image_url if p.images else None

        product_cards.append(
            CompareProductCard(
                id=p.id,
                name=p.name,
                slug=p.slug,
                brand_name=p.brand.name if p.brand else "NovaMart",
                category_name=p.category.name if p.category else "Electronics",
                price=price,
                mrp=mrp,
                discount_percentage=disc,
                rating_avg=float(p.rating_avg or 4.2),
                rating_count=p.review_count or 120,
                image_url=img,
                in_stock=p.is_active,
                highlights=[
                    f"Ratings: {float(p.rating_avg or 4.2)} ★",
                    f"Brand: {p.brand.name if p.brand else 'NovaMart'}",
                    "1 Year Manufacturer Warranty",
                    "7 Days Return & Replacement",
                ],
            )
        )

    # General Section
    general_specs: List[SpecRow] = [
        SpecRow(
            spec_key="price",
            spec_label="Price",
            values_by_product_id={p.id: f"₹{(p.variants[0].price if p.variants else 0):,.2f}" for p in products},
            is_different=len(set((p.variants[0].price if p.variants else 0) for p in products)) > 1,
        ),
        SpecRow(
            spec_key="brand",
            spec_label="Brand",
            values_by_product_id={p.id: (p.brand.name if p.brand else "NovaMart") for p in products},
            is_different=len(set((p.brand.name if p.brand else "") for p in products)) > 1,
        ),
        SpecRow(
            spec_key="warranty",
            spec_label="Warranty",
            values_by_product_id={p.id: "1 Year Domestic Warranty" for p in products},
            is_different=False,
        ),
    ]

    # Collect Dynamic Product Attributes
    all_attr_keys: Dict[str, str] = {}  # key -> label
    values_map: Dict[str, Dict[int, str]] = {}

    for p in products:
        for attr in p.attributes:
            name = attr.attribute_name
            val = attr.attribute_value
            all_attr_keys[name] = name
            if name not in values_map:
                values_map[name] = {}
            values_map[name][p.id] = val

    detailed_specs: List[SpecRow] = []
    for code, label in all_attr_keys.items():
        val_by_prod = {p.id: values_map[code].get(p.id, "—") for p in products}
        is_diff = len(set(val_by_prod.values())) > 1
        detailed_specs.append(
            SpecRow(
                spec_key=code,
                spec_label=label,
                values_by_product_id=val_by_prod,
                is_different=is_diff,
            )
        )

    spec_sections = [
        SpecSection(section_title="General Summary", specs=general_specs),
        SpecSection(section_title="Technical Specifications", specs=detailed_specs),
    ]

    return ProductComparisonMatrixResponse(
        category_id=category_id,
        category_name=category_name,
        products=product_cards,
        spec_sections=spec_sections,
        verdict=f"Comparing {len(products)} models in {category_name}. Compare prices, ratings, and key differences above.",
    )
