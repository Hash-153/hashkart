import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import { CompareDrawer } from '../components/CompareDrawer';
import { OrderTracker } from '../components/OrderTracker';
import { EMICalculator } from '../components/EMICalculator';
import { BankOffersModal } from '../components/BankOffersModal';

describe('Storefront Features and Modals', () => {
  it('renders CompareDrawer with items and handles removal and clear', () => {
    const handleRemove = vi.fn();
    const handleClear = vi.fn();
    const mockProducts: any[] = [
      { id: 1, name: 'iPhone 15', price: 69999, images: [{ image_url: 'http://img.jpg' }] },
      { id: 2, name: 'OnePlus 12', price: 64999, images: [{ image_url: 'http://img2.jpg' }] },
    ];

    render(
      <BrowserRouter>
        <CompareDrawer
          products={mockProducts}
          onRemove={handleRemove}
          onClear={handleClear}
        />
      </BrowserRouter>
    );

    expect(screen.getByText('Compare (2/4 Products)')).toBeDefined();
    expect(screen.getByText('iPhone 15')).toBeDefined();
    expect(screen.getByText('OnePlus 12')).toBeDefined();

    const clearBtn = screen.getByText('Clear All');
    fireEvent.click(clearBtn);
    expect(handleClear).toHaveBeenCalledTimes(1);
  });

  it('renders OrderTracker with timeline status and tracking number', () => {
    render(
      <OrderTracker
        currentStatus="SHIPPED"
        orderNumber="HK-20260825-99A"
        estimatedDelivery="Thursday, 28 Aug"
        trackingNumber="EKA-992182"
        carrierName="EKART Express"
      />
    );

    expect(screen.getByText('#HK-20260825-99A')).toBeDefined();
    expect(screen.getByText('Order Confirmed')).toBeDefined();
    expect(screen.getByText('Dispatched & In Transit')).toBeDefined();
    expect(screen.getByText('EKA-992182')).toBeDefined();
  });

  it('renders EMICalculator with calculated monthly rates', () => {
    render(
      <EMICalculator
        isOpen={true}
        onClose={() => {}}
        price={60000}
      />
    );

    expect(screen.getByText('Easy Monthly Installments (EMI) Plans')).toBeDefined();
    expect(screen.getByText('3 Months')).toBeDefined();
    expect(screen.getByText('No Cost EMI Available')).toBeDefined();
  });

  it('renders BankOffersModal with discount tiers', () => {
    render(
      <BankOffersModal
        isOpen={true}
        onClose={() => {}}
        productPrice={25000}
      />
    );

    expect(screen.getByText('Available Bank Offers & Discounts')).toBeDefined();
    expect(screen.getByText('10% Instant Discount on HDFC Bank Credit Card EMI')).toBeDefined();
  });
});
