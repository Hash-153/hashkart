import React, { useState, useEffect } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { api } from '../services/api';
import { Address, UserSession, SecurityAuditLog, Order, WishlistItem } from '../types';

export const AccountDashboard: React.FC = () => {
  const { user, refreshUser, logout } = useAuth();
  const [searchParams, setSearchParams] = useSearchParams();
  const activeTab = searchParams.get('tab') || 'profile';
  const navigate = useNavigate();

  // State
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  // Profile Form State
  const [fullName, setFullName] = useState(user?.full_name || '');
  const [firstName, setFirstName] = useState(user?.first_name || '');
  const [lastName, setLastName] = useState(user?.last_name || '');
  const [phone, setPhone] = useState(user?.phone_number || '');
  const [profileImg, setProfileImg] = useState(user?.profile_image_url || '');

  // Address Book State
  const [addresses, setAddresses] = useState<Address[]>([]);
  const [showAddressModal, setShowAddressModal] = useState(false);
  const [editingAddress, setEditingAddress] = useState<Address | null>(null);

  // Address Form State
  const [addrName, setAddrName] = useState('');
  const [addrPhone, setAddrPhone] = useState('');
  const [addrLine1, setAddrLine1] = useState('');
  const [addrLine2, setAddrLine2] = useState('');
  const [addrLocality, setAddrLocality] = useState('');
  const [addrCity, setAddrCity] = useState('');
  const [addrState, setAddrState] = useState('');
  const [addrPin, setAddrPin] = useState('');
  const [addrType, setAddrType] = useState('HOME');
  const [isDefaultShipping, setIsDefaultShipping] = useState(false);

  // Password Change State
  const [currPassword, setCurrPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [logoutOthers, setLogoutOthers] = useState(true);

  // Sessions & Security Logs State
  const [sessions, setSessions] = useState<UserSession[]>([]);
  const [auditLogs, setAuditLogs] = useState<SecurityAuditLog[]>([]);

  // Orders & Wishlist State
  const [orders, setOrders] = useState<Order[]>([]);
  const [wishlistItems, setWishlistItems] = useState<WishlistItem[]>([]);

  useEffect(() => {
    if (user) {
      setFullName(user.full_name || '');
      setFirstName(user.first_name || '');
      setLastName(user.last_name || '');
      setPhone(user.phone_number || '');
      setProfileImg(user.profile_image_url || '');
    }
  }, [user]);

  useEffect(() => {
    loadTabData();
  }, [activeTab]);

  const loadTabData = async () => {
    setError('');
    setMessage('');
    try {
      if (activeTab === 'addresses') {
        const addrs = await api.getUserAddresses();
        setAddresses(addrs);
      } else if (activeTab === 'security') {
        const [sessData, logsData] = await Promise.all([
          api.getActiveSessions(),
          api.getSecurityAuditLogs(),
        ]);
        setSessions(sessData);
        setAuditLogs(logsData);
      } else if (activeTab === 'orders') {
        const ords = await api.getOrders();
        setOrders(ords);
      } else if (activeTab === 'wishlist') {
        const wl = await api.getWishlist();
        setWishlistItems(wl.items || []);
      }
    } catch (err: any) {
      setError(err.message || 'Failed to load account data.');
    }
  };

  const handleProfileSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setMessage('');
    try {
      await api.updateProfile({
        full_name: fullName,
        first_name: firstName,
        last_name: lastName,
        phone_number: phone,
        profile_image_url: profileImg,
      });
      await refreshUser();
      setMessage('Profile updated successfully!');
    } catch (err: any) {
      setError(err.message || 'Failed to update profile.');
    } finally {
      setLoading(false);
    }
  };

  const handleOpenAddAddress = () => {
    setEditingAddress(null);
    setAddrName(user?.full_name || '');
    setAddrPhone(user?.phone_number || '');
    setAddrLine1('');
    setAddrLine2('');
    setAddrLocality('');
    setAddrCity('Bengaluru');
    setAddrState('Karnataka');
    setAddrPin('560034');
    setAddrType('HOME');
    setIsDefaultShipping(false);
    setShowAddressModal(true);
  };

  const handleOpenEditAddress = (addr: Address) => {
    setEditingAddress(addr);
    setAddrName(addr.full_name);
    setAddrPhone(addr.phone_number);
    setAddrLine1(addr.address_line1);
    setAddrLine2(addr.address_line2 || '');
    setAddrLocality(addr.locality || '');
    setAddrCity(addr.city);
    setAddrState(addr.state);
    setAddrPin(addr.postal_code);
    setAddrType(addr.address_type);
    setIsDefaultShipping(addr.is_default_shipping);
    setShowAddressModal(true);
  };

  const handleSaveAddress = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    try {
      const payload = {
        full_name: addrName,
        phone_number: addrPhone,
        address_line1: addrLine1,
        address_line2: addrLine2,
        locality: addrLocality,
        city: addrCity,
        state: addrState,
        postal_code: addrPin,
        address_type: addrType,
        is_default_shipping: isDefaultShipping,
      };

      if (editingAddress) {
        await api.updateUserAddress(editingAddress.id, payload);
      } else {
        await api.addUserAddress(payload);
      }

      setShowAddressModal(false);
      const updated = await api.getUserAddresses();
      setAddresses(updated);
      setMessage('Address saved successfully!');
    } catch (err: any) {
      setError(err.message || 'Failed to save address.');
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteAddress = async (id: number) => {
    if (!window.confirm('Are you sure you want to delete this address?')) return;
    try {
      await api.deleteUserAddress(id);
      setAddresses(addresses.filter((a) => a.id !== id));
      setMessage('Address deleted.');
    } catch (err: any) {
      setError(err.message || 'Failed to delete address.');
    }
  };

  const handlePasswordChange = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setMessage('');
    try {
      await api.changePassword({
        current_password: currPassword,
        new_password: newPassword,
        logout_other_sessions: logoutOthers,
      });
      setCurrPassword('');
      setNewPassword('');
      setMessage('Password changed successfully! Other sessions have been revoked.');
      const updatedSess = await api.getActiveSessions();
      setSessions(updatedSess);
    } catch (err: any) {
      setError(err.message || 'Password change failed.');
    } finally {
      setLoading(false);
    }
  };

  const handleRevokeSession = async (sessId: number) => {
    try {
      await api.revokeSession(sessId);
      setSessions(sessions.filter((s) => s.id !== sessId));
      setMessage(`Session ${sessId} revoked.`);
    } catch (err: any) {
      setError(err.message || 'Failed to revoke session.');
    }
  };

  const handleRevokeAllOtherSessions = async () => {
    try {
      await api.revokeOtherSessions();
      const updatedSess = await api.getActiveSessions();
      setSessions(updatedSess);
      setMessage('All other active sessions revoked successfully.');
    } catch (err: any) {
      setError(err.message || 'Failed to revoke other sessions.');
    }
  };

  return (
    <div className="max-w-7xl mx-auto py-8 px-4">
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        {/* Sidebar Navigation */}
        <div className="bg-white rounded-lg p-4 shadow-sm border border-gray-200 h-fit">
          <div className="flex items-center space-x-3 p-3 border-b border-gray-100 mb-4">
            <div className="w-12 h-12 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-bold text-xl">
              {user?.full_name?.charAt(0) || 'U'}
            </div>
            <div>
              <div className="text-xs text-gray-500 font-semibold uppercase">Hello,</div>
              <div className="font-bold text-gray-800 text-base">{user?.full_name}</div>
              <div className="text-xs text-blue-600 font-medium">{user?.email}</div>
            </div>
          </div>

          <nav className="space-y-1">
            <button
              onClick={() => setSearchParams({ tab: 'profile' })}
              className={`w-full text-left px-4 py-3 rounded-md text-sm font-semibold flex items-center space-x-3 transition-colors ${
                activeTab === 'profile' ? 'bg-blue-50 text-blue-600 border-l-4 border-blue-600' : 'text-gray-700 hover:bg-gray-50'
              }`}
            >
              <span>👤</span>
              <span>Personal Information</span>
            </button>

            <button
              onClick={() => setSearchParams({ tab: 'addresses' })}
              className={`w-full text-left px-4 py-3 rounded-md text-sm font-semibold flex items-center space-x-3 transition-colors ${
                activeTab === 'addresses' ? 'bg-blue-50 text-blue-600 border-l-4 border-blue-600' : 'text-gray-700 hover:bg-gray-50'
              }`}
            >
              <span>📍</span>
              <span>Manage Addresses</span>
            </button>

            <button
              onClick={() => setSearchParams({ tab: 'security' })}
              className={`w-full text-left px-4 py-3 rounded-md text-sm font-semibold flex items-center space-x-3 transition-colors ${
                activeTab === 'security' ? 'bg-blue-50 text-blue-600 border-l-4 border-blue-600' : 'text-gray-700 hover:bg-gray-50'
              }`}
            >
              <span>🛡️</span>
              <span>Security & Sessions</span>
            </button>

            <button
              onClick={() => setSearchParams({ tab: 'orders' })}
              className={`w-full text-left px-4 py-3 rounded-md text-sm font-semibold flex items-center space-x-3 transition-colors ${
                activeTab === 'orders' ? 'bg-blue-50 text-blue-600 border-l-4 border-blue-600' : 'text-gray-700 hover:bg-gray-50'
              }`}
            >
              <span>📦</span>
              <span>My Orders</span>
            </button>

            <button
              onClick={() => setSearchParams({ tab: 'wishlist' })}
              className={`w-full text-left px-4 py-3 rounded-md text-sm font-semibold flex items-center space-x-3 transition-colors ${
                activeTab === 'wishlist' ? 'bg-blue-50 text-blue-600 border-l-4 border-blue-600' : 'text-gray-700 hover:bg-gray-50'
              }`}
            >
              <span>❤️</span>
              <span>Wishlist</span>
            </button>

            <button
              onClick={() => logout()}
              className="w-full text-left px-4 py-3 rounded-md text-sm font-semibold text-red-600 hover:bg-red-50 flex items-center space-x-3 transition-colors mt-4"
            >
              <span>🚪</span>
              <span>Logout</span>
            </button>
          </nav>
        </div>

        {/* Main Content Area */}
        <div className="md:col-span-3 bg-white rounded-lg p-6 shadow-sm border border-gray-200">
          {error && (
            <div className="bg-red-50 border-l-4 border-red-500 text-red-700 p-4 rounded text-sm mb-6">
              {error}
            </div>
          )}

          {message && (
            <div className="bg-green-50 border-l-4 border-green-500 text-green-700 p-4 rounded text-sm mb-6">
              {message}
            </div>
          )}

          {/* TAB 1: PROFILE */}
          {activeTab === 'profile' && (
            <div>
              <h2 className="text-xl font-bold text-gray-800 mb-6 border-b pb-3">Personal Information</h2>
              <form onSubmit={handleProfileSubmit} className="space-y-6 max-w-xl">
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">First Name</label>
                    <input
                      type="text"
                      value={firstName}
                      onChange={(e) => setFirstName(e.target.value)}
                      className="w-full p-2.5 border border-gray-300 rounded text-sm focus:ring-2 focus:ring-blue-500 outline-none"
                    />
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">Last Name</label>
                    <input
                      type="text"
                      value={lastName}
                      onChange={(e) => setLastName(e.target.value)}
                      className="w-full p-2.5 border border-gray-300 rounded text-sm focus:ring-2 focus:ring-blue-500 outline-none"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">Display Name</label>
                  <input
                    type="text"
                    required
                    value={fullName}
                    onChange={(e) => setFullName(e.target.value)}
                    className="w-full p-2.5 border border-gray-300 rounded text-sm focus:ring-2 focus:ring-blue-500 outline-none"
                  />
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">Email Address</label>
                  <input
                    type="email"
                    disabled
                    value={user?.email || ''}
                    className="w-full p-2.5 border border-gray-200 bg-gray-50 rounded text-sm text-gray-500 cursor-not-allowed"
                  />
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">Mobile Number</label>
                  <input
                    type="text"
                    value={phone}
                    onChange={(e) => setPhone(e.target.value)}
                    placeholder="+91 9876543210"
                    className="w-full p-2.5 border border-gray-300 rounded text-sm focus:ring-2 focus:ring-blue-500 outline-none"
                  />
                </div>

                <div>
                  <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">Roles & Status</label>
                  <div className="flex items-center space-x-2">
                    {user?.roles?.map((r) => (
                      <span key={r} className="bg-blue-100 text-blue-800 text-xs font-bold px-2.5 py-1 rounded">
                        {r}
                      </span>
                    ))}
                    <span className="bg-green-100 text-green-800 text-xs font-bold px-2.5 py-1 rounded">
                      {user?.account_status || 'ACTIVE'}
                    </span>
                  </div>
                </div>

                <button
                  type="submit"
                  disabled={loading}
                  className="bg-blue-600 hover:bg-blue-700 text-white font-bold px-6 py-3 rounded text-sm transition-colors"
                >
                  {loading ? 'Saving Changes...' : 'Save Profile Changes'}
                </button>
              </form>
            </div>
          )}

          {/* TAB 2: ADDRESSES */}
          {activeTab === 'addresses' && (
            <div>
              <div className="flex justify-between items-center mb-6 border-b pb-3">
                <h2 className="text-xl font-bold text-gray-800">Manage Saved Addresses</h2>
                <button
                  onClick={handleOpenAddAddress}
                  className="bg-blue-600 hover:bg-blue-700 text-white font-semibold text-sm px-4 py-2 rounded transition-colors"
                >
                  + Add New Address
                </button>
              </div>

              {addresses.length === 0 ? (
                <div className="text-center py-12 text-gray-500">
                  <span className="text-4xl block mb-2">📍</span>
                  No saved addresses found. Add a delivery address for faster checkout.
                </div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {addresses.map((addr) => (
                    <div key={addr.id} className="border border-gray-200 rounded-lg p-4 relative hover:shadow-md transition-shadow">
                      <div className="flex justify-between items-start mb-2">
                        <span className="bg-gray-100 text-gray-700 text-xs font-bold px-2 py-0.5 rounded uppercase">
                          {addr.address_type}
                        </span>
                        {addr.is_default_shipping && (
                          <span className="bg-blue-100 text-blue-800 text-xs font-bold px-2 py-0.5 rounded">
                            Default Shipping
                          </span>
                        )}
                      </div>
                      <div className="font-bold text-gray-800">{addr.full_name}</div>
                      <div className="text-sm text-gray-600 mt-1">{addr.address_line1}</div>
                      {addr.address_line2 && <div className="text-sm text-gray-600">{addr.address_line2}</div>}
                      <div className="text-sm text-gray-600">
                        {addr.city}, {addr.state} - <span className="font-semibold">{addr.postal_code}</span>
                      </div>
                      <div className="text-sm text-gray-600 font-medium mt-1">Phone: {addr.phone_number}</div>

                      <div className="flex space-x-3 mt-4 pt-3 border-t border-gray-100 text-xs font-semibold">
                        <button onClick={() => handleOpenEditAddress(addr)} className="text-blue-600 hover:underline">
                          Edit
                        </button>
                        <button onClick={() => handleDeleteAddress(addr.id)} className="text-red-600 hover:underline">
                          Delete
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {/* TAB 3: SECURITY & SESSIONS */}
          {activeTab === 'security' && (
            <div>
              <h2 className="text-xl font-bold text-gray-800 mb-6 border-b pb-3">Security Settings & Active Sessions</h2>

              {/* Password Change Form */}
              <div className="bg-gray-50 p-5 rounded-lg border border-gray-200 mb-8">
                <h3 className="text-base font-bold text-gray-800 mb-4">Change Account Password</h3>
                <form onSubmit={handlePasswordChange} className="space-y-4 max-w-md">
                  <div>
                    <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">Current Password</label>
                    <input
                      type="password"
                      required
                      value={currPassword}
                      onChange={(e) => setCurrPassword(e.target.value)}
                      className="w-full p-2 border border-gray-300 rounded text-sm outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  </div>

                  <div>
                    <label className="block text-xs font-semibold text-gray-600 uppercase mb-1">New Password</label>
                    <input
                      type="password"
                      required
                      value={newPassword}
                      onChange={(e) => setNewPassword(e.target.value)}
                      className="w-full p-2 border border-gray-300 rounded text-sm outline-none focus:ring-2 focus:ring-blue-500"
                    />
                  </div>

                  <div className="flex items-center space-x-2">
                    <input
                      type="checkbox"
                      id="logoutOthers"
                      checked={logoutOthers}
                      onChange={(e) => setLogoutOthers(e.target.checked)}
                    />
                    <label htmlFor="logoutOthers" className="text-xs text-gray-700 font-medium">
                      Logout all other active sessions on password update
                    </label>
                  </div>

                  <button
                    type="submit"
                    disabled={loading}
                    className="bg-blue-600 hover:bg-blue-700 text-white font-bold px-5 py-2 rounded text-sm"
                  >
                    Update Password
                  </button>
                </form>
              </div>

              {/* Active Sessions */}
              <div className="mb-8">
                <div className="flex justify-between items-center mb-4">
                  <h3 className="text-base font-bold text-gray-800">Active Login Sessions</h3>
                  <button
                    onClick={handleRevokeAllOtherSessions}
                    className="text-xs text-red-600 hover:bg-red-50 font-bold px-3 py-1.5 border border-red-200 rounded"
                  >
                    Logout All Other Devices
                  </button>
                </div>

                <div className="overflow-x-auto">
                  <table className="w-full text-left text-sm border-collapse">
                    <thead>
                      <tr className="bg-gray-100 text-gray-600 font-semibold text-xs uppercase border-b">
                        <th className="p-3">Device / IP</th>
                        <th className="p-3">User Agent</th>
                        <th className="p-3">Last Active</th>
                        <th className="p-3">Status</th>
                        <th className="p-3 text-right">Action</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100">
                      {sessions.map((s) => (
                        <tr key={s.id} className="hover:bg-gray-50">
                          <td className="p-3 font-medium">
                            {s.device_type === 'Mobile' ? '📱' : '💻'} {s.ip_address || '127.0.0.1'}
                          </td>
                          <td className="p-3 text-xs text-gray-500 max-w-xs truncate">{s.user_agent}</td>
                          <td className="p-3 text-xs text-gray-600">{new Date(s.last_active_at).toLocaleString()}</td>
                          <td className="p-3">
                            {s.is_current ? (
                              <span className="bg-green-100 text-green-800 text-xs font-bold px-2 py-0.5 rounded">Current Session</span>
                            ) : (
                              <span className="bg-blue-100 text-blue-800 text-xs font-bold px-2 py-0.5 rounded">Active</span>
                            )}
                          </td>
                          <td className="p-3 text-right">
                            {!s.is_current && (
                              <button onClick={() => handleRevokeSession(s.id)} className="text-xs text-red-600 hover:underline font-semibold">
                                Revoke
                              </button>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>

              {/* Audit Logs */}
              <div>
                <h3 className="text-base font-bold text-gray-800 mb-4">Security Event Audit Log</h3>
                <div className="max-h-60 overflow-y-auto border border-gray-200 rounded">
                  <table className="w-full text-left text-xs border-collapse">
                    <thead>
                      <tr className="bg-gray-100 text-gray-600 font-semibold uppercase border-b sticky top-0">
                        <th className="p-2">Timestamp</th>
                        <th className="p-2">Action</th>
                        <th className="p-2">Details</th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-100">
                      {auditLogs.map((log) => (
                        <tr key={log.id}>
                          <td className="p-2 text-gray-500 whitespace-nowrap">{new Date(log.created_at).toLocaleString()}</td>
                          <td className="p-2 font-bold text-blue-700">{log.action}</td>
                          <td className="p-2 text-gray-700">{log.details}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          )}

          {/* TAB 4: ORDERS */}
          {activeTab === 'orders' && (
            <div>
              <h2 className="text-xl font-bold text-gray-800 mb-6 border-b pb-3">My Orders</h2>
              {orders.length === 0 ? (
                <div className="text-center py-12 text-gray-500">
                  <span className="text-4xl block mb-2">📦</span>
                  No orders placed yet.
                </div>
              ) : (
                <div className="space-y-4">
                  {orders.map((o) => (
                    <div key={o.id} className="border border-gray-200 rounded-lg p-4 flex justify-between items-center">
                      <div>
                        <div className="font-bold text-gray-800">{o.order_number}</div>
                        <div className="text-xs text-gray-500">{new Date(o.created_at).toLocaleDateString()}</div>
                        <div className="text-sm font-semibold text-gray-700 mt-1">Total: ₹{o.grand_total.toLocaleString()}</div>
                      </div>
                      <div className="text-right">
                        <span className="bg-blue-100 text-blue-800 text-xs font-bold px-2.5 py-1 rounded block mb-2">{o.status}</span>
                        <button onClick={() => navigate(`/orders/${o.order_number}`)} className="text-xs text-blue-600 font-bold hover:underline">
                          View Details →
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}

          {/* TAB 5: WISHLIST */}
          {activeTab === 'wishlist' && (
            <div>
              <h2 className="text-xl font-bold text-gray-800 mb-6 border-b pb-3">My Wishlist</h2>
              {wishlistItems.length === 0 ? (
                <div className="text-center py-12 text-gray-500">
                  <span className="text-4xl block mb-2">❤️</span>
                  Your wishlist is empty.
                </div>
              ) : (
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                  {wishlistItems.map((item) => (
                    <div key={item.id} className="border border-gray-200 rounded p-3 text-center">
                      <div className="font-bold text-sm text-gray-800 truncate">{item.variant.title}</div>
                      <div className="text-blue-600 font-bold mt-1">₹{item.variant.price.toLocaleString()}</div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>
      </div>

      {/* Address Add/Edit Modal */}
      {showAddressModal && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
          <div className="bg-white rounded-lg p-6 max-w-lg w-full shadow-xl">
            <h3 className="text-lg font-bold text-gray-800 mb-4">{editingAddress ? 'Edit Address' : 'Add New Address'}</h3>
            <form onSubmit={handleSaveAddress} className="space-y-4">
              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">Full Name</label>
                  <input
                    type="text"
                    required
                    value={addrName}
                    onChange={(e) => setAddrName(e.target.value)}
                    className="w-full p-2 border rounded text-sm"
                  />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">Mobile Phone</label>
                  <input
                    type="text"
                    required
                    value={addrPhone}
                    onChange={(e) => setAddrPhone(e.target.value)}
                    className="w-full p-2 border rounded text-sm"
                  />
                </div>
              </div>

              <div>
                <label className="block text-xs font-semibold text-gray-600 mb-1">Address Line 1</label>
                <input
                  type="text"
                  required
                  value={addrLine1}
                  onChange={(e) => setAddrLine1(e.target.value)}
                  className="w-full p-2 border rounded text-sm"
                />
              </div>

              <div>
                <label className="block text-xs font-semibold text-gray-600 mb-1">Address Line 2 (Optional)</label>
                <input
                  type="text"
                  value={addrLine2}
                  onChange={(e) => setAddrLine2(e.target.value)}
                  className="w-full p-2 border rounded text-sm"
                />
              </div>

              <div className="grid grid-cols-3 gap-3">
                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">Locality</label>
                  <input
                    type="text"
                    value={addrLocality}
                    onChange={(e) => setAddrLocality(e.target.value)}
                    className="w-full p-2 border rounded text-sm"
                  />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">City</label>
                  <input
                    type="text"
                    required
                    value={addrCity}
                    onChange={(e) => setAddrCity(e.target.value)}
                    className="w-full p-2 border rounded text-sm"
                  />
                </div>
                <div>
                  <label className="block text-xs font-semibold text-gray-600 mb-1">PIN Code (6 digits)</label>
                  <input
                    type="text"
                    required
                    value={addrPin}
                    onChange={(e) => setAddrPin(e.target.value)}
                    className="w-full p-2 border rounded text-sm"
                  />
                </div>
              </div>

              <div className="flex space-x-4 pt-2">
                <label className="flex items-center space-x-1 text-sm">
                  <input
                    type="radio"
                    name="type"
                    value="HOME"
                    checked={addrType === 'HOME'}
                    onChange={() => setAddrType('HOME')}
                  />
                  <span>Home</span>
                </label>
                <label className="flex items-center space-x-1 text-sm">
                  <input
                    type="radio"
                    name="type"
                    value="WORK"
                    checked={addrType === 'WORK'}
                    onChange={() => setAddrType('WORK')}
                  />
                  <span>Work</span>
                </label>
              </div>

              <div className="flex justify-end space-x-3 pt-4 border-t">
                <button
                  type="button"
                  onClick={() => setShowAddressModal(false)}
                  className="px-4 py-2 border rounded text-sm font-semibold hover:bg-gray-50"
                >
                  Cancel
                </button>
                <button type="submit" disabled={loading} className="px-5 py-2 bg-blue-600 text-white rounded text-sm font-bold hover:bg-blue-700">
                  Save Address
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
