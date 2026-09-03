import React, { useEffect, useState } from 'react';
import { BarChart3, Package, IndianRupee, ShoppingBag, Store } from 'lucide-react';
import { api } from '../services/api';
import { SellerDashboard, SellerProfile } from '../types';

const money = (value: number) => `₹${value.toLocaleString('en-IN', { maximumFractionDigits: 0 })}`;

export const SellerDashboardPage: React.FC = () => {
  const [profile, setProfile] = useState<SellerProfile | null>(null);
  const [dashboard, setDashboard] = useState<SellerDashboard | null>(null);
  const [days, setDays] = useState(30);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const load = async () => {
      setLoading(true);
      setError('');
      try {
        const [seller, stats] = await Promise.all([api.getSellerProfile(), api.getSellerDashboard(days)]);
        setProfile(seller);
        setDashboard(stats);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unable to load seller dashboard.');
      } finally {
        setLoading(false);
      }
    };
    load();
  }, [days]);

  if (loading) return <div className="operation-state">Loading seller workspace...</div>;
  if (error) return <div className="operation-state operation-error">{error}</div>;

  return (
    <section className="seller-dashboard">
      <header className="operation-header">
        <div>
          <span className="eyebrow"><Store size={14} /> Seller workspace</span>
          <h1>{profile?.business_name || 'Seller dashboard'}</h1>
          <p>Track catalog health, orders, and marketplace earnings.</p>
        </div>
        <label className="period-select">
          Period
          <select value={days} onChange={(event) => setDays(Number(event.target.value))}>
            <option value={7}>7 days</option>
            <option value={30}>30 days</option>
            <option value={90}>90 days</option>
          </select>
        </label>
      </header>

      {profile?.status !== 'APPROVED' && (
        <div className="seller-status-banner">Seller approval status: <strong>{profile?.status}</strong></div>
      )}

      <div className="seller-kpi-grid">
        <article className="seller-kpi"><Package size={22} /><span>Active listings</span><strong>{dashboard?.active_listings ?? 0}</strong></article>
        <article className="seller-kpi"><ShoppingBag size={22} /><span>Attributed orders</span><strong>{dashboard?.orders ?? 0}</strong></article>
        <article className="seller-kpi"><IndianRupee size={22} /><span>Gross revenue</span><strong>{money(dashboard?.revenue ?? 0)}</strong></article>
        <article className="seller-kpi"><BarChart3 size={22} /><span>Pending payout</span><strong>{money(dashboard?.pending_payout ?? 0)}</strong></article>
      </div>

      <div className="seller-dashboard-note">
        <BarChart3 size={18} /> Revenue is calculated from completed marketplace order lines attributed to your active listings.
      </div>
    </section>
  );
};
