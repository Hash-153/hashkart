from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field
from app.schemas.user import AddressResponse


class CheckoutValidateRequest(BaseModel):
    address_id: int
    coupon_code: Optional[str] = None
    shipping_method: str = "STANDARD"  # STANDARD, EXPRESS


class CheckoutProcessRequest(CheckoutValidateRequest):
    payment_method: str = Field(..., description="CARD, UPI, NETBANKING, WALLET, COD")
    mock_payment_details: Optional[dict] = Field(
        default=None,
        description="Mock card info or UPI VPA (e.g. {'card_number': '4000000000000000', 'simulate_failure': false})"
    )


class OrderItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_id: int
    variant_id: int
    product_name: str
    variant_title: str
    sku: str
    unit_price: float
    discount_price: Optional[float] = None
    quantity: int
    line_subtotal: float


class PaymentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_id: int
    payment_method: str
    transaction_reference: str
    amount: float
    status: str
    created_at: datetime


class ShipmentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_id: int
    tracking_number: str
    carrier_name: str
    shipment_status: str
    shipped_at: Optional[datetime] = None
    estimated_delivery: Optional[datetime] = None
    delivered_at: Optional[datetime] = None


class OrderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    order_number: str
    user_id: int
    address_id: int
    status: str
    payment_status: str
    subtotal: float
    tax_amount: float
    shipping_fee: float
    discount_amount: float
    grand_total: float
    created_at: datetime
    updated_at: datetime

    address: Optional[AddressResponse] = None
    items: List[OrderItemResponse] = []
    payment: Optional[PaymentResponse] = None
    shipment: Optional[ShipmentResponse] = None


class OrderStatusUpdate(BaseModel):
    status: str = Field(..., description="PENDING, CONFIRMED, PACKED, SHIPPED, OUT_FOR_DELIVERY, DELIVERED, CANCELLED, RETURNED, REFUNDED")
    notes: Optional[str] = None
