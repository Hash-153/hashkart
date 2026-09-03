from typing import List, Optional, Any, Dict
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from app.schemas.catalog import ProductDetailResponse


class AutocompleteSuggestion(BaseModel):
    label: str
    type: str  # "category" | "brand" | "product" | "keyword"
    slug: Optional[str] = None
    id: Optional[int] = None
    search_count: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class FacetCategoryItem(BaseModel):
    id: int
    name: str
    slug: str
    count: int


class FacetBrandItem(BaseModel):
    id: int
    name: str
    slug: str
    count: int


class FacetPriceRange(BaseModel):
    min: float
    max: float


class FacetRatingItem(BaseModel):
    rating: int
    count: int
    label: str


class FacetDynamicAttributeOption(BaseModel):
    value: str
    count: int


class FacetDynamicAttribute(BaseModel):
    name: str
    options: List[FacetDynamicAttributeOption]


class SearchFacets(BaseModel):
    categories: List[FacetCategoryItem]
    brands: List[FacetBrandItem]
    price_range: FacetPriceRange
    ratings: List[FacetRatingItem]
    dynamic_attributes: List[FacetDynamicAttribute]


class SearchResponse(BaseModel):
    items: List[ProductDetailResponse]
    total: int
    page: int
    limit: int
    pages: int
    has_next: bool
    has_prev: bool
    query: Optional[str] = None
    did_you_mean: Optional[str] = None
    facets: SearchFacets


class UserSearchHistoryResponse(BaseModel):
    id: int
    query: str
    result_count: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TrendingSearchResponse(BaseModel):
    query: str
    search_count: int

    model_config = ConfigDict(from_attributes=True)
