import React, { useState } from 'react';
import { Package, Plus, Search, Edit2, CheckCircle2, AlertTriangle } from 'lucide-react';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { Modal } from '../../components/ui/Modal';
import { useToast } from '../../components/ui/Toast';

interface InventoryItem {
  id: number;
  sku: string;
  title: string;
  category: string;
  price: number;
  stock: number;
  reserved: number;
  status: 'ACTIVE' | 'LOW_STOCK' | 'OUT_OF_STOCK';
}

const MOCK_INVENTORY: InventoryItem[] = [
  { id: 1, sku: 'APL-IP15-128-BLK', title: 'Apple iPhone 15 (128 GB) - Black', category: 'Smartphones', price: 69999, stock: 45, reserved: 3, status: 'ACTIVE' },
  { id: 2, sku: 'SAM-S24U-256-GRY', title: 'Samsung Galaxy S24 Ultra 5G - Titanium', category: 'Smartphones', price: 129999, stock: 12, reserved: 2, status: 'ACTIVE' },
  { id: 3, sku: 'SNY-WH1000-XM5', title: 'Sony WH-1000XM5 Noise Cancelling Headphones', category: 'Audio', price: 26990, stock: 4, reserved: 1, status: 'LOW_STOCK' },
  { id: 4, sku: 'DEL-XPS13-512', title: 'Dell XPS 13 Core i7 16GB/512GB SSD', category: 'Laptops', price: 119990, stock: 0, reserved: 0, status: 'OUT_OF_STOCK' },
  { id: 5, sku: 'RME-GT6T-128', title: 'Realme GT 6T 5G (8GB/128GB)', category: 'Smartphones', price: 24999, stock: 80, reserved: 12, status: 'ACTIVE' },
];

export const SellerInventoryPage: React.FC = () => {
  const { showToast } = useToast();
  const [inventory, setInventory] = useState<InventoryItem[]>(MOCK_INVENTORY);
  const [editingItem, setEditingItem] = useState<InventoryItem | null>(null);
  const [newStock, setNewStock] = useState<number>(0);
  const [newPrice, setNewPrice] = useState<number>(0);

  const handleOpenEdit = (item: InventoryItem) => {
    setEditingItem(item);
    setNewStock(item.stock);
    setNewPrice(item.price);
  };

  const handleSaveEdit = () => {
    if (!editingItem) return;
    setInventory((prev) =>
      prev.map((it) =>
        it.id === editingItem.id
          ? {
              ...it,
              stock: newStock,
              price: newPrice,
              status: newStock === 0 ? 'OUT_OF_STOCK' : newStock < 10 ? 'LOW_STOCK' : 'ACTIVE',
            }
          : it
      )
    );
    showToast('success', 'Listing Updated', `Stock and pricing updated for ${editingItem.sku}.`);
    setEditingItem(null);
  };

  const columns: ColumnDef<InventoryItem>[] = [
    {
      key: 'sku',
      header: 'SKU / Title',
      render: (item) => (
        <div>
          <span className="font-mono text-xs font-bold text-gray-900">{item.sku}</span>
          <p className="text-xs text-gray-500 line-clamp-1">{item.title}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'category',
      header: 'Category',
      render: (item) => <span className="text-xs text-gray-600">{item.category}</span>,
      sortable: true,
    },
    {
      key: 'price',
      header: 'Price (INR)',
      render: (item) => <span className="font-bold text-xs">₹{item.price.toLocaleString('en-IN')}</span>,
      sortable: true,
    },
    {
      key: 'stock',
      header: 'Available Stock',
      render: (item) => (
        <div className="text-xs">
          <span className="font-bold">{item.stock} Units</span>
          {item.reserved > 0 && (
            <span className="text-gray-400 text-[11px] ml-1">({item.reserved} reserved)</span>
          )}
        </div>
      ),
      sortable: true,
    },
    {
      key: 'status',
      header: 'Stock Status',
      render: (item) => {
        if (item.status === 'ACTIVE') {
          return (
            <span className="px-2 py-0.5 bg-green-100 text-green-800 rounded font-semibold text-[11px]">
              In Stock
            </span>
          );
        }
        if (item.status === 'LOW_STOCK') {
          return (
            <span className="px-2 py-0.5 bg-amber-100 text-amber-800 rounded font-semibold text-[11px]">
              Low Stock (&lt;10)
            </span>
          );
        }
        return (
          <span className="px-2 py-0.5 bg-red-100 text-red-800 rounded font-semibold text-[11px]">
            Out of Stock
          </span>
        );
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Actions',
      render: (item) => (
        <button
          type="button"
          className="btn btn-neutral btn-sm flex items-center gap-1"
          onClick={() => handleOpenEdit(item)}
        >
          <Edit2 size={12} />
          <span>Edit</span>
        </button>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Seller Inventory & Price Management</h1>
          <p className="text-xs text-gray-500 mt-0.5">Manage SKU stocks, real-time prices, and buffer allocations.</p>
        </div>
      </div>

      <DataTable
        data={inventory}
        columns={columns}
        searchPlaceholder="Search by SKU or Title..."
        searchKey="title"
      />

      {/* Edit Modal */}
      {editingItem && (
        <Modal
          isOpen={true}
          onClose={() => setEditingItem(null)}
          title={`Edit SKU: ${editingItem.sku}`}
        >
          <div className="space-y-4 text-xs">
            <div>
              <label className="block font-bold text-gray-700 mb-1">Product Title</label>
              <p className="p-2 bg-gray-50 rounded border text-gray-600">{editingItem.title}</p>
            </div>

            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block font-bold text-gray-700 mb-1">Selling Price (₹)</label>
                <input
                  type="number"
                  value={newPrice}
                  onChange={(e) => setNewPrice(Number(e.target.value))}
                  className="w-full p-2 border rounded font-bold"
                />
              </div>

              <div>
                <label className="block font-bold text-gray-700 mb-1">Stock Units</label>
                <input
                  type="number"
                  value={newStock}
                  onChange={(e) => setNewStock(Number(e.target.value))}
                  className="w-full p-2 border rounded font-bold"
                />
              </div>
            </div>

            <div className="pt-3 flex justify-end gap-2 border-t">
              <button
                type="button"
                className="btn btn-neutral btn-sm"
                onClick={() => setEditingItem(null)}
              >
                Cancel
              </button>
              <button
                type="button"
                className="btn btn-primary btn-sm"
                onClick={handleSaveEdit}
              >
                Save Changes
              </button>
            </div>
          </div>
        </Modal>
      )}
    </div>
  );
};
