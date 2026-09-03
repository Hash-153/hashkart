import React, { useState, useEffect } from 'react';
import { useSearchParams, Link, useNavigate } from 'react-router-dom';
import { ArrowLeft, ShoppingCart, Star, Check, AlertCircle } from 'lucide-react';
import { api } from '../services/api';
import { useCart } from '../context/CartContext';
import { useToast } from '../components/ui/Toast';

export const ComparePage: React.FC = () => {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const { addToCart } = useCart();
  const { showToast } = useToast();

  const [data, setData] = useState<any | null>(null);
  const [loading, setLoading] = useState(true);
  const [highlightDifferences, setHighlightDifferences] = useState(false);

  const productIds = searchParams.get('ids') || '';

  useEffect(() => {
    const fetchMatrix = async () => {
      if (!productIds) {
        setLoading(false);
        return;
      }
      try {
        setLoading(true);
        const res = await api.getProductComparisonMatrix(productIds);
        setData(res);
      } catch (err) {
        console.error('Failed to load comparison matrix:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchMatrix();
  }, [productIds]);

  const handleAddToCart = async (product: any) => {
    const variantId = product.variants?.[0]?.id || product.id;
    try {
      await addToCart(variantId, 1);
      showToast('success', 'Added to Cart', `${product.name} added to your cart.`);
    } catch {
      showToast('error', 'Cart Error', 'Failed to add item to cart.');
    }
  };

  if (loading) {
    return (
      <div className="container py-12 text-center text-xs text-gray-500">
        Generating side-by-side product comparison matrix...
      </div>
    );
  }

  if (!data || !data.products || data.products.length === 0) {
    return (
      <div className="container py-12 text-center space-y-4">
        <AlertCircle size={40} className="mx-auto text-gray-400" />
        <h3 className="text-lg font-bold text-gray-900">No Products to Compare</h3>
        <p className="text-xs text-gray-500 max-w-sm mx-auto">
          Please select 2 or more products from the catalog to compare their technical specifications side-by-side.
        </p>
        <Link to="/products" className="btn btn-primary btn-sm inline-flex">
          Browse Products
        </Link>
      </div>
    );
  }

  return (
    <div className="compare-page container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <button
            type="button"
            onClick={() => navigate(-1)}
            className="p-2 border rounded-lg hover:bg-gray-50"
            aria-label="Back"
          >
            <ArrowLeft size={16} />
          </button>
          <div>
            <h1 className="text-xl font-bold text-gray-900">
              Product Comparison — {data.category_name}
            </h1>
            <p className="text-xs text-gray-500 mt-0.5">
              Comparing {data.products.length} models side-by-side
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2">
          <label className="flex items-center gap-2 text-xs font-medium text-gray-700 cursor-pointer bg-white px-3 py-1.5 border rounded-lg">
            <input
              type="checkbox"
              checked={highlightDifferences}
              onChange={(e) => setHighlightDifferences(e.target.checked)}
              className="rounded text-blue-600 focus:ring-blue-500"
            />
            <span>Highlight Differences Only</span>
          </label>
        </div>
      </div>

      {/* Comparison Grid Table */}
      <div className="compare-matrix-wrapper overflow-x-auto bg-white border border-gray-200 rounded-xl shadow-sm">
        <table className="w-full text-left border-collapse">
          {/* Header Row with Product Cards */}
          <thead>
            <tr className="border-b bg-gray-50/50">
              <th className="p-4 w-60 min-w-[200px] align-bottom bg-gray-50 text-xs font-bold text-gray-700">
                Specification Key
              </th>
              {data.products.map((p: any) => (
                <th key={p.id} className="p-4 w-72 min-w-[240px] align-top border-l border-gray-200">
                  <div className="space-y-2">
                    <div className="aspect-square w-32 mx-auto overflow-hidden rounded-lg bg-gray-100 flex items-center justify-center p-2">
                      <img
                        src={p.image_url || 'https://via.placeholder.com/150'}
                        alt={p.name}
                        className="max-h-full max-w-full object-contain"
                      />
                    </div>
                    <Link
                      to={`/products/${p.slug || p.id}`}
                      className="block text-xs font-bold text-gray-900 hover:text-blue-600 line-clamp-2"
                    >
                      {p.name}
                    </Link>
                    <div className="flex items-center gap-2">
                      <span className="text-base font-extrabold text-gray-900">
                        ₹{p.price.toLocaleString('en-IN')}
                      </span>
                      {p.mrp > p.price && (
                        <span className="text-xs text-gray-400 line-through">
                          ₹{p.mrp.toLocaleString('en-IN')}
                        </span>
                      )}
                    </div>
                    <button
                      type="button"
                      onClick={() => handleAddToCart(p)}
                      className="btn btn-primary btn-sm w-full flex items-center justify-center gap-1.5"
                    >
                      <ShoppingCart size={14} />
                      <span>Add to Cart</span>
                    </button>
                  </div>
                </th>
              ))}
            </tr>
          </thead>

          {/* Sections & Specs */}
          <tbody>
            {data.spec_sections?.map((section: any, sIdx: number) => {
              const visibleSpecs = highlightDifferences
                ? section.specs.filter((s: any) => s.is_different)
                : section.specs;

              if (visibleSpecs.length === 0) return null;

              return (
                <React.Fragment key={sIdx}>
                  <tr className="bg-gray-100/80 border-t border-b">
                    <td
                      colSpan={data.products.length + 1}
                      className="p-2.5 px-4 font-bold text-xs text-gray-800 uppercase tracking-wider"
                    >
                      {section.section_title}
                    </td>
                  </tr>

                  {visibleSpecs.map((spec: any, rIdx: number) => (
                    <tr
                      key={rIdx}
                      className={`border-b hover:bg-blue-50/30 transition-colors ${
                        spec.is_different ? 'bg-amber-50/40' : ''
                      }`}
                    >
                      <td className="p-3.5 px-4 text-xs font-semibold text-gray-700 bg-gray-50/50">
                        <span>{spec.spec_label}</span>
                        {spec.is_different && (
                          <span className="ml-2 text-[10px] text-amber-700 font-normal">
                            (differs)
                          </span>
                        )}
                      </td>
                      {data.products.map((p: any) => (
                        <td
                          key={p.id}
                          className="p-3.5 px-4 text-xs text-gray-900 border-l border-gray-200"
                        >
                          {spec.values_by_product_id?.[p.id] || '—'}
                        </td>
                      ))}
                    </tr>
                  ))}
                </React.Fragment>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};
