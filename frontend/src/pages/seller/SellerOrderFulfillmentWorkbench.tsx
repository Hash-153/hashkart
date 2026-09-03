import React, { useState } from 'react';
import { Package, Truck, Printer, CheckCircle2, AlertTriangle, Clock, Download, FileText, Check } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { Badge } from '../../components/ui/Badge';
import { useToast } from '../../components/ui/Toast';

interface FulfillmentOrderRecord {
  id: string;
  orderNumber: string;
  customerName: string;
  destinationCity: string;
  pincode: string;
  itemCount: number;
  totalValue: number;
  carrier: 'EKART' | 'DELHIVERY' | 'BLUEDART';
  dispatchDeadline: string;
  status: 'PENDING_PACKING' | 'PACKED_READY_FOR_MANIFEST' | 'MANIFESTED' | 'HANDED_TO_COURIER';
  isCod: boolean;
}

const MOCK_FULFILLMENT_ORDERS: FulfillmentOrderRecord[] = [
  { id: '1', orderNumber: 'HK-20260825-99A1', customerName: 'Rohit Sharma', destinationCity: 'Bengaluru', pincode: '560038', itemCount: 1, totalValue: 149900, carrier: 'EKART', dispatchDeadline: 'Today, 6:00 PM', status: 'PENDING_PACKING', isCod: false },
  { id: '2', orderNumber: 'HK-20260825-88B2', customerName: 'Priya Patel', destinationCity: 'Mumbai', pincode: '400050', itemCount: 2, totalValue: 26990, carrier: 'DELHIVERY', dispatchDeadline: 'Today, 7:30 PM', status: 'PACKED_READY_FOR_MANIFEST', isCod: false },
  { id: '3', orderNumber: 'HK-20260825-77C3', customerName: 'Amit Verma', destinationCity: 'New Delhi', pincode: '110001', itemCount: 1, totalValue: 38999, carrier: 'BLUEDART', dispatchDeadline: 'Tomorrow, 11:00 AM', status: 'PENDING_PACKING', isCod: true },
  { id: '4', orderNumber: 'HK-20260825-66D4', customerName: 'Ananya Reddy', destinationCity: 'Hyderabad', pincode: '500081', itemCount: 3, totalValue: 18450, carrier: 'EKART', dispatchDeadline: 'Tomorrow, 2:00 PM', status: 'MANIFESTED', isCod: false },
];

export const SellerOrderFulfillmentWorkbench: React.FC = () => {
  const { showToast } = useToast();
  const [orders, setOrders] = useState<FulfillmentOrderRecord[]>(MOCK_FULFILLMENT_ORDERS);
  const [selectedOrderIds, setSelectedOrderIds] = useState<Set<string>>(new Set());

  const toggleSelectOrder = (id: string) => {
    setSelectedOrderIds((prev) => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  const handleMarkPacked = (id: string) => {
    setOrders((prev) =>
      prev.map((o) => (o.id === id ? { ...o, status: 'PACKED_READY_FOR_MANIFEST' } : o))
    );
    showToast('success', 'Order Packed', 'Generated shipping label & moved to manifest queue.');
  };

  const handleGenerateBatchManifest = () => {
    if (selectedOrderIds.size === 0) {
      showToast('warning', 'Select Orders', 'Please select at least 1 order to generate courier manifest.');
      return;
    }
    setOrders((prev) =>
      prev.map((o) => (selectedOrderIds.has(o.id) ? { ...o, status: 'MANIFESTED' } : o))
    );
    showToast('success', 'Manifest Generated', `Batch manifest with ${selectedOrderIds.size} orders ready for driver handover.`);
    setSelectedOrderIds(new Set());
  };

  const columns: ColumnDef<FulfillmentOrderRecord>[] = [
    {
      key: 'id',
      header: 'Select',
      render: (item) => (
        <input
          type="checkbox"
          checked={selectedOrderIds.has(item.id)}
          onChange={() => toggleSelectOrder(item.id)}
          className="rounded border-gray-300 text-blue-600"
        />
      ),
    },
    {
      key: 'orderNumber',
      header: 'Order & Customer',
      render: (item) => (
        <div>
          <span className="font-mono text-xs font-bold text-gray-900">{item.orderNumber}</span>
          <p className="text-xs text-gray-600 font-medium">{item.customerName}</p>
          <span className="text-[11px] text-gray-400">{item.destinationCity} ({item.pincode})</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'totalValue',
      header: 'Value & Items',
      render: (item) => (
        <div>
          <span className="font-bold text-xs text-gray-900">₹{item.totalValue.toLocaleString('en-IN')}</span>
          <p className="text-[11px] text-gray-500">{item.itemCount} Item(s) • {item.isCod ? 'COD' : 'PREPAID'}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'carrier',
      header: 'Carrier & SLA',
      render: (item) => (
        <div>
          <span className="font-bold text-xs text-blue-700 bg-blue-50 px-2 py-0.5 rounded">{item.carrier}</span>
          <p className="text-[11px] text-amber-700 font-semibold mt-0.5">SLA: {item.dispatchDeadline}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'status',
      header: 'Fulfillment Stage',
      render: (item) => {
        const variants: Record<string, 'warning' | 'info' | 'purple' | 'success'> = {
          PENDING_PACKING: 'warning',
          PACKED_READY_FOR_MANIFEST: 'info',
          MANIFESTED: 'purple',
          HANDED_TO_COURIER: 'success',
        };
        return (
          <Badge variant={variants[item.status] || 'neutral'}>
            {item.status.replace(/_/g, ' ')}
          </Badge>
        );
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Packing Action',
      render: (item) => (
        item.status === 'PENDING_PACKING' ? (
          <button
            type="button"
            className="btn btn-primary btn-sm flex items-center gap-1 text-xs"
            onClick={() => handleMarkPacked(item.id)}
          >
            <Package size={12} />
            <span>Mark Packed</span>
          </button>
        ) : (
          <button
            type="button"
            className="btn btn-neutral btn-sm flex items-center gap-1 text-xs"
            onClick={() => showToast('info', 'Printing Label', `Printing 4x6 thermal AWB for ${item.orderNumber}`)}
          >
            <Printer size={12} />
            <span>Print Label</span>
          </button>
        )
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Order Fulfillment & Courier Handover Workbench</h1>
          <p className="text-xs text-gray-500 mt-0.5">Pick, pack, print thermal shipping labels, and generate daily carrier manifests.</p>
        </div>

        <div className="flex items-center gap-2">
          <button
            type="button"
            className="btn btn-primary btn-sm flex items-center gap-1.5"
            onClick={handleGenerateBatchManifest}
          >
            <FileText size={14} />
            <span>Generate Carrier Manifest ({selectedOrderIds.size})</span>
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Pending Packing" value="18 Orders" subtitle="SLA expiring in 2 hours" variant="amber" />
        <MetricCard title="Packed & Ready" value="34 Orders" subtitle="Awaiting driver pickup" variant="blue" />
        <MetricCard title="Dispatched Today" value="142 Orders" subtitle="100% on-time dispatch" variant="green" />
        <MetricCard title="Average Dispatch Speed" value="3.4 Hours" subtitle="Target < 6.0 Hours" variant="neutral" />
      </div>

      <DataTable
        data={orders}
        columns={columns}
        searchPlaceholder="Search order number or customer name..."
        searchKey="orderNumber"
      />
    </div>
  );
};
