import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Star, ShoppingCart, Zap, CheckCircle2 } from 'lucide-react';
import { ProductDetail as ProductDetailType, ProductVariant, Review } from '../types';
import { api } from '../services/api';
import { useCart } from '../context/CartContext';
import { ProductCard } from '../components/ProductCard';

export const ProductDetail: React.FC = () => {
  const { idOrSlug } = useParams<{ idOrSlug: string }>();
  const [product, setProduct] = useState<ProductDetailType | null>(null);
  const [selectedVariant, setSelectedVariant] = useState<ProductVariant | null>(null);
  const [reviews, setReviews] = useState<Review[]>([]);
  const [selectedImage, setSelectedImage] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string>('');

  const { addToCart } = useCart();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchDetail = async () => {
      if (!idOrSlug) return;
      setLoading(true);
      setError('');
      try {
        const data = await api.getProductDetail(idOrSlug);
        setProduct(data);
        if (data.variants && data.variants.length > 0) {
          setSelectedVariant(data.variants[0]);
        }
        if (data.images && data.images.length > 0) {
          setSelectedImage(data.images[0].image_url);
        }

        const revs = await api.getProductReviews(data.id);
        setReviews(revs);
        api.recordRecentlyViewed(data.id).catch(() => {});
      } catch (err: any) {
        setError(err.message || 'Failed to load product details.');
      } finally {
        setLoading(false);
      }
    };
    fetchDetail();
  }, [idOrSlug]);

  if (loading) return <div style={{ padding: '60px', textAlign: 'center' }}>Loading product details...</div>;
  if (error || !product) return <div style={{ padding: '60px', textAlign: 'center', color: 'red' }}>{error || 'Product not found.'}</div>;

  const price = selectedVariant ? selectedVariant.price : 0;
  const discountPrice = selectedVariant ? selectedVariant.discount_price : undefined;
  const inStock = selectedVariant ? selectedVariant.stock_quantity > 0 : false;

  const handleAddToCart = async () => {
    if (selectedVariant) {
      try {
        await addToCart(selectedVariant.id, 1);
        navigate('/cart');
      } catch (err: any) {
        alert(err.message);
      }
    }
  };

  const handleBuyNow = async () => {
    if (selectedVariant) {
      try {
        await addToCart(selectedVariant.id, 1);
        navigate('/checkout');
      } catch (err: any) {
        alert(err.message);
      }
    }
  };

  return (
    <div style={{ backgroundColor: 'var(--bg-card)', padding: '24px', borderRadius: '4px', border: '1px solid var(--border-color)', marginTop: '16px' }}>
      <div style={{ display: 'grid', gridTemplateColumns: 'minmax(300px, 450px) 1fr', gap: '36px' }}>
        {/* Left Column: Gallery */}
        <div>
          <div style={{ height: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center', border: '1px solid var(--border-color)', borderRadius: '4px', padding: '16px', marginBottom: '16px' }}>
            <img src={selectedImage || 'https://via.placeholder.com/400'} alt={product.name} style={{ maxHeight: '100%', maxWidth: '100%', objectFit: 'contain' }} />
          </div>

          <div style={{ display: 'flex', gap: '12px', overflowX: 'auto' }}>
            {product.images.map((img) => (
              <img
                key={img.id}
                src={img.image_url}
                alt="Thumbnail"
                onClick={() => setSelectedImage(img.image_url)}
                style={{
                  width: '64px',
                  height: '64px',
                  objectFit: 'contain',
                  border: selectedImage === img.image_url ? '2px solid var(--primary-2874f0)' : '1px solid var(--border-color)',
                  borderRadius: '4px',
                  cursor: 'pointer',
                }}
              />
            ))}
          </div>

          {/* Action Buttons */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '12px', marginTop: '24px' }}>
            <button onClick={handleAddToCart} disabled={!inStock} className="btn-secondary">
              <ShoppingCart size={18} /> ADD TO CART
            </button>
            <button onClick={handleBuyNow} disabled={!inStock} className="btn-primary">
              <Zap size={18} /> BUY NOW
            </button>
          </div>
        </div>

        {/* Right Column: Information & Specs */}
        <div>
          <span style={{ fontSize: '12px', color: 'var(--text-muted)', textTransform: 'uppercase', fontWeight: 600 }}>
            {product.brand?.name || 'HashKart Certified'}
          </span>
          <h1 style={{ fontSize: '22px', fontWeight: 700, margin: '4px 0 12px' }}>{product.name}</h1>

          {/* Rating */}
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px', marginBottom: '16px' }}>
            <div className="rating-badge">
              <span>{product.rating_avg}</span>
              <Star size={12} fill="#ffffff" />
            </div>
            <span style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
              {product.review_count} Ratings & Reviews
            </span>
          </div>

          {/* Price Block */}
          <div style={{ display: 'flex', alignItems: 'baseline', gap: '12px', marginBottom: '16px' }}>
            <span style={{ fontSize: '28px', fontWeight: 800 }}>
              ₹{(discountPrice || price).toLocaleString('en-IN')}
            </span>
            {discountPrice && (
              <>
                <span style={{ fontSize: '16px', color: 'var(--text-muted)', textDecoration: 'line-through' }}>
                  ₹{price.toLocaleString('en-IN')}
                </span>
                <span style={{ fontSize: '16px', color: 'var(--success-green)', fontWeight: 700 }}>
                  {Math.round(((price - discountPrice) / price) * 100)}% off
                </span>
              </>
            )}
          </div>

          {/* Stock Indicator */}
          <div style={{ marginBottom: '20px' }}>
            {inStock ? (
              <span style={{ color: 'var(--success-green)', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '6px' }}>
                <CheckCircle2 size={16} /> In Stock ({selectedVariant?.stock_quantity} remaining)
              </span>
            ) : (
              <span style={{ color: 'var(--danger-red)', fontWeight: 700 }}>Out of Stock</span>
            )}
          </div>

          {/* Variant Selector */}
          {product.variants.length > 1 && (
            <div style={{ marginBottom: '24px' }}>
              <h4 style={{ fontSize: '14px', fontWeight: 600, marginBottom: '8px' }}>Select Variant</h4>
              <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
                {product.variants.map((v) => (
                  <button
                    key={v.id}
                    onClick={() => setSelectedVariant(v)}
                    style={{
                      padding: '8px 16px',
                      border: selectedVariant?.id === v.id ? '2px solid var(--primary-2874f0)' : '1px solid var(--border-color)',
                      borderRadius: '4px',
                      backgroundColor: selectedVariant?.id === v.id ? 'var(--primary-light)' : 'transparent',
                      fontWeight: selectedVariant?.id === v.id ? 700 : 400,
                      cursor: 'pointer',
                    }}
                  >
                    {v.title}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Specifications Table */}
          {product.attributes && product.attributes.length > 0 && (
            <div style={{ marginBottom: '24px' }}>
              <h4 style={{ fontSize: '14px', fontWeight: 700, marginBottom: '8px' }}>Product Specifications</h4>
              <table style={{ width: '100%', fontSize: '13px', borderCollapse: 'collapse', border: '1px solid #eee' }}>
                <tbody>
                  {product.attributes.map((attr) => (
                    <tr key={attr.id} style={{ borderBottom: '1px solid #eee' }}>
                      <td style={{ padding: '8px 12px', fontWeight: 600, color: '#666', width: '30%', backgroundColor: '#f9f9f9' }}>
                        {attr.attribute_name}
                      </td>
                      <td style={{ padding: '8px 12px', color: '#222' }}>{attr.attribute_value}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {/* Highlights */}
          {product.highlight_features && (
            <div style={{ marginBottom: '24px' }}>
              <h4 style={{ fontSize: '14px', fontWeight: 700, marginBottom: '8px' }}>Highlights</h4>
              <ul style={{ paddingLeft: '20px', fontSize: '14px', lineHeight: '1.8' }}>
                {product.highlight_features.split('\n').map((h, idx) => (
                  <li key={idx}>{h}</li>
                ))}
              </ul>
            </div>
          )}

          {/* Description */}
          <div style={{ marginBottom: '24px' }}>
            <h4 style={{ fontSize: '14px', fontWeight: 700, marginBottom: '8px' }}>Description</h4>
            <p style={{ fontSize: '14px', lineHeight: '1.6', color: 'var(--text-main)' }}>{product.description}</p>
          </div>
        </div>
      </div>

      {/* Related Products Section */}
      {product.related_products && product.related_products.length > 0 && (
        <div style={{ marginTop: '40px', borderTop: '1px solid var(--border-color)', paddingTop: '24px' }}>
          <h3 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '16px' }}>Similar Products You Might Like</h3>
          <div className="product-grid">
            {product.related_products.map((relProd) => (
              <ProductCard key={relProd.id} product={relProd} />
            ))}
          </div>
        </div>
      )}

      {/* Customer Reviews Section */}
      <div style={{ marginTop: '40px', borderTop: '1px solid var(--border-color)', paddingTop: '24px' }}>
        <h3 style={{ fontSize: '18px', fontWeight: 700, marginBottom: '16px' }}>Ratings & Customer Reviews</h3>

        {reviews.length === 0 ? (
          <p style={{ color: 'var(--text-muted)' }}>No customer reviews yet. Be the first to review this product!</p>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {reviews.map((r) => (
              <div key={r.id} style={{ borderBottom: '1px solid var(--border-color)', paddingBottom: '16px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px' }}>
                  <div className="rating-badge">
                    <span>{r.rating}</span>
                    <Star size={10} fill="#ffffff" />
                  </div>
                  <h4 style={{ fontSize: '14px', fontWeight: 700 }}>{r.title}</h4>
                </div>
                <p style={{ fontSize: '13px', color: 'var(--text-main)', marginBottom: '6px' }}>{r.comment}</p>
                <div style={{ fontSize: '12px', color: 'var(--text-muted)' }}>
                  By {r.user_name || 'Customer'} {r.is_verified_purchase && <span style={{ color: 'var(--success-green)', fontWeight: 600 }}>✔ Verified Buyer</span>}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
