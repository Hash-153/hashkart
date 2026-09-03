import React, { useState } from 'react';
import { Layers, Plus, Edit2, Trash2, CheckCircle2, ChevronRight, Folder } from 'lucide-react';
import { useToast } from '../../components/ui/Toast';
import { Modal } from '../../components/ui/Modal';

interface CategoryNode {
  id: number;
  name: string;
  slug: string;
  commissionRate: number;
  productCount: number;
  subcategories: { id: number; name: string; slug: string; productCount: number }[];
}

const MOCK_CATEGORIES: CategoryNode[] = [
  {
    id: 1,
    name: 'Mobiles & Tablets',
    slug: 'mobiles-tablets',
    commissionRate: 5.5,
    productCount: 840,
    subcategories: [
      { id: 11, name: 'Smartphones', slug: 'smartphones', productCount: 520 },
      { id: 12, name: 'Tablets & iPads', slug: 'tablets', productCount: 180 },
      { id: 13, name: 'Mobile Accessories', slug: 'mobile-accessories', productCount: 140 },
    ],
  },
  {
    id: 2,
    name: 'Laptops & Computers',
    slug: 'laptops-computers',
    commissionRate: 6.0,
    productCount: 410,
    subcategories: [
      { id: 21, name: 'Gaming Laptops', slug: 'gaming-laptops', productCount: 120 },
      { id: 22, name: 'Thin & Light Laptops', slug: 'thin-light-laptops', productCount: 190 },
      { id: 23, name: 'PC Components', slug: 'pc-components', productCount: 100 },
    ],
  },
  {
    id: 3,
    name: 'Audio & Sound',
    slug: 'audio-sound',
    commissionRate: 10.0,
    productCount: 650,
    subcategories: [
      { id: 31, name: 'Wireless Headphones', slug: 'wireless-headphones', productCount: 280 },
      { id: 32, name: 'Soundbars & Home Theatres', slug: 'soundbars', productCount: 170 },
      { id: 33, name: 'Bluetooth Speakers', slug: 'bluetooth-speakers', productCount: 200 },
    ],
  },
];

export const AdminCategoryManagementPage: React.FC = () => {
  const { showToast } = useToast();
  const [categories, setCategories] = useState<CategoryNode[]>(MOCK_CATEGORIES);
  const [selectedCategory, setSelectedCategory] = useState<CategoryNode>(MOCK_CATEGORIES[0]);

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Category Hierarchy & Commission Rate Matrix</h1>
          <p className="text-xs text-gray-500 mt-0.5">Manage marketplace taxonomy trees, attribute schemas, and category-level fee percentages.</p>
        </div>

        <button
          type="button"
          className="btn btn-primary btn-sm flex items-center gap-1.5"
          onClick={() => showToast('info', 'Add Category', 'Category creation dialog opened.')}
        >
          <Plus size={14} />
          <span>Add Primary Category</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Category Tree Navigation */}
        <div className="bg-white border border-gray-200 rounded-xl p-4 space-y-2 shadow-sm">
          <h3 className="text-xs font-bold uppercase tracking-wider text-gray-500 mb-3">Primary Categories</h3>
          {categories.map((c) => (
            <button
              key={c.id}
              type="button"
              className={`w-full p-3 rounded-lg text-left text-xs font-semibold flex items-center justify-between transition-all ${
                selectedCategory.id === c.id
                  ? 'bg-blue-50 text-blue-900 border border-blue-200 shadow-sm'
                  : 'hover:bg-gray-50 text-gray-700'
              }`}
              onClick={() => setSelectedCategory(c)}
            >
              <div className="flex items-center gap-2">
                <Folder size={16} className={selectedCategory.id === c.id ? 'text-blue-600' : 'text-gray-400'} />
                <span>{c.name}</span>
              </div>
              <ChevronRight size={14} className="text-gray-400" />
            </button>
          ))}
        </div>

        {/* Selected Category Details & Subcategories */}
        <div className="md:col-span-2 bg-white border border-gray-200 rounded-xl p-6 space-y-6 shadow-sm">
          <div className="flex items-center justify-between border-b pb-4">
            <div>
              <h2 className="text-lg font-bold text-gray-900">{selectedCategory.name}</h2>
              <p className="text-xs text-gray-400 font-mono mt-0.5">Slug: {selectedCategory.slug}</p>
            </div>

            <div className="flex items-center gap-3">
              <span className="text-xs font-bold text-green-800 bg-green-50 px-2.5 py-1 rounded-full border border-green-200">
                {selectedCategory.commissionRate}% Commission
              </span>
            </div>
          </div>

          <div className="space-y-3">
            <h3 className="text-xs font-bold uppercase tracking-wider text-gray-500">Subcategories ({selectedCategory.subcategories.length})</h3>
            <div className="divide-y divide-gray-100 border rounded-lg">
              {selectedCategory.subcategories.map((sub) => (
                <div key={sub.id} className="p-3.5 flex items-center justify-between text-xs">
                  <div>
                    <p className="font-bold text-gray-900">{sub.name}</p>
                    <span className="text-[11px] text-gray-400">{sub.productCount} Active Catalog Listings</span>
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      type="button"
                      className="p-1.5 hover:bg-gray-100 rounded text-gray-500"
                      onClick={() => showToast('info', 'Edit Subcategory', `Editing ${sub.name}`)}
                    >
                      <Edit2 size={14} />
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
