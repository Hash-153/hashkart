import React from 'react';
import { X } from 'lucide-react';

interface FilterChipsProps {
  query?: string;
  categoryName?: string;
  brandName?: string;
  minRating?: number;
  minPrice?: number;
  maxPrice?: number;
  onRemoveQuery?: () => void;
  onRemoveCategory?: () => void;
  onRemoveBrand?: () => void;
  onRemoveRating?: () => void;
  onRemovePrice?: () => void;
  onClearAll: () => void;
}

export const FilterChips: React.FC<FilterChipsProps> = ({
  query,
  categoryName,
  brandName,
  minRating,
  minPrice,
  maxPrice,
  onRemoveQuery,
  onRemoveCategory,
  onRemoveBrand,
  onRemoveRating,
  onRemovePrice,
  onClearAll,
}) => {
  const hasActiveFilters = Boolean(query || categoryName || brandName || minRating || minPrice || maxPrice);

  if (!hasActiveFilters) return null;

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '8px', flexWrap: 'wrap', marginBottom: '16px' }}>
      <span style={{ fontSize: '12px', fontWeight: 700, color: '#666' }}>Active Filters:</span>

      {query && (
        <span
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '4px',
            padding: '4px 10px',
            backgroundColor: '#e8f0fe',
            color: '#1a73e8',
            borderRadius: '16px',
            fontSize: '12px',
            fontWeight: 600,
          }}
        >
          Keyword: "{query}"
          {onRemoveQuery && <X size={14} style={{ cursor: 'pointer' }} onClick={onRemoveQuery} />}
        </span>
      )}

      {categoryName && (
        <span
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '4px',
            padding: '4px 10px',
            backgroundColor: '#e8f0fe',
            color: '#1a73e8',
            borderRadius: '16px',
            fontSize: '12px',
            fontWeight: 600,
          }}
        >
          Category: {categoryName}
          {onRemoveCategory && <X size={14} style={{ cursor: 'pointer' }} onClick={onRemoveCategory} />}
        </span>
      )}

      {brandName && (
        <span
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '4px',
            padding: '4px 10px',
            backgroundColor: '#e8f0fe',
            color: '#1a73e8',
            borderRadius: '16px',
            fontSize: '12px',
            fontWeight: 600,
          }}
        >
          Brand: {brandName}
          {onRemoveBrand && <X size={14} style={{ cursor: 'pointer' }} onClick={onRemoveBrand} />}
        </span>
      )}

      {minRating && (
        <span
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '4px',
            padding: '4px 10px',
            backgroundColor: '#e8f0fe',
            color: '#1a73e8',
            borderRadius: '16px',
            fontSize: '12px',
            fontWeight: 600,
          }}
        >
          Rating: {minRating}★ & above
          {onRemoveRating && <X size={14} style={{ cursor: 'pointer' }} onClick={onRemoveRating} />}
        </span>
      )}

      {(minPrice || maxPrice) && (
        <span
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '4px',
            padding: '4px 10px',
            backgroundColor: '#e8f0fe',
            color: '#1a73e8',
            borderRadius: '16px',
            fontSize: '12px',
            fontWeight: 600,
          }}
        >
          Price: ₹{minPrice || 0} - ₹{maxPrice || 'Any'}
          {onRemovePrice && <X size={14} style={{ cursor: 'pointer' }} onClick={onRemovePrice} />}
        </span>
      )}

      <button
        onClick={onClearAll}
        style={{
          background: 'none',
          border: 'none',
          color: '#d93025',
          fontSize: '12px',
          fontWeight: 700,
          cursor: 'pointer',
          marginLeft: '4px',
        }}
      >
        Clear All
      </button>
    </div>
  );
};
