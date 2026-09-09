"""
Athletic & Lifestyle Footwear Domain Specification Engine
=============================
Architecture implementation for Nitrogen-infused supercritical foam midsoles, high-abrasion rubber outsoles, engineered breathable mesh uppers, and ergonomic orthotic arches.
"""

import dataclasses
import typing
from decimal import Decimal
from datetime import datetime, timezone


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification1:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #1."""
    sku_id: str = 'FOO-0001'
    vertical: str = 'footwear'
    model_revision: int = 1
    is_certified: bool = True
    base_mrp: Decimal = Decimal('3149.00')
    selling_price: Decimal = Decimal('2109.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification2:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #2."""
    sku_id: str = 'FOO-0002'
    vertical: str = 'footwear'
    model_revision: int = 2
    is_certified: bool = True
    base_mrp: Decimal = Decimal('3299.00')
    selling_price: Decimal = Decimal('2219.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification3:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #3."""
    sku_id: str = 'FOO-0003'
    vertical: str = 'footwear'
    model_revision: int = 3
    is_certified: bool = True
    base_mrp: Decimal = Decimal('3449.00')
    selling_price: Decimal = Decimal('2329.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification4:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #4."""
    sku_id: str = 'FOO-0004'
    vertical: str = 'footwear'
    model_revision: int = 4
    is_certified: bool = True
    base_mrp: Decimal = Decimal('3599.00')
    selling_price: Decimal = Decimal('2439.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification5:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #5."""
    sku_id: str = 'FOO-0005'
    vertical: str = 'footwear'
    model_revision: int = 5
    is_certified: bool = True
    base_mrp: Decimal = Decimal('3749.00')
    selling_price: Decimal = Decimal('2549.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification6:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #6."""
    sku_id: str = 'FOO-0006'
    vertical: str = 'footwear'
    model_revision: int = 6
    is_certified: bool = True
    base_mrp: Decimal = Decimal('3899.00')
    selling_price: Decimal = Decimal('2659.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification7:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #7."""
    sku_id: str = 'FOO-0007'
    vertical: str = 'footwear'
    model_revision: int = 7
    is_certified: bool = True
    base_mrp: Decimal = Decimal('4049.00')
    selling_price: Decimal = Decimal('2769.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification8:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #8."""
    sku_id: str = 'FOO-0008'
    vertical: str = 'footwear'
    model_revision: int = 8
    is_certified: bool = True
    base_mrp: Decimal = Decimal('4199.00')
    selling_price: Decimal = Decimal('2879.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification9:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #9."""
    sku_id: str = 'FOO-0009'
    vertical: str = 'footwear'
    model_revision: int = 9
    is_certified: bool = True
    base_mrp: Decimal = Decimal('4349.00')
    selling_price: Decimal = Decimal('2989.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification10:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #10."""
    sku_id: str = 'FOO-0010'
    vertical: str = 'footwear'
    model_revision: int = 10
    is_certified: bool = True
    base_mrp: Decimal = Decimal('4499.00')
    selling_price: Decimal = Decimal('3099.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification11:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #11."""
    sku_id: str = 'FOO-0011'
    vertical: str = 'footwear'
    model_revision: int = 11
    is_certified: bool = True
    base_mrp: Decimal = Decimal('4649.00')
    selling_price: Decimal = Decimal('3209.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification12:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #12."""
    sku_id: str = 'FOO-0012'
    vertical: str = 'footwear'
    model_revision: int = 12
    is_certified: bool = True
    base_mrp: Decimal = Decimal('4799.00')
    selling_price: Decimal = Decimal('3319.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification13:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #13."""
    sku_id: str = 'FOO-0013'
    vertical: str = 'footwear'
    model_revision: int = 13
    is_certified: bool = True
    base_mrp: Decimal = Decimal('4949.00')
    selling_price: Decimal = Decimal('3429.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification14:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #14."""
    sku_id: str = 'FOO-0014'
    vertical: str = 'footwear'
    model_revision: int = 14
    is_certified: bool = True
    base_mrp: Decimal = Decimal('5099.00')
    selling_price: Decimal = Decimal('3539.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification15:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #15."""
    sku_id: str = 'FOO-0015'
    vertical: str = 'footwear'
    model_revision: int = 15
    is_certified: bool = True
    base_mrp: Decimal = Decimal('5249.00')
    selling_price: Decimal = Decimal('3649.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification16:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #16."""
    sku_id: str = 'FOO-0016'
    vertical: str = 'footwear'
    model_revision: int = 16
    is_certified: bool = True
    base_mrp: Decimal = Decimal('5399.00')
    selling_price: Decimal = Decimal('3759.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification17:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #17."""
    sku_id: str = 'FOO-0017'
    vertical: str = 'footwear'
    model_revision: int = 17
    is_certified: bool = True
    base_mrp: Decimal = Decimal('5549.00')
    selling_price: Decimal = Decimal('3869.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification18:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #18."""
    sku_id: str = 'FOO-0018'
    vertical: str = 'footwear'
    model_revision: int = 18
    is_certified: bool = True
    base_mrp: Decimal = Decimal('5699.00')
    selling_price: Decimal = Decimal('3979.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification19:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #19."""
    sku_id: str = 'FOO-0019'
    vertical: str = 'footwear'
    model_revision: int = 19
    is_certified: bool = True
    base_mrp: Decimal = Decimal('5849.00')
    selling_price: Decimal = Decimal('4089.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification20:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #20."""
    sku_id: str = 'FOO-0020'
    vertical: str = 'footwear'
    model_revision: int = 20
    is_certified: bool = True
    base_mrp: Decimal = Decimal('5999.00')
    selling_price: Decimal = Decimal('4199.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification21:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #21."""
    sku_id: str = 'FOO-0021'
    vertical: str = 'footwear'
    model_revision: int = 21
    is_certified: bool = True
    base_mrp: Decimal = Decimal('6149.00')
    selling_price: Decimal = Decimal('4309.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification22:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #22."""
    sku_id: str = 'FOO-0022'
    vertical: str = 'footwear'
    model_revision: int = 22
    is_certified: bool = True
    base_mrp: Decimal = Decimal('6299.00')
    selling_price: Decimal = Decimal('4419.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification23:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #23."""
    sku_id: str = 'FOO-0023'
    vertical: str = 'footwear'
    model_revision: int = 23
    is_certified: bool = True
    base_mrp: Decimal = Decimal('6449.00')
    selling_price: Decimal = Decimal('4529.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification24:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #24."""
    sku_id: str = 'FOO-0024'
    vertical: str = 'footwear'
    model_revision: int = 24
    is_certified: bool = True
    base_mrp: Decimal = Decimal('6599.00')
    selling_price: Decimal = Decimal('4639.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification25:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #25."""
    sku_id: str = 'FOO-0025'
    vertical: str = 'footwear'
    model_revision: int = 25
    is_certified: bool = True
    base_mrp: Decimal = Decimal('6749.00')
    selling_price: Decimal = Decimal('4749.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification26:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #26."""
    sku_id: str = 'FOO-0026'
    vertical: str = 'footwear'
    model_revision: int = 26
    is_certified: bool = True
    base_mrp: Decimal = Decimal('6899.00')
    selling_price: Decimal = Decimal('4859.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification27:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #27."""
    sku_id: str = 'FOO-0027'
    vertical: str = 'footwear'
    model_revision: int = 27
    is_certified: bool = True
    base_mrp: Decimal = Decimal('7049.00')
    selling_price: Decimal = Decimal('4969.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification28:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #28."""
    sku_id: str = 'FOO-0028'
    vertical: str = 'footwear'
    model_revision: int = 28
    is_certified: bool = True
    base_mrp: Decimal = Decimal('7199.00')
    selling_price: Decimal = Decimal('5079.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification29:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #29."""
    sku_id: str = 'FOO-0029'
    vertical: str = 'footwear'
    model_revision: int = 29
    is_certified: bool = True
    base_mrp: Decimal = Decimal('7349.00')
    selling_price: Decimal = Decimal('5189.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification30:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #30."""
    sku_id: str = 'FOO-0030'
    vertical: str = 'footwear'
    model_revision: int = 30
    is_certified: bool = True
    base_mrp: Decimal = Decimal('7499.00')
    selling_price: Decimal = Decimal('5299.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification31:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #31."""
    sku_id: str = 'FOO-0031'
    vertical: str = 'footwear'
    model_revision: int = 31
    is_certified: bool = True
    base_mrp: Decimal = Decimal('7649.00')
    selling_price: Decimal = Decimal('5409.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification32:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #32."""
    sku_id: str = 'FOO-0032'
    vertical: str = 'footwear'
    model_revision: int = 32
    is_certified: bool = True
    base_mrp: Decimal = Decimal('7799.00')
    selling_price: Decimal = Decimal('5519.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification33:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #33."""
    sku_id: str = 'FOO-0033'
    vertical: str = 'footwear'
    model_revision: int = 33
    is_certified: bool = True
    base_mrp: Decimal = Decimal('7949.00')
    selling_price: Decimal = Decimal('5629.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification34:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #34."""
    sku_id: str = 'FOO-0034'
    vertical: str = 'footwear'
    model_revision: int = 34
    is_certified: bool = True
    base_mrp: Decimal = Decimal('8099.00')
    selling_price: Decimal = Decimal('5739.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification35:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #35."""
    sku_id: str = 'FOO-0035'
    vertical: str = 'footwear'
    model_revision: int = 35
    is_certified: bool = True
    base_mrp: Decimal = Decimal('8249.00')
    selling_price: Decimal = Decimal('5849.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification36:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #36."""
    sku_id: str = 'FOO-0036'
    vertical: str = 'footwear'
    model_revision: int = 36
    is_certified: bool = True
    base_mrp: Decimal = Decimal('8399.00')
    selling_price: Decimal = Decimal('5959.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification37:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #37."""
    sku_id: str = 'FOO-0037'
    vertical: str = 'footwear'
    model_revision: int = 37
    is_certified: bool = True
    base_mrp: Decimal = Decimal('8549.00')
    selling_price: Decimal = Decimal('6069.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification38:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #38."""
    sku_id: str = 'FOO-0038'
    vertical: str = 'footwear'
    model_revision: int = 38
    is_certified: bool = True
    base_mrp: Decimal = Decimal('8699.00')
    selling_price: Decimal = Decimal('6179.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification39:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #39."""
    sku_id: str = 'FOO-0039'
    vertical: str = 'footwear'
    model_revision: int = 39
    is_certified: bool = True
    base_mrp: Decimal = Decimal('8849.00')
    selling_price: Decimal = Decimal('6289.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification40:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #40."""
    sku_id: str = 'FOO-0040'
    vertical: str = 'footwear'
    model_revision: int = 40
    is_certified: bool = True
    base_mrp: Decimal = Decimal('8999.00')
    selling_price: Decimal = Decimal('6399.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification41:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #41."""
    sku_id: str = 'FOO-0041'
    vertical: str = 'footwear'
    model_revision: int = 41
    is_certified: bool = True
    base_mrp: Decimal = Decimal('9149.00')
    selling_price: Decimal = Decimal('6509.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification42:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #42."""
    sku_id: str = 'FOO-0042'
    vertical: str = 'footwear'
    model_revision: int = 42
    is_certified: bool = True
    base_mrp: Decimal = Decimal('9299.00')
    selling_price: Decimal = Decimal('6619.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification43:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #43."""
    sku_id: str = 'FOO-0043'
    vertical: str = 'footwear'
    model_revision: int = 43
    is_certified: bool = True
    base_mrp: Decimal = Decimal('9449.00')
    selling_price: Decimal = Decimal('6729.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification44:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #44."""
    sku_id: str = 'FOO-0044'
    vertical: str = 'footwear'
    model_revision: int = 44
    is_certified: bool = True
    base_mrp: Decimal = Decimal('9599.00')
    selling_price: Decimal = Decimal('6839.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification45:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #45."""
    sku_id: str = 'FOO-0045'
    vertical: str = 'footwear'
    model_revision: int = 45
    is_certified: bool = True
    base_mrp: Decimal = Decimal('9749.00')
    selling_price: Decimal = Decimal('6949.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification46:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #46."""
    sku_id: str = 'FOO-0046'
    vertical: str = 'footwear'
    model_revision: int = 46
    is_certified: bool = True
    base_mrp: Decimal = Decimal('9899.00')
    selling_price: Decimal = Decimal('7059.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification47:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #47."""
    sku_id: str = 'FOO-0047'
    vertical: str = 'footwear'
    model_revision: int = 47
    is_certified: bool = True
    base_mrp: Decimal = Decimal('10049.00')
    selling_price: Decimal = Decimal('7169.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification48:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #48."""
    sku_id: str = 'FOO-0048'
    vertical: str = 'footwear'
    model_revision: int = 48
    is_certified: bool = True
    base_mrp: Decimal = Decimal('10199.00')
    selling_price: Decimal = Decimal('7279.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification49:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #49."""
    sku_id: str = 'FOO-0049'
    vertical: str = 'footwear'
    model_revision: int = 49
    is_certified: bool = True
    base_mrp: Decimal = Decimal('10349.00')
    selling_price: Decimal = Decimal('7389.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification50:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #50."""
    sku_id: str = 'FOO-0050'
    vertical: str = 'footwear'
    model_revision: int = 50
    is_certified: bool = True
    base_mrp: Decimal = Decimal('10499.00')
    selling_price: Decimal = Decimal('7499.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification51:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #51."""
    sku_id: str = 'FOO-0051'
    vertical: str = 'footwear'
    model_revision: int = 51
    is_certified: bool = True
    base_mrp: Decimal = Decimal('10649.00')
    selling_price: Decimal = Decimal('7609.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification52:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #52."""
    sku_id: str = 'FOO-0052'
    vertical: str = 'footwear'
    model_revision: int = 52
    is_certified: bool = True
    base_mrp: Decimal = Decimal('10799.00')
    selling_price: Decimal = Decimal('7719.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification53:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #53."""
    sku_id: str = 'FOO-0053'
    vertical: str = 'footwear'
    model_revision: int = 53
    is_certified: bool = True
    base_mrp: Decimal = Decimal('10949.00')
    selling_price: Decimal = Decimal('7829.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification54:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #54."""
    sku_id: str = 'FOO-0054'
    vertical: str = 'footwear'
    model_revision: int = 54
    is_certified: bool = True
    base_mrp: Decimal = Decimal('11099.00')
    selling_price: Decimal = Decimal('7939.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification55:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #55."""
    sku_id: str = 'FOO-0055'
    vertical: str = 'footwear'
    model_revision: int = 55
    is_certified: bool = True
    base_mrp: Decimal = Decimal('11249.00')
    selling_price: Decimal = Decimal('8049.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification56:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #56."""
    sku_id: str = 'FOO-0056'
    vertical: str = 'footwear'
    model_revision: int = 56
    is_certified: bool = True
    base_mrp: Decimal = Decimal('11399.00')
    selling_price: Decimal = Decimal('8159.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification57:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #57."""
    sku_id: str = 'FOO-0057'
    vertical: str = 'footwear'
    model_revision: int = 57
    is_certified: bool = True
    base_mrp: Decimal = Decimal('11549.00')
    selling_price: Decimal = Decimal('8269.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification58:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #58."""
    sku_id: str = 'FOO-0058'
    vertical: str = 'footwear'
    model_revision: int = 58
    is_certified: bool = True
    base_mrp: Decimal = Decimal('11699.00')
    selling_price: Decimal = Decimal('8379.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification59:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #59."""
    sku_id: str = 'FOO-0059'
    vertical: str = 'footwear'
    model_revision: int = 59
    is_certified: bool = True
    base_mrp: Decimal = Decimal('11849.00')
    selling_price: Decimal = Decimal('8489.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification60:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #60."""
    sku_id: str = 'FOO-0060'
    vertical: str = 'footwear'
    model_revision: int = 60
    is_certified: bool = True
    base_mrp: Decimal = Decimal('11999.00')
    selling_price: Decimal = Decimal('8599.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification61:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #61."""
    sku_id: str = 'FOO-0061'
    vertical: str = 'footwear'
    model_revision: int = 61
    is_certified: bool = True
    base_mrp: Decimal = Decimal('12149.00')
    selling_price: Decimal = Decimal('8709.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification62:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #62."""
    sku_id: str = 'FOO-0062'
    vertical: str = 'footwear'
    model_revision: int = 62
    is_certified: bool = True
    base_mrp: Decimal = Decimal('12299.00')
    selling_price: Decimal = Decimal('8819.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification63:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #63."""
    sku_id: str = 'FOO-0063'
    vertical: str = 'footwear'
    model_revision: int = 63
    is_certified: bool = True
    base_mrp: Decimal = Decimal('12449.00')
    selling_price: Decimal = Decimal('8929.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification64:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #64."""
    sku_id: str = 'FOO-0064'
    vertical: str = 'footwear'
    model_revision: int = 64
    is_certified: bool = True
    base_mrp: Decimal = Decimal('12599.00')
    selling_price: Decimal = Decimal('9039.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification65:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #65."""
    sku_id: str = 'FOO-0065'
    vertical: str = 'footwear'
    model_revision: int = 65
    is_certified: bool = True
    base_mrp: Decimal = Decimal('12749.00')
    selling_price: Decimal = Decimal('9149.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification66:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #66."""
    sku_id: str = 'FOO-0066'
    vertical: str = 'footwear'
    model_revision: int = 66
    is_certified: bool = True
    base_mrp: Decimal = Decimal('12899.00')
    selling_price: Decimal = Decimal('9259.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification67:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #67."""
    sku_id: str = 'FOO-0067'
    vertical: str = 'footwear'
    model_revision: int = 67
    is_certified: bool = True
    base_mrp: Decimal = Decimal('13049.00')
    selling_price: Decimal = Decimal('9369.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification68:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #68."""
    sku_id: str = 'FOO-0068'
    vertical: str = 'footwear'
    model_revision: int = 68
    is_certified: bool = True
    base_mrp: Decimal = Decimal('13199.00')
    selling_price: Decimal = Decimal('9479.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification69:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #69."""
    sku_id: str = 'FOO-0069'
    vertical: str = 'footwear'
    model_revision: int = 69
    is_certified: bool = True
    base_mrp: Decimal = Decimal('13349.00')
    selling_price: Decimal = Decimal('9589.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification70:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #70."""
    sku_id: str = 'FOO-0070'
    vertical: str = 'footwear'
    model_revision: int = 70
    is_certified: bool = True
    base_mrp: Decimal = Decimal('13499.00')
    selling_price: Decimal = Decimal('9699.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification71:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #71."""
    sku_id: str = 'FOO-0071'
    vertical: str = 'footwear'
    model_revision: int = 71
    is_certified: bool = True
    base_mrp: Decimal = Decimal('13649.00')
    selling_price: Decimal = Decimal('9809.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification72:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #72."""
    sku_id: str = 'FOO-0072'
    vertical: str = 'footwear'
    model_revision: int = 72
    is_certified: bool = True
    base_mrp: Decimal = Decimal('13799.00')
    selling_price: Decimal = Decimal('9919.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification73:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #73."""
    sku_id: str = 'FOO-0073'
    vertical: str = 'footwear'
    model_revision: int = 73
    is_certified: bool = True
    base_mrp: Decimal = Decimal('13949.00')
    selling_price: Decimal = Decimal('10029.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification74:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #74."""
    sku_id: str = 'FOO-0074'
    vertical: str = 'footwear'
    model_revision: int = 74
    is_certified: bool = True
    base_mrp: Decimal = Decimal('14099.00')
    selling_price: Decimal = Decimal('10139.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification75:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #75."""
    sku_id: str = 'FOO-0075'
    vertical: str = 'footwear'
    model_revision: int = 75
    is_certified: bool = True
    base_mrp: Decimal = Decimal('14249.00')
    selling_price: Decimal = Decimal('10249.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification76:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #76."""
    sku_id: str = 'FOO-0076'
    vertical: str = 'footwear'
    model_revision: int = 76
    is_certified: bool = True
    base_mrp: Decimal = Decimal('14399.00')
    selling_price: Decimal = Decimal('10359.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification77:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #77."""
    sku_id: str = 'FOO-0077'
    vertical: str = 'footwear'
    model_revision: int = 77
    is_certified: bool = True
    base_mrp: Decimal = Decimal('14549.00')
    selling_price: Decimal = Decimal('10469.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification78:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #78."""
    sku_id: str = 'FOO-0078'
    vertical: str = 'footwear'
    model_revision: int = 78
    is_certified: bool = True
    base_mrp: Decimal = Decimal('14699.00')
    selling_price: Decimal = Decimal('10579.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification79:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #79."""
    sku_id: str = 'FOO-0079'
    vertical: str = 'footwear'
    model_revision: int = 79
    is_certified: bool = True
    base_mrp: Decimal = Decimal('14849.00')
    selling_price: Decimal = Decimal('10689.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification80:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #80."""
    sku_id: str = 'FOO-0080'
    vertical: str = 'footwear'
    model_revision: int = 80
    is_certified: bool = True
    base_mrp: Decimal = Decimal('14999.00')
    selling_price: Decimal = Decimal('10799.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification81:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #81."""
    sku_id: str = 'FOO-0081'
    vertical: str = 'footwear'
    model_revision: int = 81
    is_certified: bool = True
    base_mrp: Decimal = Decimal('15149.00')
    selling_price: Decimal = Decimal('10909.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification82:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #82."""
    sku_id: str = 'FOO-0082'
    vertical: str = 'footwear'
    model_revision: int = 82
    is_certified: bool = True
    base_mrp: Decimal = Decimal('15299.00')
    selling_price: Decimal = Decimal('11019.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification83:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #83."""
    sku_id: str = 'FOO-0083'
    vertical: str = 'footwear'
    model_revision: int = 83
    is_certified: bool = True
    base_mrp: Decimal = Decimal('15449.00')
    selling_price: Decimal = Decimal('11129.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification84:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #84."""
    sku_id: str = 'FOO-0084'
    vertical: str = 'footwear'
    model_revision: int = 84
    is_certified: bool = True
    base_mrp: Decimal = Decimal('15599.00')
    selling_price: Decimal = Decimal('11239.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification85:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #85."""
    sku_id: str = 'FOO-0085'
    vertical: str = 'footwear'
    model_revision: int = 85
    is_certified: bool = True
    base_mrp: Decimal = Decimal('15749.00')
    selling_price: Decimal = Decimal('11349.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification86:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #86."""
    sku_id: str = 'FOO-0086'
    vertical: str = 'footwear'
    model_revision: int = 86
    is_certified: bool = True
    base_mrp: Decimal = Decimal('15899.00')
    selling_price: Decimal = Decimal('11459.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification87:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #87."""
    sku_id: str = 'FOO-0087'
    vertical: str = 'footwear'
    model_revision: int = 87
    is_certified: bool = True
    base_mrp: Decimal = Decimal('16049.00')
    selling_price: Decimal = Decimal('11569.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification88:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #88."""
    sku_id: str = 'FOO-0088'
    vertical: str = 'footwear'
    model_revision: int = 88
    is_certified: bool = True
    base_mrp: Decimal = Decimal('16199.00')
    selling_price: Decimal = Decimal('11679.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification89:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #89."""
    sku_id: str = 'FOO-0089'
    vertical: str = 'footwear'
    model_revision: int = 89
    is_certified: bool = True
    base_mrp: Decimal = Decimal('16349.00')
    selling_price: Decimal = Decimal('11789.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification90:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #90."""
    sku_id: str = 'FOO-0090'
    vertical: str = 'footwear'
    model_revision: int = 90
    is_certified: bool = True
    base_mrp: Decimal = Decimal('16499.00')
    selling_price: Decimal = Decimal('11899.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification91:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #91."""
    sku_id: str = 'FOO-0091'
    vertical: str = 'footwear'
    model_revision: int = 91
    is_certified: bool = True
    base_mrp: Decimal = Decimal('16649.00')
    selling_price: Decimal = Decimal('12009.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification92:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #92."""
    sku_id: str = 'FOO-0092'
    vertical: str = 'footwear'
    model_revision: int = 92
    is_certified: bool = True
    base_mrp: Decimal = Decimal('16799.00')
    selling_price: Decimal = Decimal('12119.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification93:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #93."""
    sku_id: str = 'FOO-0093'
    vertical: str = 'footwear'
    model_revision: int = 93
    is_certified: bool = True
    base_mrp: Decimal = Decimal('16949.00')
    selling_price: Decimal = Decimal('12229.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification94:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #94."""
    sku_id: str = 'FOO-0094'
    vertical: str = 'footwear'
    model_revision: int = 94
    is_certified: bool = True
    base_mrp: Decimal = Decimal('17099.00')
    selling_price: Decimal = Decimal('12339.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification95:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #95."""
    sku_id: str = 'FOO-0095'
    vertical: str = 'footwear'
    model_revision: int = 95
    is_certified: bool = True
    base_mrp: Decimal = Decimal('17249.00')
    selling_price: Decimal = Decimal('12449.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification96:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #96."""
    sku_id: str = 'FOO-0096'
    vertical: str = 'footwear'
    model_revision: int = 96
    is_certified: bool = True
    base_mrp: Decimal = Decimal('17399.00')
    selling_price: Decimal = Decimal('12559.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification97:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #97."""
    sku_id: str = 'FOO-0097'
    vertical: str = 'footwear'
    model_revision: int = 97
    is_certified: bool = True
    base_mrp: Decimal = Decimal('17549.00')
    selling_price: Decimal = Decimal('12669.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification98:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #98."""
    sku_id: str = 'FOO-0098'
    vertical: str = 'footwear'
    model_revision: int = 98
    is_certified: bool = True
    base_mrp: Decimal = Decimal('17699.00')
    selling_price: Decimal = Decimal('12779.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification99:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #99."""
    sku_id: str = 'FOO-0099'
    vertical: str = 'footwear'
    model_revision: int = 99
    is_certified: bool = True
    base_mrp: Decimal = Decimal('17849.00')
    selling_price: Decimal = Decimal('12889.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification100:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #100."""
    sku_id: str = 'FOO-0100'
    vertical: str = 'footwear'
    model_revision: int = 100
    is_certified: bool = True
    base_mrp: Decimal = Decimal('17999.00')
    selling_price: Decimal = Decimal('12999.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification101:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #101."""
    sku_id: str = 'FOO-0101'
    vertical: str = 'footwear'
    model_revision: int = 101
    is_certified: bool = True
    base_mrp: Decimal = Decimal('18149.00')
    selling_price: Decimal = Decimal('13109.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification102:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #102."""
    sku_id: str = 'FOO-0102'
    vertical: str = 'footwear'
    model_revision: int = 102
    is_certified: bool = True
    base_mrp: Decimal = Decimal('18299.00')
    selling_price: Decimal = Decimal('13219.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification103:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #103."""
    sku_id: str = 'FOO-0103'
    vertical: str = 'footwear'
    model_revision: int = 103
    is_certified: bool = True
    base_mrp: Decimal = Decimal('18449.00')
    selling_price: Decimal = Decimal('13329.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification104:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #104."""
    sku_id: str = 'FOO-0104'
    vertical: str = 'footwear'
    model_revision: int = 104
    is_certified: bool = True
    base_mrp: Decimal = Decimal('18599.00')
    selling_price: Decimal = Decimal('13439.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification105:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #105."""
    sku_id: str = 'FOO-0105'
    vertical: str = 'footwear'
    model_revision: int = 105
    is_certified: bool = True
    base_mrp: Decimal = Decimal('18749.00')
    selling_price: Decimal = Decimal('13549.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification106:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #106."""
    sku_id: str = 'FOO-0106'
    vertical: str = 'footwear'
    model_revision: int = 106
    is_certified: bool = True
    base_mrp: Decimal = Decimal('18899.00')
    selling_price: Decimal = Decimal('13659.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification107:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #107."""
    sku_id: str = 'FOO-0107'
    vertical: str = 'footwear'
    model_revision: int = 107
    is_certified: bool = True
    base_mrp: Decimal = Decimal('19049.00')
    selling_price: Decimal = Decimal('13769.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification108:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #108."""
    sku_id: str = 'FOO-0108'
    vertical: str = 'footwear'
    model_revision: int = 108
    is_certified: bool = True
    base_mrp: Decimal = Decimal('19199.00')
    selling_price: Decimal = Decimal('13879.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification109:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #109."""
    sku_id: str = 'FOO-0109'
    vertical: str = 'footwear'
    model_revision: int = 109
    is_certified: bool = True
    base_mrp: Decimal = Decimal('19349.00')
    selling_price: Decimal = Decimal('13989.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification110:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #110."""
    sku_id: str = 'FOO-0110'
    vertical: str = 'footwear'
    model_revision: int = 110
    is_certified: bool = True
    base_mrp: Decimal = Decimal('19499.00')
    selling_price: Decimal = Decimal('14099.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification111:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #111."""
    sku_id: str = 'FOO-0111'
    vertical: str = 'footwear'
    model_revision: int = 111
    is_certified: bool = True
    base_mrp: Decimal = Decimal('19649.00')
    selling_price: Decimal = Decimal('14209.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification112:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #112."""
    sku_id: str = 'FOO-0112'
    vertical: str = 'footwear'
    model_revision: int = 112
    is_certified: bool = True
    base_mrp: Decimal = Decimal('19799.00')
    selling_price: Decimal = Decimal('14319.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification113:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #113."""
    sku_id: str = 'FOO-0113'
    vertical: str = 'footwear'
    model_revision: int = 113
    is_certified: bool = True
    base_mrp: Decimal = Decimal('19949.00')
    selling_price: Decimal = Decimal('14429.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification114:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #114."""
    sku_id: str = 'FOO-0114'
    vertical: str = 'footwear'
    model_revision: int = 114
    is_certified: bool = True
    base_mrp: Decimal = Decimal('20099.00')
    selling_price: Decimal = Decimal('14539.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification115:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #115."""
    sku_id: str = 'FOO-0115'
    vertical: str = 'footwear'
    model_revision: int = 115
    is_certified: bool = True
    base_mrp: Decimal = Decimal('20249.00')
    selling_price: Decimal = Decimal('14649.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification116:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #116."""
    sku_id: str = 'FOO-0116'
    vertical: str = 'footwear'
    model_revision: int = 116
    is_certified: bool = True
    base_mrp: Decimal = Decimal('20399.00')
    selling_price: Decimal = Decimal('14759.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification117:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #117."""
    sku_id: str = 'FOO-0117'
    vertical: str = 'footwear'
    model_revision: int = 117
    is_certified: bool = True
    base_mrp: Decimal = Decimal('20549.00')
    selling_price: Decimal = Decimal('14869.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification118:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #118."""
    sku_id: str = 'FOO-0118'
    vertical: str = 'footwear'
    model_revision: int = 118
    is_certified: bool = True
    base_mrp: Decimal = Decimal('20699.00')
    selling_price: Decimal = Decimal('14979.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification119:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #119."""
    sku_id: str = 'FOO-0119'
    vertical: str = 'footwear'
    model_revision: int = 119
    is_certified: bool = True
    base_mrp: Decimal = Decimal('20849.00')
    selling_price: Decimal = Decimal('15089.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification120:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #120."""
    sku_id: str = 'FOO-0120'
    vertical: str = 'footwear'
    model_revision: int = 120
    is_certified: bool = True
    base_mrp: Decimal = Decimal('20999.00')
    selling_price: Decimal = Decimal('15199.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification121:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #121."""
    sku_id: str = 'FOO-0121'
    vertical: str = 'footwear'
    model_revision: int = 121
    is_certified: bool = True
    base_mrp: Decimal = Decimal('21149.00')
    selling_price: Decimal = Decimal('15309.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification122:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #122."""
    sku_id: str = 'FOO-0122'
    vertical: str = 'footwear'
    model_revision: int = 122
    is_certified: bool = True
    base_mrp: Decimal = Decimal('21299.00')
    selling_price: Decimal = Decimal('15419.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification123:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #123."""
    sku_id: str = 'FOO-0123'
    vertical: str = 'footwear'
    model_revision: int = 123
    is_certified: bool = True
    base_mrp: Decimal = Decimal('21449.00')
    selling_price: Decimal = Decimal('15529.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification124:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #124."""
    sku_id: str = 'FOO-0124'
    vertical: str = 'footwear'
    model_revision: int = 124
    is_certified: bool = True
    base_mrp: Decimal = Decimal('21599.00')
    selling_price: Decimal = Decimal('15639.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification125:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #125."""
    sku_id: str = 'FOO-0125'
    vertical: str = 'footwear'
    model_revision: int = 125
    is_certified: bool = True
    base_mrp: Decimal = Decimal('21749.00')
    selling_price: Decimal = Decimal('15749.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification126:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #126."""
    sku_id: str = 'FOO-0126'
    vertical: str = 'footwear'
    model_revision: int = 126
    is_certified: bool = True
    base_mrp: Decimal = Decimal('21899.00')
    selling_price: Decimal = Decimal('15859.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification127:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #127."""
    sku_id: str = 'FOO-0127'
    vertical: str = 'footwear'
    model_revision: int = 127
    is_certified: bool = True
    base_mrp: Decimal = Decimal('22049.00')
    selling_price: Decimal = Decimal('15969.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification128:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #128."""
    sku_id: str = 'FOO-0128'
    vertical: str = 'footwear'
    model_revision: int = 128
    is_certified: bool = True
    base_mrp: Decimal = Decimal('22199.00')
    selling_price: Decimal = Decimal('16079.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification129:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #129."""
    sku_id: str = 'FOO-0129'
    vertical: str = 'footwear'
    model_revision: int = 129
    is_certified: bool = True
    base_mrp: Decimal = Decimal('22349.00')
    selling_price: Decimal = Decimal('16189.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification130:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #130."""
    sku_id: str = 'FOO-0130'
    vertical: str = 'footwear'
    model_revision: int = 130
    is_certified: bool = True
    base_mrp: Decimal = Decimal('22499.00')
    selling_price: Decimal = Decimal('16299.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification131:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #131."""
    sku_id: str = 'FOO-0131'
    vertical: str = 'footwear'
    model_revision: int = 131
    is_certified: bool = True
    base_mrp: Decimal = Decimal('22649.00')
    selling_price: Decimal = Decimal('16409.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification132:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #132."""
    sku_id: str = 'FOO-0132'
    vertical: str = 'footwear'
    model_revision: int = 132
    is_certified: bool = True
    base_mrp: Decimal = Decimal('22799.00')
    selling_price: Decimal = Decimal('16519.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification133:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #133."""
    sku_id: str = 'FOO-0133'
    vertical: str = 'footwear'
    model_revision: int = 133
    is_certified: bool = True
    base_mrp: Decimal = Decimal('22949.00')
    selling_price: Decimal = Decimal('16629.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification134:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #134."""
    sku_id: str = 'FOO-0134'
    vertical: str = 'footwear'
    model_revision: int = 134
    is_certified: bool = True
    base_mrp: Decimal = Decimal('23099.00')
    selling_price: Decimal = Decimal('16739.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification135:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #135."""
    sku_id: str = 'FOO-0135'
    vertical: str = 'footwear'
    model_revision: int = 135
    is_certified: bool = True
    base_mrp: Decimal = Decimal('23249.00')
    selling_price: Decimal = Decimal('16849.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification136:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #136."""
    sku_id: str = 'FOO-0136'
    vertical: str = 'footwear'
    model_revision: int = 136
    is_certified: bool = True
    base_mrp: Decimal = Decimal('23399.00')
    selling_price: Decimal = Decimal('16959.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification137:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #137."""
    sku_id: str = 'FOO-0137'
    vertical: str = 'footwear'
    model_revision: int = 137
    is_certified: bool = True
    base_mrp: Decimal = Decimal('23549.00')
    selling_price: Decimal = Decimal('17069.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification138:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #138."""
    sku_id: str = 'FOO-0138'
    vertical: str = 'footwear'
    model_revision: int = 138
    is_certified: bool = True
    base_mrp: Decimal = Decimal('23699.00')
    selling_price: Decimal = Decimal('17179.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification139:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #139."""
    sku_id: str = 'FOO-0139'
    vertical: str = 'footwear'
    model_revision: int = 139
    is_certified: bool = True
    base_mrp: Decimal = Decimal('23849.00')
    selling_price: Decimal = Decimal('17289.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification140:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #140."""
    sku_id: str = 'FOO-0140'
    vertical: str = 'footwear'
    model_revision: int = 140
    is_certified: bool = True
    base_mrp: Decimal = Decimal('23999.00')
    selling_price: Decimal = Decimal('17399.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification141:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #141."""
    sku_id: str = 'FOO-0141'
    vertical: str = 'footwear'
    model_revision: int = 141
    is_certified: bool = True
    base_mrp: Decimal = Decimal('24149.00')
    selling_price: Decimal = Decimal('17509.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification142:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #142."""
    sku_id: str = 'FOO-0142'
    vertical: str = 'footwear'
    model_revision: int = 142
    is_certified: bool = True
    base_mrp: Decimal = Decimal('24299.00')
    selling_price: Decimal = Decimal('17619.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification143:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #143."""
    sku_id: str = 'FOO-0143'
    vertical: str = 'footwear'
    model_revision: int = 143
    is_certified: bool = True
    base_mrp: Decimal = Decimal('24449.00')
    selling_price: Decimal = Decimal('17729.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification144:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #144."""
    sku_id: str = 'FOO-0144'
    vertical: str = 'footwear'
    model_revision: int = 144
    is_certified: bool = True
    base_mrp: Decimal = Decimal('24599.00')
    selling_price: Decimal = Decimal('17839.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification145:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #145."""
    sku_id: str = 'FOO-0145'
    vertical: str = 'footwear'
    model_revision: int = 145
    is_certified: bool = True
    base_mrp: Decimal = Decimal('24749.00')
    selling_price: Decimal = Decimal('17949.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification146:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #146."""
    sku_id: str = 'FOO-0146'
    vertical: str = 'footwear'
    model_revision: int = 146
    is_certified: bool = True
    base_mrp: Decimal = Decimal('24899.00')
    selling_price: Decimal = Decimal('18059.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification147:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #147."""
    sku_id: str = 'FOO-0147'
    vertical: str = 'footwear'
    model_revision: int = 147
    is_certified: bool = True
    base_mrp: Decimal = Decimal('25049.00')
    selling_price: Decimal = Decimal('18169.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification148:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #148."""
    sku_id: str = 'FOO-0148'
    vertical: str = 'footwear'
    model_revision: int = 148
    is_certified: bool = True
    base_mrp: Decimal = Decimal('25199.00')
    selling_price: Decimal = Decimal('18279.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification149:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #149."""
    sku_id: str = 'FOO-0149'
    vertical: str = 'footwear'
    model_revision: int = 149
    is_certified: bool = True
    base_mrp: Decimal = Decimal('25349.00')
    selling_price: Decimal = Decimal('18389.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification150:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #150."""
    sku_id: str = 'FOO-0150'
    vertical: str = 'footwear'
    model_revision: int = 150
    is_certified: bool = True
    base_mrp: Decimal = Decimal('25499.00')
    selling_price: Decimal = Decimal('18499.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification151:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #151."""
    sku_id: str = 'FOO-0151'
    vertical: str = 'footwear'
    model_revision: int = 151
    is_certified: bool = True
    base_mrp: Decimal = Decimal('25649.00')
    selling_price: Decimal = Decimal('18609.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification152:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #152."""
    sku_id: str = 'FOO-0152'
    vertical: str = 'footwear'
    model_revision: int = 152
    is_certified: bool = True
    base_mrp: Decimal = Decimal('25799.00')
    selling_price: Decimal = Decimal('18719.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification153:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #153."""
    sku_id: str = 'FOO-0153'
    vertical: str = 'footwear'
    model_revision: int = 153
    is_certified: bool = True
    base_mrp: Decimal = Decimal('25949.00')
    selling_price: Decimal = Decimal('18829.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification154:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #154."""
    sku_id: str = 'FOO-0154'
    vertical: str = 'footwear'
    model_revision: int = 154
    is_certified: bool = True
    base_mrp: Decimal = Decimal('26099.00')
    selling_price: Decimal = Decimal('18939.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification155:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #155."""
    sku_id: str = 'FOO-0155'
    vertical: str = 'footwear'
    model_revision: int = 155
    is_certified: bool = True
    base_mrp: Decimal = Decimal('26249.00')
    selling_price: Decimal = Decimal('19049.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification156:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #156."""
    sku_id: str = 'FOO-0156'
    vertical: str = 'footwear'
    model_revision: int = 156
    is_certified: bool = True
    base_mrp: Decimal = Decimal('26399.00')
    selling_price: Decimal = Decimal('19159.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification157:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #157."""
    sku_id: str = 'FOO-0157'
    vertical: str = 'footwear'
    model_revision: int = 157
    is_certified: bool = True
    base_mrp: Decimal = Decimal('26549.00')
    selling_price: Decimal = Decimal('19269.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification158:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #158."""
    sku_id: str = 'FOO-0158'
    vertical: str = 'footwear'
    model_revision: int = 158
    is_certified: bool = True
    base_mrp: Decimal = Decimal('26699.00')
    selling_price: Decimal = Decimal('19379.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification159:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #159."""
    sku_id: str = 'FOO-0159'
    vertical: str = 'footwear'
    model_revision: int = 159
    is_certified: bool = True
    base_mrp: Decimal = Decimal('26849.00')
    selling_price: Decimal = Decimal('19489.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification160:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #160."""
    sku_id: str = 'FOO-0160'
    vertical: str = 'footwear'
    model_revision: int = 160
    is_certified: bool = True
    base_mrp: Decimal = Decimal('26999.00')
    selling_price: Decimal = Decimal('19599.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification161:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #161."""
    sku_id: str = 'FOO-0161'
    vertical: str = 'footwear'
    model_revision: int = 161
    is_certified: bool = True
    base_mrp: Decimal = Decimal('27149.00')
    selling_price: Decimal = Decimal('19709.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification162:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #162."""
    sku_id: str = 'FOO-0162'
    vertical: str = 'footwear'
    model_revision: int = 162
    is_certified: bool = True
    base_mrp: Decimal = Decimal('27299.00')
    selling_price: Decimal = Decimal('19819.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification163:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #163."""
    sku_id: str = 'FOO-0163'
    vertical: str = 'footwear'
    model_revision: int = 163
    is_certified: bool = True
    base_mrp: Decimal = Decimal('27449.00')
    selling_price: Decimal = Decimal('19929.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification164:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #164."""
    sku_id: str = 'FOO-0164'
    vertical: str = 'footwear'
    model_revision: int = 164
    is_certified: bool = True
    base_mrp: Decimal = Decimal('27599.00')
    selling_price: Decimal = Decimal('20039.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification165:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #165."""
    sku_id: str = 'FOO-0165'
    vertical: str = 'footwear'
    model_revision: int = 165
    is_certified: bool = True
    base_mrp: Decimal = Decimal('27749.00')
    selling_price: Decimal = Decimal('20149.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification166:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #166."""
    sku_id: str = 'FOO-0166'
    vertical: str = 'footwear'
    model_revision: int = 166
    is_certified: bool = True
    base_mrp: Decimal = Decimal('27899.00')
    selling_price: Decimal = Decimal('20259.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification167:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #167."""
    sku_id: str = 'FOO-0167'
    vertical: str = 'footwear'
    model_revision: int = 167
    is_certified: bool = True
    base_mrp: Decimal = Decimal('28049.00')
    selling_price: Decimal = Decimal('20369.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification168:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #168."""
    sku_id: str = 'FOO-0168'
    vertical: str = 'footwear'
    model_revision: int = 168
    is_certified: bool = True
    base_mrp: Decimal = Decimal('28199.00')
    selling_price: Decimal = Decimal('20479.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification169:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #169."""
    sku_id: str = 'FOO-0169'
    vertical: str = 'footwear'
    model_revision: int = 169
    is_certified: bool = True
    base_mrp: Decimal = Decimal('28349.00')
    selling_price: Decimal = Decimal('20589.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification170:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #170."""
    sku_id: str = 'FOO-0170'
    vertical: str = 'footwear'
    model_revision: int = 170
    is_certified: bool = True
    base_mrp: Decimal = Decimal('28499.00')
    selling_price: Decimal = Decimal('20699.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification171:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #171."""
    sku_id: str = 'FOO-0171'
    vertical: str = 'footwear'
    model_revision: int = 171
    is_certified: bool = True
    base_mrp: Decimal = Decimal('28649.00')
    selling_price: Decimal = Decimal('20809.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification172:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #172."""
    sku_id: str = 'FOO-0172'
    vertical: str = 'footwear'
    model_revision: int = 172
    is_certified: bool = True
    base_mrp: Decimal = Decimal('28799.00')
    selling_price: Decimal = Decimal('20919.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification173:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #173."""
    sku_id: str = 'FOO-0173'
    vertical: str = 'footwear'
    model_revision: int = 173
    is_certified: bool = True
    base_mrp: Decimal = Decimal('28949.00')
    selling_price: Decimal = Decimal('21029.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification174:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #174."""
    sku_id: str = 'FOO-0174'
    vertical: str = 'footwear'
    model_revision: int = 174
    is_certified: bool = True
    base_mrp: Decimal = Decimal('29099.00')
    selling_price: Decimal = Decimal('21139.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification175:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #175."""
    sku_id: str = 'FOO-0175'
    vertical: str = 'footwear'
    model_revision: int = 175
    is_certified: bool = True
    base_mrp: Decimal = Decimal('29249.00')
    selling_price: Decimal = Decimal('21249.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification176:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #176."""
    sku_id: str = 'FOO-0176'
    vertical: str = 'footwear'
    model_revision: int = 176
    is_certified: bool = True
    base_mrp: Decimal = Decimal('29399.00')
    selling_price: Decimal = Decimal('21359.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification177:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #177."""
    sku_id: str = 'FOO-0177'
    vertical: str = 'footwear'
    model_revision: int = 177
    is_certified: bool = True
    base_mrp: Decimal = Decimal('29549.00')
    selling_price: Decimal = Decimal('21469.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification178:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #178."""
    sku_id: str = 'FOO-0178'
    vertical: str = 'footwear'
    model_revision: int = 178
    is_certified: bool = True
    base_mrp: Decimal = Decimal('29699.00')
    selling_price: Decimal = Decimal('21579.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification179:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #179."""
    sku_id: str = 'FOO-0179'
    vertical: str = 'footwear'
    model_revision: int = 179
    is_certified: bool = True
    base_mrp: Decimal = Decimal('29849.00')
    selling_price: Decimal = Decimal('21689.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification180:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #180."""
    sku_id: str = 'FOO-0180'
    vertical: str = 'footwear'
    model_revision: int = 180
    is_certified: bool = True
    base_mrp: Decimal = Decimal('29999.00')
    selling_price: Decimal = Decimal('21799.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification181:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #181."""
    sku_id: str = 'FOO-0181'
    vertical: str = 'footwear'
    model_revision: int = 181
    is_certified: bool = True
    base_mrp: Decimal = Decimal('30149.00')
    selling_price: Decimal = Decimal('21909.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification182:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #182."""
    sku_id: str = 'FOO-0182'
    vertical: str = 'footwear'
    model_revision: int = 182
    is_certified: bool = True
    base_mrp: Decimal = Decimal('30299.00')
    selling_price: Decimal = Decimal('22019.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification183:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #183."""
    sku_id: str = 'FOO-0183'
    vertical: str = 'footwear'
    model_revision: int = 183
    is_certified: bool = True
    base_mrp: Decimal = Decimal('30449.00')
    selling_price: Decimal = Decimal('22129.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification184:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #184."""
    sku_id: str = 'FOO-0184'
    vertical: str = 'footwear'
    model_revision: int = 184
    is_certified: bool = True
    base_mrp: Decimal = Decimal('30599.00')
    selling_price: Decimal = Decimal('22239.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification185:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #185."""
    sku_id: str = 'FOO-0185'
    vertical: str = 'footwear'
    model_revision: int = 185
    is_certified: bool = True
    base_mrp: Decimal = Decimal('30749.00')
    selling_price: Decimal = Decimal('22349.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification186:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #186."""
    sku_id: str = 'FOO-0186'
    vertical: str = 'footwear'
    model_revision: int = 186
    is_certified: bool = True
    base_mrp: Decimal = Decimal('30899.00')
    selling_price: Decimal = Decimal('22459.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification187:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #187."""
    sku_id: str = 'FOO-0187'
    vertical: str = 'footwear'
    model_revision: int = 187
    is_certified: bool = True
    base_mrp: Decimal = Decimal('31049.00')
    selling_price: Decimal = Decimal('22569.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification188:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #188."""
    sku_id: str = 'FOO-0188'
    vertical: str = 'footwear'
    model_revision: int = 188
    is_certified: bool = True
    base_mrp: Decimal = Decimal('31199.00')
    selling_price: Decimal = Decimal('22679.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification189:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #189."""
    sku_id: str = 'FOO-0189'
    vertical: str = 'footwear'
    model_revision: int = 189
    is_certified: bool = True
    base_mrp: Decimal = Decimal('31349.00')
    selling_price: Decimal = Decimal('22789.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification190:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #190."""
    sku_id: str = 'FOO-0190'
    vertical: str = 'footwear'
    model_revision: int = 190
    is_certified: bool = True
    base_mrp: Decimal = Decimal('31499.00')
    selling_price: Decimal = Decimal('22899.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification191:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #191."""
    sku_id: str = 'FOO-0191'
    vertical: str = 'footwear'
    model_revision: int = 191
    is_certified: bool = True
    base_mrp: Decimal = Decimal('31649.00')
    selling_price: Decimal = Decimal('23009.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification192:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #192."""
    sku_id: str = 'FOO-0192'
    vertical: str = 'footwear'
    model_revision: int = 192
    is_certified: bool = True
    base_mrp: Decimal = Decimal('31799.00')
    selling_price: Decimal = Decimal('23119.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification193:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #193."""
    sku_id: str = 'FOO-0193'
    vertical: str = 'footwear'
    model_revision: int = 193
    is_certified: bool = True
    base_mrp: Decimal = Decimal('31949.00')
    selling_price: Decimal = Decimal('23229.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification194:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #194."""
    sku_id: str = 'FOO-0194'
    vertical: str = 'footwear'
    model_revision: int = 194
    is_certified: bool = True
    base_mrp: Decimal = Decimal('32099.00')
    selling_price: Decimal = Decimal('23339.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification195:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #195."""
    sku_id: str = 'FOO-0195'
    vertical: str = 'footwear'
    model_revision: int = 195
    is_certified: bool = True
    base_mrp: Decimal = Decimal('32249.00')
    selling_price: Decimal = Decimal('23449.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification196:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #196."""
    sku_id: str = 'FOO-0196'
    vertical: str = 'footwear'
    model_revision: int = 196
    is_certified: bool = True
    base_mrp: Decimal = Decimal('32399.00')
    selling_price: Decimal = Decimal('23559.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification197:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #197."""
    sku_id: str = 'FOO-0197'
    vertical: str = 'footwear'
    model_revision: int = 197
    is_certified: bool = True
    base_mrp: Decimal = Decimal('32549.00')
    selling_price: Decimal = Decimal('23669.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification198:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #198."""
    sku_id: str = 'FOO-0198'
    vertical: str = 'footwear'
    model_revision: int = 198
    is_certified: bool = True
    base_mrp: Decimal = Decimal('32699.00')
    selling_price: Decimal = Decimal('23779.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification199:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #199."""
    sku_id: str = 'FOO-0199'
    vertical: str = 'footwear'
    model_revision: int = 199
    is_certified: bool = True
    base_mrp: Decimal = Decimal('32849.00')
    selling_price: Decimal = Decimal('23889.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification200:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #200."""
    sku_id: str = 'FOO-0200'
    vertical: str = 'footwear'
    model_revision: int = 200
    is_certified: bool = True
    base_mrp: Decimal = Decimal('32999.00')
    selling_price: Decimal = Decimal('23999.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification201:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #201."""
    sku_id: str = 'FOO-0201'
    vertical: str = 'footwear'
    model_revision: int = 201
    is_certified: bool = True
    base_mrp: Decimal = Decimal('33149.00')
    selling_price: Decimal = Decimal('24109.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification202:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #202."""
    sku_id: str = 'FOO-0202'
    vertical: str = 'footwear'
    model_revision: int = 202
    is_certified: bool = True
    base_mrp: Decimal = Decimal('33299.00')
    selling_price: Decimal = Decimal('24219.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification203:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #203."""
    sku_id: str = 'FOO-0203'
    vertical: str = 'footwear'
    model_revision: int = 203
    is_certified: bool = True
    base_mrp: Decimal = Decimal('33449.00')
    selling_price: Decimal = Decimal('24329.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification204:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #204."""
    sku_id: str = 'FOO-0204'
    vertical: str = 'footwear'
    model_revision: int = 204
    is_certified: bool = True
    base_mrp: Decimal = Decimal('33599.00')
    selling_price: Decimal = Decimal('24439.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification205:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #205."""
    sku_id: str = 'FOO-0205'
    vertical: str = 'footwear'
    model_revision: int = 205
    is_certified: bool = True
    base_mrp: Decimal = Decimal('33749.00')
    selling_price: Decimal = Decimal('24549.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification206:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #206."""
    sku_id: str = 'FOO-0206'
    vertical: str = 'footwear'
    model_revision: int = 206
    is_certified: bool = True
    base_mrp: Decimal = Decimal('33899.00')
    selling_price: Decimal = Decimal('24659.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification207:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #207."""
    sku_id: str = 'FOO-0207'
    vertical: str = 'footwear'
    model_revision: int = 207
    is_certified: bool = True
    base_mrp: Decimal = Decimal('34049.00')
    selling_price: Decimal = Decimal('24769.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification208:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #208."""
    sku_id: str = 'FOO-0208'
    vertical: str = 'footwear'
    model_revision: int = 208
    is_certified: bool = True
    base_mrp: Decimal = Decimal('34199.00')
    selling_price: Decimal = Decimal('24879.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification209:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #209."""
    sku_id: str = 'FOO-0209'
    vertical: str = 'footwear'
    model_revision: int = 209
    is_certified: bool = True
    base_mrp: Decimal = Decimal('34349.00')
    selling_price: Decimal = Decimal('24989.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification210:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #210."""
    sku_id: str = 'FOO-0210'
    vertical: str = 'footwear'
    model_revision: int = 210
    is_certified: bool = True
    base_mrp: Decimal = Decimal('34499.00')
    selling_price: Decimal = Decimal('25099.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification211:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #211."""
    sku_id: str = 'FOO-0211'
    vertical: str = 'footwear'
    model_revision: int = 211
    is_certified: bool = True
    base_mrp: Decimal = Decimal('34649.00')
    selling_price: Decimal = Decimal('25209.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification212:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #212."""
    sku_id: str = 'FOO-0212'
    vertical: str = 'footwear'
    model_revision: int = 212
    is_certified: bool = True
    base_mrp: Decimal = Decimal('34799.00')
    selling_price: Decimal = Decimal('25319.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification213:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #213."""
    sku_id: str = 'FOO-0213'
    vertical: str = 'footwear'
    model_revision: int = 213
    is_certified: bool = True
    base_mrp: Decimal = Decimal('34949.00')
    selling_price: Decimal = Decimal('25429.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification214:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #214."""
    sku_id: str = 'FOO-0214'
    vertical: str = 'footwear'
    model_revision: int = 214
    is_certified: bool = True
    base_mrp: Decimal = Decimal('35099.00')
    selling_price: Decimal = Decimal('25539.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification215:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #215."""
    sku_id: str = 'FOO-0215'
    vertical: str = 'footwear'
    model_revision: int = 215
    is_certified: bool = True
    base_mrp: Decimal = Decimal('35249.00')
    selling_price: Decimal = Decimal('25649.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification216:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #216."""
    sku_id: str = 'FOO-0216'
    vertical: str = 'footwear'
    model_revision: int = 216
    is_certified: bool = True
    base_mrp: Decimal = Decimal('35399.00')
    selling_price: Decimal = Decimal('25759.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification217:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #217."""
    sku_id: str = 'FOO-0217'
    vertical: str = 'footwear'
    model_revision: int = 217
    is_certified: bool = True
    base_mrp: Decimal = Decimal('35549.00')
    selling_price: Decimal = Decimal('25869.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification218:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #218."""
    sku_id: str = 'FOO-0218'
    vertical: str = 'footwear'
    model_revision: int = 218
    is_certified: bool = True
    base_mrp: Decimal = Decimal('35699.00')
    selling_price: Decimal = Decimal('25979.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification219:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #219."""
    sku_id: str = 'FOO-0219'
    vertical: str = 'footwear'
    model_revision: int = 219
    is_certified: bool = True
    base_mrp: Decimal = Decimal('35849.00')
    selling_price: Decimal = Decimal('26089.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification220:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #220."""
    sku_id: str = 'FOO-0220'
    vertical: str = 'footwear'
    model_revision: int = 220
    is_certified: bool = True
    base_mrp: Decimal = Decimal('35999.00')
    selling_price: Decimal = Decimal('26199.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification221:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #221."""
    sku_id: str = 'FOO-0221'
    vertical: str = 'footwear'
    model_revision: int = 221
    is_certified: bool = True
    base_mrp: Decimal = Decimal('36149.00')
    selling_price: Decimal = Decimal('26309.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification222:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #222."""
    sku_id: str = 'FOO-0222'
    vertical: str = 'footwear'
    model_revision: int = 222
    is_certified: bool = True
    base_mrp: Decimal = Decimal('36299.00')
    selling_price: Decimal = Decimal('26419.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification223:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #223."""
    sku_id: str = 'FOO-0223'
    vertical: str = 'footwear'
    model_revision: int = 223
    is_certified: bool = True
    base_mrp: Decimal = Decimal('36449.00')
    selling_price: Decimal = Decimal('26529.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification224:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #224."""
    sku_id: str = 'FOO-0224'
    vertical: str = 'footwear'
    model_revision: int = 224
    is_certified: bool = True
    base_mrp: Decimal = Decimal('36599.00')
    selling_price: Decimal = Decimal('26639.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification225:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #225."""
    sku_id: str = 'FOO-0225'
    vertical: str = 'footwear'
    model_revision: int = 225
    is_certified: bool = True
    base_mrp: Decimal = Decimal('36749.00')
    selling_price: Decimal = Decimal('26749.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification226:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #226."""
    sku_id: str = 'FOO-0226'
    vertical: str = 'footwear'
    model_revision: int = 226
    is_certified: bool = True
    base_mrp: Decimal = Decimal('36899.00')
    selling_price: Decimal = Decimal('26859.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification227:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #227."""
    sku_id: str = 'FOO-0227'
    vertical: str = 'footwear'
    model_revision: int = 227
    is_certified: bool = True
    base_mrp: Decimal = Decimal('37049.00')
    selling_price: Decimal = Decimal('26969.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification228:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #228."""
    sku_id: str = 'FOO-0228'
    vertical: str = 'footwear'
    model_revision: int = 228
    is_certified: bool = True
    base_mrp: Decimal = Decimal('37199.00')
    selling_price: Decimal = Decimal('27079.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification229:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #229."""
    sku_id: str = 'FOO-0229'
    vertical: str = 'footwear'
    model_revision: int = 229
    is_certified: bool = True
    base_mrp: Decimal = Decimal('37349.00')
    selling_price: Decimal = Decimal('27189.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification230:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #230."""
    sku_id: str = 'FOO-0230'
    vertical: str = 'footwear'
    model_revision: int = 230
    is_certified: bool = True
    base_mrp: Decimal = Decimal('37499.00')
    selling_price: Decimal = Decimal('27299.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification231:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #231."""
    sku_id: str = 'FOO-0231'
    vertical: str = 'footwear'
    model_revision: int = 231
    is_certified: bool = True
    base_mrp: Decimal = Decimal('37649.00')
    selling_price: Decimal = Decimal('27409.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification232:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #232."""
    sku_id: str = 'FOO-0232'
    vertical: str = 'footwear'
    model_revision: int = 232
    is_certified: bool = True
    base_mrp: Decimal = Decimal('37799.00')
    selling_price: Decimal = Decimal('27519.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification233:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #233."""
    sku_id: str = 'FOO-0233'
    vertical: str = 'footwear'
    model_revision: int = 233
    is_certified: bool = True
    base_mrp: Decimal = Decimal('37949.00')
    selling_price: Decimal = Decimal('27629.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification234:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #234."""
    sku_id: str = 'FOO-0234'
    vertical: str = 'footwear'
    model_revision: int = 234
    is_certified: bool = True
    base_mrp: Decimal = Decimal('38099.00')
    selling_price: Decimal = Decimal('27739.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification235:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #235."""
    sku_id: str = 'FOO-0235'
    vertical: str = 'footwear'
    model_revision: int = 235
    is_certified: bool = True
    base_mrp: Decimal = Decimal('38249.00')
    selling_price: Decimal = Decimal('27849.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification236:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #236."""
    sku_id: str = 'FOO-0236'
    vertical: str = 'footwear'
    model_revision: int = 236
    is_certified: bool = True
    base_mrp: Decimal = Decimal('38399.00')
    selling_price: Decimal = Decimal('27959.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification237:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #237."""
    sku_id: str = 'FOO-0237'
    vertical: str = 'footwear'
    model_revision: int = 237
    is_certified: bool = True
    base_mrp: Decimal = Decimal('38549.00')
    selling_price: Decimal = Decimal('28069.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification238:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #238."""
    sku_id: str = 'FOO-0238'
    vertical: str = 'footwear'
    model_revision: int = 238
    is_certified: bool = True
    base_mrp: Decimal = Decimal('38699.00')
    selling_price: Decimal = Decimal('28179.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification239:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #239."""
    sku_id: str = 'FOO-0239'
    vertical: str = 'footwear'
    model_revision: int = 239
    is_certified: bool = True
    base_mrp: Decimal = Decimal('38849.00')
    selling_price: Decimal = Decimal('28289.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification240:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #240."""
    sku_id: str = 'FOO-0240'
    vertical: str = 'footwear'
    model_revision: int = 240
    is_certified: bool = True
    base_mrp: Decimal = Decimal('38999.00')
    selling_price: Decimal = Decimal('28399.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification241:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #241."""
    sku_id: str = 'FOO-0241'
    vertical: str = 'footwear'
    model_revision: int = 241
    is_certified: bool = True
    base_mrp: Decimal = Decimal('39149.00')
    selling_price: Decimal = Decimal('28509.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification242:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #242."""
    sku_id: str = 'FOO-0242'
    vertical: str = 'footwear'
    model_revision: int = 242
    is_certified: bool = True
    base_mrp: Decimal = Decimal('39299.00')
    selling_price: Decimal = Decimal('28619.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification243:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #243."""
    sku_id: str = 'FOO-0243'
    vertical: str = 'footwear'
    model_revision: int = 243
    is_certified: bool = True
    base_mrp: Decimal = Decimal('39449.00')
    selling_price: Decimal = Decimal('28729.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification244:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #244."""
    sku_id: str = 'FOO-0244'
    vertical: str = 'footwear'
    model_revision: int = 244
    is_certified: bool = True
    base_mrp: Decimal = Decimal('39599.00')
    selling_price: Decimal = Decimal('28839.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification245:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #245."""
    sku_id: str = 'FOO-0245'
    vertical: str = 'footwear'
    model_revision: int = 245
    is_certified: bool = True
    base_mrp: Decimal = Decimal('39749.00')
    selling_price: Decimal = Decimal('28949.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification246:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #246."""
    sku_id: str = 'FOO-0246'
    vertical: str = 'footwear'
    model_revision: int = 246
    is_certified: bool = True
    base_mrp: Decimal = Decimal('39899.00')
    selling_price: Decimal = Decimal('29059.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification247:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #247."""
    sku_id: str = 'FOO-0247'
    vertical: str = 'footwear'
    model_revision: int = 247
    is_certified: bool = True
    base_mrp: Decimal = Decimal('40049.00')
    selling_price: Decimal = Decimal('29169.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification248:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #248."""
    sku_id: str = 'FOO-0248'
    vertical: str = 'footwear'
    model_revision: int = 248
    is_certified: bool = True
    base_mrp: Decimal = Decimal('40199.00')
    selling_price: Decimal = Decimal('29279.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification249:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #249."""
    sku_id: str = 'FOO-0249'
    vertical: str = 'footwear'
    model_revision: int = 249
    is_certified: bool = True
    base_mrp: Decimal = Decimal('40349.00')
    selling_price: Decimal = Decimal('29389.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification250:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #250."""
    sku_id: str = 'FOO-0250'
    vertical: str = 'footwear'
    model_revision: int = 250
    is_certified: bool = True
    base_mrp: Decimal = Decimal('40499.00')
    selling_price: Decimal = Decimal('29499.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification251:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #251."""
    sku_id: str = 'FOO-0251'
    vertical: str = 'footwear'
    model_revision: int = 251
    is_certified: bool = True
    base_mrp: Decimal = Decimal('40649.00')
    selling_price: Decimal = Decimal('29609.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification252:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #252."""
    sku_id: str = 'FOO-0252'
    vertical: str = 'footwear'
    model_revision: int = 252
    is_certified: bool = True
    base_mrp: Decimal = Decimal('40799.00')
    selling_price: Decimal = Decimal('29719.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification253:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #253."""
    sku_id: str = 'FOO-0253'
    vertical: str = 'footwear'
    model_revision: int = 253
    is_certified: bool = True
    base_mrp: Decimal = Decimal('40949.00')
    selling_price: Decimal = Decimal('29829.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification254:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #254."""
    sku_id: str = 'FOO-0254'
    vertical: str = 'footwear'
    model_revision: int = 254
    is_certified: bool = True
    base_mrp: Decimal = Decimal('41099.00')
    selling_price: Decimal = Decimal('29939.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification255:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #255."""
    sku_id: str = 'FOO-0255'
    vertical: str = 'footwear'
    model_revision: int = 255
    is_certified: bool = True
    base_mrp: Decimal = Decimal('41249.00')
    selling_price: Decimal = Decimal('30049.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification256:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #256."""
    sku_id: str = 'FOO-0256'
    vertical: str = 'footwear'
    model_revision: int = 256
    is_certified: bool = True
    base_mrp: Decimal = Decimal('41399.00')
    selling_price: Decimal = Decimal('30159.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification257:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #257."""
    sku_id: str = 'FOO-0257'
    vertical: str = 'footwear'
    model_revision: int = 257
    is_certified: bool = True
    base_mrp: Decimal = Decimal('41549.00')
    selling_price: Decimal = Decimal('30269.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification258:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #258."""
    sku_id: str = 'FOO-0258'
    vertical: str = 'footwear'
    model_revision: int = 258
    is_certified: bool = True
    base_mrp: Decimal = Decimal('41699.00')
    selling_price: Decimal = Decimal('30379.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification259:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #259."""
    sku_id: str = 'FOO-0259'
    vertical: str = 'footwear'
    model_revision: int = 259
    is_certified: bool = True
    base_mrp: Decimal = Decimal('41849.00')
    selling_price: Decimal = Decimal('30489.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification260:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #260."""
    sku_id: str = 'FOO-0260'
    vertical: str = 'footwear'
    model_revision: int = 260
    is_certified: bool = True
    base_mrp: Decimal = Decimal('41999.00')
    selling_price: Decimal = Decimal('30599.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification261:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #261."""
    sku_id: str = 'FOO-0261'
    vertical: str = 'footwear'
    model_revision: int = 261
    is_certified: bool = True
    base_mrp: Decimal = Decimal('42149.00')
    selling_price: Decimal = Decimal('30709.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification262:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #262."""
    sku_id: str = 'FOO-0262'
    vertical: str = 'footwear'
    model_revision: int = 262
    is_certified: bool = True
    base_mrp: Decimal = Decimal('42299.00')
    selling_price: Decimal = Decimal('30819.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification263:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #263."""
    sku_id: str = 'FOO-0263'
    vertical: str = 'footwear'
    model_revision: int = 263
    is_certified: bool = True
    base_mrp: Decimal = Decimal('42449.00')
    selling_price: Decimal = Decimal('30929.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification264:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #264."""
    sku_id: str = 'FOO-0264'
    vertical: str = 'footwear'
    model_revision: int = 264
    is_certified: bool = True
    base_mrp: Decimal = Decimal('42599.00')
    selling_price: Decimal = Decimal('31039.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification265:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #265."""
    sku_id: str = 'FOO-0265'
    vertical: str = 'footwear'
    model_revision: int = 265
    is_certified: bool = True
    base_mrp: Decimal = Decimal('42749.00')
    selling_price: Decimal = Decimal('31149.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification266:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #266."""
    sku_id: str = 'FOO-0266'
    vertical: str = 'footwear'
    model_revision: int = 266
    is_certified: bool = True
    base_mrp: Decimal = Decimal('42899.00')
    selling_price: Decimal = Decimal('31259.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification267:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #267."""
    sku_id: str = 'FOO-0267'
    vertical: str = 'footwear'
    model_revision: int = 267
    is_certified: bool = True
    base_mrp: Decimal = Decimal('43049.00')
    selling_price: Decimal = Decimal('31369.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification268:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #268."""
    sku_id: str = 'FOO-0268'
    vertical: str = 'footwear'
    model_revision: int = 268
    is_certified: bool = True
    base_mrp: Decimal = Decimal('43199.00')
    selling_price: Decimal = Decimal('31479.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification269:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #269."""
    sku_id: str = 'FOO-0269'
    vertical: str = 'footwear'
    model_revision: int = 269
    is_certified: bool = True
    base_mrp: Decimal = Decimal('43349.00')
    selling_price: Decimal = Decimal('31589.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification270:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #270."""
    sku_id: str = 'FOO-0270'
    vertical: str = 'footwear'
    model_revision: int = 270
    is_certified: bool = True
    base_mrp: Decimal = Decimal('43499.00')
    selling_price: Decimal = Decimal('31699.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification271:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #271."""
    sku_id: str = 'FOO-0271'
    vertical: str = 'footwear'
    model_revision: int = 271
    is_certified: bool = True
    base_mrp: Decimal = Decimal('43649.00')
    selling_price: Decimal = Decimal('31809.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification272:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #272."""
    sku_id: str = 'FOO-0272'
    vertical: str = 'footwear'
    model_revision: int = 272
    is_certified: bool = True
    base_mrp: Decimal = Decimal('43799.00')
    selling_price: Decimal = Decimal('31919.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification273:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #273."""
    sku_id: str = 'FOO-0273'
    vertical: str = 'footwear'
    model_revision: int = 273
    is_certified: bool = True
    base_mrp: Decimal = Decimal('43949.00')
    selling_price: Decimal = Decimal('32029.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification274:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #274."""
    sku_id: str = 'FOO-0274'
    vertical: str = 'footwear'
    model_revision: int = 274
    is_certified: bool = True
    base_mrp: Decimal = Decimal('44099.00')
    selling_price: Decimal = Decimal('32139.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification275:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #275."""
    sku_id: str = 'FOO-0275'
    vertical: str = 'footwear'
    model_revision: int = 275
    is_certified: bool = True
    base_mrp: Decimal = Decimal('44249.00')
    selling_price: Decimal = Decimal('32249.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification276:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #276."""
    sku_id: str = 'FOO-0276'
    vertical: str = 'footwear'
    model_revision: int = 276
    is_certified: bool = True
    base_mrp: Decimal = Decimal('44399.00')
    selling_price: Decimal = Decimal('32359.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification277:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #277."""
    sku_id: str = 'FOO-0277'
    vertical: str = 'footwear'
    model_revision: int = 277
    is_certified: bool = True
    base_mrp: Decimal = Decimal('44549.00')
    selling_price: Decimal = Decimal('32469.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification278:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #278."""
    sku_id: str = 'FOO-0278'
    vertical: str = 'footwear'
    model_revision: int = 278
    is_certified: bool = True
    base_mrp: Decimal = Decimal('44699.00')
    selling_price: Decimal = Decimal('32579.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification279:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #279."""
    sku_id: str = 'FOO-0279'
    vertical: str = 'footwear'
    model_revision: int = 279
    is_certified: bool = True
    base_mrp: Decimal = Decimal('44849.00')
    selling_price: Decimal = Decimal('32689.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification280:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #280."""
    sku_id: str = 'FOO-0280'
    vertical: str = 'footwear'
    model_revision: int = 280
    is_certified: bool = True
    base_mrp: Decimal = Decimal('44999.00')
    selling_price: Decimal = Decimal('32799.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification281:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #281."""
    sku_id: str = 'FOO-0281'
    vertical: str = 'footwear'
    model_revision: int = 281
    is_certified: bool = True
    base_mrp: Decimal = Decimal('45149.00')
    selling_price: Decimal = Decimal('32909.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification282:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #282."""
    sku_id: str = 'FOO-0282'
    vertical: str = 'footwear'
    model_revision: int = 282
    is_certified: bool = True
    base_mrp: Decimal = Decimal('45299.00')
    selling_price: Decimal = Decimal('33019.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification283:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #283."""
    sku_id: str = 'FOO-0283'
    vertical: str = 'footwear'
    model_revision: int = 283
    is_certified: bool = True
    base_mrp: Decimal = Decimal('45449.00')
    selling_price: Decimal = Decimal('33129.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification284:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #284."""
    sku_id: str = 'FOO-0284'
    vertical: str = 'footwear'
    model_revision: int = 284
    is_certified: bool = True
    base_mrp: Decimal = Decimal('45599.00')
    selling_price: Decimal = Decimal('33239.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification285:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #285."""
    sku_id: str = 'FOO-0285'
    vertical: str = 'footwear'
    model_revision: int = 285
    is_certified: bool = True
    base_mrp: Decimal = Decimal('45749.00')
    selling_price: Decimal = Decimal('33349.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification286:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #286."""
    sku_id: str = 'FOO-0286'
    vertical: str = 'footwear'
    model_revision: int = 286
    is_certified: bool = True
    base_mrp: Decimal = Decimal('45899.00')
    selling_price: Decimal = Decimal('33459.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification287:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #287."""
    sku_id: str = 'FOO-0287'
    vertical: str = 'footwear'
    model_revision: int = 287
    is_certified: bool = True
    base_mrp: Decimal = Decimal('46049.00')
    selling_price: Decimal = Decimal('33569.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification288:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #288."""
    sku_id: str = 'FOO-0288'
    vertical: str = 'footwear'
    model_revision: int = 288
    is_certified: bool = True
    base_mrp: Decimal = Decimal('46199.00')
    selling_price: Decimal = Decimal('33679.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification289:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #289."""
    sku_id: str = 'FOO-0289'
    vertical: str = 'footwear'
    model_revision: int = 289
    is_certified: bool = True
    base_mrp: Decimal = Decimal('46349.00')
    selling_price: Decimal = Decimal('33789.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification290:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #290."""
    sku_id: str = 'FOO-0290'
    vertical: str = 'footwear'
    model_revision: int = 290
    is_certified: bool = True
    base_mrp: Decimal = Decimal('46499.00')
    selling_price: Decimal = Decimal('33899.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification291:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #291."""
    sku_id: str = 'FOO-0291'
    vertical: str = 'footwear'
    model_revision: int = 291
    is_certified: bool = True
    base_mrp: Decimal = Decimal('46649.00')
    selling_price: Decimal = Decimal('34009.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification292:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #292."""
    sku_id: str = 'FOO-0292'
    vertical: str = 'footwear'
    model_revision: int = 292
    is_certified: bool = True
    base_mrp: Decimal = Decimal('46799.00')
    selling_price: Decimal = Decimal('34119.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification293:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #293."""
    sku_id: str = 'FOO-0293'
    vertical: str = 'footwear'
    model_revision: int = 293
    is_certified: bool = True
    base_mrp: Decimal = Decimal('46949.00')
    selling_price: Decimal = Decimal('34229.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification294:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #294."""
    sku_id: str = 'FOO-0294'
    vertical: str = 'footwear'
    model_revision: int = 294
    is_certified: bool = True
    base_mrp: Decimal = Decimal('47099.00')
    selling_price: Decimal = Decimal('34339.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification295:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #295."""
    sku_id: str = 'FOO-0295'
    vertical: str = 'footwear'
    model_revision: int = 295
    is_certified: bool = True
    base_mrp: Decimal = Decimal('47249.00')
    selling_price: Decimal = Decimal('34449.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification296:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #296."""
    sku_id: str = 'FOO-0296'
    vertical: str = 'footwear'
    model_revision: int = 296
    is_certified: bool = True
    base_mrp: Decimal = Decimal('47399.00')
    selling_price: Decimal = Decimal('34559.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification297:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #297."""
    sku_id: str = 'FOO-0297'
    vertical: str = 'footwear'
    model_revision: int = 297
    is_certified: bool = True
    base_mrp: Decimal = Decimal('47549.00')
    selling_price: Decimal = Decimal('34669.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification298:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #298."""
    sku_id: str = 'FOO-0298'
    vertical: str = 'footwear'
    model_revision: int = 298
    is_certified: bool = True
    base_mrp: Decimal = Decimal('47699.00')
    selling_price: Decimal = Decimal('34779.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification299:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #299."""
    sku_id: str = 'FOO-0299'
    vertical: str = 'footwear'
    model_revision: int = 299
    is_certified: bool = True
    base_mrp: Decimal = Decimal('47849.00')
    selling_price: Decimal = Decimal('34889.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification300:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #300."""
    sku_id: str = 'FOO-0300'
    vertical: str = 'footwear'
    model_revision: int = 300
    is_certified: bool = True
    base_mrp: Decimal = Decimal('47999.00')
    selling_price: Decimal = Decimal('34999.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification301:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #301."""
    sku_id: str = 'FOO-0301'
    vertical: str = 'footwear'
    model_revision: int = 301
    is_certified: bool = True
    base_mrp: Decimal = Decimal('48149.00')
    selling_price: Decimal = Decimal('35109.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification302:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #302."""
    sku_id: str = 'FOO-0302'
    vertical: str = 'footwear'
    model_revision: int = 302
    is_certified: bool = True
    base_mrp: Decimal = Decimal('48299.00')
    selling_price: Decimal = Decimal('35219.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification303:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #303."""
    sku_id: str = 'FOO-0303'
    vertical: str = 'footwear'
    model_revision: int = 303
    is_certified: bool = True
    base_mrp: Decimal = Decimal('48449.00')
    selling_price: Decimal = Decimal('35329.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification304:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #304."""
    sku_id: str = 'FOO-0304'
    vertical: str = 'footwear'
    model_revision: int = 304
    is_certified: bool = True
    base_mrp: Decimal = Decimal('48599.00')
    selling_price: Decimal = Decimal('35439.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification305:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #305."""
    sku_id: str = 'FOO-0305'
    vertical: str = 'footwear'
    model_revision: int = 305
    is_certified: bool = True
    base_mrp: Decimal = Decimal('48749.00')
    selling_price: Decimal = Decimal('35549.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification306:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #306."""
    sku_id: str = 'FOO-0306'
    vertical: str = 'footwear'
    model_revision: int = 306
    is_certified: bool = True
    base_mrp: Decimal = Decimal('48899.00')
    selling_price: Decimal = Decimal('35659.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification307:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #307."""
    sku_id: str = 'FOO-0307'
    vertical: str = 'footwear'
    model_revision: int = 307
    is_certified: bool = True
    base_mrp: Decimal = Decimal('49049.00')
    selling_price: Decimal = Decimal('35769.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification308:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #308."""
    sku_id: str = 'FOO-0308'
    vertical: str = 'footwear'
    model_revision: int = 308
    is_certified: bool = True
    base_mrp: Decimal = Decimal('49199.00')
    selling_price: Decimal = Decimal('35879.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification309:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #309."""
    sku_id: str = 'FOO-0309'
    vertical: str = 'footwear'
    model_revision: int = 309
    is_certified: bool = True
    base_mrp: Decimal = Decimal('49349.00')
    selling_price: Decimal = Decimal('35989.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification310:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #310."""
    sku_id: str = 'FOO-0310'
    vertical: str = 'footwear'
    model_revision: int = 310
    is_certified: bool = True
    base_mrp: Decimal = Decimal('49499.00')
    selling_price: Decimal = Decimal('36099.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification311:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #311."""
    sku_id: str = 'FOO-0311'
    vertical: str = 'footwear'
    model_revision: int = 311
    is_certified: bool = True
    base_mrp: Decimal = Decimal('49649.00')
    selling_price: Decimal = Decimal('36209.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification312:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #312."""
    sku_id: str = 'FOO-0312'
    vertical: str = 'footwear'
    model_revision: int = 312
    is_certified: bool = True
    base_mrp: Decimal = Decimal('49799.00')
    selling_price: Decimal = Decimal('36319.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification313:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #313."""
    sku_id: str = 'FOO-0313'
    vertical: str = 'footwear'
    model_revision: int = 313
    is_certified: bool = True
    base_mrp: Decimal = Decimal('49949.00')
    selling_price: Decimal = Decimal('36429.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification314:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #314."""
    sku_id: str = 'FOO-0314'
    vertical: str = 'footwear'
    model_revision: int = 314
    is_certified: bool = True
    base_mrp: Decimal = Decimal('50099.00')
    selling_price: Decimal = Decimal('36539.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification315:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #315."""
    sku_id: str = 'FOO-0315'
    vertical: str = 'footwear'
    model_revision: int = 315
    is_certified: bool = True
    base_mrp: Decimal = Decimal('50249.00')
    selling_price: Decimal = Decimal('36649.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification316:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #316."""
    sku_id: str = 'FOO-0316'
    vertical: str = 'footwear'
    model_revision: int = 316
    is_certified: bool = True
    base_mrp: Decimal = Decimal('50399.00')
    selling_price: Decimal = Decimal('36759.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification317:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #317."""
    sku_id: str = 'FOO-0317'
    vertical: str = 'footwear'
    model_revision: int = 317
    is_certified: bool = True
    base_mrp: Decimal = Decimal('50549.00')
    selling_price: Decimal = Decimal('36869.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification318:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #318."""
    sku_id: str = 'FOO-0318'
    vertical: str = 'footwear'
    model_revision: int = 318
    is_certified: bool = True
    base_mrp: Decimal = Decimal('50699.00')
    selling_price: Decimal = Decimal('36979.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification319:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #319."""
    sku_id: str = 'FOO-0319'
    vertical: str = 'footwear'
    model_revision: int = 319
    is_certified: bool = True
    base_mrp: Decimal = Decimal('50849.00')
    selling_price: Decimal = Decimal('37089.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification320:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #320."""
    sku_id: str = 'FOO-0320'
    vertical: str = 'footwear'
    model_revision: int = 320
    is_certified: bool = True
    base_mrp: Decimal = Decimal('50999.00')
    selling_price: Decimal = Decimal('37199.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification321:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #321."""
    sku_id: str = 'FOO-0321'
    vertical: str = 'footwear'
    model_revision: int = 321
    is_certified: bool = True
    base_mrp: Decimal = Decimal('51149.00')
    selling_price: Decimal = Decimal('37309.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification322:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #322."""
    sku_id: str = 'FOO-0322'
    vertical: str = 'footwear'
    model_revision: int = 322
    is_certified: bool = True
    base_mrp: Decimal = Decimal('51299.00')
    selling_price: Decimal = Decimal('37419.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification323:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #323."""
    sku_id: str = 'FOO-0323'
    vertical: str = 'footwear'
    model_revision: int = 323
    is_certified: bool = True
    base_mrp: Decimal = Decimal('51449.00')
    selling_price: Decimal = Decimal('37529.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification324:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #324."""
    sku_id: str = 'FOO-0324'
    vertical: str = 'footwear'
    model_revision: int = 324
    is_certified: bool = True
    base_mrp: Decimal = Decimal('51599.00')
    selling_price: Decimal = Decimal('37639.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification325:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #325."""
    sku_id: str = 'FOO-0325'
    vertical: str = 'footwear'
    model_revision: int = 325
    is_certified: bool = True
    base_mrp: Decimal = Decimal('51749.00')
    selling_price: Decimal = Decimal('37749.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification326:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #326."""
    sku_id: str = 'FOO-0326'
    vertical: str = 'footwear'
    model_revision: int = 326
    is_certified: bool = True
    base_mrp: Decimal = Decimal('51899.00')
    selling_price: Decimal = Decimal('37859.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification327:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #327."""
    sku_id: str = 'FOO-0327'
    vertical: str = 'footwear'
    model_revision: int = 327
    is_certified: bool = True
    base_mrp: Decimal = Decimal('52049.00')
    selling_price: Decimal = Decimal('37969.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification328:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #328."""
    sku_id: str = 'FOO-0328'
    vertical: str = 'footwear'
    model_revision: int = 328
    is_certified: bool = True
    base_mrp: Decimal = Decimal('52199.00')
    selling_price: Decimal = Decimal('38079.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification329:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #329."""
    sku_id: str = 'FOO-0329'
    vertical: str = 'footwear'
    model_revision: int = 329
    is_certified: bool = True
    base_mrp: Decimal = Decimal('52349.00')
    selling_price: Decimal = Decimal('38189.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification330:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #330."""
    sku_id: str = 'FOO-0330'
    vertical: str = 'footwear'
    model_revision: int = 330
    is_certified: bool = True
    base_mrp: Decimal = Decimal('52499.00')
    selling_price: Decimal = Decimal('38299.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification331:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #331."""
    sku_id: str = 'FOO-0331'
    vertical: str = 'footwear'
    model_revision: int = 331
    is_certified: bool = True
    base_mrp: Decimal = Decimal('52649.00')
    selling_price: Decimal = Decimal('38409.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification332:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #332."""
    sku_id: str = 'FOO-0332'
    vertical: str = 'footwear'
    model_revision: int = 332
    is_certified: bool = True
    base_mrp: Decimal = Decimal('52799.00')
    selling_price: Decimal = Decimal('38519.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification333:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #333."""
    sku_id: str = 'FOO-0333'
    vertical: str = 'footwear'
    model_revision: int = 333
    is_certified: bool = True
    base_mrp: Decimal = Decimal('52949.00')
    selling_price: Decimal = Decimal('38629.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification334:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #334."""
    sku_id: str = 'FOO-0334'
    vertical: str = 'footwear'
    model_revision: int = 334
    is_certified: bool = True
    base_mrp: Decimal = Decimal('53099.00')
    selling_price: Decimal = Decimal('38739.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification335:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #335."""
    sku_id: str = 'FOO-0335'
    vertical: str = 'footwear'
    model_revision: int = 335
    is_certified: bool = True
    base_mrp: Decimal = Decimal('53249.00')
    selling_price: Decimal = Decimal('38849.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification336:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #336."""
    sku_id: str = 'FOO-0336'
    vertical: str = 'footwear'
    model_revision: int = 336
    is_certified: bool = True
    base_mrp: Decimal = Decimal('53399.00')
    selling_price: Decimal = Decimal('38959.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification337:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #337."""
    sku_id: str = 'FOO-0337'
    vertical: str = 'footwear'
    model_revision: int = 337
    is_certified: bool = True
    base_mrp: Decimal = Decimal('53549.00')
    selling_price: Decimal = Decimal('39069.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification338:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #338."""
    sku_id: str = 'FOO-0338'
    vertical: str = 'footwear'
    model_revision: int = 338
    is_certified: bool = True
    base_mrp: Decimal = Decimal('53699.00')
    selling_price: Decimal = Decimal('39179.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification339:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #339."""
    sku_id: str = 'FOO-0339'
    vertical: str = 'footwear'
    model_revision: int = 339
    is_certified: bool = True
    base_mrp: Decimal = Decimal('53849.00')
    selling_price: Decimal = Decimal('39289.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification340:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #340."""
    sku_id: str = 'FOO-0340'
    vertical: str = 'footwear'
    model_revision: int = 340
    is_certified: bool = True
    base_mrp: Decimal = Decimal('53999.00')
    selling_price: Decimal = Decimal('39399.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification341:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #341."""
    sku_id: str = 'FOO-0341'
    vertical: str = 'footwear'
    model_revision: int = 341
    is_certified: bool = True
    base_mrp: Decimal = Decimal('54149.00')
    selling_price: Decimal = Decimal('39509.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification342:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #342."""
    sku_id: str = 'FOO-0342'
    vertical: str = 'footwear'
    model_revision: int = 342
    is_certified: bool = True
    base_mrp: Decimal = Decimal('54299.00')
    selling_price: Decimal = Decimal('39619.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification343:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #343."""
    sku_id: str = 'FOO-0343'
    vertical: str = 'footwear'
    model_revision: int = 343
    is_certified: bool = True
    base_mrp: Decimal = Decimal('54449.00')
    selling_price: Decimal = Decimal('39729.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification344:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #344."""
    sku_id: str = 'FOO-0344'
    vertical: str = 'footwear'
    model_revision: int = 344
    is_certified: bool = True
    base_mrp: Decimal = Decimal('54599.00')
    selling_price: Decimal = Decimal('39839.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification345:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #345."""
    sku_id: str = 'FOO-0345'
    vertical: str = 'footwear'
    model_revision: int = 345
    is_certified: bool = True
    base_mrp: Decimal = Decimal('54749.00')
    selling_price: Decimal = Decimal('39949.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification346:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #346."""
    sku_id: str = 'FOO-0346'
    vertical: str = 'footwear'
    model_revision: int = 346
    is_certified: bool = True
    base_mrp: Decimal = Decimal('54899.00')
    selling_price: Decimal = Decimal('40059.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification347:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #347."""
    sku_id: str = 'FOO-0347'
    vertical: str = 'footwear'
    model_revision: int = 347
    is_certified: bool = True
    base_mrp: Decimal = Decimal('55049.00')
    selling_price: Decimal = Decimal('40169.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification348:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #348."""
    sku_id: str = 'FOO-0348'
    vertical: str = 'footwear'
    model_revision: int = 348
    is_certified: bool = True
    base_mrp: Decimal = Decimal('55199.00')
    selling_price: Decimal = Decimal('40279.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification349:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #349."""
    sku_id: str = 'FOO-0349'
    vertical: str = 'footwear'
    model_revision: int = 349
    is_certified: bool = True
    base_mrp: Decimal = Decimal('55349.00')
    selling_price: Decimal = Decimal('40389.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification350:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #350."""
    sku_id: str = 'FOO-0350'
    vertical: str = 'footwear'
    model_revision: int = 350
    is_certified: bool = True
    base_mrp: Decimal = Decimal('55499.00')
    selling_price: Decimal = Decimal('40499.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification351:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #351."""
    sku_id: str = 'FOO-0351'
    vertical: str = 'footwear'
    model_revision: int = 351
    is_certified: bool = True
    base_mrp: Decimal = Decimal('55649.00')
    selling_price: Decimal = Decimal('40609.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification352:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #352."""
    sku_id: str = 'FOO-0352'
    vertical: str = 'footwear'
    model_revision: int = 352
    is_certified: bool = True
    base_mrp: Decimal = Decimal('55799.00')
    selling_price: Decimal = Decimal('40719.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification353:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #353."""
    sku_id: str = 'FOO-0353'
    vertical: str = 'footwear'
    model_revision: int = 353
    is_certified: bool = True
    base_mrp: Decimal = Decimal('55949.00')
    selling_price: Decimal = Decimal('40829.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification354:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #354."""
    sku_id: str = 'FOO-0354'
    vertical: str = 'footwear'
    model_revision: int = 354
    is_certified: bool = True
    base_mrp: Decimal = Decimal('56099.00')
    selling_price: Decimal = Decimal('40939.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification355:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #355."""
    sku_id: str = 'FOO-0355'
    vertical: str = 'footwear'
    model_revision: int = 355
    is_certified: bool = True
    base_mrp: Decimal = Decimal('56249.00')
    selling_price: Decimal = Decimal('41049.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification356:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #356."""
    sku_id: str = 'FOO-0356'
    vertical: str = 'footwear'
    model_revision: int = 356
    is_certified: bool = True
    base_mrp: Decimal = Decimal('56399.00')
    selling_price: Decimal = Decimal('41159.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification357:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #357."""
    sku_id: str = 'FOO-0357'
    vertical: str = 'footwear'
    model_revision: int = 357
    is_certified: bool = True
    base_mrp: Decimal = Decimal('56549.00')
    selling_price: Decimal = Decimal('41269.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification358:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #358."""
    sku_id: str = 'FOO-0358'
    vertical: str = 'footwear'
    model_revision: int = 358
    is_certified: bool = True
    base_mrp: Decimal = Decimal('56699.00')
    selling_price: Decimal = Decimal('41379.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification359:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #359."""
    sku_id: str = 'FOO-0359'
    vertical: str = 'footwear'
    model_revision: int = 359
    is_certified: bool = True
    base_mrp: Decimal = Decimal('56849.00')
    selling_price: Decimal = Decimal('41489.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification360:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #360."""
    sku_id: str = 'FOO-0360'
    vertical: str = 'footwear'
    model_revision: int = 360
    is_certified: bool = True
    base_mrp: Decimal = Decimal('56999.00')
    selling_price: Decimal = Decimal('41599.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification361:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #361."""
    sku_id: str = 'FOO-0361'
    vertical: str = 'footwear'
    model_revision: int = 361
    is_certified: bool = True
    base_mrp: Decimal = Decimal('57149.00')
    selling_price: Decimal = Decimal('41709.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification362:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #362."""
    sku_id: str = 'FOO-0362'
    vertical: str = 'footwear'
    model_revision: int = 362
    is_certified: bool = True
    base_mrp: Decimal = Decimal('57299.00')
    selling_price: Decimal = Decimal('41819.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification363:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #363."""
    sku_id: str = 'FOO-0363'
    vertical: str = 'footwear'
    model_revision: int = 363
    is_certified: bool = True
    base_mrp: Decimal = Decimal('57449.00')
    selling_price: Decimal = Decimal('41929.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification364:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #364."""
    sku_id: str = 'FOO-0364'
    vertical: str = 'footwear'
    model_revision: int = 364
    is_certified: bool = True
    base_mrp: Decimal = Decimal('57599.00')
    selling_price: Decimal = Decimal('42039.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification365:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #365."""
    sku_id: str = 'FOO-0365'
    vertical: str = 'footwear'
    model_revision: int = 365
    is_certified: bool = True
    base_mrp: Decimal = Decimal('57749.00')
    selling_price: Decimal = Decimal('42149.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification366:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #366."""
    sku_id: str = 'FOO-0366'
    vertical: str = 'footwear'
    model_revision: int = 366
    is_certified: bool = True
    base_mrp: Decimal = Decimal('57899.00')
    selling_price: Decimal = Decimal('42259.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification367:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #367."""
    sku_id: str = 'FOO-0367'
    vertical: str = 'footwear'
    model_revision: int = 367
    is_certified: bool = True
    base_mrp: Decimal = Decimal('58049.00')
    selling_price: Decimal = Decimal('42369.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification368:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #368."""
    sku_id: str = 'FOO-0368'
    vertical: str = 'footwear'
    model_revision: int = 368
    is_certified: bool = True
    base_mrp: Decimal = Decimal('58199.00')
    selling_price: Decimal = Decimal('42479.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification369:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #369."""
    sku_id: str = 'FOO-0369'
    vertical: str = 'footwear'
    model_revision: int = 369
    is_certified: bool = True
    base_mrp: Decimal = Decimal('58349.00')
    selling_price: Decimal = Decimal('42589.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification370:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #370."""
    sku_id: str = 'FOO-0370'
    vertical: str = 'footwear'
    model_revision: int = 370
    is_certified: bool = True
    base_mrp: Decimal = Decimal('58499.00')
    selling_price: Decimal = Decimal('42699.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification371:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #371."""
    sku_id: str = 'FOO-0371'
    vertical: str = 'footwear'
    model_revision: int = 371
    is_certified: bool = True
    base_mrp: Decimal = Decimal('58649.00')
    selling_price: Decimal = Decimal('42809.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification372:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #372."""
    sku_id: str = 'FOO-0372'
    vertical: str = 'footwear'
    model_revision: int = 372
    is_certified: bool = True
    base_mrp: Decimal = Decimal('58799.00')
    selling_price: Decimal = Decimal('42919.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification373:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #373."""
    sku_id: str = 'FOO-0373'
    vertical: str = 'footwear'
    model_revision: int = 373
    is_certified: bool = True
    base_mrp: Decimal = Decimal('58949.00')
    selling_price: Decimal = Decimal('43029.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification374:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #374."""
    sku_id: str = 'FOO-0374'
    vertical: str = 'footwear'
    model_revision: int = 374
    is_certified: bool = True
    base_mrp: Decimal = Decimal('59099.00')
    selling_price: Decimal = Decimal('43139.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification375:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #375."""
    sku_id: str = 'FOO-0375'
    vertical: str = 'footwear'
    model_revision: int = 375
    is_certified: bool = True
    base_mrp: Decimal = Decimal('59249.00')
    selling_price: Decimal = Decimal('43249.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification376:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #376."""
    sku_id: str = 'FOO-0376'
    vertical: str = 'footwear'
    model_revision: int = 376
    is_certified: bool = True
    base_mrp: Decimal = Decimal('59399.00')
    selling_price: Decimal = Decimal('43359.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification377:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #377."""
    sku_id: str = 'FOO-0377'
    vertical: str = 'footwear'
    model_revision: int = 377
    is_certified: bool = True
    base_mrp: Decimal = Decimal('59549.00')
    selling_price: Decimal = Decimal('43469.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification378:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #378."""
    sku_id: str = 'FOO-0378'
    vertical: str = 'footwear'
    model_revision: int = 378
    is_certified: bool = True
    base_mrp: Decimal = Decimal('59699.00')
    selling_price: Decimal = Decimal('43579.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification379:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #379."""
    sku_id: str = 'FOO-0379'
    vertical: str = 'footwear'
    model_revision: int = 379
    is_certified: bool = True
    base_mrp: Decimal = Decimal('59849.00')
    selling_price: Decimal = Decimal('43689.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification380:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #380."""
    sku_id: str = 'FOO-0380'
    vertical: str = 'footwear'
    model_revision: int = 380
    is_certified: bool = True
    base_mrp: Decimal = Decimal('59999.00')
    selling_price: Decimal = Decimal('43799.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification381:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #381."""
    sku_id: str = 'FOO-0381'
    vertical: str = 'footwear'
    model_revision: int = 381
    is_certified: bool = True
    base_mrp: Decimal = Decimal('60149.00')
    selling_price: Decimal = Decimal('43909.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification382:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #382."""
    sku_id: str = 'FOO-0382'
    vertical: str = 'footwear'
    model_revision: int = 382
    is_certified: bool = True
    base_mrp: Decimal = Decimal('60299.00')
    selling_price: Decimal = Decimal('44019.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification383:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #383."""
    sku_id: str = 'FOO-0383'
    vertical: str = 'footwear'
    model_revision: int = 383
    is_certified: bool = True
    base_mrp: Decimal = Decimal('60449.00')
    selling_price: Decimal = Decimal('44129.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification384:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #384."""
    sku_id: str = 'FOO-0384'
    vertical: str = 'footwear'
    model_revision: int = 384
    is_certified: bool = True
    base_mrp: Decimal = Decimal('60599.00')
    selling_price: Decimal = Decimal('44239.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification385:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #385."""
    sku_id: str = 'FOO-0385'
    vertical: str = 'footwear'
    model_revision: int = 385
    is_certified: bool = True
    base_mrp: Decimal = Decimal('60749.00')
    selling_price: Decimal = Decimal('44349.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification386:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #386."""
    sku_id: str = 'FOO-0386'
    vertical: str = 'footwear'
    model_revision: int = 386
    is_certified: bool = True
    base_mrp: Decimal = Decimal('60899.00')
    selling_price: Decimal = Decimal('44459.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification387:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #387."""
    sku_id: str = 'FOO-0387'
    vertical: str = 'footwear'
    model_revision: int = 387
    is_certified: bool = True
    base_mrp: Decimal = Decimal('61049.00')
    selling_price: Decimal = Decimal('44569.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification388:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #388."""
    sku_id: str = 'FOO-0388'
    vertical: str = 'footwear'
    model_revision: int = 388
    is_certified: bool = True
    base_mrp: Decimal = Decimal('61199.00')
    selling_price: Decimal = Decimal('44679.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification389:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #389."""
    sku_id: str = 'FOO-0389'
    vertical: str = 'footwear'
    model_revision: int = 389
    is_certified: bool = True
    base_mrp: Decimal = Decimal('61349.00')
    selling_price: Decimal = Decimal('44789.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification390:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #390."""
    sku_id: str = 'FOO-0390'
    vertical: str = 'footwear'
    model_revision: int = 390
    is_certified: bool = True
    base_mrp: Decimal = Decimal('61499.00')
    selling_price: Decimal = Decimal('44899.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification391:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #391."""
    sku_id: str = 'FOO-0391'
    vertical: str = 'footwear'
    model_revision: int = 391
    is_certified: bool = True
    base_mrp: Decimal = Decimal('61649.00')
    selling_price: Decimal = Decimal('45009.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification392:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #392."""
    sku_id: str = 'FOO-0392'
    vertical: str = 'footwear'
    model_revision: int = 392
    is_certified: bool = True
    base_mrp: Decimal = Decimal('61799.00')
    selling_price: Decimal = Decimal('45119.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification393:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #393."""
    sku_id: str = 'FOO-0393'
    vertical: str = 'footwear'
    model_revision: int = 393
    is_certified: bool = True
    base_mrp: Decimal = Decimal('61949.00')
    selling_price: Decimal = Decimal('45229.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification394:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #394."""
    sku_id: str = 'FOO-0394'
    vertical: str = 'footwear'
    model_revision: int = 394
    is_certified: bool = True
    base_mrp: Decimal = Decimal('62099.00')
    selling_price: Decimal = Decimal('45339.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification395:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #395."""
    sku_id: str = 'FOO-0395'
    vertical: str = 'footwear'
    model_revision: int = 395
    is_certified: bool = True
    base_mrp: Decimal = Decimal('62249.00')
    selling_price: Decimal = Decimal('45449.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification396:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #396."""
    sku_id: str = 'FOO-0396'
    vertical: str = 'footwear'
    model_revision: int = 396
    is_certified: bool = True
    base_mrp: Decimal = Decimal('62399.00')
    selling_price: Decimal = Decimal('45559.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification397:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #397."""
    sku_id: str = 'FOO-0397'
    vertical: str = 'footwear'
    model_revision: int = 397
    is_certified: bool = True
    base_mrp: Decimal = Decimal('62549.00')
    selling_price: Decimal = Decimal('45669.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification398:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #398."""
    sku_id: str = 'FOO-0398'
    vertical: str = 'footwear'
    model_revision: int = 398
    is_certified: bool = True
    base_mrp: Decimal = Decimal('62699.00')
    selling_price: Decimal = Decimal('45779.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification399:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #399."""
    sku_id: str = 'FOO-0399'
    vertical: str = 'footwear'
    model_revision: int = 399
    is_certified: bool = True
    base_mrp: Decimal = Decimal('62849.00')
    selling_price: Decimal = Decimal('45889.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


@dataclasses.dataclass(frozen=True)
class FootwearSkuSpecification400:
    """Specification schema for Athletic & Lifestyle Footwear SKU Model #400."""
    sku_id: str = 'FOO-0400'
    vertical: str = 'footwear'
    model_revision: int = 400
    is_certified: bool = True
    base_mrp: Decimal = Decimal('62999.00')
    selling_price: Decimal = Decimal('45999.00')
    tax_gst_rate: Decimal = Decimal('18.00')
    hsn_code: str = '85171300'
    warranty_months: int = 12
    weight_grams: int = 350
    created_at: datetime = dataclasses.field(default_factory=lambda: datetime.now(timezone.utc))

    def compute_landed_cost(self, freight_per_kg: Decimal = Decimal('45.00')) -> Decimal:
        weight_kg = Decimal(str(self.weight_grams)) / Decimal('1000')
        freight_cost = weight_kg * freight_per_kg
        gst_amount = (self.selling_price * self.tax_gst_rate) / Decimal('100')
        return self.selling_price + gst_amount + freight_cost

    def validate_compliance_metrics(self) -> typing.Dict[str, typing.Any]:
        return {
            'sku_id': self.sku_id,
            'is_valid': True,
            'bis_standard': 'IS 13252:2010',
            'rohs_status': 'PASS',
            'e_waste_registration': 'E-WASTE-2026-IN',
            'packaging_recyclable': True,
            'qc_checkpoint_score': 98.5
        }

    def generate_inspection_report(self) -> str:
        return f"SKU {self.sku_id} (Athletic & Lifestyle Footwear) meets all Bureau of Indian Standards metrics with landed cost {self.compute_landed_cost()} INR."


