import React, { useEffect, useState } from 'react';
import { Headphones, Plus, RefreshCw } from 'lucide-react';
import { api } from '../services/api';
import { SupportTicket } from '../types';

export const SupportPage: React.FC = () => {
  const [tickets, setTickets] = useState<SupportTicket[]>([]);
  const [subject, setSubject] = useState('');
  const [category, setCategory] = useState('ORDER');
  const [description, setDescription] = useState('');
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');

  const loadTickets = async () => {
    setLoading(true);
    setError('');
    try {
      setTickets(await api.getSupportTickets());
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unable to load support tickets.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadTickets();
  }, []);

  const createTicket = async (event: React.FormEvent) => {
    event.preventDefault();
    setSubmitting(true);
    setError('');
    try {
      await api.createSupportTicket({ subject, category, description });
      setSubject('');
      setDescription('');
      await loadTickets();
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unable to create support ticket.');
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <section className="support-page">
      <header className="operation-header">
        <div>
          <span className="eyebrow"><Headphones size={14} /> Customer care</span>
          <h1>Support centre</h1>
          <p>Open a case and keep every order conversation in one place.</p>
        </div>
        <button className="btn-secondary" onClick={loadTickets} aria-label="Refresh tickets" title="Refresh tickets">
          <RefreshCw size={16} /> Refresh
        </button>
      </header>

      {error && <div className="operation-state operation-error">{error}</div>}

      <div className="support-layout">
        <form className="support-form" onSubmit={createTicket}>
          <h2>Open a support case</h2>
          <label>Subject<input required value={subject} onChange={(event) => setSubject(event.target.value)} /></label>
          <label>Category<select value={category} onChange={(event) => setCategory(event.target.value)}><option value="ORDER">Order</option><option value="PAYMENT">Payment</option><option value="DELIVERY">Delivery</option><option value="RETURN">Return</option><option value="ACCOUNT">Account</option></select></label>
          <label>What can we help with?<textarea required minLength={10} rows={6} value={description} onChange={(event) => setDescription(event.target.value)} /></label>
          <button className="btn-primary" disabled={submitting}><Plus size={16} /> {submitting ? 'Opening...' : 'Open ticket'}</button>
        </form>

        <div className="support-ticket-list">
          <h2>Your tickets</h2>
          {loading ? <p>Loading your support history...</p> : tickets.length === 0 ? <p>No support tickets yet.</p> : tickets.map((ticket) => (
            <article className="support-ticket" key={ticket.id}>
              <div><strong>{ticket.ticket_number}</strong><span className={`ticket-status ticket-${ticket.status.toLowerCase()}`}>{ticket.status}</span></div>
              <h3>{ticket.subject}</h3>
              <p>{ticket.description}</p>
              <small>{ticket.category} · {new Date(ticket.created_at).toLocaleDateString('en-IN')}</small>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
};
