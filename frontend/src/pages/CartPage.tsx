import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Trash2, Plus, Minus, ShieldCheck, ArrowRight, Heart, AlertCircle, Tag } from 'lucide-react';
import { useCart } from '../context/CartContext';

export const CartPage: React.FC = () => {
  const { cart, updateQuantity, removeItem, moveToWishlist } = useCart();
  const navigate = useNavigate();
  const [couponCode, setCouponCode] = useState<string>('');
  const [couponMsg, setCouponMsg] = useState<string | null>(null);

  if (!cart || cart.items.length === 0) {
    return (
      <div
        style={{
          backgroundColor: 'var(--bg-card)',
          padding: '60px 20px',
          textAlign: 'center',
          borderRadius: '4px',
          border: '1px solid var(--border-color)',
          marginTop: '16px',
        }}
      >
        <img
          src="https://images.unsplash.com/photo-1557821552-17105176677c?auto=format&fit=crop&w=400&q=80"
          alt="Empty Cart"
          style={{ height: '160px', objectFit: 'contain', marginBottom: '16px' }}
        />
        <h2 style={{ fontSize: '20px', fontWeight: 700 }}>Your Shopping Cart is Empty</h2>
        <p style={{ color: 'var(--text-muted)', marginTop: '6px' }}>Explore our catalog and add items to your cart!</p>
        <Link to="/products" className="btn-primary" style={{ marginTop: '20px', display: 'inline-flex' }}>
          Shop Now
        </Link>
      </div>
    );
  }

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 340px', gap: '16px', marginTop: '16px' }}>
      {/* Items List */}
      <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: '4px', border: '1px solid var(--border-color)', padding: '16px' }}>
        <h2 style={{ fontSize: '18px', fontWeight: 700, borderBottom: '1px solid var(--border-color)', paddingBottom: '12px', marginBottom: '16px' }}>
          My Shopping Cart ({cart.item_count} Items)
        </h2>

        {/* Stock & Price Warnings Banner */}
        {cart.stock_warnings && cart.stock_warnings.length > 0 && (
          <div style={{ backgroundColor: '#fff3cd', color: '#856404', padding: '12px', borderRadius: '4px', marginBottom: '16px', display: 'flex', gap: '8px', alignItems: 'center' }}>
            <AlertCircle size={18} />
            <div style={{ fontSize: '13px' }}>{cart.stock_warnings.join(' | ')}</div>
          </div>
        )}

        {cart.items.map((item) => {
          const variant = item.variant;
          const unitPrice = variant.discount_price || variant.price;
          const primaryImg = variant.images && variant.images.length > 0 ? variant.images[0].image_url : 'https://via.placeholder.com/100';

          return (
            <div key={item.id} style={{ display: 'flex', gap: '16px', borderBottom: '1px solid var(--border-color)', paddingBottom: '16px', marginBottom: '16px' }}>
              <img src={primaryImg} alt={variant.title} style={{ width: '80px', height: '80px', objectFit: 'contain', borderRadius: '4px' }} />

              <div style={{ flex: 1 }}>
                <h3 style={{ fontSize: '15px', fontWeight: 600 }}>{variant.title}</h3>
                <p style={{ fontSize: '12px', color: 'var(--text-muted)', margin: '4px 0 8px' }}>SKU: {variant.sku}</p>

                <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                  <span style={{ fontSize: '16px', fontWeight: 700 }}>₹{unitPrice.toLocaleString('en-IN')}</span>
                  {variant.discount_price && (
                    <span style={{ fontSize: '13px', color: 'var(--text-muted)', textDecoration: 'line-through' }}>
                      ₹{variant.price.toLocaleString('en-IN')}
                    </span>
                  )}
                </div>

                {/* Quantity Controls & Move to Wishlist */}
                <div style={{ display: 'flex', alignItems: 'center', gap: '16px', marginTop: '12px' }}>
                  <div style={{ display: 'flex', alignItems: 'center', border: '1px solid var(--border-dark)', borderRadius: '4px' }}>
                    <button
                      onClick={() => updateQuantity(item.id, Math.max(1, item.quantity - 1))}
                      style={{ padding: '6px 10px', background: 'none', border: 'none', cursor: 'pointer' }}
                    >
                      <Minus size={14} />
                    </button>
                    <span style={{ padding: '0 12px', fontSize: '14px', fontWeight: 700 }}>{item.quantity}</span>
                    <button
                      onClick={() => updateQuantity(item.id, item.quantity + 1)}
                      style={{ padding: '6px 10px', background: 'none', border: 'none', cursor: 'pointer' }}
                    >
                      <Plus size={14} />
                    </button>
                  </div>

                  <button
                    onClick={() => moveToWishlist(item.id)}
                    style={{ color: 'var(--primary-blue)', fontSize: '13px', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '4px', background: 'none', border: 'none', cursor: 'pointer' }}
                  >
                    <Heart size={14} /> Save to Wishlist
                  </button>

                  <button
                    onClick={() => removeItem(item.id)}
                    style={{ color: 'var(--danger-red)', fontSize: '13px', fontWeight: 600, display: 'flex', alignItems: 'center', gap: '4px', background: 'none', border: 'none', cursor: 'pointer' }}
                  >
                    <Trash2 size={14} /> Remove
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Price Summary Breakdown Sidebar */}
      <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: '4px', border: '1px solid var(--border-color)', padding: '16px', height: 'fit-content' }}>
        <h3 style={{ fontSize: '14px', fontWeight: 700, color: 'var(--text-muted)', borderBottom: '1px solid var(--border-color)', paddingBottom: '12px', textTransform: 'uppercase' }}>
          Price Details
        </h3>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px', padding: '16px 0', borderBottom: '1px dashed var(--border-color)', fontSize: '14px' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Price ({cart.item_count} items)</span>
            <span>₹{cart.subtotal.toLocaleString('en-IN')}</span>
          </div>

          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Estimated GST (18%)</span>
            <span>₹{cart.estimated_tax.toLocaleString('en-IN')}</span>
          </div>

          <div style={{ display: 'flex', justifyContent: 'space-between' }}>
            <span>Delivery Charges</span>
            <span style={{ color: cart.estimated_shipping === 0 ? 'var(--success-green)' : 'inherit', fontWeight: cart.estimated_shipping === 0 ? 700 : 400 }}>
              {cart.estimated_shipping === 0 ? 'FREE' : `₹${cart.estimated_shipping}`}
            </span>
          </div>
        </div>

        <div style={{ display: 'flex', justifyContent: 'space-between', padding: '16px 0', fontSize: '18px', fontWeight: 800 }}>
          <span>Total Amount</span>
          <span>₹{cart.grand_total.toLocaleString('en-IN')}</span>
        </div>

        <button
          onClick={() => navigate('/checkout')}
          className="btn-primary"
          style={{ width: '100%', fontSize: '15px', padding: '12px', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '8px' }}
        >
          PLACE ORDER <ArrowRight size={18} />
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginTop: '16px', fontSize: '12px', color: 'var(--text-muted)' }}>
          <ShieldCheck size={18} color="var(--success-green)" /> Safe and Secure Payments. 100% Authentic Products.
        </div>
      </div>
    </div>
  );
};
