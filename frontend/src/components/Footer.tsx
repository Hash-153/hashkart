import React from 'react';

export const Footer: React.FC = () => {
  return (
    <footer
      style={{
        backgroundColor: '#172337',
        color: '#ffffff',
        padding: '40px 16px 20px',
        marginTop: '40px',
        borderTop: '1px solid #2874f0',
        fontSize: '12px',
      }}
    >
      <div
        style={{
          maxWidth: 'var(--max-content-width)',
          margin: '0 auto',
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
          gap: '24px',
          marginBottom: '30px',
        }}
      >
        <div>
          <h4 style={{ color: '#878787', marginBottom: '12px', fontSize: '12px', textTransform: 'uppercase' }}>About</h4>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>Contact Us</p>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>About HashKart</p>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>Careers</p>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>Press Releases</p>
        </div>

        <div>
          <h4 style={{ color: '#878787', marginBottom: '12px', fontSize: '12px', textTransform: 'uppercase' }}>Help</h4>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>Payments</p>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>Shipping & Logistics</p>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>Cancellation & Returns</p>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>FAQ & Support</p>
        </div>

        <div>
          <h4 style={{ color: '#878787', marginBottom: '12px', fontSize: '12px', textTransform: 'uppercase' }}>Consumer Policy</h4>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>Return Policy</p>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>Terms of Use</p>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>Security & Privacy</p>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>EPR Compliance</p>
        </div>

        <div>
          <h4 style={{ color: '#878787', marginBottom: '12px', fontSize: '12px', textTransform: 'uppercase' }}>Registered Office</h4>
          <p style={{ lineHeight: '1.8', color: '#ffffff' }}>HashKart India Private Limited</p>
          <p style={{ lineHeight: '1.8', color: '#878787' }}>Outer Ring Road, Devarabeesanahalli Village,</p>
          <p style={{ lineHeight: '1.8', color: '#878787' }}>Bengaluru, 560103, Karnataka, India</p>
        </div>
      </div>

      <div
        style={{
          borderTop: '1px solid #454d5e',
          paddingTop: '16px',
          textAlign: 'center',
          color: '#878787',
        }}
      >
        © 2026 HashKart. All Rights Reserved. Built with React, TypeScript & FastAPI.
      </div>
    </footer>
  );
};
