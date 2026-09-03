import React, { useState } from 'react';
import { DollarSign, CheckCircle2, FileText, AlertTriangle, ArrowDownToLine, Landmark } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { useToast } from '../../components/ui/Toast';

interface AdminPayoutBatchRecord {
  id: number;
  batchReference: string;
  sellerCount: number;
  grossAmount: number;
  commissionWithheld: number;
  tcsWithheld: number;
  tdsWithheld: number;
  netPayout: number;
  status: 'PENDING_FINANCE_APPROVAL' | 'APPROVED_FOR_BANK' | 'DISBURSED';
  scheduledDate: string;
}

const MOCK_ADMIN_BATCHES: AdminPayoutBatchRecord[] = [
  { id: 1, batchReference: 'BATCH-20260825-NEFT-01', sellerCount: 42, grossAmount: 18450000, commissionWithheld: 1476000, tcsWithheld: 184500, tdsWithheld: 184500, netPayout: 16605000, status: 'PENDING_FINANCE_APPROVAL', scheduledDate: 'Today, 5:00 PM' },
  { id: 2, batchReference: 'BATCH-20260824-NEFT-02', sellerCount: 38, grossAmount: 14200000, commissionWithheld: 1136000, tcsWithheld: 142000, tdsWithheld: 142000, netPayout: 12780000, status: 'DISBURSED', scheduledDate: 'Yesterday' },
];

export const AdminSettlementAuditPage: React.FC = () => {
  const { showToast } = useToast();
  const [batches, setBatches] = useState<AdminPayoutBatchRecord[]>(MOCK_ADMIN_BATCHES);

  const handleApproveBatch = (id: number) => {
    setBatches((prev) =>
      prev.map((b) => (b.id === id ? { ...b, status: 'APPROVED_FOR_BANK' } : b))
    );
    showToast('success', 'Batch Approved', 'Automated NACHA NEFT payout file transmitted to bank nodal escrow.');
  };

  const columns: ColumnDef<AdminPayoutBatchRecord>[] = [
    {
      key: 'batchReference',
      header: 'Batch Reference',
      render: (item) => (
        <div>
          <span className="font-mono text-xs font-bold text-gray-900">{item.batchReference}</span>
          <p className="text-[11px] text-gray-400">{item.sellerCount} Merchant Sellers</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'grossAmount',
      header: 'Gross GMV (₹)',
      render: (item) => <span className="font-bold text-xs">₹{item.grossAmount.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'commissionWithheld',
      header: 'Commission + GST',
      render: (item) => <span className="text-xs text-blue-700 font-semibold">₹{item.commissionWithheld.toLocaleString('en-IN')}</span>,
    },
    {
      key: 'tcsWithheld',
      header: '1% TCS / TDS',
      render: (item) => (
        <span className="text-xs text-gray-600">
          ₹{(item.tcsWithheld + item.tdsWithheld).toLocaleString('en-IN')}
        </span>
      ),
    },
    {
      key: 'netPayout',
      header: 'Net Transfer (₹)',
      render: (item) => <span className="font-black text-xs text-green-700">₹{item.netPayout.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'status',
      header: 'Approval State',
      render: (item) => {
        if (item.status === 'PENDING_FINANCE_APPROVAL') {
          return <span className="px-2 py-0.5 bg-amber-100 text-amber-800 rounded font-semibold text-[11px]">Pending Approval</span>;
        }
        if (item.status === 'APPROVED_FOR_BANK') {
          return <span className="px-2 py-0.5 bg-blue-100 text-blue-800 rounded font-semibold text-[11px]">Sent to Bank</span>;
        }
        return <span className="px-2 py-0.5 bg-green-100 text-green-800 rounded font-semibold text-[11px]">Disbursed</span>;
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Audit Action',
      render: (item) => (
        item.status === 'PENDING_FINANCE_APPROVAL' ? (
          <button
            type="button"
            className="btn btn-primary btn-sm flex items-center gap-1"
            onClick={() => handleApproveBatch(item.id)}
          >
            <CheckCircle2 size={12} />
            <span>Approve & Disburse</span>
          </button>
        ) : (
          <span className="text-xs text-gray-400">Processed</span>
        )
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div>
        <h1 className="text-xl font-bold text-gray-900">Financial Settlement & Nodal Escrow Audit Console</h1>
        <p className="text-xs text-gray-500 mt-0.5">Approve merchant batch disbursements, monitor 1% TCS/TDS withholdings, and verify nodal bank balances.</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Nodal Escrow Pool Balance" value="₹4,82,50,000" subtitle="Scheduled commercial bank" variant="blue" />
        <MetricCard title="Pending Disbursement Batch" value="₹1,66,05,000" subtitle="Awaiting CFO dual-authorization" variant="amber" />
        <MetricCard title="Monthly Marketplace Commission" value="₹38,40,000" subtitle="Platform net revenue" variant="green" />
        <MetricCard title="Total Tax Withholdings (TCS/TDS)" value="₹9,60,000" subtitle="Credited to government challan" variant="purple" />
      </div>

      <DataTable
        data={batches}
        columns={columns}
        searchPlaceholder="Search payout batch..."
        searchKey="batchReference"
      />
    </div>
  );
};
