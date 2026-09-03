"""
NovaMart Indian State-by-State Statutory Financial Schedules & TCS Forms
========================================================================
Detailed statutory forms for marketplace tax filings:
- Form GSTR-8 Section 52 Tax Collection at Source Schedule
- Form 26Q & 27EQ Income Tax Act Section 194-O TDS reporting
- State-wise GSTIN jurisdiction codes, tax nodal accounts, and electronic cash ledger codes
"""

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, List, Optional


@dataclass
class StateTaxJurisdictionRecord:
    state_code: int
    state_name: str
    state_short_code: str
    gstin_prefix: str
    cgst_account_head: str
    sgst_account_head: str
    igst_account_head: str
    is_union_territory: bool = False


STATE_JURISDICTIONS_DIRECTORY: Dict[int, StateTaxJurisdictionRecord] = {
    1: StateTaxJurisdictionRecord(1, "Jammu and Kashmir", "JK", "01", "0005", "0006", "0008"),
    2: StateTaxJurisdictionRecord(2, "Himachal Pradesh", "HP", "02", "0005", "0006", "0008"),
    3: StateTaxJurisdictionRecord(3, "Punjab", "PB", "03", "0005", "0006", "0008"),
    4: StateTaxJurisdictionRecord(4, "Chandigarh", "CH", "04", "0005", "0006", "0008", True),
    5: StateTaxJurisdictionRecord(5, "Uttarakhand", "UK", "05", "0005", "0006", "0008"),
    6: StateTaxJurisdictionRecord(6, "Haryana", "HR", "06", "0005", "0006", "0008"),
    7: StateTaxJurisdictionRecord(7, "Delhi", "DL", "07", "0005", "0006", "0008", True),
    8: StateTaxJurisdictionRecord(8, "Rajasthan", "RJ", "08", "0005", "0006", "0008"),
    9: StateTaxJurisdictionRecord(9, "Uttar Pradesh", "UP", "09", "0005", "0006", "0008"),
    10: StateTaxJurisdictionRecord(10, "Bihar", "BR", "10", "0005", "0006", "0008"),
    19: StateTaxJurisdictionRecord(19, "West Bengal", "WB", "19", "0005", "0006", "0008"),
    21: StateTaxJurisdictionRecord(21, "Odisha", "OD", "21", "0005", "0006", "0008"),
    23: StateTaxJurisdictionRecord(23, "Madhya Pradesh", "MP", "23", "0005", "0006", "0008"),
    24: StateTaxJurisdictionRecord(24, "Gujarat", "GJ", "24", "0005", "0006", "0008"),
    27: StateTaxJurisdictionRecord(27, "Maharashtra", "MH", "27", "0005", "0006", "0008"),
    29: StateTaxJurisdictionRecord(29, "Karnataka", "KA", "29", "0005", "0006", "0008"),
    30: StateTaxJurisdictionRecord(30, "Goa", "GA", "30", "0005", "0006", "0008"),
    32: StateTaxJurisdictionRecord(32, "Kerala", "KL", "32", "0005", "0006", "0008"),
    33: StateTaxJurisdictionRecord(33, "Tamil Nadu", "TN", "33", "0005", "0006", "0008"),
    36: StateTaxJurisdictionRecord(36, "Telangana", "TS", "36", "0005", "0006", "0008"),
    37: StateTaxJurisdictionRecord(37, "Andhra Pradesh", "AP", "37", "0005", "0006", "0008"),
}
