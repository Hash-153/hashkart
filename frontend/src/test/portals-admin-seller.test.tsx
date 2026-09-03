import { describe, it, expect } from 'vitest';
import React from 'react';
import { render, screen } from '@testing-library/react';
import { ToastProvider } from '../components/ui/Toast';
import { SellerPerformanceScorecard } from '../components/SellerPerformanceScorecard';
import { InvoiceDownloadButton } from '../components/InvoiceDownloadButton';
import { PriceDropNotifier } from '../components/PriceDropNotifier';
import { LiveNotificationCenter } from '../components/LiveNotificationCenter';

describe('Enterprise Portals & Storefront Widgets', () => {
  it('renders SellerPerformanceScorecard with Gold Merchant tier badge and score', () => {
    render(
      <ToastProvider>
        <SellerPerformanceScorecard
          sellerTier="GOLD"
          performanceScore={95}
          dispatchSLAMetPercentage={99.4}
          cancellationRatePercentage={0.1}
          customerReturnRatePercentage={1.2}
          averageRating={4.9}
        />
      </ToastProvider>
    );

    expect(screen.getByText('Seller Performance Scorecard')).toBeDefined();
    expect(screen.getByText('Gold Merchant')).toBeDefined();
    expect(screen.getByText('95/100')).toBeDefined();
    expect(screen.getByText('99.4% On-Time')).toBeDefined();
  });

  it('renders InvoiceDownloadButton for GST Tax Invoices', () => {
    render(
      <ToastProvider>
        <InvoiceDownloadButton
          orderNumber="HK-20260825-99A1"
          grandTotal={149900}
        />
      </ToastProvider>
    );

    expect(screen.getByText('GST Invoice')).toBeDefined();
  });

  it('renders PriceDropNotifier trigger button', () => {
    render(
      <ToastProvider>
        <PriceDropNotifier
          productId={1}
          productName="Apple iPhone 15 Pro Max"
          currentPrice={149900}
        />
      </ToastProvider>
    );

    expect(screen.getByText('Set Price Drop Alert')).toBeDefined();
  });

  it('renders LiveNotificationCenter with unread indicator badge', () => {
    render(
      <ToastProvider>
        <LiveNotificationCenter />
      </ToastProvider>
    );

    const btn = screen.getByRole('button', { name: /notifications/i });
    expect(btn).toBeDefined();
  });
});
