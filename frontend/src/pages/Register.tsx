import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { api } from '../services/api';

export const Register: React.FC = () => {
  const [fullName, setFullName] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  // Password Strength Criteria Checks
  const hasMinLength = password.length >= 8;
  const hasUpper = /[A-Z]/.test(password);
  const hasLower = /[a-z]/.test(password);
  const hasDigit = /\d/.test(password);
  const hasSpecial = /[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]/.test(password);

  const passedCount = [hasMinLength, hasUpper, hasLower, hasDigit, hasSpecial].filter(Boolean).length;
  const strengthPercentage = (passedCount / 5) * 100;
  const strengthColor = passedCount <= 2 ? '#e53935' : passedCount <= 4 ? '#ff9f00' : '#388e3c';

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (passedCount < 5) {
      setError('Please fulfill all password security requirements.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      await api.register({
        full_name: fullName,
        email,
        phone_number: phoneNumber,
        password,
      });
      alert('Account registered successfully! Please login with your credentials.');
      navigate('/login');
    } catch (err: any) {
      setError(err.message || 'Registration failed.');
    } finally {
      setLoading(false);
    }
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
          <h2 style={{ fontSize: '24px', fontWeight: 800 }}>Looks like you're new here!</h2>
          <p style={{ opacity: 0.9, fontSize: '14px', marginTop: '12px', lineHeight: '1.5' }}>
            Sign up to get access to exclusive Indian marketplace offers, recommendations & order tracking.
          </p>
        </div>
        <div style={{ fontSize: '12px', opacity: 0.7 }}>NovaMart Security Guaranteed</div>
      </div>

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

        <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          <div>
            <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>
              Full Name
            </label>
            <input
              type="text"
              required
              placeholder="Enter full name"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              style={{ width: '100%', padding: '10px 12px', border: '1px solid var(--border-dark)', borderRadius: '4px', fontSize: '14px' }}
            />
          </div>

          <div>
            <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>
              Email Address
            </label>
            <input
              type="email"
              required
              placeholder="Enter email address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              style={{ width: '100%', padding: '10px 12px', border: '1px solid var(--border-dark)', borderRadius: '4px', fontSize: '14px' }}
            />
          </div>

          <div>
            <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>
              Mobile Number (10 digits)
            </label>
            <input
              type="text"
              placeholder="+91 9876543210"
              value={phoneNumber}
              onChange={(e) => setPhoneNumber(e.target.value)}
              style={{ width: '100%', padding: '10px 12px', border: '1px solid var(--border-dark)', borderRadius: '4px', fontSize: '14px' }}
            />
          </div>

          <div>
            <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>
              Set Password
            </label>
            <div style={{ position: 'relative' }}>
              <input
                type={showPassword ? 'text' : 'password'}
                required
                placeholder="Set password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                style={{ width: '100%', padding: '10px 12px', paddingRight: '40px', border: '1px solid var(--border-dark)', borderRadius: '4px', fontSize: '14px' }}
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

            {/* Password Strength Meter */}
            {password.length > 0 && (
              <div style={{ marginTop: '8px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '11px', marginBottom: '3px' }}>
                  <span>Password Strength</span>
                  <span style={{ color: strengthColor, fontWeight: 700 }}>
                    {passedCount <= 2 ? 'Weak' : passedCount <= 4 ? 'Moderate' : 'Strong Security'}
                  </span>
                </div>
                <div style={{ height: '4px', width: '100%', backgroundColor: '#eee', borderRadius: '2px', overflow: 'hidden' }}>
                  <div style={{ height: '100%', width: `${strengthPercentage}%`, backgroundColor: strengthColor, transition: 'width 0.3s' }}></div>
                </div>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '4px', marginTop: '6px', fontSize: '11px', color: '#666' }}>
                  <span style={{ color: hasMinLength ? '#388e3c' : '#999' }}>{hasMinLength ? '✓' : '•'} 8+ characters</span>
                  <span style={{ color: hasUpper ? '#388e3c' : '#999' }}>{hasUpper ? '✓' : '•'} Uppercase letter</span>
                  <span style={{ color: hasLower ? '#388e3c' : '#999' }}>{hasLower ? '✓' : '•'} Lowercase letter</span>
                  <span style={{ color: hasDigit ? '#388e3c' : '#999' }}>{hasDigit ? '✓' : '•'} Numeric digit</span>
                  <span style={{ color: hasSpecial ? '#388e3c' : '#999' }}>{hasSpecial ? '✓' : '•'} Special char (!@#$)</span>
                </div>
              </div>
            )}
          </div>

          <button type="submit" disabled={loading} className="btn-primary" style={{ padding: '12px', fontSize: '15px', fontWeight: 700, marginTop: '8px' }}>
            {loading ? 'Creating Account...' : 'CONTINUE & REGISTER'}
          </button>
        </form>

        <div style={{ marginTop: '24px', textAlign: 'center', fontSize: '13px' }}>
          Existing User?{' '}
          <Link to="/login" style={{ color: 'var(--primary-2874f0)', fontWeight: 700 }}>
            Log in to your account
          </Link>
        </div>
      </div>
    </div>
  );
};
