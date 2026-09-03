import React, { useState } from 'react';
import { Target, TrendingUp, DollarSign, Eye, MousePointer, Plus, CheckCircle2, Play, Pause } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { useToast } from '../../components/ui/Toast';

interface AdCampaignRow {
  id: number;
  name: string;
  targetKeyword: string;
  dailyBudget: number;
  totalSpent: number;
  impressions: number;
  clicks: number;
  roas: number;
  status: 'ACTIVE' | 'PAUSED';
}

const MOCK_CAMPAIGNS: AdCampaignRow[] = [
  { id: 1, name: 'iPhone 15 Festivity Push', targetKeyword: 'iphone 15, apple phone', dailyBudget: 2500, totalSpent: 1840, impressions: 48500, clicks: 1420, roas: 5.4, status: 'ACTIVE' },
  { id: 2, name: 'Sony XM5 ANC Spotlight', targetKeyword: 'noise cancelling headphones, sony', dailyBudget: 1500, totalSpent: 1200, impressions: 29100, clicks: 890, roas: 6.2, status: 'ACTIVE' },
  { id: 3, name: 'Realme GT 6T Monsoon Blitz', targetKeyword: '5g smartphone under 30k', dailyBudget: 3000, totalSpent: 3000, impressions: 64200, clicks: 2150, roas: 4.8, status: 'PAUSED' },
];

export const SellerAdvertisingPage: React.FC = () => {
  const { showToast } = useToast();
  const [campaigns, setCampaigns] = useState<AdCampaignRow[]>(MOCK_CAMPAIGNS);

  const toggleCampaign = (id: number) => {
    setCampaigns((prev) =>
      prev.map((c) => (c.id === id ? { ...c, status: c.status === 'ACTIVE' ? 'PAUSED' : 'ACTIVE' } : c))
    );
    showToast('info', 'Campaign Updated', 'Ad campaign status updated.');
  };

  const columns: ColumnDef<AdCampaignRow>[] = [
    {
      key: 'name',
      header: 'Campaign & Keywords',
      render: (item) => (
        <div>
          <p className="text-xs font-bold text-gray-900">{item.name}</p>
          <span className="font-mono text-[11px] text-gray-400">{item.targetKeyword}</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'impressions',
      header: 'Impressions',
      render: (item) => <span className="text-xs font-semibold">{item.impressions.toLocaleString()} views</span>,
      sortable: true,
    },
    {
      key: 'clicks',
      header: 'Clicks (CTR)',
      render: (item) => (
        <div>
          <span className="text-xs font-bold text-gray-900">{item.clicks}</span>
          <span className="text-[11px] text-gray-400 ml-1">({((item.clicks / item.impressions) * 100).toFixed(2)}%)</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'totalSpent',
      header: 'Spend / Budget',
      render: (item) => (
        <span className="text-xs text-gray-700 font-medium">
          ₹{item.totalSpent.toLocaleString('en-IN')} / ₹{item.dailyBudget.toLocaleString('en-IN')}
        </span>
      ),
      sortable: true,
    },
    {
      key: 'roas',
      header: 'ROAS',
      render: (item) => <span className="text-xs font-black text-green-700">{item.roas}x</span>,
      sortable: true,
    },
    {
      key: 'status',
      header: 'Status',
      render: (item) => (
        <button
          type="button"
          className={`px-2 py-0.5 text-[11px] font-bold rounded-full flex items-center gap-1 ${
            item.status === 'ACTIVE' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'
          }`}
          onClick={() => toggleCampaign(item.id)}
        >
          {item.status === 'ACTIVE' ? <Play size={10} /> : <Pause size={10} />}
          <span>{item.status}</span>
        </button>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Sponsored Product Ads & CPC Bidding Console</h1>
          <p className="text-xs text-gray-500 mt-0.5">Bid on high-intent buyer search queries to maximize catalog visibility and sales velocity.</p>
        </div>

        <button
          type="button"
          className="btn btn-primary btn-sm flex items-center gap-1.5"
          onClick={() => showToast('info', 'New Campaign', 'Campaign creation wizard opened.')}
        >
          <Plus size={14} />
          <span>Create Ad Campaign</span>
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Total Ad Revenue" value="₹32,60,000" subtitle="Attributed gross sales" variant="green" />
        <MetricCard title="Return on Ad Spend" value="5.62x" subtitle="Target > 4.0x" variant="purple" />
        <MetricCard title="Total Impressions" value="141.8K" subtitle="Top of Search + PDP" variant="blue" />
        <MetricCard title="Average Cost-Per-Click" value="₹1.35" subtitle="GSP second-price auction" variant="neutral" />
      </div>

      <DataTable
        data={campaigns}
        columns={columns}
        searchPlaceholder="Search campaigns or keywords..."
        searchKey="name"
      />
    </div>
  );
};
