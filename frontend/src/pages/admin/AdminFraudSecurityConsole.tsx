import React, { useState } from 'react';
import { ShieldAlert, AlertOctagon, UserX, MapPin, Zap, Lock, Unlock, Eye, CheckCircle2 } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { Badge } from '../../components/ui/Badge';
import { useToast } from '../../components/ui/Toast';

interface SuspiciousActivityRecord {
  id: string;
  userId: number;
  customerName: string;
  email: string;
  orderNumber: string;
  orderAmount: number;
  paymentMethod: string;
  ipAddress: string;
  riskScore: number; // 0 to 100
  riskLevel: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL_BLOCK';
  triggeredRules: string[];
  status: 'PENDING_REVIEW' | 'AUTO_BLOCKED' | 'CLEARED_LEGITIMATE';
}

const MOCK_SUSPICIOUS_ACTIVITIES: SuspiciousActivityRecord[] = [
  { id: '1', userId: 8812, customerName: 'Unknown Guest', email: 'temp_user_891@mailinator.com', orderNumber: 'HK-20260825-99X0', orderAmount: 48900, paymentMethod: 'COD', ipAddress: '185.220.101.5', riskScore: 92, riskLevel: 'CRITICAL_BLOCK', triggeredRules: ['Disposable email domain (@mailinator)', 'High-value COD (>₹25k)', 'Tor Exit Node IP'], status: 'AUTO_BLOCKED' },
  { id: '2', userId: 4410, customerName: 'Vikram Seth', email: 'vikram.seth91@gmail.com', orderNumber: 'HK-20260825-77Y1', orderAmount: 149900, paymentMethod: 'CREDIT_CARD', ipAddress: '103.21.244.2', riskScore: 68, riskLevel: 'HIGH', triggeredRules: ['Impossible travel velocity (Mumbai to London in 10 mins)', 'New device fingerprint'], status: 'PENDING_REVIEW' },
  { id: '3', userId: 1209, customerName: 'Karan Mehra', email: 'karan.m@rediffmail.com', orderNumber: 'HK-20260825-55Z2', orderAmount: 3200, paymentMethod: 'COD', ipAddress: '49.36.128.9', riskScore: 42, riskLevel: 'MEDIUM', triggeredRules: ['Past order cancellation rate > 60%'], status: 'PENDING_REVIEW' },
];

export const AdminFraudSecurityConsole: React.FC = () => {
  const { showToast } = useToast();
  const [activities, setActivities] = useState<SuspiciousActivityRecord[]>(MOCK_SUSPICIOUS_ACTIVITIES);

  const handleClearActivity = (id: string) => {
    setActivities((prev) =>
      prev.map((a) => (a.id === id ? { ...a, status: 'CLEARED_LEGITIMATE' } : a))
    );
    showToast('success', 'Risk Cleared', 'User and transaction marked legitimate.');
  };

  const handleBlockUser = (id: string) => {
    setActivities((prev) =>
      prev.map((a) => (a.id === id ? { ...a, status: 'AUTO_BLOCKED' } : a))
    );
    showToast('danger', 'User Blacklisted', 'Permanently suspended device fingerprint & account.');
  };

  const columns: ColumnDef<SuspiciousActivityRecord>[] = [
    {
      key: 'customerName',
      header: 'Customer & Risk Score',
      render: (item) => (
        <div>
          <div className="flex items-center gap-2">
            <span className="font-bold text-xs text-gray-900">{item.customerName}</span>
            <span className={`text-[11px] font-black px-1.5 py-0.2 rounded ${item.riskScore >= 75 ? 'bg-red-100 text-red-700' : 'bg-amber-100 text-amber-700'}`}>
              Risk: {item.riskScore}/100
            </span>
          </div>
          <p className="text-[11px] text-gray-500">{item.email}</p>
          <span className="text-[10px] font-mono text-gray-400">IP: {item.ipAddress}</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'orderNumber',
      header: 'Order & Amount',
      render: (item) => (
        <div>
          <span className="font-mono text-xs font-bold text-gray-900">{item.orderNumber}</span>
          <p className="text-xs font-bold text-gray-700">₹{item.orderAmount.toLocaleString('en-IN')}</p>
          <span className="text-[10px] text-blue-700 font-semibold">{item.paymentMethod}</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'triggeredRules',
      header: 'Risk Factors Triggered',
      render: (item) => (
        <div className="space-y-1 max-w-xs">
          {item.triggeredRules.map((r, i) => (
            <span key={i} className="block text-[11px] bg-red-50 text-red-700 font-medium px-2 py-0.5 rounded border border-red-100">
              ⚠️ {r}
            </span>
          ))}
        </div>
      ),
    },
    {
      key: 'status',
      header: 'Enforcement Status',
      render: (item) => {
        const variants: Record<string, 'danger' | 'warning' | 'success'> = {
          AUTO_BLOCKED: 'danger',
          PENDING_REVIEW: 'warning',
          CLEARED_LEGITIMATE: 'success',
        };
        return <Badge variant={variants[item.status] || 'neutral'}>{item.status.replace(/_/g, ' ')}</Badge>;
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'SRE Action',
      render: (item) => (
        <div className="flex items-center gap-1.5">
          {item.status !== 'AUTO_BLOCKED' && (
            <button
              type="button"
              className="btn btn-danger btn-sm text-xs px-2 py-1"
              onClick={() => handleBlockUser(item.id)}
            >
              Block User
            </button>
          )}
          {item.status !== 'CLEARED_LEGITIMATE' && (
            <button
              type="button"
              className="btn btn-neutral btn-sm text-xs px-2 py-1"
              onClick={() => handleClearActivity(item.id)}
            >
              Clear
            </button>
          )}
        </div>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Fraud Security Sentinel & Risk Control Console</h1>
          <p className="text-xs text-gray-500 mt-0.5">Real-time heuristics, device fingerprinting, ATO defense, and COD gatekeeper.</p>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Transactions Screened" value="48,210" subtitle="Last 24 hours" variant="blue" />
        <MetricCard title="High-Risk Flagged" value="14 Events" subtitle="Under active SRE triage" variant="amber" />
        <MetricCard title="Auto-Blocked Fraud" value="₹14,50,000" subtitle="Prevented chargeback loss" variant="danger" />
        <MetricCard title="False Positive Rate" value="0.04%" subtitle="Industry standard < 0.1%" variant="green" />
      </div>

      <DataTable
        data={activities}
        columns={columns}
        searchPlaceholder="Search by customer email or order number..."
        searchKey="email"
      />
    </div>
  );
};
