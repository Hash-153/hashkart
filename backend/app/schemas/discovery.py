from typing import List, Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.schemas.catalog import ProductDetailResponse


class DiscoverySection(BaseModel):
    section_key: str
    title: str
    subtitle: Optional[str] = None
    layout_type: str = "carousel"  # "carousel" | "grid"
    products: List[ProductDetailResponse]

    model_config = ConfigDict(from_attributes=True)


class RecentlyViewedResponse(BaseModel):
    id: int
    product_id: int
    viewed_at: datetime
    product: ProductDetailResponse

    model_config = ConfigDict(from_attributes=True)
