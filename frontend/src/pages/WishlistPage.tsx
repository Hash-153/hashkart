import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Trash2, ShoppingCart, Heart, ArrowRight } from 'lucide-react';
import { Wishlist } from '../types';
import { api } from '../services/api';
import { useCart } from '../context/CartContext';
import { useToast } from '../components/ui/Toast';

export const WishlistPage: React.FC = () => {
  const [wishlist, setWishlist] = useState<Wishlist | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const { refreshCart } = useCart();
  const { showToast } = useToast();

  const fetchWishlist = async () => {
    try {
      const data = await api.getWishlist();
      setWishlist(data);
    } catch (err) {
      console.error('Error fetching wishlist:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchWishlist();
  }, []);

  const handleRemove = async (itemId: number, title?: string) => {
    try {
      const updated = await api.removeFromWishlist(itemId);
      setWishlist(updated);
      showToast('info', 'Item Removed', title ? `${title} removed from your wishlist.` : 'Item removed from wishlist.');
    } catch (err: any) {
      showToast('error', 'Error', err.message || 'Could not remove item.');
    }
  };

  const handleMoveToCart = async (itemId: number, title?: string) => {
    try {
      const updated = await api.moveWishlistItemToCart(itemId);
      setWishlist(updated);
      await refreshCart();
      showToast('success', 'Moved to Cart', title ? `${title} moved to your shopping basket.` : 'Item moved to cart.');
    } catch (err: any) {
      showToast('error', 'Error', err.message || 'Could not move item to cart.');
    }
  };

  if (loading) {
    return (
      <div style={{ maxWidth: '1000px', margin: '40px auto', padding: '60px', textAlign: 'center' }}>
        <p className="text-gray-500 font-semibold">Loading your wishlist...</p>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '1000px', margin: '24px auto', padding: '0 16px' }}>
      <div
        style={{
          backgroundColor: 'var(--bg-card)',
          padding: '24px',
          borderRadius: '8px',
          border: '1px solid var(--border-color)',
          boxShadow: '0 1px 3px rgba(0,0,0,0.05)',
        }}
      >
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            borderBottom: '1px solid var(--border-color)',
            paddingBottom: '16px',
            marginBottom: '24px',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
            <div style={{ padding: '8px', backgroundColor: '#ffebee', borderRadius: '8px', color: '#ff4343' }}>
              <Heart size={20} fill="#ff4343" />
            </div>
            <div>
              <h1 style={{ fontSize: '20px', fontWeight: 800, color: '#212121', margin: 0 }}>
                My Wishlist
              </h1>
              <span style={{ fontSize: '12px', color: '#666' }}>
                {wishlist?.items.length || 0} {wishlist?.items.length === 1 ? 'item' : 'items'} saved
              </span>
            </div>
          </div>

          <Link
            to="/products"
            style={{
              fontSize: '13px',
              color: '#2874f0',
              fontWeight: 600,
              textDecoration: 'none',
              display: 'flex',
              alignItems: 'center',
              gap: '4px',
            }}
          >
            Continue Shopping <ArrowRight size={14} />
          </Link>
        </div>

        {!wishlist || wishlist.items.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '60px 20px' }}>
            <div style={{ width: '64px', height: '64px', borderRadius: '50%', backgroundColor: '#f5f5f5', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 16px', color: '#999' }}>
              <Heart size={32} />
            </div>
            <h3 style={{ fontSize: '16px', fontWeight: 700, color: '#212121', marginBottom: '6px' }}>
              Your Wishlist is Empty
            </h3>
            <p style={{ fontSize: '13px', color: '#666', marginBottom: '20px' }}>
              Explore our wide range of products and click the heart icon to save your favorites for later!
            </p>
            <Link
              to="/products"
              className="btn-primary"
              style={{ padding: '10px 24px', display: 'inline-block', textDecoration: 'none', fontWeight: 600, fontSize: '13px' }}
            >
              Explore Products
            </Link>
          </div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {wishlist.items.map((item) => {
              const variant = item.variant;
              const price = variant.price || 0;
              const discountPrice = variant.discount_price;
              const effectivePrice = discountPrice || price;
              const discountPercent =
                discountPrice && price > 0 ? Math.round(((price - discountPrice) / price) * 100) : 0;

              const img =
                variant.images && variant.images.length > 0
                  ? variant.images[0].image_url
                  : 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=800&q=80';

              const title = variant.title || 'Product Item';

              return (
                <div
                  key={item.id}
                  style={{
                    display: 'flex',
                    gap: '20px',
                    alignItems: 'center',
                    borderBottom: '1px solid var(--border-color)',
                    paddingBottom: '20px',
                  }}
                >
                  <img
                    src={img}
                    alt={title}
                    style={{
                      width: '90px',
                      height: '90px',
                      objectFit: 'contain',
                      borderRadius: '6px',
                      backgroundColor: '#f9f9f9',
                      padding: '4px',
                    }}
                  />

                  <div style={{ flex: 1 }}>
                    <h3 style={{ fontSize: '15px', fontWeight: 600, color: '#212121', margin: '0 0 6px' }}>
                      {title}
                    </h3>
                    <div style={{ display: 'flex', alignItems: 'baseline', gap: '10px' }}>
                      <span style={{ fontSize: '18px', fontWeight: 800, color: '#212121' }}>
                        ₹{effectivePrice.toLocaleString('en-IN')}
                      </span>
                      {discountPrice && (
                        <>
                          <span style={{ fontSize: '13px', color: '#878787', textDecoration: 'line-through' }}>
                            ₹{price.toLocaleString('en-IN')}
                          </span>
                          <span style={{ fontSize: '13px', color: '#388e3c', fontWeight: 700 }}>
                            {discountPercent}% off
                          </span>
                        </>
                      )}
                    </div>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                    <button
                      onClick={() => handleMoveToCart(item.id, title)}
                      className="btn-primary"
                      style={{
                        padding: '8px 18px',
                        fontSize: '13px',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '6px',
                        fontWeight: 600,
                      }}
                    >
                      <ShoppingCart size={15} /> Move to Cart
                    </button>

                    <button
                      onClick={() => handleRemove(item.id, title)}
                      title="Remove from Wishlist"
                      style={{
                        color: '#878787',
                        padding: '8px',
                        background: 'none',
                        border: '1px solid #e0e0e0',
                        borderRadius: '4px',
                        cursor: 'pointer',
                        transition: 'all 0.15s ease',
                      }}
                      onMouseOver={(e) => {
                        e.currentTarget.style.color = '#ff4343';
                        e.currentTarget.style.borderColor = '#ff4343';
                      }}
                      onMouseOut={(e) => {
                        e.currentTarget.style.color = '#878787';
                        e.currentTarget.style.borderColor = '#e0e0e0';
                      }}
                    >
                      <Trash2 size={16} />
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
};
