import React from 'react';
import { Link } from 'react-router-dom';
import {
  Briefcase,
  Megaphone,
  Gift,
  HelpCircle,
  Facebook,
  Twitter,
  Instagram,
  Youtube,
  Linkedin,
} from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer
      style={{
        backgroundColor: '#172337',
        color: '#ffffff',
        marginTop: '40px',
        borderTop: '1px solid #2874f0',
        fontSize: '12px',
        fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
      }}
    >
      {/* Top Multi-Column Grid */}
      <div
        style={{
          maxWidth: '1280px',
          margin: '0 auto',
          padding: '40px 20px 30px',
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(160px, 1fr))',
          gap: '24px',
        }}
      >
        {/* Column 1: ABOUT */}
        <div>
          <h4
            style={{
              color: '#878787',
              marginBottom: '14px',
              fontSize: '12px',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.5px',
            }}
          >
            About
          </h4>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <li>
              <Link to="/info/contact-us" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Contact Us
              </Link>
            </li>
            <li>
              <Link to="/info/about-us" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                About Us
              </Link>
            </li>
            <li>
              <Link to="/info/careers" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Careers
              </Link>
            </li>
            <li>
              <Link to="/info/stories" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                HashKart Stories
              </Link>
            </li>
            <li>
              <Link to="/info/press" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Press & Media
              </Link>
            </li>
            <li>
              <Link to="/info/corporate-information" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Corporate Information
              </Link>
            </li>
          </ul>
        </div>

        {/* Column 2: GROUP COMPANIES */}
        <div>
          <h4
            style={{
              color: '#878787',
              marginBottom: '14px',
              fontSize: '12px',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.5px',
            }}
          >
            Group Companies
          </h4>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <li>
              <Link to="/info/hashpay" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                HashPay
              </Link>
            </li>
            <li>
              <Link to="/info/hashlogistics" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                HashLogistics
              </Link>
            </li>
            <li>
              <Link to="/info/hashstudio" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                HashStudio Creators
              </Link>
            </li>
            <li>
              <Link to="/info/cleartrip" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Cleartrip
              </Link>
            </li>
            <li>
              <Link to="/info/shopsy" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Shopsy by HashKart
              </Link>
            </li>
          </ul>
        </div>

        {/* Column 3: HELP */}
        <div>
          <h4
            style={{
              color: '#878787',
              marginBottom: '14px',
              fontSize: '12px',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.5px',
            }}
          >
            Help
          </h4>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <li>
              <Link to="/info/payments" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Payments
              </Link>
            </li>
            <li>
              <Link to="/info/shipping" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Shipping & Delivery
              </Link>
            </li>
            <li>
              <Link to="/info/cancellation-returns" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Cancellation & Returns
              </Link>
            </li>
            <li>
              <Link to="/info/faq" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                FAQ
              </Link>
            </li>
            <li>
              <Link to="/info/report-infringement" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Report Infringement
              </Link>
            </li>
          </ul>
        </div>

        {/* Column 4: CONSUMER POLICY */}
        <div>
          <h4
            style={{
              color: '#878787',
              marginBottom: '14px',
              fontSize: '12px',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.5px',
            }}
          >
            Consumer Policy
          </h4>
          <ul style={{ listStyle: 'none', padding: 0, margin: 0, display: 'flex', flexDirection: 'column', gap: '8px' }}>
            <li>
              <Link to="/info/cancellation-returns" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Cancellation & Returns
              </Link>
            </li>
            <li>
              <Link to="/info/terms" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Terms Of Use
              </Link>
            </li>
            <li>
              <Link to="/info/security" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Security
              </Link>
            </li>
            <li>
              <Link to="/info/privacy" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Privacy
              </Link>
            </li>
            <li>
              <Link to="/info/sitemap" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Sitemap
              </Link>
            </li>
            <li>
              <Link to="/info/grievance" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                Grievance Redressal
              </Link>
            </li>
            <li>
              <Link to="/info/epr-compliance" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                EPR Compliance
              </Link>
            </li>
            <li>
              <Link to="/info/fssai" style={{ color: '#ffffff', textDecoration: 'none', transition: 'color 0.2s' }} onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')} onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}>
                FSSAI Food Safety Connect App
              </Link>
            </li>
          </ul>
        </div>

        {/* Column 5: Mail Us */}
        <div
          style={{
            borderLeft: '1px solid #384252',
            paddingLeft: '24px',
          }}
        >
          <h4
            style={{
              color: '#878787',
              marginBottom: '14px',
              fontSize: '12px',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.5px',
            }}
          >
            Mail Us:
          </h4>
          <p style={{ lineHeight: '1.6', color: '#ffffff', margin: 0, fontSize: '11px' }}>
            HashKart Internet Private Limited,
            <br />
            Buildings Alyssa, Begonia &
            <br />
            Clove Embassy Tech Village,
            <br />
            Outer Ring Road, Devarabeesanahalli Village,
            <br />
            Bengaluru, 560103,
            <br />
            Karnataka, India
          </p>

          <div style={{ marginTop: '16px' }}>
            <span style={{ color: '#878787', fontSize: '11px', display: 'block', marginBottom: '8px', fontWeight: 600 }}>
              Social:
            </span>
            <div style={{ display: 'flex', gap: '14px', alignItems: 'center' }}>
              <a
                href="https://facebook.com"
                target="_blank"
                rel="noreferrer"
                style={{ color: '#ffffff', transition: 'color 0.2s', display: 'inline-flex' }}
                onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')}
                onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}
                aria-label="Facebook"
              >
                <Facebook size={18} />
              </a>
              <a
                href="https://twitter.com"
                target="_blank"
                rel="noreferrer"
                style={{ color: '#ffffff', transition: 'color 0.2s', display: 'inline-flex' }}
                onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')}
                onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}
                aria-label="Twitter / X"
              >
                <Twitter size={18} />
              </a>
              <a
                href="https://youtube.com"
                target="_blank"
                rel="noreferrer"
                style={{ color: '#ffffff', transition: 'color 0.2s', display: 'inline-flex' }}
                onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')}
                onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}
                aria-label="YouTube"
              >
                <Youtube size={18} />
              </a>
              <a
                href="https://instagram.com"
                target="_blank"
                rel="noreferrer"
                style={{ color: '#ffffff', transition: 'color 0.2s', display: 'inline-flex' }}
                onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')}
                onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}
                aria-label="Instagram"
              >
                <Instagram size={18} />
              </a>
              <a
                href="https://linkedin.com"
                target="_blank"
                rel="noreferrer"
                style={{ color: '#ffffff', transition: 'color 0.2s', display: 'inline-flex' }}
                onMouseOver={(e) => (e.currentTarget.style.color = '#2874f0')}
                onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}
                aria-label="LinkedIn"
              >
                <Linkedin size={18} />
              </a>
            </div>
          </div>
        </div>

        {/* Column 6: Registered Office Address */}
        <div>
          <h4
            style={{
              color: '#878787',
              marginBottom: '14px',
              fontSize: '12px',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '0.5px',
            }}
          >
            Registered Office Address:
          </h4>
          <p style={{ lineHeight: '1.6', color: '#ffffff', margin: 0, fontSize: '11px' }}>
            HashKart Internet Private Limited,
            <br />
            Buildings Alyssa, Begonia &
            <br />
            Clove Embassy Tech Village,
            <br />
            Outer Ring Road, Devarabeesanahalli Village,
            <br />
            Bengaluru, 560103,
            <br />
            Karnataka, India
            <br />
            <span style={{ color: '#878787' }}>CIN :</span> U51109KA2024PTC066107
            <br />
            <span style={{ color: '#878787' }}>Telephone:</span>{' '}
            <a
              href="tel:04445614700"
              style={{ color: '#2874f0', textDecoration: 'none', fontWeight: 600 }}
            >
              044-45614700
            </a>{' '}
            /{' '}
            <a
              href="tel:04467415800"
              style={{ color: '#2874f0', textDecoration: 'none', fontWeight: 600 }}
            >
              044-67415800
            </a>
          </p>
        </div>
      </div>

      {/* Bottom Features & Payment Bar */}
      <div
        style={{
          borderTop: '1px solid #384252',
          backgroundColor: '#172337',
          padding: '18px 20px',
        }}
      >
        <div
          style={{
            maxWidth: '1280px',
            margin: '0 auto',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexWrap: 'wrap',
            gap: '16px',
            fontSize: '12px',
          }}
        >
          {/* Quick Action Feature Links with Golden Icons */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '28px', flexWrap: 'wrap' }}>
            <Link
              to="/seller/orders"
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                color: '#ffffff',
                textDecoration: 'none',
                fontWeight: 600,
                fontSize: '12px',
                transition: 'color 0.2s',
              }}
              onMouseOver={(e) => (e.currentTarget.style.color = '#ffc200')}
              onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}
            >
              <Briefcase size={16} color="#ffc200" />
              <span>Become a Seller</span>
            </Link>

            <Link
              to="/info/advertise"
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                color: '#ffffff',
                textDecoration: 'none',
                fontWeight: 600,
                fontSize: '12px',
                transition: 'color 0.2s',
              }}
              onMouseOver={(e) => (e.currentTarget.style.color = '#ffc200')}
              onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}
            >
              <Megaphone size={16} color="#ffc200" />
              <span>Advertise</span>
            </Link>

            <Link
              to="/info/gift-cards"
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                color: '#ffffff',
                textDecoration: 'none',
                fontWeight: 600,
                fontSize: '12px',
                transition: 'color 0.2s',
              }}
              onMouseOver={(e) => (e.currentTarget.style.color = '#ffc200')}
              onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}
            >
              <Gift size={16} color="#ffc200" />
              <span>Gift Cards</span>
            </Link>

            <Link
              to="/info/help-center"
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                color: '#ffffff',
                textDecoration: 'none',
                fontWeight: 600,
                fontSize: '12px',
                transition: 'color 0.2s',
              }}
              onMouseOver={(e) => (e.currentTarget.style.color = '#ffc200')}
              onMouseOut={(e) => (e.currentTarget.style.color = '#ffffff')}
            >
              <HelpCircle size={16} color="#ffc200" />
              <span>Help Center</span>
            </Link>
          </div>

          {/* Copyright text */}
          <div style={{ color: '#ffffff', fontSize: '12px', fontWeight: 500 }}>
            © 2007-2026 HashKart.com
          </div>

          {/* Payment & Security Method Badges */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', flexWrap: 'wrap' }}>
            <span
              style={{
                backgroundColor: '#ffffff',
                color: '#1a1f71',
                padding: '2px 6px',
                borderRadius: '3px',
                fontWeight: 800,
                fontSize: '10px',
                letterSpacing: '0.5px',
                display: 'inline-block',
              }}
            >
              VISA
            </span>
            <span
              style={{
                backgroundColor: '#ffffff',
                color: '#eb001b',
                padding: '2px 6px',
                borderRadius: '3px',
                fontWeight: 800,
                fontSize: '10px',
                letterSpacing: '0.5px',
                display: 'inline-block',
              }}
            >
              Mastercard
            </span>
            <span
              style={{
                backgroundColor: '#ffffff',
                color: '#097939',
                padding: '2px 6px',
                borderRadius: '3px',
                fontWeight: 800,
                fontSize: '10px',
                letterSpacing: '0.5px',
                display: 'inline-block',
              }}
            >
              RuPay
            </span>
            <span
              style={{
                backgroundColor: '#ffffff',
                color: '#0070ba',
                padding: '2px 6px',
                borderRadius: '3px',
                fontWeight: 800,
                fontSize: '10px',
                letterSpacing: '0.5px',
                display: 'inline-block',
              }}
            >
              UPI
            </span>
            <span
              style={{
                backgroundColor: '#ffffff',
                color: '#212121',
                padding: '2px 6px',
                borderRadius: '3px',
                fontWeight: 800,
                fontSize: '10px',
                letterSpacing: '0.5px',
                display: 'inline-block',
              }}
            >
              NET BANKING
            </span>
            <span
              style={{
                backgroundColor: '#ffffff',
                color: '#d32f2f',
                padding: '2px 6px',
                borderRadius: '3px',
                fontWeight: 800,
                fontSize: '10px',
                letterSpacing: '0.5px',
                display: 'inline-block',
              }}
            >
              EMI
            </span>
            <span
              style={{
                backgroundColor: '#ffffff',
                color: '#ff6f00',
                padding: '2px 6px',
                borderRadius: '3px',
                fontWeight: 800,
                fontSize: '10px',
                letterSpacing: '0.5px',
                display: 'inline-block',
              }}
            >
              COD
            </span>
          </div>
        </div>
      </div>
    </footer>
  );
};
