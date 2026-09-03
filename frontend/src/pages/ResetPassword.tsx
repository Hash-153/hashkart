import React, { useState } from 'react';
import { Link, useNavigate, useSearchParams } from 'react-router-dom';
import { api } from '../services/api';

export const ResetPassword: React.FC = () => {
  const [searchParams] = useSearchParams();
  const tokenFromUrl = searchParams.get('token') || '';

  const [resetToken, setResetToken] = useState(tokenFromUrl);
  const [newPassword, setNewPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  // Password Strength Criteria Checks
  const hasMinLength = newPassword.length >= 8;
  const hasUpper = /[A-Z]/.test(newPassword);
  const hasLower = /[a-z]/.test(newPassword);
  const hasDigit = /\d/.test(newPassword);
  const hasSpecial = /[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]/.test(newPassword);

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
    setSuccessMsg('');

    try {
      const res = await api.resetPassword({
        reset_token: resetToken,
        new_password: newPassword,
      });
      setSuccessMsg(res.message);
      setTimeout(() => {
        navigate('/login');
      }, 2500);
    } catch (err: any) {
      setError(err.message || 'Password reset failed.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '500px', margin: '40px auto', backgroundColor: 'var(--bg-card)', padding: '32px', borderRadius: '8px', boxShadow: '0 4px 16px rgba(0,0,0,0.08)' }}>
      <h2 style={{ fontSize: '22px', fontWeight: 800, color: 'var(--text-main)', marginBottom: '8px' }}>Set New Password</h2>
      <p style={{ fontSize: '13px', color: '#666', marginBottom: '20px' }}>
        Provide your one-time reset token and enter a strong new password.
      </p>

      {error && (
        <div style={{ backgroundColor: 'var(--danger-light)', color: 'var(--danger-red)', padding: '10px 14px', borderRadius: '4px', fontSize: '13px', marginBottom: '16px' }}>
          {error}
        </div>
      )}

      {successMsg && (
        <div style={{ backgroundColor: '#e8f5e9', color: '#2e7d32', padding: '12px 14px', borderRadius: '4px', fontSize: '13px', marginBottom: '16px' }}>
          {successMsg} Redirecting to login...
        </div>
      )}

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
        <div>
          <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '6px' }}>Reset Token</label>
          <input
            type="text"
            required
            placeholder="Paste reset token hex"
            value={resetToken}
            onChange={(e) => setResetToken(e.target.value)}
            style={{ width: '100%', padding: '10px 12px', border: '1px solid var(--border-dark)', borderRadius: '4px', fontSize: '13px', fontFamily: 'monospace' }}
          />
        </div>

        <div>
          <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '6px' }}>New Password</label>
          <div style={{ position: 'relative' }}>
            <input
              type={showPassword ? 'text' : 'password'}
              required
              placeholder="Enter new strong password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
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
          {newPassword.length > 0 && (
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

        <button type="submit" disabled={loading} className="btn-primary" style={{ padding: '12px', fontSize: '14px', fontWeight: 700 }}>
          {loading ? 'Resetting Password...' : 'Reset Password & Revoke Sessions'}
        </button>
      </form>

      <div style={{ marginTop: '20px', textAlign: 'center', fontSize: '13px' }}>
        <Link to="/login" style={{ color: 'var(--primary-2874f0)', fontWeight: 700 }}>
          Back to Login
        </Link>
      </div>
    </div>
  );
};
