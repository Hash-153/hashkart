from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from app.schemas.catalog import ProductVariantResponse, ProductResponse


class CartItemCreate(BaseModel):
    variant_id: int
    quantity: int = Field(default=1, ge=1)


class CartItemUpdate(BaseModel):
    quantity: int = Field(..., ge=1)


class CartItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    cart_id: int
    variant_id: int
    quantity: int
    added_at: datetime
    variant: ProductVariantResponse
    price_changed: bool = False
    old_price: Optional[float] = None
    stock_warning: Optional[str] = None


class CartResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: Optional[int] = None
    session_id: Optional[str] = None
    items: List[CartItemResponse] = []
    subtotal: float = 0.0
    estimated_tax: float = 0.0
    estimated_shipping: float = 0.0
    discount_amount: float = 0.0
    grand_total: float = 0.0
    item_count: int = 0
    price_change_warnings: List[str] = []
    stock_warnings: List[str] = []


class WishlistItemCreate(BaseModel):
    variant_id: int


class WishlistItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    wishlist_id: int
    variant_id: int
    added_at: datetime
    variant: ProductVariantResponse
    is_available: bool = True
    current_price: Optional[float] = None


class WishlistResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    items: List[WishlistItemResponse] = []
