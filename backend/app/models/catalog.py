from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Category(Base):
    """Hierarchical Product Category model."""
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    parent_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    image_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    parent: Mapped[Optional["Category"]] = relationship(
        "Category", remote_side="Category.id", back_populates="subcategories", lazy="selectin"
    )
    subcategories: Mapped[List["Category"]] = relationship(
        "Category", back_populates="parent", cascade="all, delete-orphan", lazy="selectin"
    )
    products: Mapped[List["Product"]] = relationship("Product", back_populates="category")
    attribute_definitions: Mapped[List["AttributeDefinition"]] = relationship(
        "AttributeDefinition", back_populates="category", cascade="all, delete-orphan"
    )


class Brand(Base):
    """Brand / Manufacturer entity."""
    __tablename__ = "brands"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(120), unique=True, index=True, nullable=False)
    logo_url: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    products: Mapped[List["Product"]] = relationship("Product", back_populates="brand")


class AttributeDefinition(Base):
    """Category-specific specification & attribute definition model."""
    __tablename__ = "attribute_definitions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    code: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    data_type: Mapped[str] = mapped_column(String(20), default="TEXT", nullable=False)  # TEXT, NUMBER, BOOLEAN, SELECT, MULTI_SELECT
    unit: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)  # GB, mAh, cm, kg
    is_filterable: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_required: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    options_json: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    category: Mapped[Optional[Category]] = relationship("Category", back_populates="attribute_definitions")
    attribute_values: Mapped[List["AttributeValue"]] = relationship(
        "AttributeValue", back_populates="definition", cascade="all, delete-orphan"
    )


class Product(Base):
    """Catalog Product model."""
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    category_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    brand_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("brands.id", ondelete="SET NULL"), nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(280), unique=True, index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    short_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    highlight_features: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    # Status & Visibility
    status: Mapped[str] = mapped_column(String(30), default="ACTIVE", nullable=False, index=True)  # DRAFT, ACTIVE, OUT_OF_STOCK, ARCHIVED, DISCONTINUED
    visibility: Mapped[str] = mapped_column(String(30), default="SEARCH_CATALOG", nullable=False, index=True)  # SEARCH_CATALOG, CATALOG_ONLY, HIDDEN
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_featured: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
    is_bestseller: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
    
    # SEO
    meta_title: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    meta_keywords: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    meta_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    # Ratings
    rating_avg: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    review_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    
    # Timestamps
    published_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.utcnow, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    category: Mapped[Category] = relationship("Category", back_populates="products", lazy="selectin")
    brand: Mapped[Optional[Brand]] = relationship("Brand", back_populates="products", lazy="selectin")
    variants: Mapped[List["ProductVariant"]] = relationship(
        "ProductVariant", back_populates="product", cascade="all, delete-orphan", lazy="selectin"
    )
    attributes: Mapped[List["ProductAttribute"]] = relationship(
        "ProductAttribute", back_populates="product", cascade="all, delete-orphan", lazy="selectin"
    )
    typed_attribute_values: Mapped[List["AttributeValue"]] = relationship(
        "AttributeValue", back_populates="product", cascade="all, delete-orphan", lazy="selectin"
    )
    images: Mapped[List["ProductImage"]] = relationship(
        "ProductImage", back_populates="product", cascade="all, delete-orphan", lazy="selectin"
    )
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="product")


class ProductVariant(Base):
    """Specific SKU / Variant model (Size, Color, Storage, Model)."""
    __tablename__ = "product_variants"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True
    )
    sku: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    title: Mapped[str] = mapped_column(String(150), nullable=False)  # e.g., "128GB - Space Black"
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    discount_price: Mapped[Optional[float]] = mapped_column(Numeric(10, 2), nullable=True)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    reserved_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    weight_grams: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    dimensions: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)  # "10x5x2 cm"
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    product: Mapped[Product] = relationship("Product", back_populates="variants")
    images: Mapped[List["ProductImage"]] = relationship(
        "ProductImage", back_populates="variant", cascade="all, delete-orphan", lazy="selectin"
    )
    inventory_records: Mapped[List["Inventory"]] = relationship(
        "Inventory", back_populates="variant", cascade="all, delete-orphan"
    )
    variant_attributes: Mapped[List["VariantAttribute"]] = relationship(
        "VariantAttribute", back_populates="variant", cascade="all, delete-orphan", lazy="selectin"
    )


class AttributeValue(Base):
    """Specific attribute value assigned to a product or variant."""
    __tablename__ = "attribute_values"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    attribute_definition_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("attribute_definitions.id", ondelete="CASCADE"), nullable=False, index=True
    )
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True
    )
    variant_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=True, index=True
    )
    value: Mapped[str] = mapped_column(String(255), nullable=False, index=True)

    definition: Mapped[AttributeDefinition] = relationship("AttributeDefinition", back_populates="attribute_values", lazy="selectin")
    product: Mapped[Product] = relationship("Product", back_populates="typed_attribute_values")


class VariantAttribute(Base):
    """Junction mapping variant to specific attribute value definition for unique option checking."""
    __tablename__ = "variant_attributes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    variant_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=False, index=True
    )
    attribute_definition_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("attribute_definitions.id", ondelete="CASCADE"), nullable=False, index=True
    )
    attribute_value_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("attribute_values.id", ondelete="CASCADE"), nullable=False, index=True
    )

    variant: Mapped[ProductVariant] = relationship("ProductVariant", back_populates="variant_attributes")
    definition: Mapped[AttributeDefinition] = relationship("AttributeDefinition", lazy="selectin")
    attribute_value: Mapped[AttributeValue] = relationship("AttributeValue", lazy="selectin")


class ProductImage(Base):
    """Product & Variant Image gallery model."""
    __tablename__ = "product_images"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True
    )
    variant_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("product_variants.id", ondelete="CASCADE"), nullable=True, index=True
    )
    image_url: Mapped[str] = mapped_column(String(500), nullable=False)
    alt_text: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    display_order: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    product: Mapped[Product] = relationship("Product", back_populates="images")
    variant: Mapped[Optional[ProductVariant]] = relationship("ProductVariant", back_populates="images")


class ProductAttribute(Base):
    """Product key-value specifications model (RAM, Processor, Battery, etc.)."""
    __tablename__ = "product_attributes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True
    )
    attribute_name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    attribute_value: Mapped[str] = mapped_column(String(255), nullable=False)

    product: Mapped[Product] = relationship("Product", back_populates="attributes")
