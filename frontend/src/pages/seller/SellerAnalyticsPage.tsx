import React, { useState } from 'react';
import { TrendingUp, BarChart2, DollarSign, ShoppingCart, Percent, ArrowUpRight, ArrowDownRight, Award } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { ProgressBar } from '../../components/ui/ProgressBar';

interface TopProductPerformance {
  id: number;
  name: string;
  sku: string;
  unitsSold: number;
  grossRevenue: number;
  buyboxWinRate: number;
  returnRate: number;
}

const TOP_PRODUCTS: TopProductPerformance[] = [
  { id: 1, name: 'Apple iPhone 15 (128 GB) Black', sku: 'APL-IP15-128', unitsSold: 142, grossRevenue: 9939858, buyboxWinRate: 88, returnRate: 1.2 },
  { id: 2, name: 'Sony WH-1000XM5 ANC Headphones', sku: 'SNY-XM5-BLK', unitsSold: 89, grossRevenue: 2402110, buyboxWinRate: 94, returnRate: 2.1 },
  { id: 3, name: 'Realme GT 6T 5G (8GB/128GB)', sku: 'RME-GT6T-128', unitsSold: 215, grossRevenue: 5374785, buyboxWinRate: 72, returnRate: 3.4 },
  { id: 4, name: 'Dell XPS 13 Core i7 16GB/512GB', sku: 'DEL-XPS13-512', unitsSold: 34, grossRevenue: 4079660, buyboxWinRate: 65, returnRate: 0.8 },
];

export const SellerAnalyticsPage: React.FC = () => {
  const [timeframe, setTimeframe] = useState<'7d' | '30d' | '90d'>('30d');

  const columns: ColumnDef<TopProductPerformance>[] = [
    {
      key: 'name',
      header: 'Product / SKU',
      render: (item) => (
        <div>
          <p className="text-xs font-bold text-gray-900">{item.name}</p>
          <span className="font-mono text-[11px] text-gray-400">{item.sku}</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'unitsSold',
      header: 'Units Dispatched',
      render: (item) => <span className="text-xs font-semibold">{item.unitsSold} units</span>,
      sortable: true,
    },
    {
      key: 'grossRevenue',
      header: 'Gross GMV',
      render: (item) => <span className="text-xs font-bold text-green-700">₹{item.grossRevenue.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'buyboxWinRate',
      header: 'BuyBox Win %',
      render: (item) => (
        <div className="w-32">
          <ProgressBar
            value={item.buyboxWinRate}
            showPercentage={true}
            variant={item.buyboxWinRate >= 80 ? 'success' : 'amber'}
            height={6}
          />
        </div>
      ),
      sortable: true,
    },
    {
      key: 'returnRate',
      header: 'Return Rate %',
      render: (item) => (
        <span className={`text-xs font-semibold ${item.returnRate > 3 ? 'text-amber-600 font-bold' : 'text-green-600'}`}>
          {item.returnRate}%
        </span>
      ),
      sortable: true,
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Seller Business Analytics & BuyBox Intelligence</h1>
          <p className="text-xs text-gray-500 mt-0.5">Real-time GMV sales telemetry, conversion funnel, and listing competitiveness.</p>
        </div>

        <div className="flex items-center gap-1 bg-gray-100 p-1 rounded-lg border border-gray-200">
          {(['7d', '30d', '90d'] as const).map((tf) => (
            <button
              key={tf}
              type="button"
              className={`px-3 py-1 text-xs font-bold rounded-md transition-all ${
                timeframe === tf ? 'bg-white text-blue-600 shadow-sm' : 'text-gray-600 hover:text-gray-900'
              }`}
              onClick={() => setTimeframe(tf)}
            >
              {tf === '7d' ? 'Last 7 Days' : tf === '30d' ? 'Last 30 Days' : 'Last Quarter'}
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard
          title="Total Gross Merchandise Value"
          value="₹2,17,96,413"
          subtitle="vs previous month"
          trendPercentage={18.4}
          variant="blue"
        />
        <MetricCard
          title="Fulfillment Units"
          value="480 Orders"
          subtitle="99.2% on-time dispatch"
          trendPercentage={12.1}
          variant="green"
        />
        <MetricCard
          title="Average BuyBox Win Rate"
          value="79.8%"
          subtitle="Across 24 active catalog SKUs"
          trendPercentage={4.5}
          variant="purple"
        />
        <MetricCard
          title="Product Return Defect Rate"
          value="1.85%"
          subtitle="Target < 3.0%"
          trendPercentage={-0.4}
          variant="neutral"
        />
      </div>

      {/* Top Performing SKUs */}
      <div className="space-y-2">
        <h3 className="text-sm font-bold text-gray-900">Catalog Performance & SKU Matrix</h3>
        <DataTable
          data={TOP_PRODUCTS}
          columns={columns}
          searchPlaceholder="Search product by title or SKU..."
          searchKey="name"
        />
      </div>
    </div>
  );
};
