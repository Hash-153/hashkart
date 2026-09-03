import React, { useState } from 'react';
import { Landmark, CheckCircle2, ShieldAlert, FileSpreadsheet, ArrowUpRight, DollarSign, Download, Lock, Check } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { Badge } from '../../components/ui/Badge';
import { Modal } from '../../components/ui/Modal';
import { useToast } from '../../components/ui/Toast';

interface EscrowAccountRecord {
  sellerId: number;
  sellerName: string;
  gstin: string;
  bankName: string;
  accountNumberMasked: string;
  heldEscrowBalance: number;
  clearedPayableBalance: number;
  tcsDeductionsMonthly: number;
  tdsDeductionsMonthly: number;
  status: 'ELIGIBLE_FOR_PAYOUT' | 'HELD_RETURN_WINDOW' | 'FROZEN_SECURITY';
}

const MOCK_ESCROW_ACCOUNTS: EscrowAccountRecord[] = [
  { sellerId: 1, sellerName: 'Official Apple Premium Reseller', gstin: '29AAACB1234K1Z5', bankName: 'HDFC Bank', accountNumberMasked: 'XXXX-XXXX-4921', heldEscrowBalance: 4500000, clearedPayableBalance: 8250000, tcsDeductionsMonthly: 127500, tdsDeductionsMonthly: 127500, status: 'ELIGIBLE_FOR_PAYOUT' },
  { sellerId: 2, sellerName: 'Sony Audio World India', gstin: '27AAACB5678K1Z2', bankName: 'ICICI Bank', accountNumberMasked: 'XXXX-XXXX-8819', heldEscrowBalance: 1200000, clearedPayableBalance: 3400000, tcsDeductionsMonthly: 46000, tdsDeductionsMonthly: 46000, status: 'ELIGIBLE_FOR_PAYOUT' },
  { sellerId: 3, sellerName: 'Fastrack Accessories Hub', gstin: '33AAACB9921K1Z0', bankName: 'State Bank of India', accountNumberMasked: 'XXXX-XXXX-1024', heldEscrowBalance: 850000, clearedPayableBalance: 0, tcsDeductionsMonthly: 8500, tdsDeductionsMonthly: 8500, status: 'HELD_RETURN_WINDOW' },
  { sellerId: 4, sellerName: 'Suspicious Device Reseller', gstin: '07AAACB0000K1Z9', bankName: 'Axis Bank', accountNumberMasked: 'XXXX-XXXX-9901', heldEscrowBalance: 320000, clearedPayableBalance: 0, tcsDeductionsMonthly: 3200, tdsDeductionsMonthly: 3200, status: 'FROZEN_SECURITY' },
];

export const AdminFinancialEscrowWorkbench: React.FC = () => {
  const { showToast } = useToast();
  const [accounts, setAccounts] = useState<EscrowAccountRecord[]>(MOCK_ESCROW_ACCOUNTS);
  const [selectedAccount, setSelectedAccount] = useState<EscrowAccountRecord | null>(null);

  const handleDisburseTransfer = (sellerId: number) => {
    setAccounts((prev) =>
      prev.map((a) => (a.sellerId === sellerId ? { ...a, clearedPayableBalance: 0 } : a))
    );
    showToast('success', 'Transfer Transmitted', `Transmitted NEFT payout batch to bank nodal escrow.`);
    setSelectedAccount(null);
  };

  const columns: ColumnDef<EscrowAccountRecord>[] = [
    {
      key: 'sellerName',
      header: 'Merchant & Banking Details',
      render: (item) => (
        <div>
          <p className="font-bold text-xs text-gray-900">{item.sellerName}</p>
          <p className="font-mono text-[11px] text-gray-500">GSTIN: {item.gstin}</p>
          <span className="text-[10px] text-blue-700 font-semibold">{item.bankName} ({item.accountNumberMasked})</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'clearedPayableBalance',
      header: 'Cleared Payable (₹)',
      render: (item) => (
        <span className="font-black text-xs text-green-700">
          ₹{item.clearedPayableBalance.toLocaleString('en-IN')}
        </span>
      ),
      sortable: true,
    },
    {
      key: 'heldEscrowBalance',
      header: 'Escrow In-Hold (₹)',
      render: (item) => (
        <span className="font-semibold text-xs text-amber-700">
          ₹{item.heldEscrowBalance.toLocaleString('en-IN')}
        </span>
      ),
      sortable: true,
    },
    {
      key: 'tcsDeductionsMonthly',
      header: '1% TCS & TDS (₹)',
      render: (item) => (
        <span className="text-xs text-gray-600">
          ₹{(item.tcsDeductionsMonthly + item.tdsDeductionsMonthly).toLocaleString('en-IN')}
        </span>
      ),
    },
    {
      key: 'status',
      header: 'Escrow Status',
      render: (item) => {
        const variants: Record<string, 'success' | 'warning' | 'danger'> = {
          ELIGIBLE_FOR_PAYOUT: 'success',
          HELD_RETURN_WINDOW: 'warning',
          FROZEN_SECURITY: 'danger',
        };
        return <Badge variant={variants[item.status] || 'neutral'}>{item.status.replace(/_/g, ' ')}</Badge>;
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Treasury Action',
      render: (item) => (
        item.status === 'ELIGIBLE_FOR_PAYOUT' && item.clearedPayableBalance > 0 ? (
          <button
            type="button"
            className="btn btn-primary btn-sm flex items-center gap-1 text-xs"
            onClick={() => setSelectedAccount(item)}
          >
            <CheckCircle2 size={12} />
            <span>Disburse NEFT</span>
          </button>
        ) : (
          <span className="text-xs text-gray-400 font-medium">No Action</span>
        )
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Marketplace Nodal Escrow & Dual-Auth Settlement Workbench</h1>
          <p className="text-xs text-gray-500 mt-0.5">RBI Nodal Escrow compliance, Section 194-O TDS & Section 52 TCS tax withholdings.</p>
        </div>

        <button
          type="button"
          className="btn btn-neutral btn-sm flex items-center gap-1.5"
          onClick={() => showToast('success', 'NACHA Exported', 'Downloaded daily NEFT payout file.')}
        >
          <Download size={14} />
          <span>Export NACHA NEFT File</span>
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Total Nodal Escrow Balance" value="₹1,82,70,000" subtitle="In commercial bank pool" variant="blue" />
        <MetricCard title="Cleared Ready for Payout" value="₹1,16,50,000" subtitle="Post 7-day return window" variant="green" />
        <MetricCard title="In Return Hold" value="₹68,70,000" subtitle="Pending buyer return expiry" variant="amber" />
        <MetricCard title="Monthly TCS/TDS Withheld" value="₹3,65,400" subtitle="Credited to government challan" variant="purple" />
      </div>

      <DataTable
        data={accounts}
        columns={columns}
        searchPlaceholder="Search merchant name or GSTIN..."
        searchKey="sellerName"
      />

      {/* Disburse Confirmation Modal */}
      {selectedAccount && (
        <Modal
          isOpen={true}
          onClose={() => setSelectedAccount(null)}
          title="Dual-Authorization NEFT Payout Approval"
        >
          <div className="space-y-4 text-xs">
            <div className="p-3 bg-green-50 border border-green-200 rounded-lg">
              <p className="font-bold text-green-900">Authorize Bank Transfer of ₹{selectedAccount.clearedPayableBalance.toLocaleString('en-IN')}</p>
              <p className="text-green-700 mt-1">
                Beneficiary: <span className="font-semibold">{selectedAccount.sellerName}</span> ({selectedAccount.bankName})
              </p>
            </div>

            <div className="space-y-2">
              <p className="text-gray-600">Dual approval requires cryptographic signature verification with nodal bank.</p>
              <input
                type="password"
                placeholder="Enter Senior Finance Authorizer PIN"
                className="w-full p-2 border rounded font-mono text-xs"
                defaultValue="••••••••"
              />
            </div>

            <div className="pt-3 border-t flex justify-end gap-2">
              <button
                type="button"
                className="btn btn-neutral btn-sm"
                onClick={() => setSelectedAccount(null)}
              >
                Cancel
              </button>
              <button
                type="button"
                className="btn btn-primary btn-sm flex items-center gap-1"
                onClick={() => handleDisburseTransfer(selectedAccount.sellerId)}
              >
                <Check size={14} />
                <span>Confirm & Transmit Payout</span>
              </button>
            </div>
          </div>
        </Modal>
      )}
    </div>
  );
};
