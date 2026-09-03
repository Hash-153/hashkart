from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict


class CompareProductCard(BaseModel):
    id: int
    name: str
    slug: str
    brand_name: str
    category_name: str
    price: Decimal
    mrp: Decimal
    discount_percentage: int
    rating_avg: float
    rating_count: int
    image_url: Optional[str]
    in_stock: bool
    highlights: List[str] = []


class SpecRow(BaseModel):
    spec_key: str
    spec_label: str
    values_by_product_id: Dict[int, str]
    is_different: bool = False


class SpecSection(BaseModel):
    section_title: str
    specs: List[SpecRow] = []


class ProductComparisonMatrixResponse(BaseModel):
    category_id: int
    category_name: str
    products: List[CompareProductCard] = []
    spec_sections: List[SpecSection] = []
    verdict: Optional[str] = None


class SaveComparisonRequest(BaseModel):
    category_id: int
    product_ids: List[int]
    session_id: Optional[str] = None
