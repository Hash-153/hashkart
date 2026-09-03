import React, { useState } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';

export const Login: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const { login } = useAuth();
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const redirect = searchParams.get('redirect') || '/';

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const res = await api.login({ email, password });
      await login(res.access_token, res.refresh_token);
      navigate(redirect);
    } catch (err: any) {
      setError(err.message || 'Incorrect email or password.');
    } finally {
      setLoading(false);
    }
  };

  const handleDemoFill = (demoEmail: string, demoPw: string) => {
    setEmail(demoEmail);
    setPassword(demoPw);
  };

  return (
    <div
      style={{
        maxWidth: '820px',
        margin: '40px auto',
        display: 'grid',
        gridTemplateColumns: '300px 1fr',
        backgroundColor: 'var(--bg-card)',
        borderRadius: '8px',
        overflow: 'hidden',
        boxShadow: '0 4px 20px rgba(0,0,0,0.08)',
      }}
    >
      {/* Left Banner */}
      <div
        style={{
          backgroundColor: 'var(--primary-2874f0)',
          color: '#ffffff',
          padding: '36px 28px',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'space-between',
        }}
      >
        <div>
          <h2 style={{ fontSize: '24px', fontWeight: 800 }}>Login</h2>
          <p style={{ opacity: 0.9, fontSize: '14px', marginTop: '12px', lineHeight: '1.5' }}>
            Access your Orders, Wishlist, Saved Addresses, and Security Settings.
          </p>
        </div>

        {/* Demo Fast Login Helpers */}
        <div style={{ marginTop: '24px', background: 'rgba(255,255,255,0.1)', padding: '14px', borderRadius: '6px' }}>
          <div style={{ fontSize: '12px', fontWeight: 700, marginBottom: '8px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
            ⚡ Fast Demo Credentials
          </div>
          <button
            type="button"
            onClick={() => handleDemoFill('customer@novamart.demo', 'CustomerPass123!')}
            style={{
              width: '100%',
              padding: '6px 10px',
              fontSize: '12px',
              backgroundColor: '#ffffff',
              color: '#2874f0',
              border: 'none',
              borderRadius: '4px',
              fontWeight: 600,
              cursor: 'pointer',
              marginBottom: '6px',
            }}
          >
            Fill Customer Demo
          </button>
          <button
            type="button"
            onClick={() => handleDemoFill('admin@novamart.demo', 'AdminPass123!')}
            style={{
              width: '100%',
              padding: '6px 10px',
              fontSize: '12px',
              backgroundColor: '#ff9f00',
              color: '#ffffff',
              border: 'none',
              borderRadius: '4px',
              fontWeight: 600,
              cursor: 'pointer',
            }}
          >
            Fill Admin Demo
          </button>
        </div>

        <div style={{ fontSize: '12px', opacity: 0.7, marginTop: '20px' }}>NovaMart Security Guaranteed</div>
      </div>

      {/* Form Area */}
      <div style={{ padding: '36px 32px' }}>
        {error && (
          <div
            style={{
              backgroundColor: 'var(--danger-light)',
              color: 'var(--danger-red)',
              padding: '10px 14px',
              borderRadius: '4px',
              fontSize: '13px',
              marginBottom: '20px',
              borderLeft: '4px solid var(--danger-red)',
            }}
          >
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
          <div>
            <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '6px' }}>
              Email Address
            </label>
            <input
              type="email"
              required
              placeholder="Enter email address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              style={{
                width: '100%',
                padding: '10px 12px',
                border: '1px solid var(--border-dark)',
                borderRadius: '4px',
                fontSize: '14px',
              }}
            />
          </div>

          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '6px' }}>
              <label style={{ fontSize: '13px', fontWeight: 600 }}>Password</label>
              <Link to="/forgot-password" style={{ fontSize: '12px', color: 'var(--primary-2874f0)', fontWeight: 600 }}>
                Forgot Password?
              </Link>
            </div>
            <div style={{ position: 'relative' }}>
              <input
                type={showPassword ? 'text' : 'password'}
                required
                placeholder="Enter password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                style={{
                  width: '100%',
                  padding: '10px 12px',
                  paddingRight: '40px',
                  border: '1px solid var(--border-dark)',
                  borderRadius: '4px',
                  fontSize: '14px',
                }}
              />
              <button
                type="button"
                onClick={() => setShowPassword(!showPassword)}
                style={{
                  position: 'absolute',
                  right: '10px',
                  top: '50%',
                  transform: 'translateY(-50%)',
                  background: 'none',
                  border: 'none',
                  color: '#666',
                  cursor: 'pointer',
                  fontSize: '13px',
                }}
              >
                {showPassword ? 'Hide' : 'Show'}
              </button>
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="btn-primary"
            style={{ padding: '12px', fontSize: '15px', fontWeight: 700, borderRadius: '4px' }}
          >
            {loading ? 'Authenticating...' : 'Login to NovaMart'}
          </button>
        </form>

        <div style={{ marginTop: '24px', textAlign: 'center', fontSize: '13px' }}>
          New to NovaMart?{' '}
          <Link to="/register" style={{ color: 'var(--primary-2874f0)', fontWeight: 700 }}>
            Create an account
          </Link>
        </div>
      </div>
    </div>
  );
};
