from decimal import Decimal
import pytest

from app.services.tax_compliance_gstr_engine import (
    GSTComplianceEngine,
    GSTR8MonthlyStatement,
)


def test_gstr8_monthly_statement_tcs_calculation():
    seller_orders = [
        # Seller 1: Karnataka (Intra-state)
        {
            "seller_gstin": "29AAACB1234K1Z5",
            "seller_name": "Retail Hub BLR",
            "gross_amount": Decimal("100000.00"),
            "return_amount": Decimal("5000.00"),
            "is_interstate": False,
        },
        # Seller 2: Maharashtra (Inter-state)
        {
            "seller_gstin": "27AAACB5678K1Z2",
            "seller_name": "Mumbai Electronics",
            "gross_amount": Decimal("200000.00"),
            "return_amount": Decimal("0.00"),
            "is_interstate": True,
        },
    ]

    stmt = GSTComplianceEngine.generate_gstr8_monthly_statement(
        return_period="08-2026",
        ecommerce_gstin="29NOVAMART001Z9",
        seller_orders_data=seller_orders,
    )

    assert stmt.return_period_month == "08-2026"
    assert stmt.total_gross_supplies == Decimal("300000.00")
    assert stmt.total_returns == Decimal("5000.00")
    assert stmt.total_net_taxable_supplies == Decimal("295000.00")
    assert len(stmt.seller_records) == 2
    assert stmt.total_tcs_igst == Decimal("2000.00") # 1% on 200,000
    assert stmt.grand_total_tcs_deposited > Decimal("2000.00")
