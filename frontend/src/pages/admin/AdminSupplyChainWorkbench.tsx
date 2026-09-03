import React, { useState } from 'react';
import { Warehouse, TrendingUp, AlertTriangle, Truck, MapPin, Layers, RefreshCw, BarChart2, CheckCircle2 } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { Badge } from '../../components/ui/Badge';
import { useToast } from '../../components/ui/Toast';

interface SupplyChainFCRecord {
  fcId: string;
  facilityName: string;
  city: string;
  state: string;
  totalCapacitySqFt: number;
  utilizationPercent: number;
  inboundUnitsPending: number;
  outboundUnitsPending: number;
  activeDockDoors: number;
  status: 'OPTIMAL' | 'HIGH_LOAD' | 'CONGESTED';
}

const MOCK_FCS: SupplyChainFCRecord[] = [
  { fcId: 'FC-BLR-01', facilityName: 'Bengaluru South Mega Hub (Whitefield)', city: 'Bengaluru', state: 'Karnataka', totalCapacitySqFt: 500000, utilizationPercent: 78, inboundUnitsPending: 12400, outboundUnitsPending: 8900, activeDockDoors: 18, status: 'OPTIMAL' },
  { fcId: 'FC-BOM-02', facilityName: 'Bhiwandi Western Gateway Hub', city: 'Mumbai', state: 'Maharashtra', totalCapacitySqFt: 750000, utilizationPercent: 91, inboundUnitsPending: 34000, outboundUnitsPending: 22000, activeDockDoors: 24, status: 'HIGH_LOAD' },
  { fcId: 'FC-DEL-01', facilityName: 'Gurugram Northern Fulfillment Center', city: 'Delhi NCR', state: 'Haryana', totalCapacitySqFt: 600000, utilizationPercent: 84, inboundUnitsPending: 18000, outboundUnitsPending: 14500, activeDockDoors: 20, status: 'OPTIMAL' },
  { fcId: 'FC-HYD-01', facilityName: 'Shamshabad Air-Cargo Connected Hub', city: 'Hyderabad', state: 'Telangana', totalCapacitySqFt: 400000, utilizationPercent: 65, inboundUnitsPending: 8500, outboundUnitsPending: 6100, activeDockDoors: 12, status: 'OPTIMAL' },
  { fcId: 'FC-CCU-01', facilityName: 'Dankuni Eastern Mother Hub', city: 'Kolkata', state: 'West Bengal', totalCapacitySqFt: 350000, utilizationPercent: 94, inboundUnitsPending: 28000, outboundUnitsPending: 19000, activeDockDoors: 14, status: 'CONGESTED' },
];

export const AdminSupplyChainWorkbench: React.FC = () => {
  const { showToast } = useToast();
  const [fcs, setFcs] = useState<SupplyChainFCRecord[]>(MOCK_FCS);

  const columns: ColumnDef<SupplyChainFCRecord>[] = [
    {
      key: 'facilityName',
      header: 'Fulfillment Center & Location',
      render: (item) => (
        <div>
          <div className="flex items-center gap-2">
            <span className="font-bold text-xs text-gray-900">{item.facilityName}</span>
            <span className="text-[10px] font-mono font-bold bg-blue-50 text-blue-700 px-1.5 py-0.2 rounded">{item.fcId}</span>
          </div>
          <span className="text-[11px] text-gray-500">{item.city}, {item.state} • {item.totalCapacitySqFt.toLocaleString('en-IN')} sq.ft</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'utilizationPercent',
      header: 'Floor Space Utilization',
      render: (item) => (
        <div>
          <div className="flex items-center justify-between text-xs mb-1">
            <span className="font-bold text-gray-800">{item.utilizationPercent}%</span>
            <span className="text-[10px] text-gray-400">{item.activeDockDoors} Docks Live</span>
          </div>
          <div className="w-32 h-2 bg-gray-100 rounded-full overflow-hidden">
            <div
              className={`h-full ${item.utilizationPercent >= 90 ? 'bg-red-500' : item.utilizationPercent >= 80 ? 'bg-amber-500' : 'bg-green-500'}`}
              style={{ width: `${item.utilizationPercent}%` }}
            />
          </div>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'inboundUnitsPending',
      header: 'Inbound / Outbound Load',
      render: (item) => (
        <div className="text-xs">
          <p className="font-semibold text-blue-700">↓ {item.inboundUnitsPending.toLocaleString('en-IN')} Inbound</p>
          <p className="font-semibold text-emerald-700">↑ {item.outboundUnitsPending.toLocaleString('en-IN')} Outbound</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'status',
      header: 'Facility Health',
      render: (item) => {
        const variants: Record<string, 'success' | 'warning' | 'danger'> = {
          OPTIMAL: 'success',
          HIGH_LOAD: 'warning',
          CONGESTED: 'danger',
        };
        return <Badge variant={variants[item.status] || 'neutral'}>{item.status.replace(/_/g, ' ')}</Badge>;
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Load Balancing',
      render: (item) => (
        <button
          type="button"
          className="btn btn-neutral btn-sm text-xs"
          onClick={() => showToast('info', 'Rerouting Orders', `Rerouted 2,500 postal volume from ${item.fcId}`)}
        >
          Reroute Traffic
        </button>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">National Supply Chain & FC Load Balancing Workbench</h1>
          <p className="text-xs text-gray-500 mt-0.5">Real-time floor capacity, dock door scheduling, and cross-docking linehaul optimization.</p>
        </div>

        <button
          type="button"
          className="btn btn-primary btn-sm flex items-center gap-1.5"
          onClick={() => showToast('success', 'Topology Refreshed', 'Synced all national mother hubs.')}
        >
          <RefreshCw size={14} />
          <span>Refresh Network Topology</span>
        </button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Total National Warehousing" value="2.6 Million sq.ft" subtitle="Across 5 mother hubs" variant="blue" />
        <MetricCard title="Active Inbound Shipments" value="1,00,900 Units" subtitle="Receiving at dock doors" variant="green" />
        <MetricCard title="Dispatched Today" value="70,500 Units" subtitle="100% SLA compliance" variant="purple" />
        <MetricCard title="Critical Congestion Alerts" value="1 Hub (Kolkata)" subtitle="Rerouting recommended" variant="danger" />
      </div>

      <DataTable
        data={fcs}
        columns={columns}
        searchPlaceholder="Search fulfillment centers..."
        searchKey="facilityName"
      />
    </div>
  );
};
