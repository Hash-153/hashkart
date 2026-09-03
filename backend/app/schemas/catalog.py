from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, ConfigDict, Field, computed_field


# Attribute Definitions & Values
class AttributeDefinitionCreate(BaseModel):
    category_id: Optional[int] = None
    name: str = Field(..., min_length=2, max_length=100)
    code: str = Field(..., min_length=2, max_length=100)
    data_type: str = Field(default="TEXT", max_length=20)  # TEXT, NUMBER, BOOLEAN, SELECT, MULTI_SELECT
    unit: Optional[str] = Field(None, max_length=20)
    is_filterable: bool = True
    is_required: bool = False
    options: Optional[List[str]] = None


class AttributeDefinitionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category_id: Optional[int] = None
    name: str
    code: str
    data_type: str
    unit: Optional[str] = None
    is_filterable: bool
    is_required: bool
    options: Optional[List[str]] = None


class AttributeValueCreate(BaseModel):
    attribute_definition_id: int
    product_id: int
    variant_id: Optional[int] = None
    value: str


class AttributeValueResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    attribute_definition_id: int
    product_id: int
    variant_id: Optional[int] = None
    value: str
    definition: Optional[AttributeDefinitionResponse] = None


# Category Schemas
class CategoryCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    parent_id: Optional[int] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    display_order: int = 0
    is_active: bool = True


class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    parent_id: Optional[int] = None
    description: Optional[str] = None
    image_url: Optional[str] = None
    display_order: Optional[int] = None
    is_active: Optional[bool] = None


class CategorySimpleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    parent_id: Optional[int] = None
    name: str
    slug: str
    description: Optional[str] = None
    image_url: Optional[str] = None
    display_order: int = 0
    is_active: bool = True
    created_at: Optional[datetime] = None


class CategoryResponse(CategorySimpleResponse):
    subcategories: List[CategorySimpleResponse] = []


class CategoryTreeResponse(CategorySimpleResponse):
    subcategories: List["CategoryTreeResponse"] = []


# Brand Schemas
class BrandCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    logo_url: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    is_featured: bool = False


class BrandUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    logo_url: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    is_featured: Optional[bool] = None


class BrandResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str
    logo_url: Optional[str] = None
    description: Optional[str] = None
    is_active: bool = True
    is_featured: bool = False
    product_count: int = 0
    created_at: Optional[datetime] = None


# Product Component Schemas
class ProductImageCreate(BaseModel):
    image_url: str
    alt_text: Optional[str] = None
    variant_id: Optional[int] = None
    display_order: int = 0
    is_primary: bool = False


class ProductImageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    variant_id: Optional[int] = None
    image_url: str
    alt_text: Optional[str] = None
    display_order: int = 0
    is_primary: bool = False


class ProductAttributeResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    attribute_name: str
    attribute_value: str


class ProductVariantCreate(BaseModel):
    sku: str = Field(..., min_length=3, max_length=100)
    title: str = Field(..., min_length=2, max_length=150)
    price: float = Field(..., gt=0)
    discount_price: Optional[float] = Field(None, gt=0)
    stock_quantity: int = Field(default=0, ge=0)
    weight_grams: Optional[int] = None
    dimensions: Optional[str] = None
    is_active: bool = True


class ProductVariantResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    sku: str
    title: str
    price: float
    discount_price: Optional[float] = None
    stock_quantity: int = 0
    reserved_quantity: int = 0
    weight_grams: Optional[int] = None
    dimensions: Optional[str] = None
    is_active: bool = True
    images: List[ProductImageResponse] = []


class ProductCreate(BaseModel):
    category_id: int
    brand_id: Optional[int] = None
    name: str = Field(..., min_length=3, max_length=255)
    description: str = Field(..., min_length=10)
    short_description: Optional[str] = None
    highlight_features: Optional[str] = None
    status: str = Field(default="ACTIVE")
    visibility: str = Field(default="SEARCH_CATALOG")
    is_active: bool = True
    is_featured: bool = False
    is_bestseller: bool = False
    meta_title: Optional[str] = None
    meta_keywords: Optional[str] = None
    meta_description: Optional[str] = None


class ProductUpdate(BaseModel):
    category_id: Optional[int] = None
    brand_id: Optional[int] = None
    name: Optional[str] = Field(None, min_length=3, max_length=255)
    description: Optional[str] = Field(None, min_length=10)
    short_description: Optional[str] = None
    highlight_features: Optional[str] = None
    status: Optional[str] = None
    visibility: Optional[str] = None
    is_active: Optional[bool] = None
    is_featured: Optional[bool] = None
    is_bestseller: Optional[bool] = None
    meta_title: Optional[str] = None
    meta_keywords: Optional[str] = None
    meta_description: Optional[str] = None


class PricingSummary(BaseModel):
    original_price: float
    sale_price: float
    discount_amount: float
    discount_percentage: int
    has_discount: bool


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    category_id: int
    brand_id: Optional[int] = None
    name: str
    slug: str
    description: str
    short_description: Optional[str] = None
    highlight_features: Optional[str] = None
    status: str = "ACTIVE"
    visibility: str = "SEARCH_CATALOG"
    is_active: bool
    is_featured: bool
    is_bestseller: bool
    rating_avg: float = 0.0
    review_count: int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    category: Optional[CategorySimpleResponse] = None
    brand: Optional[BrandResponse] = None
    variants: List[ProductVariantResponse] = []
    attributes: List[ProductAttributeResponse] = []
    typed_attribute_values: List[AttributeValueResponse] = []
    images: List[ProductImageResponse] = []

    @computed_field
    @property
    def sale_price(self) -> float:
        active_variants = [variant for variant in self.variants if variant.is_active]
        return min(
            (variant.discount_price or variant.price for variant in active_variants),
            default=0,
        )

    @computed_field
    @property
    def discount_percentage(self) -> int:
        active_variants = [variant for variant in self.variants if variant.is_active]
        discounts = [
            round(((variant.price - variant.discount_price) / variant.price) * 100)
            for variant in active_variants
            if variant.discount_price and variant.price > 0
        ]
        return max(discounts, default=0)

    @computed_field
    @property
    def stock_status(self) -> str:
        quantity = sum(
            max(variant.stock_quantity - (variant.reserved_quantity or 0), 0)
            for variant in self.variants
            if variant.is_active
        )
        if quantity == 0:
            return "OUT_OF_STOCK"
        if quantity <= 10:
            return "LOW_STOCK"
        return "IN_STOCK"


class ProductDetailResponse(ProductResponse):
    pricing_summary: Optional[PricingSummary] = None
    related_products: List[ProductResponse] = []


class ProductListResponse(BaseModel):
    items: List[ProductResponse]
    total: int
    page: int
    limit: int
    pages: int
    has_next: bool = False
    has_prev: bool = False
