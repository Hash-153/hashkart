import React, { useState, useEffect } from 'react';
import { IndianRupee, ArrowDownToLine, CheckCircle2, Clock, FileText, AlertCircle } from 'lucide-react';
import { api } from '../../services/api';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { useToast } from '../../components/ui/Toast';

export const SellerPayoutsPage: React.FC = () => {
  const { showToast } = useToast();
  const [summary, setSummary] = useState<any | null>(null);
  const [loading, setLoading] = useState(true);
  const [requesting, setRequesting] = useState(false);

  const fetchSummary = async () => {
    try {
      setLoading(true);
      const data = await api.getSellerEscrowSummary();
      setSummary(data);
    } catch (err) {
      console.error('Failed to load escrow summary:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSummary();
  }, []);

  const handleRequestPayout = async () => {
    if (!summary || summary.available_balance < 500) {
      showToast('warning', 'Threshold Not Met', 'Minimum payout request amount is ₹500.00.');
      return;
    }

    setRequesting(true);
    try {
      await api.requestSellerPayout(summary.seller_id, 'NEFT');
      showToast('success', 'Payout Requested', 'Your NEFT transfer request is queued for processing.');
      fetchSummary();
    } catch (err: any) {
      showToast('error', 'Request Failed', err.message || 'Failed to request payout.');
    } finally {
      setRequesting(false);
    }
  };

  const columns: ColumnDef<any>[] = [
    {
      key: 'batch_reference',
      header: 'Batch Reference',
      render: (item) => <span className="font-mono text-xs font-bold text-gray-900">{item.batch_reference}</span>,
      sortable: true,
    },
    {
      key: 'payout_method',
      header: 'Transfer Type',
      render: (item) => <span className="text-xs text-gray-600 font-semibold">{item.payout_method}</span>,
    },
    {
      key: 'net_payout',
      header: 'Net Transfer (₹)',
      render: (item) => <span className="font-bold text-xs text-green-700">₹{item.net_payout.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'status',
      header: 'Settlement Status',
      render: (item) => {
        const isSettled = item.status === 'SETTLED';
        return (
          <span className={`px-2 py-0.5 rounded font-semibold text-[11px] ${
            isSettled ? 'bg-green-100 text-green-800' : 'bg-amber-100 text-amber-800'
          }`}>
            {isSettled ? 'Settled to Bank' : 'Processing NEFT'}
          </span>
        );
      },
      sortable: true,
    },
    {
      key: 'scheduled_date',
      header: 'Date Processed',
      render: (item) => (
        <span className="text-xs text-gray-500">
          {new Date(item.scheduled_date || item.created_at).toLocaleDateString('en-IN', { dateStyle: 'medium' })}
        </span>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Seller Escrow & Bank Payout Reconciliation</h1>
          <p className="text-xs text-gray-500 mt-0.5">Automated settlement statements, GST/TDS tax deductions, and NEFT payout ledger.</p>
        </div>

        <button
          type="button"
          disabled={requesting || !summary || summary.available_balance < 500}
          onClick={handleRequestPayout}
          className="btn btn-primary btn-md flex items-center gap-2"
        >
          <ArrowDownToLine size={16} />
          <span>Request Payout Transfer</span>
        </button>
      </div>

      {/* Metrics Row */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard
          title="Available for Withdrawal"
          value={`₹${(summary?.available_balance || 0).toLocaleString('en-IN')}`}
          subtitle="Cleared after return window"
          variant="green"
        />
        <MetricCard
          title="Escrow Hold Balance"
          value={`₹${(summary?.held_balance || 0).toLocaleString('en-IN')}`}
          subtitle="Orders within 7-day return period"
          variant="amber"
        />
        <MetricCard
          title="Pending Bank Payouts"
          value={`₹${(summary?.pending_payout_balance || 0).toLocaleString('en-IN')}`}
          subtitle="In transit with payment gateway"
          variant="blue"
        />
        <MetricCard
          title="Lifetime Settled Revenue"
          value={`₹${(summary?.total_lifetime_settled || 0).toLocaleString('en-IN')}`}
          subtitle="Total net earnings deposited"
          variant="purple"
        />
      </div>

      {/* Batch History */}
      <div className="space-y-2">
        <h3 className="text-sm font-bold text-gray-900">Bank Settlement Batches</h3>
        <DataTable
          data={summary?.recent_batches || []}
          columns={columns}
          searchPlaceholder="Search payout batch reference..."
          searchKey="batch_reference"
          emptyMessage="No payout batches generated yet."
        />
      </div>
    </div>
  );
};
