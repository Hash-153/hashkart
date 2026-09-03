export interface User {
  id: number;
  email: string;
  full_name: string;
  first_name?: string;
  last_name?: string;
  phone_number?: string;
  profile_image_url?: string;
  account_status?: string;
  is_active: boolean;
  is_verified: boolean;
  preferred_language?: string;
  preferred_currency?: string;
  last_login_at?: string;
  roles: string[];
  permissions?: string[];
  created_at: string;
  updated_at: string;
}

export interface Permission {
  id: number;
  code: string;
  name: string;
  description?: string;
}

export interface UserSession {
  id: number;
  token_jti: string;
  ip_address?: string;
  user_agent?: string;
  device_type?: string;
  is_revoked: boolean;
  is_current: boolean;
  created_at: string;
  last_active_at: string;
  expires_at: string;
}

export interface SecurityAuditLog {
  id: number;
  user_id?: number;
  action: string;
  entity_type?: string;
  entity_id?: string;
  details?: string;
  created_at: string;
}

export interface Address {
  id: number;
  user_id: number;
  full_name: string;
  phone_number: string;
  address_line1: string;
  address_line2?: string;
  locality?: string;
  city: string;
  state: string;
  postal_code: string;
  country: string;
  address_type: string;
  is_default: boolean;
  is_default_shipping: boolean;
  is_default_billing: boolean;
  created_at?: string;
}

export interface AttributeDefinition {
  id: number;
  category_id?: number;
  name: string;
  code: string;
  data_type: string;
  unit?: string;
  is_filterable: boolean;
  is_required: boolean;
  options?: string[];
}

export interface AttributeValue {
  id: number;
  attribute_definition_id: number;
  product_id: number;
  variant_id?: number;
  value: string;
  definition?: AttributeDefinition;
}

export interface Category {
  id: number;
  parent_id?: number;
  name: string;
  slug: string;
  description?: string;
  image_url?: string;
  display_order: number;
  is_active: boolean;
  subcategories: Category[];
}

export interface CategoryTree {
  id: number;
  parent_id?: number;
  name: string;
  slug: string;
  description?: string;
  image_url?: string;
  display_order: number;
  is_active: boolean;
  subcategories: CategoryTree[];
}

export interface Brand {
  id: number;
  name: string;
  slug: string;
  logo_url?: string;
  description?: string;
  is_active: boolean;
  is_featured?: boolean;
  product_count?: number;
}

export interface ProductImage {
  id: number;
  variant_id?: number;
  image_url: string;
  alt_text?: string;
  display_order: number;
  is_primary: boolean;
}

export interface ProductAttribute {
  id: number;
  attribute_name: string;
  attribute_value: string;
}

export interface ProductVariant {
  id: number;
  product_id: number;
  sku: string;
  title: string;
  price: number;
  discount_price?: number;
  stock_quantity: number;
  reserved_quantity?: number;
  weight_grams?: number;
  dimensions?: string;
  is_active: boolean;
  images: ProductImage[];
  sale_price?: number;
  discount_percentage?: number;
  stock_status?: 'IN_STOCK' | 'LOW_STOCK' | 'OUT_OF_STOCK';
}

export interface PricingSummary {
  original_price: number;
  sale_price: number;
  discount_amount: number;
  discount_percentage: number;
  has_discount: boolean;
}

export interface Product {
  id: number;
  category_id: number;
  brand_id?: number;
  name: string;
  slug: string;
  description: string;
  short_description?: string;
  highlight_features?: string;
  status: string;
  visibility: string;
  is_active: boolean;
  is_featured: boolean;
  is_bestseller: boolean;
  rating_avg: number;
  review_count: number;
  created_at: string;
  updated_at: string;
  category?: Category;
  brand?: Brand;
  variants: ProductVariant[];
  attributes: ProductAttribute[];
  typed_attribute_values?: AttributeValue[];
  images: ProductImage[];
  sale_price?: number;
  discount_percentage?: number;
  stock_status?: 'IN_STOCK' | 'LOW_STOCK' | 'OUT_OF_STOCK';
}

export interface ProductDetail extends Product {
  pricing_summary?: PricingSummary;
  related_products: Product[];
}

export interface AutocompleteSuggestion {
  label: string;
  type: 'category' | 'brand' | 'product' | 'keyword';
  slug?: string;
  id?: number;
  search_count?: number;
}

export interface FacetCategoryItem {
  id: number;
  name: string;
  slug: string;
  count: number;
}

export interface FacetBrandItem {
  id: number;
  name: string;
  slug: string;
  count: number;
}

export interface FacetPriceRange {
  min: number;
  max: number;
}

export interface FacetRatingItem {
  rating: number;
  count: number;
  label: string;
}

export interface FacetDynamicAttributeOption {
  value: string;
  count: number;
}

export interface FacetDynamicAttribute {
  name: string;
  options: FacetDynamicAttributeOption[];
}

export interface SearchFacets {
  categories: FacetCategoryItem[];
  brands: FacetBrandItem[];
  price_range: FacetPriceRange;
  ratings: FacetRatingItem[];
  dynamic_attributes: FacetDynamicAttribute[];
}

export interface ProductListResponse {
  items: Product[];
  total: number;
  page: number;
  limit: number;
  pages: number;
  has_next: boolean;
  has_prev: boolean;
  query?: string;
  did_you_mean?: string;
  facets?: SearchFacets;
}

export interface SellerDashboard {
  seller_id: number | null;
  period_days: number;
  active_listings: number;
  orders: number;
  revenue: number;
  pending_payout: number;
}

export interface SellerProfile {
  id: number;
  user_id: number;
  business_name: string;
  legal_name: string;
  tax_identifier: string;
  phone: string;
  status: string;
  rejection_reason?: string;
  approved_at?: string;
  created_at: string;
}

export interface SupportTicket {
  id: number;
  ticket_number: string;
  customer_id: number;
  subject: string;
  category: string;
  priority: string;
  status: string;
  description: string;
  assigned_to?: number;
  created_at: string;
  updated_at: string;
}

export interface UserSearchHistoryItem {
  id: number;
  query: string;
  result_count: number;
  created_at: string;
}

export interface TrendingSearchItem {
  query: string;
  search_count: number;
}

export interface DiscoverySection {
  section_key: string;
  title: string;
  subtitle?: string;
  layout_type: string;
  products: Product[];
}

export interface RecentlyViewedItem {
  id: number;
  product_id: number;
  viewed_at: string;
  product: Product;
}

export interface CartItem {
  id: number;
  cart_id: number;
  variant_id: number;
  quantity: number;
  added_at: string;
  variant: ProductVariant;
  price_changed?: boolean;
  old_price?: number;
  stock_warning?: string;
}

export interface Cart {
  id: number;
  user_id?: number;
  session_id?: string;
  items: CartItem[];
  subtotal: number;
  estimated_tax: number;
  estimated_shipping: number;
  discount_amount: number;
  grand_total: number;
  item_count: number;
  price_change_warnings?: string[];
  stock_warnings?: string[];
}

export interface WishlistItem {
  id: number;
  wishlist_id: number;
  variant_id: number;
  added_at: string;
  variant: ProductVariant;
  is_available?: boolean;
  current_price?: number;
}

export interface Wishlist {
  id: number;
  user_id: number;
  items: WishlistItem[];
}

export interface PreviewLineItem {
  variant_id: number;
  product_name: string;
  variant_title: string;
  sku: string;
  unit_price: number;
  quantity: number;
  line_total: number;
}

export interface CheckoutPreview {
  address_id: number;
  items: PreviewLineItem[];
  subtotal: number;
  promotion_discount: number;
  coupon_discount: number;
  total_discount: number;
  tax: number;
  shipping: number;
  grand_total: number;
  applied_promotions: Array<{ name: string; description: string; discount_amount: number }>;
  price_changes: string[];
  stock_warnings: string[];
}

export interface OrderRefund {
  id: number;
  order_id: number;
  refund_reference: string;
  amount: number;
  reason: string;
  refund_status: string;
  created_at: string;
}

export interface OrderItem {
  id: number;
  order_id: number;
  variant_id: number;
  product_name: string;
  variant_title: string;
  sku: string;
  unit_price: number;
  discount_price?: number;
  quantity: number;
  line_subtotal: number;
}

export interface Payment {
  id: number;
  order_id: number;
  payment_method: string;
  transaction_reference: string;
  amount: number;
  status: string;
  created_at: string;
}

export interface Shipment {
  id: number;
  order_id: number;
  tracking_number: string;
  carrier_name: string;
  shipment_status: string;
  shipped_at?: string;
  estimated_delivery?: string;
  delivered_at?: string;
}

export interface Order {
  id: number;
  order_number: string;
  user_id: number;
  address_id: number;
  status: string;
  payment_status: string;
  subtotal: number;
  tax_amount: number;
  shipping_fee: number;
  discount_amount: number;
  grand_total: number;
  created_at: string;
  updated_at: string;
  address?: Address;
  items: OrderItem[];
  payment?: Payment;
  shipment?: Shipment;
}

export interface Review {
  id: number;
  product_id: number;
  user_id: number;
  variant_id?: number;
  rating: number;
  title: string;
  comment: string;
  is_verified_purchase: boolean;
  status: string;
  created_at: string;
  user_name?: string;
}

export interface Notification {
  id: number;
  user_id: number;
  title: string;
  message: string;
  notification_type: string;
  is_read: boolean;
  link?: string;
  created_at: string;
}

export interface DashboardStats {
  total_sales_revenue: number;
  total_orders_count: number;
  total_customers_count: number;
  total_products_count: number;
  low_stock_products_count: number;
  pending_orders_count: number;
  average_order_value: number;
}

export interface SalesAnalyticsPoint {
  date: string;
  sales_amount: number;
  orders_count: number;
}
