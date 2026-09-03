import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Heart, Star, ShoppingCart } from 'lucide-react';
import { Product } from '../types';
import { useCart } from '../context/CartContext';
import { api } from '../services/api';

interface ProductCardProps {
  product: Product;
  onWishlistToggle?: () => void;
}

export const ProductCard: React.FC<ProductCardProps> = ({ product, onWishlistToggle }) => {
  const { addToCart } = useCart();
  const navigate = useNavigate();

  const primaryVariant = product.variants && product.variants.length > 0 ? product.variants[0] : null;
  const primaryImage =
    product.images && product.images.length > 0
      ? product.images[0].image_url
      : 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=800&q=80';

  const price = primaryVariant ? primaryVariant.price : 0;
  const discountPrice = primaryVariant ? primaryVariant.discount_price : undefined;

  const discountPercent =
    discountPrice && price > 0 ? Math.round(((price - discountPrice) / price) * 100) : 0;
  const availableQuantity = primaryVariant
    ? Math.max(primaryVariant.stock_quantity - (primaryVariant.reserved_quantity || 0), 0)
    : 0;
  const isOutOfStock = product.stock_status === 'OUT_OF_STOCK' || availableQuantity === 0;

  const handleAddToCart = async (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (primaryVariant && !isOutOfStock) {
      try {
        await addToCart(primaryVariant.id, 1);
        navigate('/cart');
      } catch (err: any) {
        alert(err.message || 'Error adding to cart');
      }
    }
  };

  const handleToggleWishlist = async (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (primaryVariant) {
      try {
        await api.addToWishlist(primaryVariant.id);
        if (onWishlistToggle) onWishlistToggle();
        alert('Added item to Wishlist!');
      } catch (err: any) {
        alert(err.message || 'Please login to save items to wishlist.');
      }
    }
  };

  return (
    <div className="product-card">
      <button
        className="wishlist-icon-btn"
        onClick={handleToggleWishlist}
        title="Add to Wishlist"
        aria-label="Add to Wishlist"
      >
        <Heart size={20} />
      </button>

      <Link to={`/products/${product.slug || product.id}`}>
        <div className="product-image-wrapper">
          <img src={primaryImage} alt={product.name} className="product-image" loading="lazy" />
          {product.is_bestseller && <span className="product-badge bestseller-badge">Bestseller</span>}
          {product.stock_status === 'LOW_STOCK' && (
            <span className="product-badge stock-badge">Only a few left</span>
          )}
        </div>

        <h3 className="product-title" title={product.name}>
          {product.name}
        </h3>

        {product.rating_avg > 0 && (
          <div className="rating-badge">
            <span>{product.rating_avg}</span>
            <Star size={12} fill="#ffffff" />
            <span style={{ fontSize: '11px', opacity: 0.85 }}>({product.review_count})</span>
          </div>
        )}

        <div className="price-row">
          <span className="current-price">
            ₹{(discountPrice || price).toLocaleString('en-IN')}
          </span>
          {discountPrice && (
            <>
              <span className="original-price">₹{price.toLocaleString('en-IN')}</span>
              <span className="discount-percentage">{discountPercent}% off</span>
            </>
          )}
        </div>
        {isOutOfStock && <div className="stock-message out-of-stock-message">Currently unavailable</div>}
        {!isOutOfStock && product.stock_status === 'LOW_STOCK' && (
          <div className="stock-message low-stock-message">Selling fast</div>
        )}
      </Link>

      <button
        onClick={handleAddToCart}
        className="btn-primary"
        disabled={isOutOfStock}
        style={{ marginTop: '12px', width: '100%', fontSize: '13px', padding: '8px' }}
      >
        <ShoppingCart size={16} /> {isOutOfStock ? 'Out of Stock' : 'Add to Cart'}
      </button>
    </div>
  );
};
