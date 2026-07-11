import React, { useState } from 'react';
import { Category, Brand, SearchFacets } from '../types';
import { Filter, Star } from 'lucide-react';

interface FilterSidebarProps {
  categories: Category[];
  brands: Brand[];
  facets?: SearchFacets;
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
  facets,
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

  const handleCategoryClick = (catId: number) => {
    if (selectedCategoryId === catId) {
      // Toggle off
      onFilterChange({
        category_id: undefined,
        brand_id: selectedBrandId,
        min_rating: selectedMinRating,
        min_price: selectedMinPrice,
        max_price: selectedMaxPrice,
      });
    } else {
      // Select new category
      onFilterChange({
        category_id: catId,
        brand_id: selectedBrandId,
        min_rating: selectedMinRating,
        min_price: selectedMinPrice,
        max_price: selectedMaxPrice,
      });
    }
  };

  const handleBrandClick = (brandId: number) => {
    if (selectedBrandId === brandId) {
      // Toggle off
      onFilterChange({
        category_id: selectedCategoryId,
        brand_id: undefined,
        min_rating: selectedMinRating,
        min_price: selectedMinPrice,
        max_price: selectedMaxPrice,
      });
    } else {
      // Select new brand
      onFilterChange({
        category_id: selectedCategoryId,
        brand_id: brandId,
        min_rating: selectedMinRating,
        min_price: selectedMinPrice,
        max_price: selectedMaxPrice,
      });
    }
  };

  const handleRatingClick = (stars: number) => {
    if (selectedMinRating === stars) {
      // Toggle off
      onFilterChange({
        category_id: selectedCategoryId,
        brand_id: selectedBrandId,
        min_rating: undefined,
        min_price: selectedMinPrice,
        max_price: selectedMaxPrice,
      });
    } else {
      onFilterChange({
        category_id: selectedCategoryId,
        brand_id: selectedBrandId,
        min_rating: stars,
        min_price: selectedMinPrice,
        max_price: selectedMaxPrice,
      });
    }
  };

  // Build facet lookup map for fast brand counts
  const facetBrandCountMap = new Map<number, number>();
  if (facets?.brands) {
    facets.brands.forEach((fb) => {
      facetBrandCountMap.set(fb.id, fb.count);
    });
  }

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
            padding: '6px',
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
          {categories.map((c) => {
            const isSelected = selectedCategoryId === c.id;
            return (
              <label
                key={c.id}
                onClick={(e) => {
                  e.preventDefault();
                  handleCategoryClick(c.id);
                }}
                style={{
                  fontSize: '13px',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  color: isSelected ? 'var(--primary-2874f0)' : 'var(--text-main)',
                  fontWeight: isSelected ? 700 : 400,
                }}
              >
                <input
                  type="checkbox"
                  checked={isSelected}
                  readOnly
                  style={{ cursor: 'pointer' }}
                />
                {c.name}
              </label>
            );
          })}
        </div>
      </div>

      {/* Brand Filter */}
      <div style={{ marginBottom: '20px' }}>
        <h4 style={{ fontSize: '14px', fontWeight: 600, marginBottom: '10px' }}>Brands</h4>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px', maxHeight: '220px', overflowY: 'auto' }}>
          {brands.map((b) => {
            const isSelected = selectedBrandId === b.id;
            const count = facetBrandCountMap.has(b.id) ? facetBrandCountMap.get(b.id) : b.product_count;
            return (
              <label
                key={b.id}
                onClick={(e) => {
                  e.preventDefault();
                  handleBrandClick(b.id);
                }}
                style={{
                  fontSize: '13px',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  gap: '8px',
                  color: isSelected ? 'var(--primary-2874f0)' : 'var(--text-main)',
                  fontWeight: isSelected ? 700 : 400,
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <input
                    type="checkbox"
                    checked={isSelected}
                    readOnly
                    style={{ cursor: 'pointer' }}
                  />
                  <span>{b.name}</span>
                </div>
                {count !== undefined && (
                  <span style={{ fontSize: '11px', color: '#888', fontWeight: 400 }}>({count})</span>
                )}
              </label>
            );
          })}
        </div>
      </div>

      {/* Rating Filter */}
      <div>
        <h4 style={{ fontSize: '14px', fontWeight: 600, marginBottom: '10px' }}>Customer Ratings</h4>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {[4, 3, 2, 1].map((stars) => {
            const isSelected = selectedMinRating === stars;
            return (
              <label
                key={stars}
                onClick={(e) => {
                  e.preventDefault();
                  handleRatingClick(stars);
                }}
                style={{
                  fontSize: '13px',
                  cursor: 'pointer',
                  display: 'flex',
                  alignItems: 'center',
                  gap: '8px',
                  color: isSelected ? 'var(--primary-2874f0)' : 'var(--text-main)',
                  fontWeight: isSelected ? 700 : 400,
                }}
              >
                <input
                  type="checkbox"
                  checked={isSelected}
                  readOnly
                  style={{ cursor: 'pointer' }}
                />
                <span style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                  {stars} <Star size={12} fill="#ff9f00" color="#ff9f00" /> & above
                </span>
              </label>
            );
          })}
        </div>
      </div>
    </aside>
  );
};
