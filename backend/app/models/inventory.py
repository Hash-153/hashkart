from datetime import datetime
from typing import Optional
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Inventory(Base):
    """Warehouse stock tracking model per product variant."""
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    variant_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=False, index=True
    )
    warehouse_location: Mapped[str] = mapped_column(String(100), default="WH-BLR-01", nullable=False)
    stock_available: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    stock_reserved: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    reorder_level: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
    last_restocked_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    variant: Mapped["ProductVariant"] = relationship("ProductVariant", back_populates="inventory_records")


class InventoryTransaction(Base):
    """Audit log of stock movements (RESTOCK, RESERVATION, RELEASE, ORDER_FULFILLMENT, RETURN)."""
    __tablename__ = "inventory_transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    variant_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=False, index=True
    )
    transaction_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    reference_id: Mapped[Optional[str]] = mapped_column(String(100), nullable=True, index=True)  # Order No or Restock Ref
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
