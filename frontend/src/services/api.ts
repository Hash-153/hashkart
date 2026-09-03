import {
  User,
  Category,
  CategoryTree,
  Brand,
  Product,
  ProductDetail,
  ProductListResponse,
  Cart,
  Wishlist,
  Order,
  Review,
  Notification,
  DashboardStats,
  SalesAnalyticsPoint,
  Address,
  UserSession,
  SecurityAuditLog,
  AttributeDefinition,
  AutocompleteSuggestion,
  TrendingSearchItem,
  UserSearchHistoryItem,
  DiscoverySection,
  CheckoutPreview,
  OrderRefund,
  SellerDashboard,
  SellerProfile,
  SupportTicket,
} from '../types';

const API_BASE = '/api/v1';

const getSessionId = (): string => {
  let sid = localStorage.getItem('hashkart_session_id');
  if (!sid) {
    sid = 'sid_' + Math.random().toString(36).substring(2) + Date.now().toString(36);
    localStorage.setItem('hashkart_session_id', sid);
  }
  return sid;
};

let isRefreshing = false;

async function request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
  const token = localStorage.getItem('novamart_token') || localStorage.getItem('hashkart_token');
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    'X-Session-ID': getSessionId(),
    ...(options.headers as Record<string, string>),
  };

  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  let response = await fetch(`${API_BASE}${endpoint}`, {
    ...options,
    headers,
  });

  if (response.status === 401 && !endpoint.startsWith('/auth/login') && !endpoint.startsWith('/auth/refresh') && !isRefreshing) {
    const refreshToken = localStorage.getItem('hashkart_refresh_token') || localStorage.getItem('novamart_refresh_token');
    if (refreshToken) {
      isRefreshing = true;
      try {
        const refreshRes = await fetch(`${API_BASE}/auth/refresh?refresh_token=${encodeURIComponent(refreshToken)}`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
        });
        if (refreshRes.ok) {
          const tokenData = await refreshRes.json();
          localStorage.setItem('hashkart_token', tokenData.access_token);
          localStorage.setItem('hashkart_refresh_token', tokenData.refresh_token);

          headers['Authorization'] = `Bearer ${tokenData.access_token}`;
          response = await fetch(`${API_BASE}${endpoint}`, {
            ...options,
            headers,
          });
        } else {
          localStorage.removeItem('hashkart_token');
          localStorage.removeItem('hashkart_refresh_token');
        }
      } catch {
        localStorage.removeItem('hashkart_token');
        localStorage.removeItem('hashkart_refresh_token');
      } finally {
        isRefreshing = false;
      }
    }
  }

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    const message = errorData.detail || errorData.error?.message || 'An error occurred';
    throw new Error(message);
  }

  return response.json();
}

export const api = {
  // Auth & Account Security
  register: (data: any) => request<User>('/auth/register', { method: 'POST', body: JSON.stringify(data) }),
  login: (data: any) => request<{ access_token: string; refresh_token: string }>('/auth/login', { method: 'POST', body: JSON.stringify(data) }),
  logout: () => request<{ message: string }>('/auth/logout', { method: 'POST' }),
  getMe: () => request<User>('/auth/me'),
  updateProfile: (data: any) => request<User>('/auth/profile', { method: 'PUT', body: JSON.stringify(data) }),
  changePassword: (data: any) => request<{ message: string }>('/auth/change-password', { method: 'POST', body: JSON.stringify(data) }),
  forgotPassword: (email: string) => request<{ message: string; dev_simulation_reset_token?: string; dev_reset_url?: string }>('/auth/forgot-password', { method: 'POST', body: JSON.stringify({ email }) }),
  resetPassword: (data: any) => request<{ message: string }>('/auth/reset-password', { method: 'POST', body: JSON.stringify(data) }),
  getActiveSessions: () => request<UserSession[]>('/auth/sessions'),
  revokeSession: (sessionId: number) => request<{ message: string }>(`/auth/sessions/${sessionId}`, { method: 'DELETE' }),
  revokeOtherSessions: () => request<{ message: string }>('/auth/sessions/other/all', { method: 'DELETE' }),

  // User Address Book & Security Logs
  getUserAddresses: () => request<Address[]>('/users/me/addresses'),
  addUserAddress: (data: any) => request<Address>('/users/me/addresses', { method: 'POST', body: JSON.stringify(data) }),
  updateUserAddress: (id: number, data: any) => request<Address>(`/users/me/addresses/${id}`, { method: 'PUT', body: JSON.stringify(data) }),
  deleteUserAddress: (id: number) => request<{ message: string }>(`/users/me/addresses/${id}`, { method: 'DELETE' }),
  setDefaultShippingAddress: (id: number) => request<Address>(`/users/me/addresses/${id}/default-shipping`, { method: 'POST' }),
  getSecurityAuditLogs: () => request<SecurityAuditLog[]>('/users/me/security-events'),

  // Catalog & Search Subsystem
  getCategories: () => request<Category[]>('/catalog/categories'),
  getCategoryTree: () => request<CategoryTree[]>('/catalog/categories/tree'),
  getBrands: (featuredOnly: boolean = false) => request<Brand[]>(`/catalog/brands?featured_only=${featuredOnly}`),
  getAttributeDefinitions: (categoryId?: number) => request<AttributeDefinition[]>(`/catalog/attributes${categoryId ? `?category_id=${categoryId}` : ''}`),
  getProducts: (params: string = '') => request<ProductListResponse>(`/search?${params}`),
  getProductDetail: (idOrSlug: string) => request<ProductDetail>(`/catalog/products/${idOrSlug}`),

  // Search & Autocomplete
  getAutocompleteSuggestions: (query: string) => request<AutocompleteSuggestion[]>(`/search/autocomplete?q=${encodeURIComponent(query)}`),
  getTrendingSearches: () => request<TrendingSearchItem[]>('/search/trending'),
  getUserSearchHistory: () => request<UserSearchHistoryItem[]>('/search/history'),
  deleteSearchHistoryItem: (id: number) => request<{ message: string }>(`/search/history/${id}`, { method: 'DELETE' }),
  clearUserSearchHistory: () => request<{ message: string }>('/search/history', { method: 'DELETE' }),

  // Discovery & Recommendations
  getRecommendedDiscovery: () => request<DiscoverySection>('/discovery/recommended'),
  getBestSellingDiscovery: () => request<DiscoverySection>('/discovery/best-selling'),
  getDealsDiscovery: () => request<DiscoverySection>('/discovery/deals'),
  getNewArrivalsDiscovery: () => request<DiscoverySection>('/discovery/new-arrivals'),
  getRecentlyViewed: () => request<Product[]>('/discovery/recently-viewed'),
  recordRecentlyViewed: (productId: number) => request<{ message: string }>(`/discovery/recently-viewed/${productId}`, { method: 'POST' }),
  clearRecentlyViewed: () => request<{ message: string }>('/discovery/recently-viewed', { method: 'DELETE' }),

  // Cart
  getCart: () => request<Cart>('/cart'),
  addToCart: (variantId: number, quantity: number = 1) => request<Cart>('/cart/items', { method: 'POST', body: JSON.stringify({ variant_id: variantId, quantity }) }),
  updateCartItem: (itemId: number, quantity: number) => request<Cart>(`/cart/items/${itemId}`, { method: 'PUT', body: JSON.stringify({ quantity }) }),
  removeCartItem: (itemId: number) => request<Cart>(`/cart/items/${itemId}`, { method: 'DELETE' }),
  moveCartItemToWishlist: (itemId: number) => request<Cart>(`/cart/items/${itemId}/move-to-wishlist`, { method: 'POST' }),
  mergeCart: () => request<Cart>('/cart/merge', { method: 'POST' }),

  // Wishlist
  getWishlist: () => request<Wishlist>('/wishlist'),
  addToWishlist: (variantId: number) => request<Wishlist>('/wishlist/items', { method: 'POST', body: JSON.stringify({ variant_id: variantId }) }),
  removeFromWishlist: (itemId: number) => request<Wishlist>(`/wishlist/items/${itemId}`, { method: 'DELETE' }),
  moveWishlistItemToCart: (itemId: number) => request<Wishlist>(`/wishlist/items/${itemId}/move-to-cart`, { method: 'POST' }),

  // Addresses & Checkout
  getAddresses: () => request<Address[]>('/users/me/addresses'),
  addAddress: (data: any) => request<Address>('/users/me/addresses', { method: 'POST', body: JSON.stringify(data) }),
  validateCoupon: (code: string, subtotal: number) => request<any>(`/checkout/coupons/validate?code=${encodeURIComponent(code)}&subtotal=${subtotal}`, { method: 'POST' }),
  getCheckoutPreview: (addressId: number, couponCode?: string) =>
    request<CheckoutPreview>(`/checkout/preview?address_id=${addressId}${couponCode ? `&coupon_code=${encodeURIComponent(couponCode)}` : ''}`, { method: 'POST' }),
  processCheckout: (data: any, idempotencyKey?: string) =>
    request<Order>('/checkout/process', {
      method: 'POST',
      headers: idempotencyKey ? { 'X-Idempotency-Key': idempotencyKey } : {},
      body: JSON.stringify(data),
    }),

  // Orders
  getOrders: () => request<Order[]>('/orders'),
  getOrderDetail: (orderNumber: string) => request<Order>(`/orders/${orderNumber}`),
  cancelOrder: (orderNumber: string) => request<Order>(`/orders/${orderNumber}/cancel`, { method: 'POST' }),
  requestOrderRefund: (orderNumber: string, reason: string, amount?: number) =>
    request<OrderRefund>(`/orders/${orderNumber}/refund`, { method: 'POST', body: JSON.stringify({ reason, amount }) }),

  // Reviews
  getProductReviews: (productId: number) => request<Review[]>(`/reviews/product/${productId}`),
  submitReview: (data: any) => request<Review>('/reviews', { method: 'POST', body: JSON.stringify(data) }),

  // Notifications
  getNotifications: () => request<Notification[]>('/notifications'),
  markNotificationRead: (id: number) => request<Notification>(`/notifications/${id}/read`, { method: 'PUT' }),

  // Admin Portal & Inventory Management
  getDashboardStats: () => request<DashboardStats>('/admin/dashboard/stats'),
  adminCreateCategory: (data: any) => request<Category>('/admin/categories', { method: 'POST', body: JSON.stringify(data) }),
  adminUpdateCategory: (id: number, data: any) => request<Category>(`/admin/categories/${id}`, { method: 'PUT', body: JSON.stringify(data) }),
  adminDeleteCategory: (id: number) => request<{ message: string }>(`/admin/categories/${id}`, { method: 'DELETE' }),

  adminCreateBrand: (data: any) => request<Brand>('/admin/brands', { method: 'POST', body: JSON.stringify(data) }),
  adminUpdateBrand: (id: number, data: any) => request<Brand>(`/admin/brands/${id}`, { method: 'PUT', body: JSON.stringify(data) }),

  createProduct: (data: any) => request<Product>('/admin/products', { method: 'POST', body: JSON.stringify(data) }),
  adminUpdateProduct: (id: number, data: any) => request<Product>(`/admin/products/${id}`, { method: 'PUT', body: JSON.stringify(data) }),
  adminAddVariant: (productId: number, data: any) => request<any>(`/admin/products/${productId}/variants`, { method: 'POST', body: JSON.stringify(data) }),
  adminAdjustInventory: (variantId: number, newQuantity: number, reason: string) =>
    request<any>('/admin/inventory/adjust', { method: 'POST', body: JSON.stringify({ variant_id: variantId, new_quantity: newQuantity, reason }) }),

  getAdminOrders: () => request<Order[]>('/admin/orders'),
  updateOrderStatus: (orderId: number, status: string) => request<Order>(`/admin/orders/${orderId}/status`, { method: 'PUT', body: JSON.stringify({ status }) }),
  getSalesAnalytics: (days: number = 7) => request<{ timeframe: string; data_points: SalesAnalyticsPoint[] }>(`/admin/analytics/sales?days=${days}`),

  // Seller and Support Operations
  getSellerProfile: () => request<SellerProfile>('/seller/profile'),
  onboardSeller: (data: any) => request<SellerProfile>('/seller/onboarding', { method: 'POST', body: JSON.stringify(data) }),
  getSellerDashboard: (days: number = 30) => request<SellerDashboard>(`/seller/analytics/dashboard?days=${days}`),
  getSupportTickets: () => request<SupportTicket[]>('/support/tickets'),
  createSupportTicket: (data: any) => request<SupportTicket>('/support/tickets', { method: 'POST', body: JSON.stringify(data) }),
  submitPaymentWebhook: (provider: string, data: any, signature: string) => request<any>(`/payments/webhooks/${provider}`, { method: 'POST', headers: { 'X-Webhook-Signature': signature }, body: JSON.stringify(data) }),
  getPaymentReconciliation: () => request<any[]>('/payments/reconciliation'),

  // Enterprise Logistics & Pincode Matrix
  checkPincodeServiceability: (pincode: string, cartTotal: number = 0) =>
    request<any>(`/logistics/serviceability/check?pincode=${encodeURIComponent(pincode)}&cart_total=${cartTotal}`),

  // Loyalty & SuperCoins
  getLoyaltyProfile: () => request<any>('/loyalty/profile'),
  redeemCoins: (coinsToSpend: number, orderId?: number) =>
    request<any>('/loyalty/redeem', { method: 'POST', body: JSON.stringify({ coins_to_spend: coinsToSpend, order_id: orderId }) }),

  // Flash Sales & Lightning Deals
  getActiveFlashSales: () => request<any[]>('/flash-sales/active'),
  reserveFlashDeal: (eventId: number, productId: number, quantity: number = 1) =>
    request<any>(`/flash-sales/${eventId}/reserve?product_id=${productId}&quantity=${quantity}`, { method: 'POST' }),

  // Product Comparison Matrix
  getProductComparisonMatrix: (productIds: string) =>
    request<any>(`/compare?product_ids=${encodeURIComponent(productIds)}`),

  // Community Product Q&A
  getProductQA: (productId: number) => request<any[]>(`/qa/products/${productId}`),
  postProductQuestion: (productId: number, questionText: string) =>
    request<any>(`/qa/products/${productId}/questions`, { method: 'POST', body: JSON.stringify({ question_text: questionText }) }),
  postProductAnswer: (questionId: number, answerText: string) =>
    request<any>(`/qa/questions/${questionId}/answers`, { method: 'POST', body: JSON.stringify({ answer_text: answerText }) }),
  upvoteQuestion: (questionId: number) =>
    request<any>(`/qa/questions/${questionId}/upvote`, { method: 'POST' }),

  // Seller Escrow & Settlement Engine
  getSellerEscrowSummary: () => request<any>('/seller/settlement/escrow'),
  requestSellerPayout: (sellerId: number, payoutMethod: string = 'NEFT') =>
    request<any>('/seller/settlement/payout/request', { method: 'POST', body: JSON.stringify({ seller_id: sellerId, payout_method: payoutMethod }) }),
};

