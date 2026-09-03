import React, { useState } from 'react';
import { Category, Brand } from '../types';
import { Filter, Star } from 'lucide-react';

interface FilterSidebarProps {
  categories: Category[];
  brands: Brand[];
  selectedCategoryId?: number;
  selectedBrandId?: number;
  selectedMinRating?: number;
  selectedMinPrice?: number;
  selectedMaxPrice?: number;
  onFilterChange: (filters: {
    category_id?: number;
    brand_id?: number;
    min_rating?: number;
    min_price?: number;
    max_price?: number;
  }) => void;
  onClear: () => void;
}

export const FilterSidebar: React.FC<FilterSidebarProps> = ({
  categories,
  brands,
  selectedCategoryId,
  selectedBrandId,
  selectedMinRating,
  selectedMinPrice,
  selectedMaxPrice,
  onFilterChange,
  onClear,
}) => {
  const [minP, setMinP] = useState<string>(selectedMinPrice?.toString() || '');
  const [maxP, setMaxP] = useState<string>(selectedMaxPrice?.toString() || '');

  const handlePriceApply = () => {
    onFilterChange({
      category_id: selectedCategoryId,
      brand_id: selectedBrandId,
      min_rating: selectedMinRating,
      min_price: minP ? Number(minP) : undefined,
      max_price: maxP ? Number(maxP) : undefined,
    });
  };

  return (
    <aside
      style={{
        backgroundColor: 'var(--bg-card)',
        border: '1px solid var(--border-color)',
        borderRadius: '4px',
        padding: '16px',
        width: '260px',
        flexShrink: 0,
      }}
    >
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          borderBottom: '1px solid var(--border-color)',
          paddingBottom: '12px',
          marginBottom: '16px',
        }}
      >
        <h3 style={{ fontSize: '16px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '6px' }}>
          <Filter size={18} /> Filters
        </h3>
        <button
          onClick={() => {
            setMinP('');
            setMaxP('');
            onClear();
          }}
          style={{ fontSize: '13px', color: 'var(--primary-2874f0)', fontWeight: 600, cursor: 'pointer', background: 'none', border: 'none' }}
        >
          CLEAR ALL
        </button>
      </div>

      {/* Price Range Filter */}
      <div style={{ marginBottom: '20px' }}>
        <h4 style={{ fontSize: '14px', fontWeight: 600, marginBottom: '10px' }}>Price Range (₹)</h4>
        <div style={{ display: 'flex', gap: '8px', alignItems: 'center', marginBottom: '8px' }}>
          <input
            type="number"
            placeholder="Min"
            value={minP}
            onChange={(e) => setMinP(e.target.value)}
            style={{ width: '80px', padding: '4px 8px', fontSize: '12px', border: '1px solid #ccc', borderRadius: '3px' }}
          />
          <span style={{ fontSize: '12px', color: '#666' }}>to</span>
          <input
            type="number"
            placeholder="Max"
            value={maxP}
            onChange={(e) => setMaxP(e.target.value)}
            style={{ width: '80px', padding: '4px 8px', fontSize: '12px', border: '1px solid #ccc', borderRadius: '3px' }}
          />
        </div>
        <button
          onClick={handlePriceApply}
          style={{
            width: '100%',
            padding: '4px',
            fontSize: '12px',
            backgroundColor: '#2874f0',
            color: '#fff',
            border: 'none',
            borderRadius: '3px',
            fontWeight: 600,
            cursor: 'pointer',
          }}
        >
          Apply Price
        </button>
      </div>

      {/* Category Filter */}
      <div style={{ marginBottom: '20px' }}>
        <h4 style={{ fontSize: '14px', fontWeight: 600, marginBottom: '10px' }}>Categories</h4>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '200px', overflowY: 'auto' }}>
          {categories.map((c) => (
            <label
              key={c.id}
              style={{
                fontSize: '13px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                color: selectedCategoryId === c.id ? 'var(--primary-2874f0)' : 'var(--text-main)',
                fontWeight: selectedCategoryId === c.id ? 700 : 400,
              }}
            >
              <input
                type="radio"
                name="category"
                checked={selectedCategoryId === c.id}
                onChange={() =>
                  onFilterChange({
                    category_id: c.id,
                    brand_id: selectedBrandId,
                    min_rating: selectedMinRating,
                    min_price: selectedMinPrice,
                    max_price: selectedMaxPrice,
                  })
                }
              />
              {c.name}
            </label>
          ))}
        </div>
      </div>

      {/* Brand Filter */}
      <div style={{ marginBottom: '20px' }}>
        <h4 style={{ fontSize: '14px', fontWeight: 600, marginBottom: '10px' }}>Brands</h4>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '200px', overflowY: 'auto' }}>
          {brands.map((b) => (
            <label
              key={b.id}
              style={{
                fontSize: '13px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                color: selectedBrandId === b.id ? 'var(--primary-2874f0)' : 'var(--text-main)',
              }}
            >
              <input
                type="radio"
                name="brand"
                checked={selectedBrandId === b.id}
                onChange={() =>
                  onFilterChange({
                    category_id: selectedCategoryId,
                    brand_id: b.id,
                    min_rating: selectedMinRating,
                    min_price: selectedMinPrice,
                    max_price: selectedMaxPrice,
                  })
                }
              />
              {b.name}
            </label>
          ))}
        </div>
      </div>

      {/* Rating Filter */}
      <div>
        <h4 style={{ fontSize: '14px', fontWeight: 600, marginBottom: '10px' }}>Customer Ratings</h4>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {[4, 3, 2, 1].map((stars) => (
            <label
              key={stars}
              style={{
                fontSize: '13px',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
              }}
            >
              <input
                type="radio"
                name="rating"
                checked={selectedMinRating === stars}
                onChange={() =>
                  onFilterChange({
                    category_id: selectedCategoryId,
                    brand_id: selectedBrandId,
                    min_rating: stars,
                    min_price: selectedMinPrice,
                    max_price: selectedMaxPrice,
                  })
                }
              />
              <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                {stars} <Star size={12} fill="#ff9f00" color="#ff9f00" /> & above
              </span>
            </label>
          ))}
        </div>
      </div>
    </aside>
  );
};
