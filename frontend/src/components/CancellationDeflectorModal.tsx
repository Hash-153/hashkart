import React, { useState } from 'react';
import { AlertTriangle, Gift, Clock, ShieldCheck, X } from 'lucide-react';
import { Modal } from './ui/Modal';
import { useToast } from './ui/Toast';

export interface CancellationDeflectorProps {
  orderNumber: string;
  itemTitle: string;
  orderTotal: number;
  isOpen: boolean;
  onClose: () => void;
  onConfirmCancel: (reason: string) => void;
}

export const CancellationDeflectorModal: React.FC<CancellationDeflectorProps> = ({
  orderNumber,
  itemTitle,
  orderTotal,
  isOpen,
  onClose,
  onConfirmCancel,
}) => {
  const { showToast } = useToast();
  const [step, setStep] = useState<'OFFER' | 'REASON'>('OFFER');
  const [reason, setReason] = useState('Found cheaper elsewhere');

  const handleAcceptDiscount = () => {
    showToast(
      'success',
      '₹200 Instant Credit Applied!',
      '₹200 has been credited to your SuperCoin wallet and order discount recorded.'
    );
    onClose();
  };

  const handleProceedToCancel = () => {
    onConfirmCancel(reason);
    onClose();
  };

  if (!isOpen) return null;

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="Before You Cancel Your Order..."
      maxWidth="md"
    >
      {step === 'OFFER' ? (
        <div className="space-y-4 text-xs">
          <div className="p-3 bg-amber-50 border border-amber-200 rounded-lg flex items-start gap-3">
            <Gift size={24} className="text-amber-600 shrink-0 mt-0.5" />
            <div>
              <p className="font-bold text-amber-900">Wait! Keep your order & get ₹200 SuperCoin Credit</p>
              <p className="text-amber-700 mt-1 leading-relaxed">
                Your order for <span className="font-semibold">{itemTitle}</span> is packed and scheduled for priority dispatch tomorrow.
              </p>
            </div>
          </div>

          <div className="space-y-2">
            <button
              type="button"
              className="w-full btn btn-primary btn-md py-2.5 font-bold flex items-center justify-center gap-2"
              onClick={handleAcceptDiscount}
            >
              <Gift size={16} />
              <span>Keep Order & Claim ₹200 Cashback</span>
            </button>

            <button
              type="button"
              className="w-full text-center text-xs text-gray-400 hover:text-red-600 font-semibold py-1.5 transition-colors"
              onClick={() => setStep('REASON')}
            >
              No thanks, I still want to cancel order #{orderNumber}
            </button>
          </div>
        </div>
      ) : (
        <div className="space-y-4 text-xs">
          <p className="text-gray-600">Please tell us why you wish to cancel this item:</p>
          <div className="space-y-2">
            {[
              'Found a better price elsewhere',
              'Delivery date is too late',
              'Ordered by mistake / wrong address',
              'Want to change color or model variant',
            ].map((r) => (
              <label
                key={r}
                className="flex items-center gap-2.5 p-2.5 border rounded-lg cursor-pointer hover:bg-gray-50 transition-colors"
              >
                <input
                  type="radio"
                  name="cancel_reason"
                  checked={reason === r}
                  onChange={() => setReason(r)}
                  className="text-blue-600"
                />
                <span className="font-medium text-gray-800">{r}</span>
              </label>
            ))}
          </div>

          <div className="pt-3 border-t flex justify-end gap-2">
            <button
              type="button"
              className="btn btn-neutral btn-sm"
              onClick={() => setStep('OFFER')}
            >
              Back
            </button>
            <button
              type="button"
              className="btn bg-red-600 hover:bg-red-700 text-white btn-sm"
              onClick={handleProceedToCancel}
            >
              Confirm Cancellation
            </button>
          </div>
        </div>
      )}
    </Modal>
  );
};
