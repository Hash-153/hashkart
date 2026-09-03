import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Package, Truck, CheckCircle2, Clock, XCircle, RotateCcw } from 'lucide-react';
import { Order } from '../types';
import { api } from '../services/api';

export const OrderHistoryPage: React.FC = () => {
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState<boolean>(true);

  const fetchOrders = async () => {
    try {
      const list = await api.getOrders();
      setOrders(list);
    } catch (err) {
      console.error('Error fetching order history:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  const handleCancelOrder = async (orderNumber: string) => {
    if (!window.confirm(`Are you sure you want to cancel order #${orderNumber}?`)) return;
    try {
      await api.cancelOrder(orderNumber);
      await fetchOrders();
      alert('Order cancelled successfully!');
    } catch (err: any) {
      alert(err.message || 'Failed to cancel order.');
    }
  };

  const handleRefundOrder = async (orderNumber: string) => {
    const reason = window.prompt('Please enter the reason for refund request:', 'Customer cancellation');
    if (!reason) return;
    try {
      const ref = await api.requestOrderRefund(orderNumber, reason);
      await fetchOrders();
      alert(`Refund processed! Reference: ${ref.refund_reference}`);
    } catch (err: any) {
      alert(err.message || 'Refund request failed.');
    }
  };

  if (loading) return <div style={{ padding: '60px', textAlign: 'center' }}>Loading your order history...</div>;

  return (
    <div style={{ backgroundColor: 'var(--bg-card)', padding: '24px', borderRadius: '4px', border: '1px solid var(--border-color)', marginTop: '16px' }}>
      <h2 style={{ fontSize: '20px', fontWeight: 700, borderBottom: '1px solid var(--border-color)', paddingBottom: '12px', marginBottom: '20px' }}>
        My Orders
      </h2>

      {orders.length === 0 ? (
        <div style={{ textAlign: 'center', padding: '40px 0' }}>
          <Package size={48} color="var(--text-muted)" />
          <h3 style={{ fontSize: '16px', fontWeight: 600, marginTop: '12px' }}>No Orders Found</h3>
          <p style={{ color: 'var(--text-muted)', marginTop: '4px' }}>Looks like you haven't placed any orders yet.</p>
          <Link to="/products" className="btn-primary" style={{ marginTop: '16px', display: 'inline-flex' }}>
            Start Shopping
          </Link>
        </div>
      ) : (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {orders.map((o) => (
            <div
              key={o.id}
              style={{
                border: '1px solid var(--border-color)',
                borderRadius: '4px',
                padding: '16px',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                backgroundColor: 'var(--bg-card)',
              }}
            >
              <div>
                <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Order #{o.order_number}</span>
                <h4 style={{ fontSize: '15px', fontWeight: 700, margin: '4px 0' }}>
                  Total: ₹{o.grand_total.toLocaleString('en-IN')} ({o.items.length} Items)
                </h4>
                <p style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
                  Placed on {new Date(o.created_at).toLocaleDateString('en-IN', { day: 'numeric', month: 'short', year: 'numeric' })}
                </p>
                {o.shipment?.tracking_number && (
                  <div style={{ fontSize: '12px', color: 'var(--text-muted)', marginTop: '4px' }}>
                    Carrier: <strong>{o.shipment.carrier_name}</strong> | Tracking: <code>{o.shipment.tracking_number}</code>
                  </div>
                )}
              </div>

              <div style={{ textAlign: 'right', display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: '8px' }}>
                <span
                  style={{
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: '6px',
                    fontWeight: 700,
                    fontSize: '13px',
                    color:
                      o.status === 'DELIVERED'
                        ? 'var(--success-green)'
                        : o.status === 'CANCELLED'
                        ? 'var(--danger-red)'
                        : 'var(--warning-amber)',
                  }}
                >
                  {o.status === 'DELIVERED' ? <CheckCircle2 size={16} /> : o.status === 'CANCELLED' ? <XCircle size={16} /> : <Truck size={16} />}
                  {o.status} ({o.payment_status})
                </span>

                {['PENDING', 'CONFIRMED', 'PACKED'].includes(o.status) && (
                  <button
                    onClick={() => handleCancelOrder(o.order_number)}
                    className="btn-secondary"
                    style={{ fontSize: '12px', padding: '4px 10px', color: 'var(--danger-red)', borderColor: 'var(--danger-red)' }}
                  >
                    Cancel Order
                  </button>
                )}

                {o.status === 'CANCELLED' && o.payment_status !== 'REFUNDED' && (
                  <button
                    onClick={() => handleRefundOrder(o.order_number)}
                    className="btn-secondary"
                    style={{ fontSize: '12px', padding: '4px 10px', display: 'flex', alignItems: 'center', gap: '4px' }}
                  >
                    <RotateCcw size={12} /> Request Refund
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
