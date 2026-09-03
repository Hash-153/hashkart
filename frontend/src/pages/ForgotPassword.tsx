import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../services/api';

export const ForgotPassword: React.FC = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [devSimulationToken, setDevSimulationToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setMessage('');
    setDevSimulationToken(null);

    try {
      const res = await api.forgotPassword(email);
      setMessage(res.message);
      if (res.dev_simulation_reset_token) {
        setDevSimulationToken(res.dev_simulation_reset_token);
      }
    } catch (err: any) {
      setError(err.message || 'Failed to process request.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '500px', margin: '40px auto', backgroundColor: 'var(--bg-card)', padding: '32px', borderRadius: '8px', boxShadow: '0 4px 16px rgba(0,0,0,0.08)' }}>
      <h2 style={{ fontSize: '22px', fontWeight: 800, color: 'var(--text-main)', marginBottom: '8px' }}>Forgot Password</h2>
      <p style={{ fontSize: '13px', color: '#666', marginBottom: '20px' }}>
        Enter your registered email address below. We'll generate password reset instructions.
      </p>

      {error && (
        <div style={{ backgroundColor: 'var(--danger-light)', color: 'var(--danger-red)', padding: '10px 14px', borderRadius: '4px', fontSize: '13px', marginBottom: '16px' }}>
          {error}
        </div>
      )}

      {message && (
        <div style={{ backgroundColor: '#e8f5e9', color: '#2e7d32', padding: '12px 14px', borderRadius: '4px', fontSize: '13px', marginBottom: '16px' }}>
          {message}
        </div>
      )}

      {devSimulationToken && (
        <div style={{ backgroundColor: '#fff8e1', border: '1px solid #ffe082', padding: '14px', borderRadius: '6px', marginBottom: '20px' }}>
          <div style={{ fontSize: '12px', fontWeight: 700, color: '#b78103', marginBottom: '4px' }}>
            ⚡ Local Development Password Reset Link
          </div>
          <p style={{ fontSize: '12px', color: '#555', marginBottom: '10px' }}>
            Since external email services are disabled, use this simulated one-time link:
          </p>
          <Link
            to={`/reset-password?token=${devSimulationToken}`}
            style={{
              display: 'inline-block',
              backgroundColor: '#2874f0',
              color: '#ffffff',
              padding: '8px 14px',
              borderRadius: '4px',
              fontSize: '12px',
              fontWeight: 700,
              textDecoration: 'none',
            }}
          >
            Reset Password Now →
          </Link>
        </div>
      )}

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        <div>
          <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '6px' }}>Email Address</label>
          <input
            type="email"
            required
            placeholder="Enter your registered email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            style={{ width: '100%', padding: '10px 12px', border: '1px solid var(--border-dark)', borderRadius: '4px', fontSize: '14px' }}
          />
        </div>

        <button type="submit" disabled={loading} className="btn-primary" style={{ padding: '12px', fontSize: '14px', fontWeight: 700 }}>
          {loading ? 'Sending Instructions...' : 'Send Reset Link'}
        </button>
      </form>

      <div style={{ marginTop: '20px', textAlign: 'center', fontSize: '13px' }}>
        Remembered your password?{' '}
        <Link to="/login" style={{ color: 'var(--primary-2874f0)', fontWeight: 700 }}>
          Back to Login
        </Link>
      </div>
    </div>
  );
};
