import React, { useState } from 'react';
import { FileText, Download, CheckCircle2, AlertCircle, Calendar, Landmark } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { useToast } from '../../components/ui/Toast';

interface GSTRStatementRecord {
  id: string;
  month: string;
  formType: 'GSTR-8 (TCS)' | 'GSTR-1 (Outward)' | 'GSTR-7 (TDS)';
  grossSupplies: number;
  returns: number;
  netTaxable: number;
  taxWithheld: number;
  filingStatus: 'FILED_WITH_GOVT' | 'READY_FOR_FILING' | 'GENERATING';
  challanNumber: string;
}

const MOCK_GSTR_STATEMENTS: GSTRStatementRecord[] = [
  { id: 'GST-2026-08', month: 'August 2026', formType: 'GSTR-8 (TCS)', grossSupplies: 48500000, returns: 1200000, netTaxable: 47300000, taxWithheld: 473000, filingStatus: 'READY_FOR_FILING', challanNumber: 'CH-202608-8921' },
  { id: 'GST-2026-07', month: 'July 2026', formType: 'GSTR-8 (TCS)', grossSupplies: 42100000, returns: 950000, netTaxable: 41150000, taxWithheld: 411500, filingStatus: 'FILED_WITH_GOVT', challanNumber: 'CH-202607-4401' },
  { id: 'GST-2026-06', month: 'June 2026', formType: 'GSTR-8 (TCS)', grossSupplies: 38900000, returns: 800000, netTaxable: 38100000, taxWithheld: 381000, filingStatus: 'FILED_WITH_GOVT', challanNumber: 'CH-202606-1290' },
];

export const AdminTaxReportingPage: React.FC = () => {
  const { showToast } = useToast();
  const [statements] = useState<GSTRStatementRecord[]>(MOCK_GSTR_STATEMENTS);

  const columns: ColumnDef<GSTRStatementRecord>[] = [
    {
      key: 'month',
      header: 'Filing Month / Form',
      render: (item) => (
        <div>
          <p className="text-xs font-bold text-gray-900">{item.month}</p>
          <span className="font-mono text-[11px] text-blue-700 font-semibold">{item.formType}</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'grossSupplies',
      header: 'Gross GMV (₹)',
      render: (item) => <span className="text-xs font-semibold">₹{item.grossSupplies.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'returns',
      header: 'Customer Returns (₹)',
      render: (item) => <span className="text-xs text-red-600 font-medium">-₹{item.returns.toLocaleString('en-IN')}</span>,
    },
    {
      key: 'netTaxable',
      header: 'Net Taxable (₹)',
      render: (item) => <span className="text-xs font-bold text-gray-900">₹{item.netTaxable.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'taxWithheld',
      header: '1% TCS Deposited (₹)',
      render: (item) => <span className="text-xs font-black text-green-700">₹{item.taxWithheld.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'filingStatus',
      header: 'Govt GSTN Status',
      render: (item) => (
        item.filingStatus === 'FILED_WITH_GOVT' ? (
          <span className="px-2 py-0.5 bg-green-100 text-green-800 text-[10px] font-bold rounded-full">
            Filed & Acknowledged
          </span>
        ) : (
          <span className="px-2 py-0.5 bg-amber-100 text-amber-800 text-[10px] font-bold rounded-full">
            Ready for Sign
          </span>
        )
      ),
    },
    {
      key: 'actions',
      header: 'JSON / PDF Export',
      render: (item) => (
        <button
          type="button"
          className="btn btn-neutral btn-sm flex items-center gap-1"
          onClick={() => showToast('success', 'GSTR-8 JSON Exported', `${item.month} GSTR-8 offline utility JSON downloaded.`)}
        >
          <Download size={12} />
          <span>Export JSON</span>
        </button>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">GST E-Commerce Compliance & GSTR-8 Reporting</h1>
          <p className="text-xs text-gray-500 mt-0.5">Section 52 Tax Collection at Source (TCS) monthly filing and GSTN integration statements.</p>
        </div>

        <button
          type="button"
          className="btn btn-primary btn-sm flex items-center gap-1.5"
          onClick={() => showToast('info', 'Generating Return', 'Aggregating August 2026 ledger records...')}
        >
          <Landmark size={14} />
          <span>Generate Current Month GSTR-8</span>
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="FY 2026-27 Net Turnover" value="₹12.95 Cr" subtitle="Supplies via NovaMart" variant="blue" />
        <MetricCard title="Cumulative TCS Deposited" value="₹12.95 Lakh" subtitle="1% TCS credited to merchants" variant="green" />
        <MetricCard title="Active Seller GSTINs" value="1,240 Verified" subtitle="100% GSTIN verification" variant="purple" />
        <MetricCard title="GSTN Filing Compliance" value="100% On-Time" subtitle="Filed by 10th of every month" variant="neutral" />
      </div>

      <DataTable
        data={statements}
        columns={columns}
        searchPlaceholder="Search filing period..."
        searchKey="month"
      />
    </div>
  );
};
