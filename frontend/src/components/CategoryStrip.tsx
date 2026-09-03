import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Category } from '../types';

interface CategoryStripProps {
  categories: Category[];
}

export const CategoryStrip: React.FC<CategoryStripProps> = ({ categories }) => {
  const navigate = useNavigate();

  return (
    <div className="category-strip">
      <div className="category-strip-container">
        {categories.map((cat) => (
          <div
            key={cat.id}
            className="category-pill-item"
            onClick={() => navigate(`/products?category_id=${cat.id}`)}
          >
            <div
              style={{
                width: '56px',
                height: '56px',
                borderRadius: '50%',
                backgroundColor: '#f1f3f6',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                overflow: 'hidden',
              }}
            >
              {cat.image_url ? (
                <img
                  src={cat.image_url}
                  alt={cat.name}
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                />
              ) : (
                <span style={{ fontSize: '20px' }}>📦</span>
              )}
            </div>
            <span className="category-pill-title">{cat.name}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
