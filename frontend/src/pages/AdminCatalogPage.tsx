import React, { useState, useEffect } from 'react';
import { api } from '../services/api';
import { Product, Category, Brand } from '../types';

export const AdminCatalogPage: React.FC = () => {
  const [activeSubTab, setActiveSubTab] = useState<'products' | 'categories' | 'brands'>('products');
  const [products, setProducts] = useState<Product[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [brands, setBrands] = useState<Brand[]>([]);

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [message, setMessage] = useState('');

  // Modals
  const [showProductModal, setShowProductModal] = useState(false);
  const [showCategoryModal, setShowCategoryModal] = useState(false);
  const [showBrandModal, setShowBrandModal] = useState(false);

  // Product Form
  const [prodName, setProdName] = useState('');
  const [prodCatId, setProdCatId] = useState<number>(0);
  const [prodBrandId, setProdBrandId] = useState<number | undefined>(undefined);
  const [prodDesc, setProdDesc] = useState('');
  const [prodStatus, setProdStatus] = useState('ACTIVE');
  const [sku, setSku] = useState('');
  const [price, setPrice] = useState('');
  const [discPrice, setDiscPrice] = useState('');
  const [stock, setStock] = useState('50');

  // Category Form
  const [catName, setCatName] = useState('');
  const [catParentId, setCatParentId] = useState<number | undefined>(undefined);

  // Brand Form
  const [brandName, setBrandName] = useState('');
  const [brandDesc, setBrandDesc] = useState('');

  useEffect(() => {
    loadData();
  }, [activeSubTab]);

  const loadData = async () => {
    setLoading(true);
    setError('');
    setMessage('');
    try {
      if (activeSubTab === 'products') {
        const [pRes, cList, bList] = await Promise.all([
          api.getProducts('limit=100'),
          api.getCategories(),
          api.getBrands(),
        ]);
        setProducts(pRes.items);
        setCategories(cList);
        setBrands(bList);
        if (cList.length > 0) setProdCatId(cList[0].id);
      } else if (activeSubTab === 'categories') {
        const cList = await api.getCategories();
        setCategories(cList);
      } else if (activeSubTab === 'brands') {
        const bList = await api.getBrands();
        setBrands(bList);
      }
    } catch (err: any) {
      setError(err.message || 'Failed to load catalog data.');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateProduct = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const newProd = await api.createProduct({
        name: prodName,
        category_id: prodCatId,
        brand_id: prodBrandId || null,
        description: prodDesc,
        status: prodStatus,
        is_active: true,
      });

      // Add variant SKU
      if (sku && price) {
        await api.adminAddVariant(newProd.id, {
          sku,
          title: 'Default Variant',
          price: parseFloat(price),
          discount_price: discPrice ? parseFloat(discPrice) : null,
          stock_quantity: parseInt(stock),
        });
      }

      setShowProductModal(false);
      setMessage(`Product "${prodName}" created successfully!`);
      loadData();
    } catch (err: any) {
      setError(err.message || 'Failed to create product.');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateCategory = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await api.adminCreateCategory({
        name: catName,
        parent_id: catParentId || null,
        is_active: true,
      });
      setShowCategoryModal(false);
      setCatName('');
      setMessage(`Category "${catName}" created!`);
      loadData();
    } catch (err: any) {
      setError(err.message || 'Failed to create category.');
    } finally {
      setLoading(false);
    }
  };

  const handleCreateBrand = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      await api.adminCreateBrand({
        name: brandName,
        description: brandDesc,
        is_active: true,
      });
      setShowBrandModal(false);
      setBrandName('');
      setBrandDesc('');
      setMessage(`Brand "${brandName}" created!`);
      loadData();
    } catch (err: any) {
      setError(err.message || 'Failed to create brand.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto py-8 px-4">
      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-2xl font-bold text-gray-800">HashKart Catalog Administration</h1>
          <p className="text-xs text-gray-500">Manage categories, brands, products, variants, and specifications.</p>
        </div>

        <div className="flex space-x-3">
          {activeSubTab === 'products' && (
            <button onClick={() => setShowProductModal(true)} className="bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-4 py-2 rounded shadow">
              + Create Product
            </button>
          )}
          {activeSubTab === 'categories' && (
            <button onClick={() => setShowCategoryModal(true)} className="bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-4 py-2 rounded shadow">
              + Add Category
            </button>
          )}
          {activeSubTab === 'brands' && (
            <button onClick={() => setShowBrandModal(true)} className="bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold px-4 py-2 rounded shadow">
              + Add Brand
            </button>
          )}
        </div>
      </div>

      {error && <div className="bg-red-50 border-l-4 border-red-500 text-red-700 p-3 rounded text-xs mb-4">{error}</div>}
      {message && <div className="bg-green-50 border-l-4 border-green-500 text-green-700 p-3 rounded text-xs mb-4">{message}</div>}

      {/* Subtabs */}
      <div className="flex border-b border-gray-200 mb-6">
        <button
          onClick={() => setActiveSubTab('products')}
          className={`px-4 py-2.5 text-sm font-bold border-b-2 transition-colors ${
            activeSubTab === 'products' ? 'border-blue-600 text-blue-600' : 'border-transparent text-gray-500 hover:text-gray-700'
          }`}
        >
          Products Catalog ({products.length})
        </button>
        <button
          onClick={() => setActiveSubTab('categories')}
          className={`px-4 py-2.5 text-sm font-bold border-b-2 transition-colors ${
            activeSubTab === 'categories' ? 'border-blue-600 text-blue-600' : 'border-transparent text-gray-500 hover:text-gray-700'
          }`}
        >
          Categories ({categories.length})
        </button>
        <button
          onClick={() => setActiveSubTab('brands')}
          className={`px-4 py-2.5 text-sm font-bold border-b-2 transition-colors ${
            activeSubTab === 'brands' ? 'border-blue-600 text-blue-600' : 'border-transparent text-gray-500 hover:text-gray-700'
          }`}
        >
          Brands ({brands.length})
        </button>
      </div>

      {/* Products Table */}
      {activeSubTab === 'products' && (
        <div className="bg-white rounded-lg shadow border overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="bg-gray-100 text-gray-600 uppercase border-b">
                <th className="p-3">ID / SKU</th>
                <th className="p-3">Product Name</th>
                <th className="p-3">Category</th>
                <th className="p-3">Brand</th>
                <th className="p-3">Status</th>
                <th className="p-3">Rating</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {products.map((p) => (
                <tr key={p.id} className="hover:bg-gray-50">
                  <td className="p-3 font-mono font-bold text-gray-500">#{p.id}</td>
                  <td className="p-3 font-bold text-gray-800">{p.name}</td>
                  <td className="p-3 text-gray-600">{p.category?.name || 'Uncategorized'}</td>
                  <td className="p-3 text-gray-600">{p.brand?.name || 'Generic'}</td>
                  <td className="p-3">
                    <span className={`px-2 py-0.5 rounded text-xs font-bold ${p.status === 'ACTIVE' ? 'bg-green-100 text-green-800' : 'bg-yellow-100 text-yellow-800'}`}>
                      {p.status}
                    </span>
                  </td>
                  <td className="p-3 font-semibold text-gray-700">★ {p.rating_avg} ({p.review_count})</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Categories Table */}
      {activeSubTab === 'categories' && (
        <div className="bg-white rounded-lg shadow border overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="bg-gray-100 text-gray-600 uppercase border-b">
                <th className="p-3">ID</th>
                <th className="p-3">Category Name</th>
                <th className="p-3">Slug</th>
                <th className="p-3">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {categories.map((c) => (
                <tr key={c.id} className="hover:bg-gray-50">
                  <td className="p-3 font-mono font-bold">#{c.id}</td>
                  <td className="p-3 font-bold text-gray-800">{c.name}</td>
                  <td className="p-3 font-mono text-gray-500">{c.slug}</td>
                  <td className="p-3">
                    <span className="bg-green-100 text-green-800 text-xs font-bold px-2 py-0.5 rounded">Active</span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Brands Table */}
      {activeSubTab === 'brands' && (
        <div className="bg-white rounded-lg shadow border overflow-x-auto">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="bg-gray-100 text-gray-600 uppercase border-b">
                <th className="p-3">ID</th>
                <th className="p-3">Brand Name</th>
                <th className="p-3">Slug</th>
                <th className="p-3">Products</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {brands.map((b) => (
                <tr key={b.id} className="hover:bg-gray-50">
                  <td className="p-3 font-mono font-bold">#{b.id}</td>
                  <td className="p-3 font-bold text-gray-800">{b.name}</td>
                  <td className="p-3 font-mono text-gray-500">{b.slug}</td>
                  <td className="p-3 font-bold text-blue-600">{b.product_count || 0}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      {/* Create Product Modal */}
      {showProductModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg p-6 max-w-lg w-full shadow-xl">
            <h3 className="text-lg font-bold text-gray-800 mb-4">Create New Catalog Product</h3>
            <form onSubmit={handleCreateProduct} className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-gray-600 mb-1">Product Name</label>
                <input type="text" required value={prodName} onChange={(e) => setProdName(e.target.value)} className="w-full p-2 border rounded text-xs" />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">Category</label>
                  <select value={prodCatId} onChange={(e) => setProdCatId(Number(e.target.value))} className="w-full p-2 border rounded text-xs">
                    {categories.map((c) => (
                      <option key={c.id} value={c.id}>{c.name}</option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">Brand</label>
                  <select value={prodBrandId || ''} onChange={(e) => setProdBrandId(e.target.value ? Number(e.target.value) : undefined)} className="w-full p-2 border rounded text-xs">
                    <option value="">None / Generic</option>
                    {brands.map((b) => (
                      <option key={b.id} value={b.id}>{b.name}</option>
                    ))}
                  </select>
                </div>
              </div>

              <div>
                <label className="block text-xs font-semibold text-gray-600 mb-1">Description</label>
                <textarea required rows={3} value={prodDesc} onChange={(e) => setProdDesc(e.target.value)} className="w-full p-2 border rounded text-xs" />
              </div>

              <div className="grid grid-cols-3 gap-2 pt-2 border-t">
                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">Variant SKU</label>
                  <input type="text" required value={sku} onChange={(e) => setSku(e.target.value)} placeholder="HK-SKU-100" className="w-full p-2 border rounded text-xs" />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">Price (₹)</label>
                  <input type="number" required value={price} onChange={(e) => setPrice(e.target.value)} placeholder="1999" className="w-full p-2 border rounded text-xs" />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">Sale Price (₹)</label>
                  <input type="number" value={discPrice} onChange={(e) => setDiscPrice(e.target.value)} placeholder="1499" className="w-full p-2 border rounded text-xs" />
                </div>
              </div>

              <div className="flex justify-end space-x-2 pt-3 border-t">
                <button type="button" onClick={() => setShowProductModal(false)} className="px-3 py-1.5 border rounded text-xs font-semibold">Cancel</button>
                <button type="submit" disabled={loading} className="px-4 py-1.5 bg-blue-600 text-white rounded text-xs font-bold">Save Product</button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Create Category Modal */}
      {showCategoryModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg p-6 max-w-sm w-full shadow-xl">
            <h3 className="text-base font-bold text-gray-800 mb-4">Add Category</h3>
            <form onSubmit={handleCreateCategory} className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-gray-600 mb-1">Category Name</label>
                <input type="text" required value={catName} onChange={(e) => setCatName(e.target.value)} className="w-full p-2 border rounded text-xs" />
              </div>
              <div className="flex justify-end space-x-2 pt-3">
                <button type="button" onClick={() => setShowCategoryModal(false)} className="px-3 py-1.5 border rounded text-xs">Cancel</button>
                <button type="submit" disabled={loading} className="px-4 py-1.5 bg-blue-600 text-white rounded text-xs font-bold">Save</button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Create Brand Modal */}
      {showBrandModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg p-6 max-w-sm w-full shadow-xl">
            <h3 className="text-base font-bold text-gray-800 mb-4">Add Brand</h3>
            <form onSubmit={handleCreateBrand} className="space-y-3">
              <div>
                <label className="block text-xs font-semibold text-gray-600 mb-1">Brand Name</label>
                <input type="text" required value={brandName} onChange={(e) => setBrandName(e.target.value)} className="w-full p-2 border rounded text-xs" />
              </div>
              <div>
                <label className="block text-xs font-semibold text-gray-600 mb-1">Description</label>
                <input type="text" value={brandDesc} onChange={(e) => setBrandDesc(e.target.value)} className="w-full p-2 border rounded text-xs" />
              </div>
              <div className="flex justify-end space-x-2 pt-3">
                <button type="button" onClick={() => setShowBrandModal(false)} className="px-3 py-1.5 border rounded text-xs">Cancel</button>
                <button type="submit" disabled={loading} className="px-4 py-1.5 bg-blue-600 text-white rounded text-xs font-bold">Save</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
