from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Protocol
from uuid import uuid4

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order_payment import Shipment


@dataclass(frozen=True, slots=True)
class ShipmentLabel:
    carrier_name: str
    tracking_number: str
    estimated_delivery: datetime


class CarrierProvider(Protocol):
    name: str

    async def create_label(self, order_number: str, postal_code: str) -> ShipmentLabel: ...


class MockCarrierProvider:
    """Deterministic provider contract used until a carrier API is configured."""

    name = "NovaExpress Logistics"

    async def create_label(self, order_number: str, postal_code: str) -> ShipmentLabel:
        del postal_code
        return ShipmentLabel(
            carrier_name=self.name,
            tracking_number=f"NOVA-{order_number}-{uuid4().hex[:8].upper()}",
            estimated_delivery=datetime.utcnow() + timedelta(days=5),
        )


async def dispatch_shipment(
    db: AsyncSession, shipment_id: int, order_number: str, postal_code: str,
    provider: CarrierProvider | None = None,
) -> Shipment:
    shipment = await db.get(Shipment, shipment_id)
    if not shipment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Shipment not found")
    if shipment.shipment_status in {"SHIPPED", "DELIVERED"}:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Shipment is already dispatched")

    label = await (provider or MockCarrierProvider()).create_label(order_number, postal_code)
    shipment.carrier_name = label.carrier_name
    shipment.tracking_number = label.tracking_number
    shipment.estimated_delivery = label.estimated_delivery
    shipment.shipped_at = datetime.utcnow()
    shipment.shipment_status = "SHIPPED"
    await db.flush()
    return shipment
