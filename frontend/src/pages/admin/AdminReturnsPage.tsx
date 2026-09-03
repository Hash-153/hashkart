import React, { useState } from 'react';
import { RotateCcw, CheckCircle2, XCircle, Search, ShieldCheck } from 'lucide-react';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { useToast } from '../../components/ui/Toast';

interface ReturnRequestRecord {
  id: number;
  returnId: string;
  orderNumber: string;
  customerName: string;
  productName: string;
  reason: string;
  refundAmount: number;
  status: 'PENDING_INSPECTION' | 'INSPECTED_APPROVED' | 'REJECTED' | 'REFUNDED';
}

const MOCK_RETURNS: ReturnRequestRecord[] = [
  { id: 1, returnId: 'RET-8921', orderNumber: 'HK-20260824-7B1C', customerName: 'Vikas Gupta', productName: 'Sony WH-1000XM5 Headphones', reason: 'Left ear cup crackling defect', refundAmount: 26990, status: 'PENDING_INSPECTION' },
  { id: 2, returnId: 'RET-8920', orderNumber: 'HK-20260823-3A1B', customerName: 'Meera Sen', productName: 'Puma Men Running Shoes (Size 9)', reason: 'Size mismatch', refundAmount: 2499, status: 'PENDING_INSPECTION' },
  { id: 3, returnId: 'RET-8919', orderNumber: 'HK-20260822-9C8D', customerName: 'Arjun Das', productName: 'Apple iPhone 15 Silicone Case', reason: 'Color not as shown', refundAmount: 4900, status: 'REFUNDED' },
];

export const AdminReturnsPage: React.FC = () => {
  const { showToast } = useToast();
  const [returns, setReturns] = useState<ReturnRequestRecord[]>(MOCK_RETURNS);

  const handleApprove = (id: number) => {
    setReturns((prev) =>
      prev.map((r) => (r.id === id ? { ...r, status: 'REFUNDED' } : r))
    );
    showToast('success', 'Return Inspected & Refund Initiated', 'Instant bank refund queued via payment gateway.');
  };

  const handleReject = (id: number) => {
    setReturns((prev) =>
      prev.map((r) => (r.id === id ? { ...r, status: 'REJECTED' } : r))
    );
    showToast('error', 'Return Rejected', 'Item failed quality inspection (signs of customer physical damage).');
  };

  const columns: ColumnDef<ReturnRequestRecord>[] = [
    {
      key: 'returnId',
      header: 'Return Ref / Order',
      render: (item) => (
        <div>
          <span className="font-mono text-xs font-bold text-gray-900">{item.returnId}</span>
          <p className="font-mono text-[11px] text-gray-400">#{item.orderNumber}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'customerName',
      header: 'Customer / Product',
      render: (item) => (
        <div>
          <p className="text-xs font-semibold text-gray-900">{item.customerName}</p>
          <p className="text-[11px] text-gray-600 line-clamp-1">{item.productName}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'reason',
      header: 'Customer Reason',
      render: (item) => <span className="text-xs text-gray-700">{item.reason}</span>,
    },
    {
      key: 'refundAmount',
      header: 'Refund (INR)',
      render: (item) => <span className="font-bold text-xs">₹{item.refundAmount.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'status',
      header: 'Inspection Status',
      render: (item) => {
        if (item.status === 'PENDING_INSPECTION') {
          return <span className="px-2 py-0.5 bg-amber-100 text-amber-800 rounded font-semibold text-[11px]">Inspection Queue</span>;
        }
        if (item.status === 'REFUNDED') {
          return <span className="px-2 py-0.5 bg-green-100 text-green-800 rounded font-semibold text-[11px]">Approved & Refunded</span>;
        }
        return <span className="px-2 py-0.5 bg-red-100 text-red-800 rounded font-semibold text-[11px]">Rejected</span>;
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Quality Decision',
      render: (item) => (
        item.status === 'PENDING_INSPECTION' ? (
          <div className="flex items-center gap-2">
            <button
              type="button"
              className="btn btn-primary btn-sm flex items-center gap-1"
              onClick={() => handleApprove(item.id)}
            >
              <CheckCircle2 size={12} />
              <span>Pass & Refund</span>
            </button>
            <button
              type="button"
              className="btn btn-danger btn-sm flex items-center gap-1"
              onClick={() => handleReject(item.id)}
            >
              <XCircle size={12} />
              <span>Reject</span>
            </button>
          </div>
        ) : (
          <span className="text-xs text-gray-400">Processed</span>
        )
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div>
        <h1 className="text-xl font-bold text-gray-900">Returns Quality Inspection & Refund Station</h1>
        <p className="text-xs text-gray-500 mt-0.5">Physical inspection validation, barcode serial matching, and automated escrow refund triggers.</p>
      </div>

      <DataTable
        data={returns}
        columns={columns}
        searchPlaceholder="Search by return ID or customer..."
        searchKey="customerName"
      />
    </div>
  );
};
