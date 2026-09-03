import React, { useState } from 'react';
import { Split, TrendingUp, CheckCircle2, AlertCircle, Plus, Play, Pause, BarChart2 } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { useToast } from '../../components/ui/Toast';

interface ABExperimentRecord {
  id: string;
  name: string;
  metric: string;
  controlConversionRate: number;
  variantConversionRate: number;
  upliftPercentage: number;
  sampleSize: number;
  isSignificant: boolean;
  status: 'RUNNING' | 'CONCLUDED';
}

const MOCK_EXPERIMENTS: ABExperimentRecord[] = [
  { id: 'exp_checkout_1click', name: '1-Click Checkout Drawer vs Full Page', metric: 'Checkout Conversion Rate', controlConversionRate: 4.8, variantConversionRate: 6.2, upliftPercentage: 29.1, sampleSize: 18400, isSignificant: true, status: 'RUNNING' },
  { id: 'exp_pdp_sticky_bar', name: 'Sticky Mobile Add-to-Cart Bar', metric: 'Add to Cart Rate', controlConversionRate: 12.1, variantConversionRate: 14.5, upliftPercentage: 19.8, sampleSize: 25600, isSignificant: true, status: 'RUNNING' },
  { id: 'exp_supercoin_banner', name: 'SuperCoin Savings Highlight on Search', metric: 'Search Click-Through Rate', controlConversionRate: 8.2, variantConversionRate: 8.4, upliftPercentage: 2.4, sampleSize: 32000, isSignificant: false, status: 'RUNNING' },
];

export const AdminABTestingPage: React.FC = () => {
  const { showToast } = useToast();
  const [experiments] = useState<ABExperimentRecord[]>(MOCK_EXPERIMENTS);

  const columns: ColumnDef<ABExperimentRecord>[] = [
    {
      key: 'name',
      header: 'Experiment & Target Metric',
      render: (item) => (
        <div>
          <p className="text-xs font-bold text-gray-900">{item.name}</p>
          <span className="text-[11px] text-gray-400">{item.metric}</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'controlConversionRate',
      header: 'Control CVR',
      render: (item) => <span className="text-xs font-semibold text-gray-600">{item.controlConversionRate}%</span>,
    },
    {
      key: 'variantConversionRate',
      header: 'Variant CVR',
      render: (item) => <span className="text-xs font-bold text-blue-700">{item.variantConversionRate}%</span>,
    },
    {
      key: 'upliftPercentage',
      header: 'Observed Uplift',
      render: (item) => (
        <span className={`text-xs font-bold ${item.upliftPercentage > 0 ? 'text-green-700' : 'text-red-600'}`}>
          +{item.upliftPercentage}%
        </span>
      ),
      sortable: true,
    },
    {
      key: 'isSignificant',
      header: 'Significance (p < 0.05)',
      render: (item) => (
        item.isSignificant ? (
          <span className="px-2 py-0.5 bg-green-100 text-green-800 text-[10px] font-bold rounded-full">
            95% Confidence (Winner)
          </span>
        ) : (
          <span className="px-2 py-0.5 bg-gray-100 text-gray-600 text-[10px] font-semibold rounded-full">
            Gathering Data
          </span>
        )
      ),
    },
    {
      key: 'actions',
      header: 'Action',
      render: (item) => (
        <button
          type="button"
          className="btn btn-neutral btn-sm"
          onClick={() => showToast('success', 'Variant Rolled Out', `100% traffic routed to winning variant in ${item.name}.`)}
        >
          Roll Out
        </button>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">A/B Testing & Feature Experimentation Lab</h1>
          <p className="text-xs text-gray-500 mt-0.5">Statistically rigorous cohort experiment launcher with automatic conversion uplift detection.</p>
        </div>

        <button
          type="button"
          className="btn btn-primary btn-sm flex items-center gap-1.5"
          onClick={() => showToast('info', 'New Experiment', 'Experiment wizard initialized.')}
        >
          <Plus size={14} />
          <span>Launch New Experiment</span>
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Active Experiments" value="3 Running" subtitle="Testing checkout & search" variant="blue" />
        <MetricCard title="Average Platform Uplift" value="+17.1%" subtitle="Across concluded winners" variant="green" />
        <MetricCard title="Total Experiment Traffic" value="76,000 Visitors" subtitle="Evenly split cohorts" variant="purple" />
        <MetricCard title="SRM Health Check" value="100% Pass" subtitle="Zero sample ratio mismatch" variant="neutral" />
      </div>

      <DataTable
        data={experiments}
        columns={columns}
        searchPlaceholder="Search experiment name..."
        searchKey="name"
      />
    </div>
  );
};
