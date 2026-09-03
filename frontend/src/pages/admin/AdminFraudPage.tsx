import React, { useState } from 'react';
import { ShieldAlert, ShieldCheck, UserX, AlertTriangle, Lock, Eye } from 'lucide-react';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { MetricCard } from '../../components/ui/MetricCard';
import { useToast } from '../../components/ui/Toast';

interface FraudAlertRecord {
  id: number;
  orderNumber: string;
  customerEmail: string;
  riskScore: number;
  riskBand: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  reasons: string[];
  totalAmount: number;
  status: 'PENDING_REVIEW' | 'CLEARED' | 'BLOCKED';
}

const MOCK_FRAUD_ALERTS: FraudAlertRecord[] = [
  { id: 1, orderNumber: 'HK-20260825-99A1', customerEmail: 'temp_user_891@mailinator.com', riskScore: 88, riskBand: 'CRITICAL', reasons: ['Disposable email domain', 'Velocity: 5 orders in 3 minutes', 'High value COD (\u20b985,000)'], totalAmount: 85000, status: 'PENDING_REVIEW' },
  { id: 2, orderNumber: 'HK-20260825-88B2', customerEmail: 'suspect99@gmail.com', riskScore: 72, riskBand: 'HIGH', reasons: ['Blacklisted phone number', 'Multiple card decline attempts'], totalAmount: 42999, status: 'PENDING_REVIEW' },
  { id: 3, orderNumber: 'HK-20260825-77C3', customerEmail: 'priya.s@corp.in', riskScore: 25, riskBand: 'LOW', reasons: ['Normal customer pattern'], totalAmount: 1499, status: 'CLEARED' },
];

export const AdminFraudPage: React.FC = () => {
  const { showToast } = useToast();
  const [alerts, setAlerts] = useState<FraudAlertRecord[]>(MOCK_FRAUD_ALERTS);

  const handleClear = (id: number) => {
    setAlerts((prev) =>
      prev.map((a) => (a.id === id ? { ...a, status: 'CLEARED' } : a))
    );
    showToast('success', 'Order Risk Cleared', 'Order approved for fulfillment.');
  };

  const handleBlock = (id: number) => {
    setAlerts((prev) =>
      prev.map((a) => (a.id === id ? { ...a, status: 'BLOCKED' } : a))
    );
    showToast('error', 'Order Blocked & User Blacklisted', 'Order cancelled and security profile blacklisted.');
  };

  const columns: ColumnDef<FraudAlertRecord>[] = [
    {
      key: 'orderNumber',
      header: 'Order Ref / Email',
      render: (item) => (
        <div>
          <span className="font-mono text-xs font-bold text-gray-900">#{item.orderNumber}</span>
          <p className="text-[11px] text-gray-500 font-mono">{item.customerEmail}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'riskScore',
      header: 'Risk Score & Band',
      render: (item) => {
        const colors: Record<string, string> = {
          LOW: 'bg-green-100 text-green-800',
          MEDIUM: 'bg-yellow-100 text-yellow-800',
          HIGH: 'bg-amber-100 text-amber-800',
          CRITICAL: 'bg-red-100 text-red-800',
        };
        return (
          <div className="flex items-center gap-2">
            <span className="font-black text-sm">{item.riskScore}/100</span>
            <span className={`px-2 py-0.5 rounded font-bold text-[10px] ${colors[item.riskBand]}`}>
              {item.riskBand}
            </span>
          </div>
        );
      },
      sortable: true,
    },
    {
      key: 'reasons',
      header: 'Risk Trigger Factors',
      render: (item) => (
        <div className="space-y-0.5">
          {item.reasons.map((r, i) => (
            <span key={i} className="block text-[11px] text-red-700 bg-red-50/50 px-1.5 py-0.5 rounded">
              • {r}
            </span>
          ))}
        </div>
      ),
    },
    {
      key: 'totalAmount',
      header: 'Order Value',
      render: (item) => <span className="font-bold text-xs">₹{item.totalAmount.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'status',
      header: 'Action / Decision',
      render: (item) => (
        item.status === 'PENDING_REVIEW' ? (
          <div className="flex items-center gap-2">
            <button
              type="button"
              className="btn btn-primary btn-sm flex items-center gap-1"
              onClick={() => handleClear(item.id)}
            >
              <ShieldCheck size={12} />
              <span>Allow</span>
            </button>
            <button
              type="button"
              className="btn btn-danger btn-sm flex items-center gap-1"
              onClick={() => handleBlock(item.id)}
            >
              <UserX size={12} />
              <span>Block</span>
            </button>
          </div>
        ) : (
          <span className={`px-2 py-0.5 rounded text-[11px] font-semibold ${
            item.status === 'CLEARED' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
          }`}>
            {item.status}
          </span>
        )
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div>
        <h1 className="text-xl font-bold text-gray-900">Fraud Prevention & COD Risk Security Control</h1>
        <p className="text-xs text-gray-500 mt-0.5">Velocity anomaly detection, blacklist enforcement, high-value COD gating, and account integrity auditing.</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="High Risk Suspicious Orders" value="2 Orders" subtitle="Requires manual approval" variant="amber" />
        <MetricCard title="Auto-Blocked Fraud" value="47 Blocked" subtitle="Saved ₹3,85,000 this week" variant="blue" />
        <MetricCard title="Blacklisted Entities" value="128 Records" subtitle="Phones, emails, device hashes" variant="neutral" />
        <MetricCard title="COD Chargeback Risk" value="0.42%" subtitle="Below 1.5% target ceiling" variant="green" />
      </div>

      <DataTable
        data={alerts}
        columns={columns}
        searchPlaceholder="Search by order or email..."
        searchKey="customerEmail"
      />
    </div>
  );
};
