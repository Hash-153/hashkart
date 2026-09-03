import React from 'react';
import { describe, it, expect, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { Modal } from '../components/ui/Modal';
import { Tabs } from '../components/ui/Tabs';
import { Accordion } from '../components/ui/Accordion';
import { Badge } from '../components/ui/Badge';
import { MetricCard } from '../components/ui/MetricCard';
import { ProgressBar } from '../components/ui/ProgressBar';
import { DataTable } from '../components/ui/DataTable';

describe('UI Design System Components', () => {
  it('renders Modal when open and fires onClose on close button click', () => {
    const handleClose = vi.fn();
    render(
      <Modal isOpen={true} onClose={handleClose} title="Test Modal">
        <p>Modal Body Content</p>
      </Modal>
    );

    expect(screen.getByText('Test Modal')).toBeDefined();
    expect(screen.getByText('Modal Body Content')).toBeDefined();

    const closeBtn = screen.getByLabelText('Close modal');
    fireEvent.click(closeBtn);
    expect(handleClose).toHaveBeenCalledTimes(1);
  });

  it('does not render Modal when isOpen is false', () => {
    render(
      <Modal isOpen={false} onClose={() => {}} title="Hidden Modal">
        <p>Hidden Content</p>
      </Modal>
    );
    expect(screen.queryByText('Hidden Modal')).toBeNull();
  });

  it('renders Tabs and switches active tab on tab click', () => {
    const tabs = [
      { id: 'tab1', label: 'Overview', content: <div>Overview Content</div> },
      { id: 'tab2', label: 'Specs', content: <div>Specs Content</div> },
    ];

    render(<Tabs tabs={tabs} defaultTab="tab1" />);

    expect(screen.getByText('Overview Content')).toBeDefined();
    expect(screen.queryByText('Specs Content')).toBeNull();

    fireEvent.click(screen.getByText('Specs'));
    expect(screen.getByText('Specs Content')).toBeDefined();
  });

  it('renders Accordion and toggles item content expansion', () => {
    const items = [
      { id: 'acc1', title: 'Return Policy', content: <p>7 days replacement</p> },
      { id: 'acc2', title: 'Warranty Info', content: <p>1 year brand warranty</p> },
    ];

    render(<Accordion items={items} />);

    expect(screen.queryByText('7 days replacement')).toBeNull();
    fireEvent.click(screen.getByText('Return Policy'));
    expect(screen.getByText('7 days replacement')).toBeDefined();
  });

  it('renders Badge with correct variant class and text', () => {
    const { container } = render(<Badge variant="success">In Stock</Badge>);
    expect(screen.getByText('In Stock')).toBeDefined();
    expect(container.querySelector('.badge-success')).toBeDefined();
  });

  it('renders MetricCard with title, value, and trend', () => {
    render(
      <MetricCard
        title="Total Revenue"
        value="₹1,24,000"
        subtitle="vs previous week"
        trendPercentage={14}
        variant="green"
      />
    );
    expect(screen.getByText('Total Revenue')).toBeDefined();
    expect(screen.getByText('₹1,24,000')).toBeDefined();
    expect(screen.getByText('14%')).toBeDefined();
  });

  it('renders ProgressBar with correct clamped width percentage', () => {
    const { container } = render(
      <ProgressBar value={75} label="Deal Claimed" />
    );
    expect(screen.getByText('Deal Claimed')).toBeDefined();
    expect(screen.getByText('75%')).toBeDefined();
    const fill = container.querySelector('.progress-fill') as HTMLElement;
    expect(fill.style.width).toBe('75%');
  });

  it('renders DataTable with records and filters data via search', () => {
    const data = [
      { id: 1, name: 'iPhone 15', price: 69999 },
      { id: 2, name: 'Samsung S24', price: 79999 },
      { id: 3, name: 'MacBook Air', price: 99999 },
    ];
    const columns = [
      { key: 'name', header: 'Product Name', sortable: true },
      { key: 'price', header: 'Price', render: (item: any) => `₹${item.price}` },
    ];

    render(<DataTable data={data} columns={columns} searchPlaceholder="Search products..." />);

    expect(screen.getByText('iPhone 15')).toBeDefined();
    expect(screen.getByText('Samsung S24')).toBeDefined();

    const searchInput = screen.getByPlaceholderText('Search products...');
    fireEvent.change(searchInput, { target: { value: 'MacBook' } });

    expect(screen.getByText('MacBook Air')).toBeDefined();
    expect(screen.queryByText('iPhone 15')).toBeNull();
  });
});
