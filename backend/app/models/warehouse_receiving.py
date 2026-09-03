from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class WarehouseReceipt(Base):
    """Inbound shipment receipt used by warehouse receiving operations."""

    __tablename__ = "warehouse_receipts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    warehouse_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("warehouses.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    supplier_name: Mapped[str] = mapped_column(String(160), nullable=False)
    purchase_reference: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="OPEN", index=True, nullable=False)
    received_by: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    received_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)


class WarehouseInspection(Base):
    """Quality inspection result for a received SKU quantity."""

    __tablename__ = "warehouse_inspections"
    __table_args__ = (UniqueConstraint("receipt_id", "variant_id", name="uq_receipt_variant_inspection"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    receipt_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("warehouse_receipts.id", ondelete="CASCADE"), index=True, nullable=False
    )
    variant_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("product_variants.id", ondelete="RESTRICT"), index=True, nullable=False
    )
    expected_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    accepted_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    rejected_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    condition: Mapped[str] = mapped_column(String(30), default="GOOD", nullable=False)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    inspected_by: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    inspected_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
