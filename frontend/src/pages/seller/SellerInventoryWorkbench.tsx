import React, { useState } from 'react';
import { Package, Search, Plus, RefreshCw, Edit3, Check, AlertCircle, TrendingDown, Layers, Filter } from 'lucide-react';
import { MetricCard } from '../../components/ui/MetricCard';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { Badge } from '../../components/ui/Badge';
import { Modal } from '../../components/ui/Modal';
import { useToast } from '../../components/ui/Toast';

interface SKUInventoryItem {
  id: number;
  sku: string;
  title: string;
  category: string;
  sellingPrice: number;
  mrp: number;
  stockAvailable: number;
  stockReserved: number;
  reorderThreshold: number;
  status: 'IN_STOCK' | 'LOW_STOCK' | 'OUT_OF_STOCK';
  fulfillmentType: 'NOVAMART_FULFILLED' | 'SELLER_FULFILLED';
}

const INITIAL_SKUS: SKUInventoryItem[] = [
  { id: 1, sku: 'APL-IP15PM-256-NT', title: 'Apple iPhone 15 Pro Max (256 GB) Natural Titanium', category: 'Smartphones', sellingPrice: 149900, mrp: 159900, stockAvailable: 45, stockReserved: 3, reorderThreshold: 10, status: 'IN_STOCK', fulfillmentType: 'NOVAMART_FULFILLED' },
  { id: 2, sku: 'SNY-XM5-BLK', title: 'Sony WH-1000XM5 ANC Wireless Headphones (Black)', category: 'Audio', sellingPrice: 26990, mrp: 34990, stockAvailable: 8, stockReserved: 2, reorderThreshold: 15, status: 'LOW_STOCK', fulfillmentType: 'NOVAMART_FULFILLED' },
  { id: 3, sku: 'SAM-S24U-512', title: 'Samsung Galaxy S24 Ultra 5G (512 GB) Titanium Gray', category: 'Smartphones', sellingPrice: 139999, mrp: 149999, stockAvailable: 22, stockReserved: 1, reorderThreshold: 8, status: 'IN_STOCK', fulfillmentType: 'NOVAMART_FULFILLED' },
  { id: 4, sku: 'DEL-XPS15-9530', title: 'Dell XPS 15 9530 Core i9 13th Gen (32GB / 1TB)', category: 'Laptops', sellingPrice: 269990, mrp: 299990, stockAvailable: 0, stockReserved: 0, reorderThreshold: 5, status: 'OUT_OF_STOCK', fulfillmentType: 'SELLER_FULFILLED' },
  { id: 5, sku: 'RME-GT6-256', title: 'Realme GT 6 5G (12GB / 256GB) Fluid Silver', category: 'Smartphones', sellingPrice: 38999, mrp: 44999, stockAvailable: 95, stockReserved: 12, reorderThreshold: 20, status: 'IN_STOCK', fulfillmentType: 'SELLER_FULFILLED' },
];

export const SellerInventoryWorkbench: React.FC = () => {
  const { showToast } = useToast();
  const [items, setItems] = useState<SKUInventoryItem[]>(INITIAL_SKUS);
  const [editingItem, setEditingItem] = useState<SKUInventoryItem | null>(null);
  const [newStock, setNewStock] = useState<number>(0);
  const [newPrice, setNewPrice] = useState<number>(0);

  const handleOpenEdit = (item: SKUInventoryItem) => {
    setEditingItem(item);
    setNewStock(item.stockAvailable);
    setNewPrice(item.sellingPrice);
  };

  const handleSaveEdit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!editingItem) return;

    setItems((prev) =>
      prev.map((i) =>
        i.id === editingItem.id
          ? {
              ...i,
              stockAvailable: newStock,
              sellingPrice: newPrice,
              status: newStock === 0 ? 'OUT_OF_STOCK' : newStock <= i.reorderThreshold ? 'LOW_STOCK' : 'IN_STOCK',
            }
          : i
      )
    );
    showToast('success', 'SKU Updated', `Updated stock and pricing for ${editingItem.sku}.`);
    setEditingItem(null);
  };

  const columns: ColumnDef<SKUInventoryItem>[] = [
    {
      key: 'sku',
      header: 'SKU & Title',
      render: (item) => (
        <div>
          <p className="font-bold text-xs text-gray-900 line-clamp-1">{item.title}</p>
          <div className="flex items-center gap-2 mt-0.5">
            <span className="font-mono text-[11px] text-blue-700 bg-blue-50 px-1.5 py-0.2 rounded font-semibold">{item.sku}</span>
            <span className="text-[11px] text-gray-400">{item.category}</span>
          </div>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'sellingPrice',
      header: 'Selling Price (₹)',
      render: (item) => (
        <div>
          <span className="font-bold text-xs text-gray-900">₹{item.sellingPrice.toLocaleString('en-IN')}</span>
          <p className="text-[10px] text-gray-400 line-through">MRP ₹{item.mrp.toLocaleString('en-IN')}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'stockAvailable',
      header: 'Live Stock',
      render: (item) => (
        <div>
          <span className={`text-xs font-bold ${item.stockAvailable === 0 ? 'text-red-600' : item.stockAvailable <= item.reorderThreshold ? 'text-amber-600' : 'text-gray-900'}`}>
            {item.stockAvailable} Units Available
          </span>
          {item.stockReserved > 0 && (
            <p className="text-[10px] text-gray-400">({item.stockReserved} In Cart Hold)</p>
          )}
        </div>
      ),
      sortable: true,
    },
    {
      key: 'status',
      header: 'Inventory State',
      render: (item) => (
        <Badge
          variant={item.status === 'IN_STOCK' ? 'success' : item.status === 'LOW_STOCK' ? 'warning' : 'danger'}
        >
          {item.status.replace(/_/g, ' ')}
        </Badge>
      ),
      sortable: true,
    },
    {
      key: 'fulfillmentType',
      header: 'Channel',
      render: (item) => (
        <span className="text-[11px] font-semibold text-gray-600">
          {item.fulfillmentType === 'NOVAMART_FULFILLED' ? 'NovaMart Assured (FBF)' : 'Merchant Handled'}
        </span>
      ),
    },
    {
      key: 'actions',
      header: 'Quick Action',
      render: (item) => (
        <button
          type="button"
          className="btn btn-neutral btn-sm flex items-center gap-1 text-xs"
          onClick={() => handleOpenEdit(item)}
        >
          <Edit3 size={12} />
          <span>Edit SKU</span>
        </button>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Multi-Channel SKU Inventory Workbench</h1>
          <p className="text-xs text-gray-500 mt-0.5">Real-time stock synchronization, reorder thresholds, and dynamic price ladders.</p>
        </div>

        <div className="flex items-center gap-2">
          <button
            type="button"
            className="btn btn-neutral btn-sm flex items-center gap-1"
            onClick={() => showToast('info', 'Sync Completed', 'All warehouse bins synced.')}
          >
            <RefreshCw size={14} />
            <span>Sync Stock</span>
          </button>
          <button
            type="button"
            className="btn btn-primary btn-sm flex items-center gap-1"
            onClick={() => showToast('info', 'Add SKU', 'Single SKU creation wizard opened.')}
          >
            <Plus size={14} />
            <span>Add Single SKU</span>
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard title="Active Catalog SKUs" value="142 SKUs" subtitle="Across 6 primary categories" variant="blue" />
        <MetricCard title="Total Stock Units" value="1,840 Units" subtitle="Live in fulfillment centers" variant="green" />
        <MetricCard title="Low Stock Alerts" value="4 SKUs" subtitle="Below reorder threshold" variant="amber" />
        <MetricCard title="Out of Stock Loss" value="₹2,40,000" subtitle="Estimated lost daily GMV" variant="neutral" />
      </div>

      <DataTable
        data={items}
        columns={columns}
        searchPlaceholder="Search by SKU code or product title..."
        searchKey="title"
      />

      {/* Edit SKU Modal */}
      {editingItem && (
        <Modal
          isOpen={true}
          onClose={() => setEditingItem(null)}
          title={`Edit Listing: ${editingItem.sku}`}
        >
          <form onSubmit={handleSaveEdit} className="space-y-4 text-xs">
            <div>
              <span className="font-semibold text-gray-700">Product Title:</span>
              <p className="font-bold text-gray-900 mt-0.5">{editingItem.title}</p>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-1">
                <label className="font-semibold text-gray-700">Available Physical Stock:</label>
                <input
                  type="number"
                  min={0}
                  value={newStock}
                  onChange={(e) => setNewStock(Number(e.target.value))}
                  className="w-full p-2 border rounded font-bold text-xs"
                  required
                />
              </div>

              <div className="space-y-1">
                <label className="font-semibold text-gray-700">Selling Price (₹):</label>
                <input
                  type="number"
                  min={1}
                  value={newPrice}
                  onChange={(e) => setNewPrice(Number(e.target.value))}
                  className="w-full p-2 border rounded font-bold text-xs"
                  required
                />
              </div>
            </div>

            <div className="pt-3 border-t flex justify-end gap-2">
              <button
                type="button"
                className="btn btn-neutral btn-sm"
                onClick={() => setEditingItem(null)}
              >
                Cancel
              </button>
              <button
                type="submit"
                className="btn btn-primary btn-sm flex items-center gap-1"
              >
                <Check size={14} />
                <span>Save Changes</span>
              </button>
            </div>
          </form>
        </Modal>
      )}
    </div>
  );
};
