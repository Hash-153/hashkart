import React, { useEffect, useState } from 'react';
import { CategoryStrip } from '../components/CategoryStrip';
import { DiscoverySection } from '../components/DiscoverySection';
import { RecentlyViewed } from '../components/RecentlyViewed';
import { Category, DiscoverySection as DiscoverySectionType } from '../types';
import { api } from '../services/api';
import { Zap, ShieldCheck, Truck, RefreshCw } from 'lucide-react';

export const Home: React.FC = () => {
  const [categories, setCategories] = useState<Category[]>([]);
  const [recommendedSec, setRecommendedSec] = useState<DiscoverySectionType | null>(null);
  const [bestSellingSec, setBestSellingSec] = useState<DiscoverySectionType | null>(null);
  const [dealsSec, setDealsSec] = useState<DiscoverySectionType | null>(null);
  const [newArrivalsSec, setNewArrivalsSec] = useState<DiscoverySectionType | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [cats, rec, best, deals, news] = await Promise.all([
          api.getCategories(),
          api.getRecommendedDiscovery(),
          api.getBestSellingDiscovery(),
          api.getDealsDiscovery(),
          api.getNewArrivalsDiscovery(),
        ]);
        setCategories(cats);
        setRecommendedSec(rec);
        setBestSellingSec(best);
        setDealsSec(deals);
        setNewArrivalsSec(news);
      } catch (err) {
        console.error('Error loading home discovery data:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  return (
    <div>
      {/* Category Pills Header */}
      <CategoryStrip categories={categories} />

      {/* Hero Banner Carousel (Flipkart Style Banner) */}
      <div
        style={{
          marginTop: '16px',
          borderRadius: '4px',
          overflow: 'hidden',
          backgroundColor: '#1a365d',
          color: '#ffffff',
          padding: '40px 32px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          background: 'linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%)',
          boxShadow: '0 4px 12px rgba(37,99,235,0.2)',
        }}
      >
        <div>
          <span
            style={{
              backgroundColor: 'var(--accent-yellow)',
              color: '#212121',
              fontWeight: 800,
              fontSize: '12px',
              padding: '4px 10px',
              borderRadius: '2px',
              textTransform: 'uppercase',
            }}
          >
            Big Festive Sale ⚡
          </span>
          <h1 style={{ fontSize: '32px', fontWeight: 800, margin: '12px 0 8px', fontFamily: 'var(--font-family-heading)' }}>
            Up to 60% Off Flagship Smartphones & Electronics
          </h1>
          <p style={{ opacity: 0.9, marginBottom: '20px', fontSize: '15px' }}>
            Instant Bank Card Discounts + Free Delivery on Orders Over ₹500
          </p>
          <a href="/products" className="btn-secondary">
            Explore Deals Now
          </a>
        </div>
        <img
          src="https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80"
          alt="Banner Product"
          style={{ height: '200px', objectFit: 'contain', borderRadius: '8px' }}
        />
      </div>

      {/* Value Proposition Highlights */}
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: '16px',
          margin: '24px 0',
          backgroundColor: '#ffffff',
          padding: '16px',
          borderRadius: '4px',
          border: '1px solid var(--border-color)',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <Truck size={28} color="var(--primary-2874f0)" />
          <div>
            <h4 style={{ fontSize: '14px', fontWeight: 700 }}>Superfast Delivery</h4>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Across 19,000+ PIN codes</p>
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <ShieldCheck size={28} color="var(--success-green)" />
          <div>
            <h4 style={{ fontSize: '14px', fontWeight: 700 }}>100% Original Products</h4>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Verified Brand Warranty</p>
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <RefreshCw size={28} color="var(--accent-orange)" />
          <div>
            <h4 style={{ fontSize: '14px', fontWeight: 700 }}>7 Days Easy Returns</h4>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Hassle-free replacement</p>
          </div>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <Zap size={28} color="var(--warning-amber)" />
          <div>
            <h4 style={{ fontSize: '14px', fontWeight: 700 }}>Best Price Guarantee</h4>
            <p style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Unbeatable deals daily</p>
          </div>
        </div>
      </div>

      {loading ? (
        <div style={{ padding: '40px', textAlign: 'center', backgroundColor: '#ffffff', borderRadius: '4px' }}>
          Loading discovery recommendations...
        </div>
      ) : (
        <>
          {recommendedSec && <DiscoverySection section={recommendedSec} viewAllLink="/products" />}
          {dealsSec && <DiscoverySection section={dealsSec} viewAllLink="/products?sort=discount_desc" />}
          {bestSellingSec && <DiscoverySection section={bestSellingSec} viewAllLink="/products?sort=popularity" />}
          {newArrivalsSec && <DiscoverySection section={newArrivalsSec} viewAllLink="/products?sort=newest" />}
          <RecentlyViewed />
        </>
      )}
    </div>
  );
};
