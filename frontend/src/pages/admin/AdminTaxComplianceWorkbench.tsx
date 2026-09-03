import React, { useState } from 'react';
import { FileText, Download, ShieldCheck, CheckCircle2, AlertCircle, Calendar, Hash, Building2 } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { Badge } from '../../components/ui/Badge';
import { useToast } from '../../components/ui/Toast';

interface GSTRStatementRecord {
  returnPeriod: string; // e.g. "August 2026"
  formType: 'GSTR-8' | 'GSTR-1' | 'GSTR-3B' | 'TCS_CHALLAN';
  grossTaxableSupplies: number;
  returnsValue: number;
  netSupplies: number;
  cgstCollected: number;
  sgstCollected: number;
  igstCollected: number;
  totalTaxLiability: number;
  filingStatus: 'FILED_ACKNOWLEDGED' | 'READY_FOR_FILING' | 'GENERATING';
  arnNumber: string;
}

const MOCK_GSTR_STATEMENTS: GSTRStatementRecord[] = [
  { returnPeriod: 'August 2026', formType: 'GSTR-8', grossTaxableSupplies: 184500000, returnsValue: 12400000, netSupplies: 172100000, cgstCollected: 860500, sgstCollected: 860500, igstCollected: 0, totalTaxLiability: 1721000, filingStatus: 'READY_FOR_FILING', arnNumber: 'ARN-PENDING-08' },
  { returnPeriod: 'July 2026', formType: 'GSTR-8', grossTaxableSupplies: 162000000, returnsValue: 10800000, netSupplies: 151200000, cgstCollected: 756000, sgstCollected: 756000, igstCollected: 0, totalTaxLiability: 1512000, filingStatus: 'FILED_ACKNOWLEDGED', arnNumber: 'AA2907260192841' },
  { returnPeriod: 'July 2026', formType: 'TCS_CHALLAN', grossTaxableSupplies: 151200000, returnsValue: 0, netSupplies: 151200000, cgstCollected: 756000, sgstCollected: 756000, igstCollected: 0, totalTaxLiability: 1512000, filingStatus: 'FILED_ACKNOWLEDGED', arnNumber: 'CIN-HDFC-991204' },
  { returnPeriod: 'June 2026', formType: 'GSTR-8', grossTaxableSupplies: 148900000, returnsValue: 9200000, netSupplies: 139700000, cgstCollected: 698500, sgstCollected: 698500, igstCollected: 0, totalTaxLiability: 1397000, filingStatus: 'FILED_ACKNOWLEDGED', arnNumber: 'AA2906260882194' },
];

export const AdminTaxComplianceWorkbench: React.FC = () => {
  const { showToast } = useToast();
  const [statements, setStatements] = useState<GSTRStatementRecord[]>(MOCK_GSTR_STATEMENTS);

  const handleTransmitGSTN = (period: string) => {
    setStatements((prev) =>
      prev.map((s) => (s.returnPeriod === period ? { ...s, filingStatus: 'FILED_ACKNOWLEDGED', arnNumber: `AA290826${Math.floor(100000 + Math.random() * 900000)}` } : s))
    );
    showToast('success', 'Return Filed with GSTN', `Successfully transmitted ${period} GSTR-8 return to government portal.`);
  };

  const columns: ColumnDef<GSTRStatementRecord>[] = [
    {
      key: 'returnPeriod',
      header: 'Return Period & Form',
      render: (item) => (
        <div>
          <div className="flex items-center gap-2">
            <span className="font-bold text-xs text-gray-900">{item.returnPeriod}</span>
            <span className="text-[10px] font-bold text-blue-700 bg-blue-50 px-2 py-0.5 rounded">{item.formType}</span>
          </div>
          <span className="font-mono text-[10px] text-gray-400">ARN: {item.arnNumber}</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'netSupplies',
      header: 'Net Taxable Supplies (₹)',
      render: (item) => (
        <div>
          <span className="font-bold text-xs text-gray-900">₹{item.netSupplies.toLocaleString('en-IN')}</span>
          <p className="text-[10px] text-gray-400">Gross: ₹{item.grossTaxableSupplies.toLocaleString('en-IN')}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'totalTaxLiability',
      header: '1% TCS Collected (₹)',
      render: (item) => (
        <div>
          <span className="font-black text-xs text-emerald-700">₹{item.totalTaxLiability.toLocaleString('en-IN')}</span>
          <p className="text-[10px] text-gray-500">CGST (0.5%) + SGST (0.5%)</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'filingStatus',
      header: 'GSTN Status',
      render: (item) => {
        const variants: Record<string, 'success' | 'warning' | 'info'> = {
          FILED_ACKNOWLEDGED: 'success',
          READY_FOR_FILING: 'warning',
          GENERATING: 'info',
        };
        return <Badge variant={variants[item.filingStatus] || 'neutral'}>{item.filingStatus.replace(/_/g, ' ')}</Badge>;
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Government Filing',
      render: (item) => (
        item.filingStatus === 'READY_FOR_FILING' ? (
          <button
            type="button"
            className="btn btn-primary btn-sm flex items-center gap-1 text-xs"
            onClick={() => handleTransmitGSTN(item.returnPeriod)}
          >
            <CheckCircle2 size={12} />
            <span>File with GSTN</span>
          </button>
        ) : (
          <button
            type="button"
            className="btn btn-neutral btn-sm flex items-center gap-1 text-xs"
            onClick={() => showToast('info', 'Downloaded JSON', `Downloaded GSTR-8 offline schema JSON for ${item.returnPeriod}`)}
          >
            <Download size={12} />
            <span>JSON Return</span>
          </button>
        )
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">GST E-Commerce Operator (ECO) Tax Compliance Console</h1>
          <p className="text-xs text-gray-500 mt-0.5">Section 52 Tax Collection at Source (TCS) statements and GSTR-8 monthly return filing.</p>
        </div>

        <button
          type="button"
          className="btn btn-neutral btn-sm flex items-center gap-1.5"
          onClick={() => showToast('success', 'Challan Generated', 'Prepared Form GST PMT-06 electronic cash challan.')}
        >
          <Download size={14} />
          <span>Generate PMT-06 Challan</span>
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Current Month Taxable GMV" value="₹17.21 Crore" subtitle="Post returns deduction" variant="blue" />
        <MetricCard title="Section 52 TCS Deposited" value="₹17.21 Lakh" subtitle="1% statutory collection" variant="green" />
        <MetricCard title="Section 194-O TDS Filed" value="₹17.21 Lakh" subtitle="Income Tax e-filing" variant="purple" />
        <MetricCard title="Audit Compliance Score" value="100% Pass" subtitle="Zero statutory notices" variant="neutral" />
      </div>

      <DataTable
        data={statements}
        columns={columns}
        searchPlaceholder="Search return period or ARN..."
        searchKey="returnPeriod"
      />
    </div>
  );
};
