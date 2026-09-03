import React, { useState } from 'react';
import { CreditCard, QrCode, Smartphone, Landmark, Wallet, Banknote, ShieldCheck, Check } from 'lucide-react';
import { Badge } from './ui/Badge';

interface PaymentAccordionProps {
  orderAmount: number;
  onSelectMethod: (method: string, details?: any) => void;
  selectedMethod: string;
}

export const CheckoutPaymentAccordion: React.FC<PaymentAccordionProps> = ({
  orderAmount,
  onSelectMethod,
  selectedMethod,
}) => {
  const [selectedUpiApp, setSelectedUpiApp] = useState<'GPAY' | 'PHONEPE' | 'PAYTM' | 'OTHER'>('GPAY');
  const [customVpa, setCustomVpa] = useState<string>('');
  const [selectedBank, setSelectedBank] = useState<string>('HDFC');
  const [cardNumber, setCardNumber] = useState<string>('4111 2222 3333 4444');
  const [expiry, setExpiry] = useState<string>('08/29');
  const [cvv, setCvv] = useState<string>('123');

  const POPULAR_BANKS = [
    { code: 'HDFC', name: 'HDFC Bank' },
    { code: 'ICIC', name: 'ICICI Bank' },
    { code: 'SBIN', name: 'State Bank of India' },
    { code: 'UTIB', name: 'Axis Bank' },
    { code: 'KKBK', name: 'Kotak Mahindra' },
  ];

  return (
    <div className="space-y-3 text-xs">
      {/* 1. UPI (Instant & Fast) */}
      <div className={`border rounded-lg overflow-hidden transition ${selectedMethod === 'UPI' ? 'border-blue-600 bg-blue-50/20' : 'border-gray-200'}`}>
        <button
          type="button"
          onClick={() => onSelectMethod('UPI')}
          className="w-full p-3.5 flex items-center justify-between text-left hover:bg-gray-50/80"
        >
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-full bg-blue-100 flex items-center justify-center text-blue-600">
              <Smartphone size={16} />
            </div>
            <div>
              <p className="font-bold text-gray-900">UPI (Google Pay, PhonePe, Paytm, BHIM)</p>
              <p className="text-[11px] text-gray-500">Instant direct bank payment with 0 transaction fees</p>
            </div>
          </div>
          <Badge variant="success">Fastest</Badge>
        </button>

        {selectedMethod === 'UPI' && (
          <div className="p-4 bg-white border-t border-gray-100 space-y-3">
            <div className="grid grid-cols-3 gap-2">
              {(['GPAY', 'PHONEPE', 'PAYTM'] as const).map((app) => (
                <button
                  key={app}
                  type="button"
                  onClick={() => setSelectedUpiApp(app)}
                  className={`p-2.5 rounded-lg border text-center font-bold text-xs transition ${
                    selectedUpiApp === app ? 'border-blue-600 bg-blue-50 text-blue-700 shadow-sm' : 'border-gray-200 text-gray-700'
                  }`}
                >
                  {app === 'GPAY' ? 'Google Pay' : app === 'PHONEPE' ? 'PhonePe' : 'Paytm'}
                </button>
              ))}
            </div>

            <div className="pt-2">
              <p className="font-semibold text-gray-700 mb-1">Or enter UPI ID / VPA:</p>
              <div className="flex gap-2">
                <input
                  type="text"
                  placeholder="username@okhdfcbank"
                  value={customVpa}
                  onChange={(e) => setCustomVpa(e.target.value)}
                  className="flex-1 p-2 border rounded text-xs font-mono"
                />
                <button
                  type="button"
                  className="btn btn-neutral btn-sm"
                  onClick={() => alert(`Verified UPI VPA: ${customVpa}`)}
                >
                  Verify
                </button>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* 2. Credit / Debit Cards with RBI Tokenization */}
      <div className={`border rounded-lg overflow-hidden transition ${selectedMethod === 'CARD' ? 'border-blue-600 bg-blue-50/20' : 'border-gray-200'}`}>
        <button
          type="button"
          onClick={() => onSelectMethod('CARD')}
          className="w-full p-3.5 flex items-center justify-between text-left hover:bg-gray-50/80"
        >
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-full bg-purple-100 flex items-center justify-center text-purple-600">
              <CreditCard size={16} />
            </div>
            <div>
              <p className="font-bold text-gray-900">Credit / Debit / ATM Card</p>
              <p className="text-[11px] text-gray-500">10% Instant Discount on HDFC & ICICI Cards</p>
            </div>
          </div>
          <Badge variant="purple">Bank Offers</Badge>
        </button>

        {selectedMethod === 'CARD' && (
          <div className="p-4 bg-white border-t border-gray-100 space-y-3">
            <div>
              <label className="block font-semibold text-gray-700 mb-1">Card Number:</label>
              <input
                type="text"
                value={cardNumber}
                onChange={(e) => setCardNumber(e.target.value)}
                placeholder="4111 XXXX XXXX 4444"
                className="w-full p-2 border rounded text-xs font-mono"
              />
            </div>
            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="block font-semibold text-gray-700 mb-1">Valid Thru:</label>
                <input
                  type="text"
                  value={expiry}
                  onChange={(e) => setExpiry(e.target.value)}
                  placeholder="MM/YY"
                  className="w-full p-2 border rounded text-xs font-mono"
                />
              </div>
              <div>
                <label className="block font-semibold text-gray-700 mb-1">CVV:</label>
                <input
                  type="password"
                  maxLength={4}
                  value={cvv}
                  onChange={(e) => setCvv(e.target.value)}
                  placeholder="•••"
                  className="w-full p-2 border rounded text-xs font-mono"
                />
              </div>
            </div>
            <div className="flex items-center gap-1.5 text-[11px] text-gray-500 pt-1">
              <ShieldCheck size={14} className="text-green-600" />
              <span>Card information secured by RBI Tokenization (CoFT) Vault.</span>
            </div>
          </div>
        )}
      </div>

      {/* 3. Net Banking */}
      <div className={`border rounded-lg overflow-hidden transition ${selectedMethod === 'NET_BANKING' ? 'border-blue-600 bg-blue-50/20' : 'border-gray-200'}`}>
        <button
          type="button"
          onClick={() => onSelectMethod('NET_BANKING')}
          className="w-full p-3.5 flex items-center justify-between text-left hover:bg-gray-50/80"
        >
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-full bg-amber-100 flex items-center justify-center text-amber-600">
              <Landmark size={16} />
            </div>
            <div>
              <p className="font-bold text-gray-900">Net Banking</p>
              <p className="text-[11px] text-gray-500">All 54 Indian commercial scheduled banks supported</p>
            </div>
          </div>
        </button>

        {selectedMethod === 'NET_BANKING' && (
          <div className="p-4 bg-white border-t border-gray-100 space-y-3">
            <div className="grid grid-cols-2 sm:grid-cols-3 gap-2">
              {POPULAR_BANKS.map((b) => (
                <button
                  key={b.code}
                  type="button"
                  onClick={() => setSelectedBank(b.code)}
                  className={`p-2 rounded border text-left font-semibold text-xs transition ${
                    selectedBank === b.code ? 'border-blue-600 bg-blue-50 text-blue-700' : 'border-gray-200'
                  }`}
                >
                  {b.name}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* 4. Cash on Delivery (COD) */}
      <div className={`border rounded-lg overflow-hidden transition ${selectedMethod === 'COD' ? 'border-blue-600 bg-blue-50/20' : 'border-gray-200'}`}>
        <button
          type="button"
          onClick={() => onSelectMethod('COD')}
          className="w-full p-3.5 flex items-center justify-between text-left hover:bg-gray-50/80"
        >
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 rounded-full bg-emerald-100 flex items-center justify-center text-emerald-600">
              <Banknote size={16} />
            </div>
            <div>
              <p className="font-bold text-gray-900">Cash on Delivery (COD)</p>
              <p className="text-[11px] text-gray-500">Pay via Cash / QR code at your doorstep upon delivery</p>
            </div>
          </div>
          <span className="font-semibold text-gray-600">₹30 fee</span>
        </button>
      </div>
    </div>
  );
};
