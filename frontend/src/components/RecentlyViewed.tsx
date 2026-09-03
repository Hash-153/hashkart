import React, { useEffect, useState } from 'react';
import { Product } from '../types';
import { api } from '../services/api';
import { ProductCard } from './ProductCard';
import { Clock, Trash2 } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export const RecentlyViewed: React.FC = () => {
  const { user } = useAuth();
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    if (user) {
      api.getRecentlyViewed().then(setProducts).catch(console.error);
    }
  }, [user]);

  if (!user || products.length === 0) return null;

  const handleClear = async () => {
    try {
      await api.clearRecentlyViewed();
      setProducts([]);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <section
      style={{
        backgroundColor: '#ffffff',
        borderRadius: '4px',
        padding: '20px',
        marginBottom: '20px',
        boxShadow: '0 1px 3px rgba(0,0,0,0.08)',
      }}
    >
      <div
        style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          borderBottom: '1px solid #f0f0f0',
          paddingBottom: '12px',
          marginBottom: '16px',
        }}
      >
        <h2 style={{ fontSize: '18px', fontWeight: 700, color: '#212121', display: 'flex', alignItems: 'center', gap: '8px', margin: 0 }}>
          <Clock size={20} color="#2874f0" /> Recently Viewed Products
        </h2>
        <button
          onClick={handleClear}
          style={{
            background: 'none',
            border: 'none',
            color: '#878787',
            cursor: 'pointer',
            fontSize: '13px',
            display: 'flex',
            alignItems: 'center',
            gap: '4px',
          }}
        >
          <Trash2 size={14} /> Clear History
        </button>
      </div>

      <div
        style={{
          display: 'flex',
          gap: '16px',
          overflowX: 'auto',
          paddingBottom: '8px',
        }}
      >
        {products.map((p) => (
          <div key={p.id} style={{ minWidth: '200px', maxWidth: '220px', flexShrink: 0 }}>
            <ProductCard product={p} />
          </div>
        ))}
      </div>
    </section>
  );
};
