import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ShoppingCart, Heart, User as UserIcon, Shield, LogOut, Key, MapPin, Package } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext';
import { SearchBar } from './SearchBar';

export const Navbar: React.FC = () => {
  const { user, logout, isAdmin, isStaff } = useAuth();
  const { cart } = useCart();
  const [showDropdown, setShowDropdown] = useState(false);

  const totalCartCount = cart?.item_count || 0;

  return (
    <header className="navbar-header">
      <div className="navbar-container">
        {/* Brand Logo */}
        <Link to="/" className="brand-logo">
          <span>HashKart</span>
          <span className="brand-tagline">
            Explore <i>Plus</i> ⚡
          </span>
        </Link>

        {/* Search Engine Bar with Autocomplete */}
        <SearchBar />

        {/* Action Links */}
        <div className="nav-actions">
          {user ? (
            <div
              className="relative-container"
              style={{ position: 'relative' }}
              onMouseEnter={() => setShowDropdown(true)}
              onMouseLeave={() => setShowDropdown(false)}
            >
              <Link to="/account" className="nav-link-header">
                <UserIcon size={18} />
                <span>{user.full_name.split(' ')[0]}</span>
              </Link>

              {showDropdown && (
                <div
                  style={{
                    position: 'absolute',
                    top: '100%',
                    right: 0,
                    backgroundColor: '#ffffff',
                    color: '#212121',
                    boxShadow: '0 4px 16px rgba(0,0,0,0.15)',
                    borderRadius: '4px',
                    padding: '8px 0',
                    minWidth: '200px',
                    zIndex: 1100,
                  }}
                >
                  <Link
                    to="/account?tab=profile"
                    style={{ padding: '10px 16px', display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px' }}
                  >
                    <UserIcon size={15} /> My Profile
                  </Link>

                  <Link
                    to="/account?tab=addresses"
                    style={{ padding: '10px 16px', display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px' }}
                  >
                    <MapPin size={15} /> Saved Addresses
                  </Link>

                  <Link
                    to="/account?tab=security"
                    style={{ padding: '10px 16px', display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px' }}
                  >
                    <Key size={15} /> Security & Sessions
                  </Link>

                  <Link
                    to="/account?tab=orders"
                    style={{ padding: '10px 16px', display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px' }}
                  >
                    <Package size={15} /> My Orders
                  </Link>

                  <Link
                    to="/account?tab=wishlist"
                    style={{ padding: '10px 16px', display: 'flex', alignItems: 'center', gap: '8px', fontSize: '13px' }}
                  >
                    <Heart size={15} /> Wishlist
                  </Link>

                  {(isAdmin || isStaff) && (
                    <>
                      <hr style={{ margin: '6px 0', borderColor: '#f0f0f0' }} />
                      <Link
                        to="/admin"
                        style={{
                          padding: '10px 16px',
                          display: 'flex',
                          alignItems: 'center',
                          gap: '8px',
                          fontSize: '13px',
                          color: '#2874f0',
                          fontWeight: 700,
                        }}
                      >
                        <Shield size={15} /> Admin Portal
                      </Link>
                    </>
                  )}

                  <hr style={{ margin: '6px 0', borderColor: '#f0f0f0' }} />
                  <button
                    onClick={() => logout()}
                    style={{
                      padding: '10px 16px',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px',
                      width: '100%',
                      textAlign: 'left',
                      color: '#ff6161',
                      fontSize: '13px',
                      fontWeight: 700,
                      cursor: 'pointer',
                    }}
                  >
                    <LogOut size={15} /> Logout
                  </button>
                </div>
              )}
            </div>
          ) : (
            <Link to="/login" className="login-btn-header">
              Login
            </Link>
          )}

          <Link to="/wishlist" className="nav-link-header" title="Wishlist">
            <Heart size={20} />
            <span style={{ fontSize: '14px' }}>Wishlist</span>
          </Link>

          <Link to="/cart" className="nav-link-header">
            <ShoppingCart size={20} />
            <span style={{ fontSize: '14px' }}>Cart</span>
            {totalCartCount > 0 && <span className="cart-badge-count">{totalCartCount}</span>}
          </Link>
        </div>
      </div>
    </header>
  );
};
