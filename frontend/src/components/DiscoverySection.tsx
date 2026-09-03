import React from 'react';
import { DiscoverySection as DiscoverySectionType } from '../types';
import { ProductCard } from './ProductCard';
import { ChevronRight } from 'lucide-react';
import { Link } from 'react-router-dom';

interface DiscoverySectionProps {
  section: DiscoverySectionType;
  viewAllLink?: string;
}

export const DiscoverySection: React.FC<DiscoverySectionProps> = ({ section, viewAllLink }) => {
  if (!section.products || section.products.length === 0) return null;

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
        <div>
          <h2 style={{ fontSize: '20px', fontWeight: 700, color: '#212121', margin: 0 }}>{section.title}</h2>
          {section.subtitle && <p style={{ fontSize: '13px', color: '#878787', margin: '4px 0 0 0' }}>{section.subtitle}</p>}
        </div>
        {viewAllLink && (
          <Link
            to={viewAllLink}
            style={{
              fontSize: '14px',
              fontWeight: 700,
              color: '#2874f0',
              display: 'flex',
              alignItems: 'center',
              gap: '4px',
              textDecoration: 'none',
            }}
          >
            VIEW ALL <ChevronRight size={16} />
          </Link>
        )}
      </div>

      <div
        style={{
          display: 'flex',
          gap: '16px',
          overflowX: 'auto',
          paddingBottom: '8px',
          scrollBehavior: 'smooth',
        }}
      >
        {section.products.map((product) => (
          <div key={product.id} style={{ minWidth: '220px', maxWidth: '240px', flexShrink: 0 }}>
            <ProductCard product={product} />
          </div>
        ))}
      </div>
    </section>
  );
};
