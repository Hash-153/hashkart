import React, { useEffect, useState } from 'react';
import { Shield, Package, ShoppingBag, Users, TrendingUp, AlertTriangle } from 'lucide-react';
import { DashboardStats, Order, SalesAnalyticsPoint } from '../types';
import { api } from '../services/api';

export const AdminDashboardPage: React.FC = () => {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [orders, setOrders] = useState<Order[]>([]);
  const [analytics, setAnalytics] = useState<SalesAnalyticsPoint[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [activeTab, setActiveTab] = useState<'overview' | 'orders' | 'products'>('overview');

  // Product creation form state
  const [prodForm, setProdForm] = useState({
    category_id: 1,
    name: '',
    description: '',
    highlight_features: '',
    is_featured: true,
  });

  const fetchData = async () => {
    try {
      const [sData, oData, aData] = await Promise.all([
        api.getDashboardStats(),
        api.getAdminOrders(),
        api.getSalesAnalytics(7),
      ]);
      setStats(sData);
      setOrders(oData);
      setAnalytics(aData.data_points);
    } catch (err) {
      console.error('Error fetching admin dashboard data:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleUpdateStatus = async (orderId: number, status: string) => {
    try {
      await api.updateOrderStatus(orderId, status);
      await fetchData();
      alert(`Updated order #${orderId} status to ${status}`);
    } catch (err: any) {
      alert(err.message);
    }
  };

  const handleCreateProductSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.createProduct(prodForm);
      alert('Product created successfully!');
      setProdForm({ category_id: 1, name: '', description: '', highlight_features: '', is_featured: true });
      await fetchData();
    } catch (err: any) {
      alert(err.message);
    }
  };

  if (loading) return <div style={{ padding: '60px', textAlign: 'center' }}>Loading Admin Portal...</div>;

  return (
    <div style={{ marginTop: '16px' }}>
      {/* Header */}
      <div style={{ backgroundColor: 'var(--bg-card)', padding: '20px', borderRadius: '4px', border: '1px solid var(--border-color)', marginBottom: '16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h1 style={{ fontSize: '22px', fontWeight: 800, display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Shield size={24} color="var(--primary-2874f0)" /> NovaMart Administration Portal
          </h1>
          <p style={{ fontSize: '13px', color: 'var(--text-muted)' }}>Storefront Metrics, Catalog Management & Order Processing</p>
        </div>

        <div style={{ display: 'flex', gap: '8px' }}>
          <button onClick={() => setActiveTab('overview')} className={activeTab === 'overview' ? 'btn-primary' : 'btn-secondary'} style={{ padding: '8px 16px', fontSize: '13px' }}>
            Overview KPI
          </button>
          <button onClick={() => setActiveTab('orders')} className={activeTab === 'orders' ? 'btn-primary' : 'btn-secondary'} style={{ padding: '8px 16px', fontSize: '13px' }}>
            Order Management
          </button>
          <button onClick={() => setActiveTab('products')} className={activeTab === 'products' ? 'btn-primary' : 'btn-secondary'} style={{ padding: '8px 16px', fontSize: '13px' }}>
            + Add Product
          </button>
        </div>
      </div>

      {activeTab === 'overview' && (
        <>
          {/* KPI Cards Grid */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '16px', marginBottom: '24px' }}>
            <div style={{ backgroundColor: 'var(--bg-card)', padding: '20px', borderRadius: '4px', border: '1px solid var(--border-color)' }}>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)', fontWeight: 600 }}>TOTAL REVENUE</span>
              <h2 style={{ fontSize: '24px', fontWeight: 800, margin: '8px 0', color: 'var(--success-green)' }}>
                ₹{stats?.total_sales_revenue.toLocaleString('en-IN')}
              </h2>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Avg Order: ₹{stats?.average_order_value}</span>
            </div>

            <div style={{ backgroundColor: 'var(--bg-card)', padding: '20px', borderRadius: '4px', border: '1px solid var(--border-color)' }}>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)', fontWeight: 600 }}>TOTAL ORDERS</span>
              <h2 style={{ fontSize: '24px', fontWeight: 800, margin: '8px 0' }}>{stats?.total_orders_count}</h2>
              <span style={{ fontSize: '12px', color: 'var(--warning-amber)', fontWeight: 700 }}>{stats?.pending_orders_count} Pending Fulfillment</span>
            </div>

            <div style={{ backgroundColor: 'var(--bg-card)', padding: '20px', borderRadius: '4px', border: '1px solid var(--border-color)' }}>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)', fontWeight: 600 }}>REGISTERED CUSTOMERS</span>
              <h2 style={{ fontSize: '24px', fontWeight: 800, margin: '8px 0' }}>{stats?.total_customers_count}</h2>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>Active Accounts</span>
            </div>

            <div style={{ backgroundColor: 'var(--bg-card)', padding: '20px', borderRadius: '4px', border: '1px solid var(--border-color)' }}>
              <span style={{ fontSize: '12px', color: 'var(--text-muted)', fontWeight: 600 }}>LOW STOCK ALERTS</span>
              <h2 style={{ fontSize: '24px', fontWeight: 800, margin: '8px 0', color: 'var(--danger-red)' }}>
                {stats?.low_stock_products_count}
              </h2>
              <span style={{ fontSize: '12px', color: 'var(--danger-red)' }}>Requires Stock Adjustment</span>
            </div>
          </div>

          {/* Sales Trend Bar Chart */}
          <div style={{ backgroundColor: 'var(--bg-card)', padding: '24px', borderRadius: '4px', border: '1px solid var(--border-color)' }}>
            <h3 style={{ fontSize: '16px', fontWeight: 700, marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
              <TrendingUp size={20} color="var(--primary-2874f0)" /> 7-Day Revenue Trend (Local DB Analytics)
            </h3>

            <div style={{ display: 'flex', alignItems: 'flex-end', gap: '16px', height: '180px', paddingTop: '20px', borderBottom: '1px solid var(--border-color)' }}>
              {analytics.map((pt) => {
                const maxSales = Math.max(...analytics.map((a) => a.sales_amount), 1);
                const heightPct = Math.max(10, Math.round((pt.sales_amount / maxSales) * 100));

                return (
                  <div key={pt.date} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%', justifyContent: 'flex-end' }}>
                    <span style={{ fontSize: '11px', fontWeight: 700, marginBottom: '4px' }}>₹{pt.sales_amount}</span>
                    <div style={{ width: '100%', height: `${heightPct}%`, backgroundColor: 'var(--primary-2874f0)', borderRadius: '4px 4px 0 0' }} />
                    <span style={{ fontSize: '11px', color: 'var(--text-muted)', marginTop: '8px' }}>{pt.date.substring(5)}</span>
                  </div>
                );
              })}
            </div>
          </div>
        </>
      )}

      {activeTab === 'orders' && (
        <div style={{ backgroundColor: 'var(--bg-card)', padding: '24px', borderRadius: '4px', border: '1px solid var(--border-color)' }}>
          <h2 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '16px' }}>Platform Order Fulfillment Management</h2>

          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
              <thead>
                <tr style={{ backgroundColor: 'var(--bg-main)', borderBottom: '1px solid var(--border-color)', textAlign: 'left' }}>
                  <th style={{ padding: '10px' }}>Order No</th>
                  <th style={{ padding: '10px' }}>Customer</th>
                  <th style={{ padding: '10px' }}>Amount</th>
                  <th style={{ padding: '10px' }}>Payment</th>
                  <th style={{ padding: '10px' }}>Status</th>
                  <th style={{ padding: '10px' }}>Action Update</th>
                </tr>
              </thead>
              <tbody>
                {orders.map((o) => (
                  <tr key={o.id} style={{ borderBottom: '1px solid var(--border-color)' }}>
                    <td style={{ padding: '12px 10px', fontWeight: 700 }}>{o.order_number}</td>
                    <td style={{ padding: '12px 10px' }}>User #{o.user_id}</td>
                    <td style={{ padding: '12px 10px', fontWeight: 700 }}>₹{o.grand_total.toLocaleString('en-IN')}</td>
                    <td style={{ padding: '12px 10px' }}>{o.payment_status}</td>
                    <td style={{ padding: '12px 10px', fontWeight: 700 }}>{o.status}</td>
                    <td style={{ padding: '12px 10px' }}>
                      <select
                        value={o.status}
                        onChange={(e) => handleUpdateStatus(o.id, e.target.value)}
                        style={{ padding: '4px 8px', borderRadius: '4px', border: '1px solid var(--border-dark)' }}
                      >
                        <option value="PENDING">PENDING</option>
                        <option value="CONFIRMED">CONFIRMED</option>
                        <option value="PACKED">PACKED</option>
                        <option value="SHIPPED">SHIPPED</option>
                        <option value="DELIVERED">DELIVERED</option>
                        <option value="CANCELLED">CANCELLED</option>
                      </select>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {activeTab === 'products' && (
        <div style={{ backgroundColor: 'var(--bg-card)', padding: '24px', borderRadius: '4px', border: '1px solid var(--border-color)', maxWidth: '600px' }}>
          <h2 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '16px' }}>Add Catalog Product</h2>

          <form onSubmit={handleCreateProductSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            <div>
              <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Product Title</label>
              <input type="text" required value={prodForm.name} onChange={(e) => setProdForm({ ...prodForm, name: e.target.value })} style={{ width: '100%', padding: '8px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
            </div>

            <div>
              <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Description</label>
              <textarea required value={prodForm.description} onChange={(e) => setProdForm({ ...prodForm, description: e.target.value })} rows={4} style={{ width: '100%', padding: '8px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
            </div>

            <div>
              <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Highlights (Newline separated)</label>
              <textarea value={prodForm.highlight_features} onChange={(e) => setProdForm({ ...prodForm, highlight_features: e.target.value })} rows={3} style={{ width: '100%', padding: '8px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
            </div>

            <button type="submit" className="btn-primary" style={{ padding: '12px' }}>
              Create Catalog Item
            </button>
          </form>
        </div>
      )}
    </div>
  );
};
