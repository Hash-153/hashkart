import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { ShieldCheck, CreditCard, Smartphone, Banknote, MapPin, Tag, AlertCircle } from 'lucide-react';
import { Address, Order, CheckoutPreview } from '../types';
import { api } from '../services/api';
import { useCart } from '../context/CartContext';
import { useAuth } from '../context/AuthContext';

export const CheckoutPage: React.FC = () => {
  const { user } = useAuth();
  const { cart, refreshCart } = useCart();
  const navigate = useNavigate();

  const [addresses, setAddresses] = useState<Address[]>([]);
  const [selectedAddressId, setSelectedAddressId] = useState<number | null>(null);
  const [couponCode, setCouponCode] = useState<string>('');
  const [appliedCoupon, setAppliedCoupon] = useState<string>('');
  const [preview, setPreview] = useState<CheckoutPreview | null>(null);
  const [paymentMethod, setPaymentMethod] = useState<string>('CARD');
  const [simulateFailure, setSimulateFailure] = useState<boolean>(false);
  const [processing, setProcessing] = useState<boolean>(false);
  const [error, setError] = useState<string>('');

  // Address creation form state
  const [showAddressForm, setShowAddressForm] = useState<boolean>(false);
  const [newAddr, setNewAddr] = useState({
    full_name: '',
    phone_number: '',
    address_line1: '',
    address_line2: '',
    city: '',
    state: '',
    postal_code: '',
    country: 'India',
    address_type: 'HOME',
  });

  useEffect(() => {
    if (!user) {
      navigate('/login?redirect=/checkout');
      return;
    }

    const fetchAddrs = async () => {
      try {
        const list = await api.getAddresses();
        setAddresses(list);
        if (list.length > 0) {
          const def = list.find((a) => a.is_default) || list[0];
          setSelectedAddressId(def.id);
        } else {
          setShowAddressForm(true);
        }
      } catch (err) {
        console.error('Error loading delivery addresses:', err);
      }
    };
    fetchAddrs();
  }, [user, navigate]);

  // Load backend checkout preview whenever selected address or coupon changes
  useEffect(() => {
    if (selectedAddressId) {
      api
        .getCheckoutPreview(selectedAddressId, appliedCoupon)
        .then((prevData) => setPreview(prevData))
        .catch((err) => console.error('Error fetching preview:', err));
    }
  }, [selectedAddressId, appliedCoupon]);

  const handleApplyCoupon = async () => {
    if (!couponCode.trim() || !selectedAddressId) return;
    try {
      const prevData = await api.getCheckoutPreview(selectedAddressId, couponCode.trim());
      setPreview(prevData);
      setAppliedCoupon(couponCode.trim());
    } catch (err: any) {
      setError(err.message || 'Invalid coupon.');
    }
  };

  const handleAddAddressSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const added = await api.addAddress(newAddr);
      setAddresses([...addresses, added]);
      setSelectedAddressId(added.id);
      setShowAddressForm(false);
    } catch (err: any) {
      alert(err.message || 'Failed to add address');
    }
  };

  const handlePlaceOrder = async () => {
    if (!selectedAddressId) {
      alert('Please select or add a delivery address.');
      return;
    }

    setProcessing(true);
    setError('');

    const idempotencyKey = `idem_${Date.now()}_${Math.random().toString(36).substring(2, 8)}`;

    try {
      const order: Order = await api.processCheckout(
        {
          address_id: selectedAddressId,
          coupon_code: appliedCoupon ? appliedCoupon : undefined,
          payment_method: paymentMethod,
          mock_payment_details: {
            simulate_failure: simulateFailure,
          },
        },
        idempotencyKey
      );

      await refreshCart();
      navigate(`/orders/${order.order_number}?placed=true`);
    } catch (err: any) {
      setError(err.message || 'Order processing failed. Please try again.');
    } finally {
      setProcessing(false);
    }
  };

  if (!cart || cart.items.length === 0) {
    return <div style={{ padding: '60px', textAlign: 'center' }}>Your cart is empty.</div>;
  }

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 360px', gap: '16px', marginTop: '16px' }}>
      {/* Checkout Steps */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        {/* Step 1: Address Selection */}
        <div style={{ backgroundColor: 'var(--bg-card)', padding: '20px', borderRadius: '4px', border: '1px solid var(--border-color)' }}>
          <h2 style={{ fontSize: '16px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '16px' }}>
            <MapPin size={20} color="var(--primary-2874f0)" /> 1. Select Delivery Address
          </h2>

          {addresses.map((a) => (
            <label
              key={a.id}
              style={{
                display: 'flex',
                gap: '12px',
                padding: '12px',
                border: selectedAddressId === a.id ? '2px solid var(--primary-2874f0)' : '1px solid var(--border-color)',
                borderRadius: '4px',
                marginBottom: '10px',
                cursor: 'pointer',
                backgroundColor: selectedAddressId === a.id ? 'var(--primary-light)' : 'transparent',
              }}
            >
              <input
                type="radio"
                name="address"
                checked={selectedAddressId === a.id}
                onChange={() => setSelectedAddressId(a.id)}
              />
              <div>
                <strong style={{ fontSize: '14px' }}>{a.full_name}</strong> ({a.address_type}) — {a.phone_number}
                <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginTop: '4px' }}>
                  {a.address_line1}, {a.address_line2 ? `${a.address_line2}, ` : ''}{a.city}, {a.state} - {a.postal_code}
                </p>
              </div>
            </label>
          ))}

          {!showAddressForm && (
            <button
              onClick={() => setShowAddressForm(true)}
              style={{ fontSize: '14px', color: 'var(--primary-2874f0)', fontWeight: 700, marginTop: '8px', background: 'none', border: 'none', cursor: 'pointer' }}
            >
              + Add New Address
            </button>
          )}

          {showAddressForm && (
            <form onSubmit={handleAddAddressSubmit} style={{ marginTop: '16px', display: 'grid', gap: '12px', gridTemplateColumns: '1fr 1fr' }}>
              <input type="text" placeholder="Full Name" required value={newAddr.full_name} onChange={(e) => setNewAddr({ ...newAddr, full_name: e.target.value })} style={{ padding: '8px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
              <input type="text" placeholder="10-digit Phone" required value={newAddr.phone_number} onChange={(e) => setNewAddr({ ...newAddr, phone_number: e.target.value })} style={{ padding: '8px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
              <input type="text" placeholder="Address Line 1" required value={newAddr.address_line1} onChange={(e) => setNewAddr({ ...newAddr, address_line1: e.target.value })} style={{ gridColumn: 'span 2', padding: '8px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
              <input type="text" placeholder="City" required value={newAddr.city} onChange={(e) => setNewAddr({ ...newAddr, city: e.target.value })} style={{ padding: '8px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
              <input type="text" placeholder="State" required value={newAddr.state} onChange={(e) => setNewAddr({ ...newAddr, state: e.target.value })} style={{ padding: '8px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
              <input type="text" placeholder="Pincode" required value={newAddr.postal_code} onChange={(e) => setNewAddr({ ...newAddr, postal_code: e.target.value })} style={{ padding: '8px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
              <button type="submit" className="btn-primary" style={{ gridColumn: 'span 2' }}>
                Save & Use Address
              </button>
            </form>
          )}
        </div>

        {/* Step 2: Payment Simulator Selection */}
        <div style={{ backgroundColor: 'var(--bg-card)', padding: '20px', borderRadius: '4px', border: '1px solid var(--border-color)' }}>
          <h2 style={{ fontSize: '16px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '16px' }}>
            <CreditCard size={20} color="var(--primary-2874f0)" /> 2. Payment Options (Local Simulator)
          </h2>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <label style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '14px', cursor: 'pointer' }}>
              <input type="radio" name="payment" value="CARD" checked={paymentMethod === 'CARD'} onChange={() => setPaymentMethod('CARD')} />
              <CreditCard size={18} /> Mock Credit / Debit Card
            </label>

            <label style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '14px', cursor: 'pointer' }}>
              <input type="radio" name="payment" value="UPI" checked={paymentMethod === 'UPI'} onChange={() => setPaymentMethod('UPI')} />
              <Smartphone size={18} /> Mock UPI / QR (Google Pay, PhonePe, Paytm)
            </label>

            <label style={{ display: 'flex', alignItems: 'center', gap: '10px', fontSize: '14px', cursor: 'pointer' }}>
              <input type="radio" name="payment" value="COD" checked={paymentMethod === 'COD'} onChange={() => setPaymentMethod('COD')} />
              <Banknote size={18} /> Cash on Delivery (COD)
            </label>
          </div>

          <div style={{ marginTop: '16px', paddingTop: '12px', borderTop: '1px dashed var(--border-color)', fontSize: '13px' }}>
            <label style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--danger-red)', fontWeight: 600 }}>
              <input type="checkbox" checked={simulateFailure} onChange={(e) => setSimulateFailure(e.target.checked)} />
              Simulate Gateway Payment Failure (Test Scenario Hook)
            </label>
          </div>
        </div>
      </div>

      {/* Order Summary & Coupon Sidebar */}
      <div style={{ backgroundColor: 'var(--bg-card)', padding: '20px', borderRadius: '4px', border: '1px solid var(--border-color)', height: 'fit-content' }}>
        <h3 style={{ fontSize: '14px', fontWeight: 700, color: 'var(--text-muted)', borderBottom: '1px solid var(--border-color)', paddingBottom: '12px', textTransform: 'uppercase' }}>
          Apply Promo Coupon
        </h3>

        <div style={{ display: 'flex', gap: '8px', margin: '16px 0 8px' }}>
          <input
            type="text"
            placeholder="Enter Code (e.g. WELCOME10)"
            value={couponCode}
            onChange={(e) => setCouponCode(e.target.value.toUpperCase())}
            style={{ flex: 1, padding: '8px 12px', border: '1px solid var(--border-dark)', borderRadius: '4px' }}
          />
          <button onClick={handleApplyCoupon} className="btn-secondary" style={{ padding: '8px 16px', fontSize: '13px' }}>
            Apply
          </button>
        </div>

        {appliedCoupon && (
          <p style={{ fontSize: '12px', color: 'var(--success-green)', marginBottom: '12px', fontWeight: 600 }}>
            Coupon '{appliedCoupon}' Applied!
          </p>
        )}

        <h3 style={{ fontSize: '14px', fontWeight: 700, color: 'var(--text-muted)', borderBottom: '1px solid var(--border-color)', paddingBottom: '12px', marginTop: '16px', textTransform: 'uppercase' }}>
          Authoritative Pricing Breakdown
        </h3>

        {preview ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '10px', padding: '12px 0', fontSize: '14px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <span>Subtotal</span>
              <span>₹{preview.subtotal.toLocaleString('en-IN')}</span>
            </div>
            {preview.promotion_discount > 0 && (
              <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--success-green)' }}>
                <span>Promotional Offer</span>
                <span>-₹{preview.promotion_discount.toLocaleString('en-IN')}</span>
              </div>
            )}
            {preview.coupon_discount > 0 && (
              <div style={{ display: 'flex', justifyContent: 'space-between', color: 'var(--success-green)', fontWeight: 700 }}>
                <span>Coupon Discount</span>
                <span>-₹{preview.coupon_discount.toLocaleString('en-IN')}</span>
              </div>
            )}
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <span>GST (18%)</span>
              <span>₹{preview.tax.toLocaleString('en-IN')}</span>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between' }}>
              <span>Shipping</span>
              <span>{preview.shipping === 0 ? 'FREE' : `₹${preview.shipping}`}</span>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', padding: '12px 0', fontSize: '18px', fontWeight: 800, borderTop: '1px solid var(--border-color)' }}>
              <span>Grand Total</span>
              <span>₹{preview.grand_total.toLocaleString('en-IN')}</span>
            </div>
          </div>
        ) : (
          <div style={{ padding: '16px 0', textAlign: 'center', fontSize: '13px' }}>Calculating backend preview...</div>
        )}

        {error && <div style={{ color: 'var(--danger-red)', fontSize: '13px', marginBottom: '12px' }}>{error}</div>}

        <button
          onClick={handlePlaceOrder}
          disabled={processing || !preview}
          className="btn-primary"
          style={{ width: '100%', padding: '14px', fontSize: '16px' }}
        >
          {processing ? 'Processing Order...' : 'CONFIRM & PLACE ORDER'}
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginTop: '16px', fontSize: '12px', color: 'var(--text-muted)' }}>
          <ShieldCheck size={18} color="var(--success-green)" /> Concurrency-safe inventory lock & 100% money math precision.
        </div>
      </div>
    </div>
  );
};
