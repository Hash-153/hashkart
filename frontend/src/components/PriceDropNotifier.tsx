import React, { useState } from 'react';
import { Bell, TrendingDown, CheckCircle2 } from 'lucide-react';
import { Modal } from './ui/Modal';
import { useToast } from './ui/Toast';

export interface PriceDropNotifierProps {
  productId: number;
  productName: string;
  currentPrice: number;
}

export const PriceDropNotifier: React.FC<PriceDropNotifierProps> = ({
  productId,
  productName,
  currentPrice,
}) => {
  const { showToast } = useToast();
  const [isOpen, setIsOpen] = useState(false);
  const [targetPrice, setTargetPrice] = useState(Math.round(currentPrice * 0.9));
  const [email, setEmail] = useState('');

  const handleSubscribe = (e: React.FormEvent) => {
    e.preventDefault();
    showToast(
      'success',
      'Price Alert Created!',
      `We will notify you at ${email || 'your account email'} when ${productName} drops to ₹${targetPrice.toLocaleString('en-IN')}.`
    );
    setIsOpen(false);
  };

  return (
    <>
      <button
        type="button"
        className="btn btn-neutral btn-sm flex items-center gap-1.5 text-xs text-blue-700 hover:bg-blue-50 border-blue-200"
        onClick={() => setIsOpen(true)}
      >
        <TrendingDown size={14} />
        <span>Set Price Drop Alert</span>
      </button>

      {isOpen && (
        <Modal
          isOpen={true}
          onClose={() => setIsOpen(false)}
          title="Get Instant Price Drop Alerts"
        >
          <form onSubmit={handleSubscribe} className="space-y-4 text-xs">
            <div className="p-3 bg-blue-50/50 border border-blue-100 rounded-lg">
              <p className="font-bold text-gray-900">{productName}</p>
              <p className="text-gray-500 mt-0.5">
                Current Price: <span className="font-bold text-gray-900">₹{currentPrice.toLocaleString('en-IN')}</span>
              </p>
            </div>

            <div className="space-y-1">
              <label className="font-semibold text-gray-700">Target Price to Alert (₹):</label>
              <input
                type="number"
                max={currentPrice - 100}
                value={targetPrice}
                onChange={(e) => setTargetPrice(Number(e.target.value))}
                className="w-full p-2 border border-gray-300 rounded text-xs font-bold"
                required
              />
              <span className="text-[11px] text-gray-400">
                You will save ₹{(currentPrice - targetPrice).toLocaleString('en-IN')} ({Math.round(((currentPrice - targetPrice) / currentPrice) * 100)}% OFF).
              </span>
            </div>

            <div className="space-y-1">
              <label className="font-semibold text-gray-700">Notify Email Address:</label>
              <input
                type="email"
                placeholder="you@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full p-2 border border-gray-300 rounded text-xs"
              />
            </div>

            <div className="pt-3 border-t flex justify-end gap-2">
              <button
                type="button"
                className="btn btn-neutral btn-sm"
                onClick={() => setIsOpen(false)}
              >
                Cancel
              </button>
              <button
                type="submit"
                className="btn btn-primary btn-sm flex items-center gap-1"
              >
                <Bell size={12} />
                <span>Activate Alert</span>
              </button>
            </div>
          </form>
        </Modal>
      )}
    </>
  );
};
