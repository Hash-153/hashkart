from typing import List, Dict, Any, Optional
from collections import defaultdict
from app.models.catalog import Product


class FacetService:
    """Dynamically calculates facet counts and distributions for product search results."""

    @staticmethod
    def calculate_facets(products: List[Product]) -> Dict[str, Any]:
        """
        Calculates category counts, brand counts, price range, rating breakdown,
        and dynamic attribute option counts for candidate products.
        """
        categories_map: Dict[int, Dict[str, Any]] = {}
        brands_map: Dict[int, Dict[str, Any]] = {}
        ratings_count = {4: 0, 3: 0, 2: 0, 1: 0}
        dynamic_attributes: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))

        min_price = float("inf")
        max_price = 0.0

        for p in products:
            # 1. Category Facet
            if p.category:
                cid = p.category.id
                if cid not in categories_map:
                    categories_map[cid] = {"id": cid, "name": p.category.name, "slug": p.category.slug, "count": 0}
                categories_map[cid]["count"] += 1

            # 2. Brand Facet
            if p.brand:
                bid = p.brand.id
                if bid not in brands_map:
                    brands_map[bid] = {"id": bid, "name": p.brand.name, "slug": p.brand.slug, "count": 0}
                brands_map[bid]["count"] += 1

            # 3. Rating Facet
            if p.rating_avg:
                for threshold in [4, 3, 2, 1]:
                    if p.rating_avg >= threshold:
                        ratings_count[threshold] += 1

            # 4. Price Min/Max Range
            for v in p.variants:
                if v.is_active:
                    eff_price = float(v.discount_price or v.price)
                    if eff_price < min_price:
                        min_price = eff_price
                    if eff_price > max_price:
                        max_price = eff_price

            # 5. Dynamic Attributes
            if p.typed_attribute_values:
                for attr_val in p.typed_attribute_values:
                    if attr_val.definition:
                        attr_name = attr_val.definition.name
                        val_str = attr_val.value
                        dynamic_attributes[attr_name][val_str] += 1

        formatted_dyn_attrs = [
            {
                "name": attr_name,
                "options": [{"value": val, "count": cnt} for val, cnt in val_counts.items()],
            }
            for attr_name, val_counts in dynamic_attributes.items()
        ]

        return {
            "categories": sorted(list(categories_map.values()), key=lambda c: c["count"], reverse=True),
            "brands": sorted(list(brands_map.values()), key=lambda b: b["count"], reverse=True),
            "price_range": {
                "min": min_price if min_price != float("inf") else 0.0,
                "max": max_price,
            },
            "ratings": [
                {"rating": 4, "count": ratings_count[4], "label": "4★ & above"},
                {"rating": 3, "count": ratings_count[3], "label": "3★ & above"},
                {"rating": 2, "count": ratings_count[2], "label": "2★ & above"},
                {"rating": 1, "count": ratings_count[1], "label": "1★ & above"},
            ],
            "dynamic_attributes": formatted_dyn_attrs,
        }
