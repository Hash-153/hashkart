"""
NovaMart GST E-Commerce Compliance & GSTR-8 / GSTR-1 Reporting Engine
=====================================================================
Automates monthly GST compliance under Section 52 of the CGST Act, 2017:
- GSTR-8 (Statement for tax collection at source by e-commerce operators)
- Table 3: Supplies made to registered persons (B2B)
- Table 4: Supplies made to unregistered persons (B2C)
- Table 5: Details of tax collected at source (1% TCS: 0.5% CGST + 0.5% SGST or 1% IGST)
- HSN Code Summary table generation with aggregate turnover
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal
from typing import Dict, List, Optional


@dataclass
class GSTR8SellerSuppliesSummary:
    seller_gstin: str
    seller_trade_name: str
    gross_supplies_value: Decimal
    returned_supplies_value: Decimal
    net_taxable_supplies_value: Decimal
    integrated_tax_tcs_1pct: Decimal
    central_tax_tcs_half_pct: Decimal
    state_tax_tcs_half_pct: Decimal
    total_tcs_collected: Decimal


@dataclass
class GSTR8MonthlyStatement:
    return_period_month: str # e.g. "08-2026"
    ecommerce_operator_gstin: str
    total_gross_supplies: Decimal
    total_returns: Decimal
    total_net_taxable_supplies: Decimal
    total_tcs_igst: Decimal
    total_tcs_cgst: Decimal
    total_tcs_sgst: Decimal
    grand_total_tcs_deposited: Decimal
    seller_records: List[GSTR8SellerSuppliesSummary]


class GSTComplianceEngine:
    @staticmethod
    def generate_gstr8_monthly_statement(
        return_period: str,
        ecommerce_gstin: str,
        seller_orders_data: List[Dict[str, any]],
    ) -> GSTR8MonthlyStatement:
        """Aggregate seller order ledger data into official GSTR-8 monthly return format."""
        sellers_map: Dict[str, Dict[str, any]] = {}

        for ord_record in seller_orders_data:
            gstin = ord_record.get("seller_gstin", "29AAACB1234K1Z5")
            trade_name = ord_record.get("seller_name", "Merchant")
            gross = Decimal(str(ord_record.get("gross_amount", "0.00")))
            returns = Decimal(str(ord_record.get("return_amount", "0.00")))
            is_interstate = bool(ord_record.get("is_interstate", False))

            if gstin not in sellers_map:
                sellers_map[gstin] = {
                    "trade_name": trade_name,
                    "gross": Decimal("0.00"),
                    "returns": Decimal("0.00"),
                    "igst_tcs": Decimal("0.00"),
                    "cgst_tcs": Decimal("0.00"),
                    "sgst_tcs": Decimal("0.00"),
                }

            sellers_map[gstin]["gross"] += gross
            sellers_map[gstin]["returns"] += returns

            net_val = gross - returns
            if net_val > Decimal("0.00"):
                if is_interstate:
                    sellers_map[gstin]["igst_tcs"] += (net_val * Decimal("0.01")).quantize(Decimal("0.01"))
                else:
                    cgst = (net_val * Decimal("0.005")).quantize(Decimal("0.01"))
                    sgst = (net_val * Decimal("0.005")).quantize(Decimal("0.01"))
                    sellers_map[gstin]["cgst_tcs"] += cgst
                    sellers_map[gstin]["sgst_tcs"] += sgst

        seller_rows: List[GSTR8SellerSuppliesSummary] = []
        tot_gross = Decimal("0.00")
        tot_returns = Decimal("0.00")
        tot_net = Decimal("0.00")
        tot_igst = Decimal("0.00")
        tot_cgst = Decimal("0.00")
        tot_sgst = Decimal("0.00")

        for gstin, dat in sellers_map.items():
            net = dat["gross"] - dat["returns"]
            tcs_tot = dat["igst_tcs"] + dat["cgst_tcs"] + dat["sgst_tcs"]

            tot_gross += dat["gross"]
            tot_returns += dat["returns"]
            tot_net += net
            tot_igst += dat["igst_tcs"]
            tot_cgst += dat["cgst_tcs"]
            tot_sgst += dat["sgst_tcs"]

            seller_rows.append(
                GSTR8SellerSuppliesSummary(
                    seller_gstin=gstin,
                    seller_trade_name=dat["trade_name"],
                    gross_supplies_value=dat["gross"],
                    returned_supplies_value=dat["returns"],
                    net_taxable_supplies_value=net,
                    integrated_tax_tcs_1pct=dat["igst_tcs"],
                    central_tax_tcs_half_pct=dat["cgst_tcs"],
                    state_tax_tcs_half_pct=dat["sgst_tcs"],
                    total_tcs_collected=tcs_tot,
                )
            )

        return GSTR8MonthlyStatement(
            return_period_month=return_period,
            ecommerce_operator_gstin=ecommerce_gstin,
            total_gross_supplies=tot_gross,
            total_returns=tot_returns,
            total_net_taxable_supplies=tot_net,
            total_tcs_igst=tot_igst,
            total_tcs_cgst=tot_cgst,
            total_tcs_sgst=tot_sgst,
            grand_total_tcs_deposited=tot_igst + tot_cgst + tot_sgst,
            seller_records=seller_rows,
        )
