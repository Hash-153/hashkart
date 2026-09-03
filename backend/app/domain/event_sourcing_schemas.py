"""
NovaMart Event-Driven Architecture & Domain Event Schemas
=========================================================
CloudEvents / Kafka / AWS EventBridge schema registry:
Strongly typed event contracts for asynchronous message buses across microservices.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from enum import Enum
from typing import Any, Dict, List, Optional
import uuid


class DomainEventType(str, Enum):
    ORDER_CREATED = "novamart.order.created.v1"
    PAYMENT_CAPTURED = "novamart.payment.captured.v1"
    INVENTORY_RESERVED = "novamart.inventory.reserved.v1"
    PACKAGE_MANIFESTED = "novamart.fulfillment.manifested.v1"
    SHIPMENT_OUT_FOR_DELIVERY = "novamart.logistics.out_for_delivery.v1"
    ORDER_DELIVERED = "novamart.logistics.delivered.v1"
    RETURN_REQUESTED = "novamart.returns.requested.v1"
    SELLER_PAYOUT_SETTLED = "novamart.settlement.payout_settled.v1"
    PRICE_DROP_DETECTED = "novamart.catalog.price_drop.v1"


@dataclass
class CloudEventHeader:
    specversion: str = "1.0"
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    source: str = "urn:novamart:ecommerce:engine"
    type: DomainEventType = DomainEventType.ORDER_CREATED
    time: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    datacontenttype: str = "application/json"


@dataclass
class OrderCreatedEventPayload:
    order_number: str
    user_id: int
    seller_id: int
    grand_total: Decimal
    currency: str
    payment_method: str
    shipping_pincode: str
    items_count: int


@dataclass
class PaymentCapturedEventPayload:
    transaction_id: str
    order_number: str
    gateway_provider: str
    amount_captured: Decimal
    utr_reference: str
    captured_at: datetime


@dataclass
class DomainEventEnvelope:
    header: CloudEventHeader
    data: Dict[str, Any]

    def to_json_dict(self) -> Dict[str, Any]:
        return {
            "specversion": self.header.specversion,
            "id": self.header.id,
            "source": self.header.source,
            "type": self.header.type.value,
            "time": self.header.time.isoformat(),
            "datacontenttype": self.header.datacontenttype,
            "data": self.data,
        }
