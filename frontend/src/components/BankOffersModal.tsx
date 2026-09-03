import React from 'react';
import { Tag, CreditCard, CheckCircle2 } from 'lucide-react';
import { Modal } from './ui/Modal';

export interface BankOffer {
  id: number;
  title: string;
  bank_code: string;
  card_type: string;
  discount_percentage?: number;
  flat_discount_amount?: number;
  min_order_value: number;
  max_discount_cap?: number;
  terms_and_conditions?: string;
}

export interface BankOffersModalProps {
  isOpen: boolean;
  onClose: () => void;
  productPrice: number;
}

const DEFAULT_BANK_OFFERS: BankOffer[] = [
  {
    id: 1,
    title: '10% Instant Discount on HDFC Bank Credit Card EMI',
    bank_code: 'HDFC',
    card_type: 'CREDIT_CARD',
    discount_percentage: 10,
    min_order_value: 5000,
    max_discount_cap: 1500,
    terms_and_conditions: 'Valid on 6, 9, and 12 months EMI tenures. Maximum discount of ₹1,500.',
  },
  {
    id: 2,
    title: '5% Unlimited Cashback on NovaMart Axis Bank Credit Card',
    bank_code: 'AXIS',
    card_type: 'CREDIT_CARD',
    discount_percentage: 5,
    min_order_value: 500,
    terms_and_conditions: 'No upper limit on cashback. Credited directly to monthly statement.',
  },
  {
    id: 3,
    title: 'Flat ₹1,000 Off on ICICI Bank Debit & Credit Cards',
    bank_code: 'ICICI',
    card_type: 'ALL_CARDS',
    flat_discount_amount: 1000,
    min_order_value: 10000,
    terms_and_conditions: 'Applicable once per card during the promotion period.',
  },
  {
    id: 4,
    title: '₹750 Instant Discount on SBI Credit Card Non-EMI Transactions',
    bank_code: 'SBI',
    card_type: 'CREDIT_CARD',
    flat_discount_amount: 750,
    min_order_value: 4999,
    terms_and_conditions: 'Minimum transaction value of ₹4,999 required.',
  },
];

export const BankOffersModal: React.FC<BankOffersModalProps> = ({
  isOpen,
  onClose,
  productPrice,
}) => {
  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="Available Bank Offers & Discounts"
      maxWidth="lg"
    >
      <div className="bank-offers-modal-body">
        <div className="p-3 bg-blue-50 border border-blue-200 rounded-lg flex items-center gap-2 mb-4">
          <Tag size={18} className="text-primary" />
          <p className="text-xs text-blue-900 font-medium">
            Offers automatically apply at checkout when choosing eligible payment method.
          </p>
        </div>

        <div className="space-y-3">
          {DEFAULT_BANK_OFFERS.map((offer) => {
            const isEligible = productPrice >= offer.min_order_value;
            let discountAmount = 0;
            if (offer.flat_discount_amount) {
              discountAmount = offer.flat_discount_amount;
            } else if (offer.discount_percentage) {
              discountAmount = Math.round((productPrice * offer.discount_percentage) / 100);
              if (offer.max_discount_cap) {
                discountAmount = Math.min(discountAmount, offer.max_discount_cap);
              }
            }

            return (
              <div
                key={offer.id}
                className={`p-3.5 rounded-lg border transition-all ${
                  isEligible
                    ? 'border-gray-200 bg-white hover:border-blue-400'
                    : 'border-gray-100 bg-gray-50 opacity-60'
                }`}
              >
                <div className="flex items-start justify-between gap-3">
                  <div className="flex items-start gap-2.5">
                    <CreditCard size={18} className="text-gray-700 mt-0.5" />
                    <div>
                      <h4 className="text-sm font-semibold text-gray-900">{offer.title}</h4>
                      <p className="text-xs text-gray-500 mt-0.5">
                        Min. Order Value: ₹{offer.min_order_value.toLocaleString('en-IN')}
                      </p>
                      {offer.terms_and_conditions && (
                        <p className="text-[11px] text-gray-400 mt-1">
                          {offer.terms_and_conditions}
                        </p>
                      )}
                    </div>
                  </div>

                  {isEligible && discountAmount > 0 && (
                    <div className="text-right whitespace-nowrap">
                      <span className="text-xs font-bold text-green-700 bg-green-50 px-2 py-0.5 rounded">
                        Save ₹{discountAmount.toLocaleString('en-IN')}
                      </span>
                    </div>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </Modal>
  );
};
