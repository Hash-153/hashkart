import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { OrderHistoryPage } from './OrderHistoryPage';

export const ProfilePage: React.FC = () => {
  const { user, refreshUser } = useAuth();
  const [fullName, setFullName] = useState(user?.full_name || '');
  const [phoneNumber, setPhoneNumber] = useState(user?.phone_number || '');
  const [activeTab, setActiveTab] = useState<'profile' | 'orders'>('profile');
  const [message, setMessage] = useState('');

  const handleUpdate = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.updateProfile({ full_name: fullName, phone_number: phoneNumber });
      await refreshUser();
      setMessage('Profile updated successfully!');
    } catch (err: any) {
      alert(err.message);
    }
  };

  if (!user) return <div style={{ padding: '60px', textAlign: 'center' }}>Please login to view your profile.</div>;

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '240px 1fr', gap: '16px', marginTop: '16px' }}>
      {/* Sidebar Navigation */}
      <div style={{ backgroundColor: 'var(--bg-card)', padding: '16px', borderRadius: '4px', border: '1px solid var(--border-color)', height: 'fit-content' }}>
        <div style={{ paddingBottom: '16px', borderBottom: '1px solid var(--border-color)', marginBottom: '16px' }}>
          <h3 style={{ fontSize: '16px', fontWeight: 700 }}>Hello, {user.full_name.split(' ')[0]}</h3>
          <span style={{ fontSize: '12px', color: 'var(--text-muted)' }}>{user.email}</span>
        </div>

        <button
          onClick={() => setActiveTab('profile')}
          style={{
            width: '100%',
            textAlign: 'left',
            padding: '10px 12px',
            fontSize: '14px',
            fontWeight: activeTab === 'profile' ? 700 : 400,
            color: activeTab === 'profile' ? 'var(--primary-2874f0)' : 'var(--text-main)',
            backgroundColor: activeTab === 'profile' ? 'var(--primary-light)' : 'transparent',
            borderRadius: '4px',
          }}
        >
          Personal Information
        </button>

        <button
          onClick={() => setActiveTab('orders')}
          style={{
            width: '100%',
            textAlign: 'left',
            padding: '10px 12px',
            fontSize: '14px',
            fontWeight: activeTab === 'orders' ? 700 : 400,
            color: activeTab === 'orders' ? 'var(--primary-2874f0)' : 'var(--text-main)',
            backgroundColor: activeTab === 'orders' ? 'var(--primary-light)' : 'transparent',
            borderRadius: '4px',
            marginTop: '4px',
          }}
        >
          My Orders History
        </button>
      </div>

      {/* Main Tab View */}
      <div>
        {activeTab === 'profile' ? (
          <div style={{ backgroundColor: 'var(--bg-card)', padding: '24px', borderRadius: '4px', border: '1px solid var(--border-color)' }}>
            <h2 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '16px' }}>Personal Information</h2>

            {message && <div style={{ backgroundColor: 'var(--success-light)', color: 'var(--success-green)', padding: '10px', borderRadius: '4px', marginBottom: '16px' }}>{message}</div>}

            <form onSubmit={handleUpdate} style={{ maxWidth: '400px', display: 'flex', flexDirection: 'column', gap: '16px' }}>
              <div>
                <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Full Name</label>
                <input type="text" value={fullName} onChange={(e) => setFullName(e.target.value)} style={{ width: '100%', padding: '10px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
              </div>

              <div>
                <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Email Address</label>
                <input type="email" disabled value={user.email} style={{ width: '100%', padding: '10px', border: '1px solid var(--border-dark)', borderRadius: '4px', opacity: 0.7 }} />
              </div>

              <div>
                <label style={{ fontSize: '13px', fontWeight: 600, display: 'block', marginBottom: '4px' }}>Phone Number</label>
                <input type="text" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} style={{ width: '100%', padding: '10px', border: '1px solid var(--border-dark)', borderRadius: '4px' }} />
              </div>

              <button type="submit" className="btn-primary" style={{ padding: '10px' }}>
                Save Changes
              </button>
            </form>
          </div>
        ) : (
          <OrderHistoryPage />
        )}
      </div>
    </div>
  );
};
