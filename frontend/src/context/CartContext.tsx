import React, { createContext, useContext, useState, useEffect } from 'react';
import { Cart } from '../types';
import { api } from '../services/api';

interface CartContextType {
  cart: Cart | null;
  loading: boolean;
  addToCart: (variantId: number, quantity?: number) => Promise<void>;
  updateQuantity: (itemId: number, quantity: number) => Promise<void>;
  removeItem: (itemId: number) => Promise<void>;
  moveToWishlist: (itemId: number) => Promise<void>;
  mergeGuestCart: () => Promise<void>;
  refreshCart: () => Promise<void>;
}

const CartContext = createContext<CartContextType | undefined>(undefined);

export const CartProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [cart, setCart] = useState<Cart | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  const fetchCart = async () => {
    try {
      const c = await api.getCart();
      setCart(c);
    } catch (err) {
      console.error('Error fetching cart:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCart();
  }, []);

  const addToCart = async (variantId: number, quantity: number = 1) => {
    const updatedCart = await api.addToCart(variantId, quantity);
    setCart(updatedCart);
  };

  const updateQuantity = async (itemId: number, quantity: number) => {
    const updatedCart = await api.updateCartItem(itemId, quantity);
    setCart(updatedCart);
  };

  const removeItem = async (itemId: number) => {
    const updatedCart = await api.removeCartItem(itemId);
    setCart(updatedCart);
  };

  const moveToWishlist = async (itemId: number) => {
    const updatedCart = await api.moveCartItemToWishlist(itemId);
    setCart(updatedCart);
  };

  const mergeGuestCart = async () => {
    try {
      const mergedCart = await api.mergeCart();
      setCart(mergedCart);
    } catch (err) {
      console.error('Error merging cart:', err);
    }
  };

  return (
    <CartContext.Provider
      value={{
        cart,
        loading,
        addToCart,
        updateQuantity,
        removeItem,
        moveToWishlist,
        mergeGuestCart,
        refreshCart: fetchCart,
      }}
    >
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error('useCart must be used within a CartProvider');
  }
  return context;
};
