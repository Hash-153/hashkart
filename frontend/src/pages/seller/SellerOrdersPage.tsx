import React, { useState } from 'react';
import { Truck, CheckCircle2, Clock, Printer, PackageCheck } from 'lucide-react';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { useToast } from '../../components/ui/Toast';

interface SellerOrder {
  id: number;
  orderNumber: string;
  customerName: string;
  city: string;
  itemCount: number;
  grossAmount: number;
  netSellerPayout: number;
  status: 'PENDING_PACK' | 'READY_FOR_PICKUP' | 'SHIPPED' | 'DELIVERED';
  orderDate: string;
}

const MOCK_ORDERS: SellerOrder[] = [
  { id: 1, orderNumber: 'HK-20260825-9A8B1C', customerName: 'Rahul Verma', city: 'Bengaluru', itemCount: 2, grossAmount: 14998, netSellerPayout: 13948, status: 'PENDING_PACK', orderDate: 'Today, 2:15 PM' },
  { id: 2, orderNumber: 'HK-20260825-3F4D2E', customerName: 'Priya Nair', city: 'Kochi', itemCount: 1, grossAmount: 69999, netSellerPayout: 65099, status: 'READY_FOR_PICKUP', orderDate: 'Today, 11:30 AM' },
  { id: 3, orderNumber: 'HK-20260824-7B1C9D', customerName: 'Amit Sharma', city: 'New Delhi', itemCount: 3, grossAmount: 4599, netSellerPayout: 4277, status: 'SHIPPED', orderDate: 'Yesterday' },
  { id: 4, orderNumber: 'HK-20260823-5A2C8F', customerName: 'Ananya Roy', city: 'Kolkata', itemCount: 1, grossAmount: 26990, netSellerPayout: 25100, status: 'DELIVERED', orderDate: '23 Aug 2026' },
];

export const SellerOrdersPage: React.FC = () => {
  const { showToast } = useToast();
  const [orders, setOrders] = useState<SellerOrder[]>(MOCK_ORDERS);

  const handleMarkPacked = (id: number) => {
    setOrders((prev) =>
      prev.map((o) => (o.id === id ? { ...o, status: 'READY_FOR_PICKUP' } : o))
    );
    showToast('success', 'Order Packed', 'Shipping label generated & queued for courier pickup.');
  };

  const columns: ColumnDef<SellerOrder>[] = [
    {
      key: 'orderNumber',
      header: 'Order Ref / Date',
      render: (item) => (
        <div>
          <span className="font-mono text-xs font-bold text-gray-900">{item.orderNumber}</span>
          <p className="text-[11px] text-gray-400">{item.orderDate}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'customerName',
      header: 'Customer / Destination',
      render: (item) => (
        <div>
          <p className="text-xs font-semibold text-gray-900">{item.customerName}</p>
          <span className="text-[11px] text-gray-500">{item.city}</span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'grossAmount',
      header: 'Amount / Payout',
      render: (item) => (
        <div>
          <span className="text-xs font-bold">₹{item.grossAmount.toLocaleString('en-IN')}</span>
          <p className="text-[11px] text-green-700 font-medium">
            Est. Payout: ₹{item.netSellerPayout.toLocaleString('en-IN')}
          </p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'status',
      header: 'Fulfillment Status',
      render: (item) => {
        const badges: Record<string, { label: string; color: string }> = {
          PENDING_PACK: { label: 'Needs Packing', color: 'bg-amber-100 text-amber-800' },
          READY_FOR_PICKUP: { label: 'Ready for Courier', color: 'bg-blue-100 text-blue-800' },
          SHIPPED: { label: 'In Transit', color: 'bg-purple-100 text-purple-800' },
          DELIVERED: { label: 'Delivered', color: 'bg-green-100 text-green-800' },
        };
        const b = badges[item.status] || { label: item.status, color: 'bg-gray-100 text-gray-800' };
        return <span className={`px-2 py-0.5 rounded font-semibold text-[11px] ${b.color}`}>{b.label}</span>;
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Dispatch Action',
      render: (item) => (
        <div className="flex items-center gap-2">
          {item.status === 'PENDING_PACK' ? (
            <button
              type="button"
              className="btn btn-primary btn-sm flex items-center gap-1"
              onClick={() => handleMarkPacked(item.id)}
            >
              <PackageCheck size={12} />
              <span>Mark Packed</span>
            </button>
          ) : (
            <button
              type="button"
              className="btn btn-neutral btn-sm flex items-center gap-1 text-gray-600"
              onClick={() => showToast('info', 'Print Label', 'Thermal shipping label sent to printer.')}
            >
              <Printer size={12} />
              <span>Print AWB</span>
            </button>
          )}
        </div>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div>
        <h1 className="text-xl font-bold text-gray-900">Seller Order Dispatch Center</h1>
        <p className="text-xs text-gray-500 mt-0.5">Manage customer shipments, print barcoded shipping labels, and track delivery SLA.</p>
      </div>

      <DataTable
        data={orders}
        columns={columns}
        searchPlaceholder="Search order number or customer..."
        searchKey="orderNumber"
      />
    </div>
  );
};
