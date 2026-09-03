import { describe, expect, it } from 'vitest';

function formatRupees(amount: number): string {
  return new Intl.NumberFormat('en-IN', {
    style: 'currency',
    currency: 'INR',
    maximumFractionDigits: 0,
  }).format(amount);
}

describe('storefront formatting', () => {
  it('formats Indian prices consistently', () => {
    expect(formatRupees(129999)).toContain('1,29,999');
  });
});
