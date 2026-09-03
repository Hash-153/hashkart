import React from 'react';
import { useNavigate } from 'react-router-dom';
import { X, ArrowRight, Layers } from 'lucide-react';
import { Product } from '../types';

export interface CompareDrawerProps {
  products: Product[];
  onRemove: (productId: number) => void;
  onClear: () => void;
}

export const CompareDrawer: React.FC<CompareDrawerProps> = ({
  products,
  onRemove,
  onClear,
}) => {
  const navigate = useNavigate();

  if (products.length === 0) return null;

  const handleCompareNow = () => {
    const ids = products.map((p) => p.id).join(',');
    navigate(`/compare?ids=${ids}`);
  };

  return (
    <div className="compare-floating-drawer">
      <div className="compare-drawer-content">
        <div className="compare-drawer-header">
          <div className="flex items-center gap-2">
            <Layers size={18} className="text-primary" />
            <span className="font-semibold text-sm">
              Compare ({products.length}/4 Products)
            </span>
          </div>
          <button
            type="button"
            className="text-xs text-gray-500 hover:text-red-600 underline"
            onClick={onClear}
          >
            Clear All
          </button>
        </div>

        <div className="compare-product-slots">
          {products.map((p) => (
            <div key={p.id} className="compare-slot-item">
              <img
                src={p.images?.[0]?.image_url || 'https://via.placeholder.com/80'}
                alt={p.name}
                className="compare-slot-thumb"
              />
              <div className="compare-slot-details">
                <p className="compare-slot-name truncate">{p.name}</p>
                <p className="compare-slot-price">
                  ₹{(p.variants?.[0]?.price || (p as any).price || 0).toLocaleString('en-IN')}
                </p>
              </div>
              <button
                type="button"
                className="compare-slot-remove"
                onClick={() => onRemove(p.id)}
                aria-label={`Remove ${p.name} from comparison`}
              >
                <X size={14} />
              </button>
            </div>
          ))}

          {/* Empty Placeholders up to 4 */}
          {Array.from({ length: Math.max(0, 4 - products.length) }).map((_, idx) => (
            <div key={`empty-${idx}`} className="compare-slot-empty">
              <span className="text-xs text-gray-400">Add Product</span>
            </div>
          ))}
        </div>

        <div className="compare-drawer-action">
          <button
            type="button"
            className="btn btn-primary btn-sm flex items-center gap-2"
            disabled={products.length < 2}
            onClick={handleCompareNow}
          >
            <span>Compare Now</span>
            <ArrowRight size={16} />
          </button>
        </div>
      </div>
    </div>
  );
};
