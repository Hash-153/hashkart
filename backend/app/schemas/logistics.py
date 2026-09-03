from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field

from app.models.logistics import (
    CarrierProviderType,
    DispatchManifestStatus,
    NDRActionType,
    ServiceabilityZone,
)


class PincodeCheckRequest(BaseModel):
    pincode: str = Field(..., pattern=r"^\d{6}$")
    cart_total: Optional[Decimal] = None
    weight_kg: Optional[Decimal] = Field(default=Decimal("0.5"))


class PincodeServiceabilityResponse(BaseModel):
    pincode: str
    city: str
    state: str
    district: Optional[str]
    zone: ServiceabilityZone
    is_serviceable: bool
    is_cod_available: bool
    is_prepaid_available: bool
    is_return_pickup_available: bool
    standard_sla_days: int
    express_sla_days: int
    estimated_delivery_date: str
    express_delivery_date: str
    shipping_charge: Decimal
    primary_carrier: CarrierProviderType
    model_config = ConfigDict(from_attributes=True)


class PincodeCreateUpdate(BaseModel):
    pincode: str = Field(..., pattern=r"^\d{6}$")
    city: str
    state: str
    district: Optional[str] = None
    zone: ServiceabilityZone = ServiceabilityZone.REST_OF_INDIA
    is_cod_available: bool = True
    is_prepaid_available: bool = True
    is_return_pickup_available: bool = True
    standard_sla_days: int = 3
    express_sla_days: int = 1
    primary_carrier: CarrierProviderType = CarrierProviderType.EKART
    backup_carrier: Optional[CarrierProviderType] = CarrierProviderType.DELHIVERY
    max_weight_kg: Decimal = Decimal("30.00")
    is_active: bool = True


class ManifestPackageCreate(BaseModel):
    shipment_id: int
    tracking_number: str
    order_number: str
    destination_pincode: str
    weight_kg: Decimal = Decimal("0.50")


class ManifestPackageResponse(BaseModel):
    id: int
    manifest_id: int
    shipment_id: int
    tracking_number: str
    order_number: str
    destination_pincode: str
    weight_kg: Decimal
    scanned_at: Optional[datetime]
    is_scanned: bool
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class DispatchManifestCreate(BaseModel):
    warehouse_id: int
    carrier_code: CarrierProviderType
    driver_name: Optional[str] = None
    driver_phone: Optional[str] = None
    vehicle_number: Optional[str] = None
    scheduled_pickup_time: Optional[datetime] = None
    shipment_ids: List[int] = []


class DispatchManifestResponse(BaseModel):
    id: int
    manifest_number: str
    warehouse_id: int
    carrier_code: CarrierProviderType
    status: DispatchManifestStatus
    total_packages: int
    total_weight_kg: Decimal
    driver_name: Optional[str]
    driver_phone: Optional[str]
    vehicle_number: Optional[str]
    scheduled_pickup_time: Optional[datetime]
    handed_over_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    packages: List[ManifestPackageResponse] = []
    model_config = ConfigDict(from_attributes=True)


class NDRTicketCreate(BaseModel):
    shipment_id: int
    tracking_number: str
    order_id: int
    carrier_failure_reason: str
    carrier_remark: Optional[str] = None


class NDRActionRequest(BaseModel):
    action: NDRActionType
    rescheduled_delivery_date: Optional[datetime] = None
    updated_address_line: Optional[str] = None
    customer_notes: Optional[str] = None


class NDRTicketResponse(BaseModel):
    id: int
    shipment_id: int
    tracking_number: str
    order_id: int
    attempt_count: int
    carrier_failure_reason: str
    carrier_remark: Optional[str]
    customer_action: Optional[NDRActionType]
    rescheduled_delivery_date: Optional[datetime]
    updated_address_line: Optional[str]
    resolution_status: str
    created_at: datetime
    resolved_at: Optional[datetime]
    model_config = ConfigDict(from_attributes=True)
