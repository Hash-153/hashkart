import React, { useState } from 'react';
import { Warehouse, Truck, Package, QrCode, FileText, CheckCircle2 } from 'lucide-react';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { MetricCard } from '../../components/ui/MetricCard';
import { useToast } from '../../components/ui/Toast';

interface ManifestItem {
  id: number;
  manifestNumber: string;
  carrier: string;
  packages: number;
  weightKg: number;
  driverName: string;
  vehicleNo: string;
  status: 'READY' | 'HANDED_OVER' | 'IN_TRANSIT';
  time: string;
}

const MOCK_MANIFESTS: ManifestItem[] = [
  { id: 1, manifestNumber: 'MNF-EKA-20260825-01', carrier: 'EKART Logistics', packages: 28, weightKg: 14.5, driverName: 'Sunil Gowda', vehicleNo: 'KA-01-MJ-8821', status: 'READY', time: '14:30' },
  { id: 2, manifestNumber: 'MNF-DEL-20260825-02', carrier: 'Delhivery Surface', packages: 45, weightKg: 32.0, driverName: 'Rajesh Khan', vehicleNo: 'DL-04-AB-1922', status: 'HANDED_OVER', time: '12:15' },
  { id: 3, manifestNumber: 'MNF-BLU-20260825-03', carrier: 'BlueDart Air Express', packages: 12, weightKg: 8.2, driverName: 'Manish Pandey', vehicleNo: 'MH-02-CD-4511', status: 'IN_TRANSIT', time: '10:00' },
];

export const AdminWMSPage: React.FC = () => {
  const { showToast } = useToast();
  const [manifests, setManifests] = useState<ManifestItem[]>(MOCK_MANIFESTS);

  const handleHandover = (id: number) => {
    setManifests((prev) =>
      prev.map((m) => (m.id === id ? { ...m, status: 'HANDED_OVER' } : m))
    );
    showToast('success', 'Carrier Handover Recorded', 'Dispatch manifest confirmed with driver digital signature.');
  };

  const columns: ColumnDef<ManifestItem>[] = [
    {
      key: 'manifestNumber',
      header: 'Manifest Number',
      render: (item) => <span className="font-mono text-xs font-bold text-gray-900">{item.manifestNumber}</span>,
      sortable: true,
    },
    {
      key: 'carrier',
      header: '3PL Carrier Partner',
      render: (item) => <span className="text-xs font-semibold text-gray-800">{item.carrier}</span>,
      sortable: true,
    },
    {
      key: 'packages',
      header: 'Packages / Weight',
      render: (item) => (
        <span className="text-xs font-medium">
          {item.packages} Bags ({item.weightKg} kg)
        </span>
      ),
      sortable: true,
    },
    {
      key: 'driverName',
      header: 'Driver / Vehicle No.',
      render: (item) => (
        <div>
          <p className="text-xs font-semibold text-gray-900">{item.driverName}</p>
          <span className="font-mono text-[11px] text-gray-400">{item.vehicleNo}</span>
        </div>
      ),
    },
    {
      key: 'status',
      header: 'Handover Status',
      render: (item) => {
        if (item.status === 'READY') {
          return <span className="px-2 py-0.5 bg-blue-100 text-blue-800 rounded font-semibold text-[11px]">Ready for Pickup</span>;
        }
        if (item.status === 'HANDED_OVER') {
          return <span className="px-2 py-0.5 bg-green-100 text-green-800 rounded font-semibold text-[11px]">Handed Over</span>;
        }
        return <span className="px-2 py-0.5 bg-purple-100 text-purple-800 rounded font-semibold text-[11px]">In Transit</span>;
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Floor Action',
      render: (item) => (
        item.status === 'READY' ? (
          <button
            type="button"
            className="btn btn-primary btn-sm flex items-center gap-1"
            onClick={() => handleHandover(item.id)}
          >
            <CheckCircle2 size={12} />
            <span>Confirm Handover</span>
          </button>
        ) : (
          <span className="text-xs text-gray-400">Completed</span>
        )
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div>
        <h1 className="text-xl font-bold text-gray-900">Warehouse Management (WMS) & Logistics Tower</h1>
        <p className="text-xs text-gray-500 mt-0.5">Floor receiving, barcode scanning, outbound dock dispatch manifests, and 3PL carrier coordination.</p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Dock Outbound Packages" value="85 Packages" subtitle="Scheduled for today's pickup" variant="blue" />
        <MetricCard title="Active 3PL Fleet Carriers" value="4 Carriers" subtitle="Ekart, Delhivery, BlueDart, Ecom" variant="green" />
        <MetricCard title="Pending Inbound Receipts" value="18 Inbounds" subtitle="Awaiting dock inspection" variant="amber" />
        <MetricCard title="Dispatch SLA Health" value="99.4%" subtitle="0 Breached manifests today" variant="purple" />
      </div>

      <div className="space-y-2">
        <h3 className="text-sm font-bold text-gray-900">Daily Carrier Dispatch Manifests</h3>
        <DataTable
          data={manifests}
          columns={columns}
          searchPlaceholder="Search manifest or carrier..."
          searchKey="carrier"
        />
      </div>
    </div>
  );
};
