import React, { useEffect, useState } from 'react';
import { Trash2, ShoppingCart } from 'lucide-react';
import { Wishlist } from '../types';
import { api } from '../services/api';
import { useCart } from '../context/CartContext';

export const WishlistPage: React.FC = () => {
  const [wishlist, setWishlist] = useState<Wishlist | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const { refreshCart } = useCart();

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

  const handleRemove = async (itemId: number) => {
    try {
      const updated = await api.removeFromWishlist(itemId);
      setWishlist(updated);
    } catch (err: any) {
      alert(err.message);
    }
  };

  const handleMoveToCart = async (itemId: number) => {
    try {
      const updated = await api.moveWishlistItemToCart(itemId);
      setWishlist(updated);
      await refreshCart();
      alert('Moved item to Cart!');
    } catch (err: any) {
      alert(err.message);
    }
  };

  if (loading) return <div style={{ padding: '60px', textAlign: 'center' }}>Loading wishlist...</div>;

  return (
    <div style={{ backgroundColor: 'var(--bg-card)', padding: '24px', borderRadius: '4px', border: '1px solid var(--border-color)', marginTop: '16px' }}>
      <h2 style={{ fontSize: '20px', fontWeight: 700, borderBottom: '1px solid var(--border-color)', paddingBottom: '12px', marginBottom: '20px' }}>
        My Wishlist ({wishlist?.items.length || 0} Items)
      </h2>

      {!wishlist || wishlist.items.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '40px 0', color: 'var(--text-muted)' }}>
          Your wishlist is empty. Save items you like to buy later!
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {wishlist.items.map((item) => {
            const variant = item.variant;
            const price = variant.discount_price || variant.price;
            const img = variant.images && variant.images.length > 0 ? variant.images[0].image_url : 'https://via.placeholder.com/100';

            return (
              <div key={item.id} style={{ display: 'flex', gap: '16px', alignItems: 'center', borderBottom: '1px solid var(--border-color)', paddingBottom: '16px' }}>
                <img src={img} alt={variant.title} style={{ width: '80px', height: '80px', objectFit: 'contain', borderRadius: '4px' }} />

                <div style={{ flex: 1 }}>
                  <h3 style={{ fontSize: '15px', fontWeight: 600 }}>{variant.title}</h3>
                  <div style={{ fontSize: '16px', fontWeight: 700, marginTop: '4px' }}>
                    ₹{price.toLocaleString('en-IN')}
                  </div>
                </div>

                <div style={{ display: 'flex', gap: '12px' }}>
                  <button
                    onClick={() => handleMoveToCart(item.id)}
                    className="btn-primary"
                    style={{ padding: '8px 16px', fontSize: '13px', display: 'flex', alignItems: 'center', gap: '6px' }}
                  >
                    <ShoppingCart size={14} /> Move to Cart
                  </button>

                  <button
                    onClick={() => handleRemove(item.id)}
                    style={{ color: 'var(--danger-red)', padding: '8px', background: 'none', border: 'none', cursor: 'pointer' }}
                  >
                    <Trash2 size={18} />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
