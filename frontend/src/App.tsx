import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { CartProvider } from './context/CartContext';
import { ToastProvider } from './components/ui/Toast';

import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { ProtectedRoute } from './components/ProtectedRoute';

import { Home } from './pages/Home';
import { ProductListing } from './pages/ProductListing';
import { ProductDetail } from './pages/ProductDetail';
import { CartPage } from './pages/CartPage';
import { CheckoutPage } from './pages/CheckoutPage';
import { Login } from './pages/Login';
import { Register } from './pages/Register';
import { ForgotPassword } from './pages/ForgotPassword';
import { ResetPassword } from './pages/ResetPassword';
import { WishlistPage } from './pages/WishlistPage';
import { AccountDashboard } from './pages/AccountDashboard';
import { OrderHistoryPage } from './pages/OrderHistoryPage';
import { AdminDashboardPage } from './pages/AdminDashboardPage';
import { AdminCatalogPage } from './pages/AdminCatalogPage';
import { SellerDashboardPage } from './pages/SellerDashboardPage';
import { SupportPage } from './pages/SupportPage';

// New Enterprise Storefront & Portal Pages
import { SuperCoinZonePage } from './pages/SuperCoinZonePage';
import { ComparePage } from './pages/ComparePage';
import { DealsPage } from './pages/DealsPage';
import { ReturnExchangePage } from './pages/ReturnExchangePage';
import { SellerInventoryPage } from './pages/seller/SellerInventoryPage';
import { SellerOrdersPage } from './pages/seller/SellerOrdersPage';
import { SellerPayoutsPage } from './pages/seller/SellerPayoutsPage';
import { SellerAnalyticsPage } from './pages/seller/SellerAnalyticsPage';
import { SellerBulkUploadPage } from './pages/seller/SellerBulkUploadPage';
import { SellerAdvertisingPage } from './pages/seller/SellerAdvertisingPage';
import { AdminWMSPage } from './pages/admin/AdminWMSPage';
import { AdminReturnsPage } from './pages/admin/AdminReturnsPage';
import { AdminFraudPage } from './pages/admin/AdminFraudPage';
import { AdminSupportPage } from './pages/admin/AdminSupportPage';
import { AdminSettlementAuditPage } from './pages/admin/AdminSettlementAuditPage';
import { AdminCategoryManagementPage } from './pages/admin/AdminCategoryManagementPage';
import { AdminAuditLogsPage } from './pages/admin/AdminAuditLogsPage';
import { AdminABTestingPage } from './pages/admin/AdminABTestingPage';
import { AdminTaxReportingPage } from './pages/admin/AdminTaxReportingPage';

export const App: React.FC = () => {
  return (
    <AuthProvider>
      <CartProvider>
        <ToastProvider>
          <Router>
            <div className="app-container">
              <Navbar />
              <main className="main-content">
                <Routes>
                  {/* Public Storefront */}
                  <Route path="/" element={<Home />} />
                  <Route path="/products" element={<ProductListing />} />
                  <Route path="/products/:idOrSlug" element={<ProductDetail />} />
                  <Route path="/supercoins" element={<SuperCoinZonePage />} />
                  <Route path="/compare" element={<ComparePage />} />
                  <Route path="/deals" element={<DealsPage />} />
                  <Route path="/returns/new" element={<ReturnExchangePage />} />
                  <Route path="/cart" element={<CartPage />} />
                  <Route path="/checkout" element={<CheckoutPage />} />
                  <Route path="/login" element={<Login />} />
                  <Route path="/register" element={<Register />} />
                  <Route path="/forgot-password" element={<ForgotPassword />} />
                  <Route path="/reset-password" element={<ResetPassword />} />
                  <Route path="/wishlist" element={<WishlistPage />} />

                  <Route
                    path="/support"
                    element={
                      <ProtectedRoute>
                        <SupportPage />
                      </ProtectedRoute>
                    }
                  />

                  {/* Customer Account */}
                  <Route
                    path="/account"
                    element={
                      <ProtectedRoute>
                        <AccountDashboard />
                      </ProtectedRoute>
                    }
                  />
                  <Route path="/profile" element={<Navigate to="/account" replace />} />
                  <Route path="/orders" element={<OrderHistoryPage />} />
                  <Route path="/orders/:orderNumber" element={<OrderHistoryPage />} />

                  {/* Seller Hub Portals */}
                  <Route
                    path="/seller"
                    element={
                      <ProtectedRoute>
                        <SellerDashboardPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/seller/inventory"
                    element={
                      <ProtectedRoute>
                        <SellerInventoryPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/seller/orders"
                    element={
                      <ProtectedRoute>
                        <SellerOrdersPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/seller/payouts"
                    element={
                      <ProtectedRoute>
                        <SellerPayoutsPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/seller/analytics"
                    element={
                      <ProtectedRoute>
                        <SellerAnalyticsPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/seller/bulk-upload"
                    element={
                      <ProtectedRoute>
                        <SellerBulkUploadPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/seller/advertising"
                    element={
                      <ProtectedRoute>
                        <SellerAdvertisingPage />
                      </ProtectedRoute>
                    }
                  />

                  {/* Admin Command Operations */}
                  <Route
                    path="/admin"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminDashboardPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/catalog"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminCatalogPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/categories"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminCategoryManagementPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/wms"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminWMSPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/returns"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminReturnsPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/fraud"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminFraudPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/support"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminSupportPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/settlements"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminSettlementAuditPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/audit-logs"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminAuditLogsPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/ab-testing"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminABTestingPage />
                      </ProtectedRoute>
                    }
                  />
                  <Route
                    path="/admin/tax-reporting"
                    element={
                      <ProtectedRoute allowedRoles={['ADMIN', 'MANAGER', 'STAFF']}>
                        <AdminTaxReportingPage />
                      </ProtectedRoute>
                    }
                  />
                </Routes>
              </main>
              <Footer />
            </div>
          </Router>
        </ToastProvider>
      </CartProvider>
    </AuthProvider>
  );
};

export default App;
