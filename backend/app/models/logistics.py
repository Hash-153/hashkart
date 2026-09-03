import enum
from datetime import datetime, timezone
from decimal import Decimal
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.database import Base


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class ServiceabilityZone(str, enum.Enum):
    LOCAL = "LOCAL"            # Intra-city (<50km)
    REGIONAL = "REGIONAL"      # Intra-state / neighboring state (<500km)
    METRO = "METRO"            # Tier 1 Metro cities (Delhi, Mumbai, Bengaluru, etc.)
    REST_OF_INDIA = "REST_OF_INDIA" # Tier 2/3 and National
    SPECIAL_ZONE = "SPECIAL_ZONE"   # J&K, Northeast, Andaman


class CarrierProviderType(str, enum.Enum):
    INTERNAL_FLEET = "INTERNAL_FLEET"
    DELHIVERY = "DELHIVERY"
    BLUEDART = "BLUEDART"
    ECOM_EXPRESS = "ECOM_EXPRESS"
    SHADOWFAX = "SHADOWFAX"
    EKART = "EKART"


class DispatchManifestStatus(str, enum.Enum):
    DRAFT = "DRAFT"
    READY_FOR_PICKUP = "READY_FOR_PICKUP"
    PICKED_UP = "PICKED_UP"
    IN_TRANSIT = "IN_TRANSIT"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class NDRActionType(str, enum.Enum):
    RE_ATTEMPT = "RE_ATTEMPT"
    CUSTOMER_CONTACTED = "CUSTOMER_CONTACTED"
    ADDRESS_CORRECTION = "ADDRESS_CORRECTION"
    RETURN_TO_ORIGIN = "RETURN_TO_ORIGIN"
    CUSTOMER_REJECTED = "CUSTOMER_REJECTED"


class PincodeServiceability(Base):
    __tablename__ = "pincode_serviceability"

    id = Column(Integer, primary_key=True, index=True)
    pincode = Column(String(6), nullable=False, unique=True, index=True)
    city = Column(String(100), nullable=False, index=True)
    state = Column(String(100), nullable=False, index=True)
    district = Column(String(100), nullable=True)
    zone = Column(SQLEnum(ServiceabilityZone), nullable=False, default=ServiceabilityZone.REST_OF_INDIA)
    is_cod_available = Column(Boolean, nullable=False, default=True)
    is_prepaid_available = Column(Boolean, nullable=False, default=True)
    is_return_pickup_available = Column(Boolean, nullable=False, default=True)
    standard_sla_days = Column(Integer, nullable=False, default=3)
    express_sla_days = Column(Integer, nullable=False, default=1)
    primary_carrier = Column(SQLEnum(CarrierProviderType), nullable=False, default=CarrierProviderType.EKART)
    backup_carrier = Column(SQLEnum(CarrierProviderType), nullable=True, default=CarrierProviderType.DELHIVERY)
    max_weight_kg = Column(Numeric(6, 2), nullable=False, default=Decimal("30.00"))
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    __table_args__ = (
        Index("ix_pincode_zone_active", "pincode", "zone", "is_active"),
    )


class CarrierAccount(Base):
    __tablename__ = "carrier_accounts"

    id = Column(Integer, primary_key=True, index=True)
    carrier_code = Column(SQLEnum(CarrierProviderType), nullable=False, unique=True, index=True)
    account_name = Column(String(100), nullable=False)
    api_key = Column(String(255), nullable=True)
    api_secret = Column(String(255), nullable=True)
    api_endpoint = Column(String(255), nullable=True)
    tracking_url_template = Column(String(255), nullable=True)
    base_rate_500g = Column(Numeric(10, 2), nullable=False, default=Decimal("40.00"))
    additional_500g_rate = Column(Numeric(10, 2), nullable=False, default=Decimal("30.00"))
    cod_charge_percentage = Column(Numeric(5, 2), nullable=False, default=Decimal("1.50"))
    min_cod_fee = Column(Numeric(10, 2), nullable=False, default=Decimal("35.00"))
    is_enabled = Column(Boolean, nullable=False, default=True)
    priority_rank = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)


class DispatchManifest(Base):
    __tablename__ = "dispatch_manifests"

    id = Column(Integer, primary_key=True, index=True)
    manifest_number = Column(String(100), unique=True, index=True, nullable=False)
    warehouse_id = Column(Integer, ForeignKey("warehouses.id", ondelete="CASCADE"), nullable=False, index=True)
    carrier_code = Column(SQLEnum(CarrierProviderType), nullable=False, index=True)
    status = Column(SQLEnum(DispatchManifestStatus), nullable=False, default=DispatchManifestStatus.DRAFT, index=True)
    total_packages = Column(Integer, nullable=False, default=0)
    total_weight_kg = Column(Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    driver_name = Column(String(100), nullable=True)
    driver_phone = Column(String(20), nullable=True)
    vehicle_number = Column(String(30), nullable=True)
    scheduled_pickup_time = Column(DateTime(timezone=True), nullable=True)
    handed_over_at = Column(DateTime(timezone=True), nullable=True)
    created_by_user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=utcnow, onupdate=utcnow, nullable=False)

    packages = relationship("ManifestPackageItem", back_populates="manifest", cascade="all, delete-orphan")


class ManifestPackageItem(Base):
    __tablename__ = "manifest_package_items"

    id = Column(Integer, primary_key=True, index=True)
    manifest_id = Column(Integer, ForeignKey("dispatch_manifests.id", ondelete="CASCADE"), nullable=False, index=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id", ondelete="CASCADE"), nullable=False, index=True)
    tracking_number = Column(String(100), nullable=False, index=True)
    order_number = Column(String(100), nullable=False, index=True)
    destination_pincode = Column(String(6), nullable=False)
    weight_kg = Column(Numeric(6, 2), nullable=False, default=Decimal("0.50"))
    scanned_at = Column(DateTime(timezone=True), nullable=True)
    is_scanned = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)

    manifest = relationship("DispatchManifest", back_populates="packages")


class NDRTicket(Base):
    """Non-Delivery Report ticket for failed delivery attempts."""
    __tablename__ = "ndr_tickets"

    id = Column(Integer, primary_key=True, index=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id", ondelete="CASCADE"), nullable=False, index=True)
    tracking_number = Column(String(100), nullable=False, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    attempt_count = Column(Integer, nullable=False, default=1)
    carrier_failure_reason = Column(String(255), nullable=False)  # Customer unavailable, Incorrect address, Door locked
    carrier_remark = Column(Text, nullable=True)
    customer_action = Column(SQLEnum(NDRActionType), nullable=True)
    rescheduled_delivery_date = Column(DateTime(timezone=True), nullable=True)
    updated_address_line = Column(String(255), nullable=True)
    resolution_status = Column(String(50), nullable=False, default="OPEN")  # OPEN, RESOLVED, RTO_INITIATED
    created_at = Column(DateTime(timezone=True), default=utcnow, nullable=False)
    resolved_at = Column(DateTime(timezone=True), nullable=True)
