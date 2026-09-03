import React, { useState } from 'react';
import { Calculator, Percent, Check } from 'lucide-react';
import { Modal } from './ui/Modal';

export interface EMICalculatorProps {
  isOpen: boolean;
  onClose: () => void;
  price: number;
}

interface EMIPlan {
  bank: string;
  months: number;
  rate: number; // annual interest %
  isNoCost?: boolean;
}

const EMI_PLANS: EMIPlan[] = [
  { bank: 'HDFC Bank', months: 3, rate: 0, isNoCost: true },
  { bank: 'HDFC Bank', months: 6, rate: 0, isNoCost: true },
  { bank: 'HDFC Bank', months: 9, rate: 14.5 },
  { bank: 'HDFC Bank', months: 12, rate: 15.0 },
  { bank: 'ICICI Bank', months: 3, rate: 0, isNoCost: true },
  { bank: 'ICICI Bank', months: 6, rate: 0, isNoCost: true },
  { bank: 'ICICI Bank', months: 12, rate: 14.0 },
  { bank: 'SBI Card', months: 3, rate: 0, isNoCost: true },
  { bank: 'SBI Card', months: 6, rate: 13.5 },
  { bank: 'SBI Card', months: 12, rate: 14.5 },
];

export const EMICalculator: React.FC<EMICalculatorProps> = ({
  isOpen,
  onClose,
  price,
}) => {
  const [selectedBank, setSelectedBank] = useState<string>('HDFC Bank');

  const banks = Array.from(new Set(EMI_PLANS.map((p) => p.bank)));
  const plansForBank = EMI_PLANS.filter((p) => p.bank === selectedBank);

  // EMI formula: P * r * (1 + r)^n / ((1 + r)^n - 1)
  const calculateMonthlyEMI = (p: number, annualRate: number, months: number): number => {
    if (annualRate === 0) {
      return Math.round(p / months);
    }
    const r = annualRate / 12 / 100;
    const emi = (p * r * Math.pow(1 + r, months)) / (Math.pow(1 + r, months) - 1);
    return Math.round(emi);
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="Easy Monthly Installments (EMI) Plans"
      maxWidth="lg"
    >
      <div className="emi-calculator-body space-y-4">
        <div className="p-3.5 bg-gray-50 border border-gray-200 rounded-lg flex items-center justify-between">
          <div>
            <p className="text-xs text-gray-500">Selected Product Price</p>
            <h3 className="text-xl font-bold text-gray-900">
              ₹{price.toLocaleString('en-IN')}
            </h3>
          </div>
          <span className="text-xs font-semibold px-2.5 py-1 bg-green-100 text-green-800 rounded-full">
            No Cost EMI Available
          </span>
        </div>

        {/* Bank Selector */}
        <div className="flex gap-2 border-b pb-2 overflow-x-auto">
          {banks.map((b) => (
            <button
              key={b}
              type="button"
              className={`px-3 py-1.5 text-xs font-semibold rounded-md transition-colors ${
                selectedBank === b
                  ? 'bg-blue-600 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
              onClick={() => setSelectedBank(b)}
            >
              {b}
            </button>
          ))}
        </div>

        {/* Plan Table */}
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead>
              <tr className="border-b bg-gray-50 text-gray-600">
                <th className="p-2.5">EMI Tenure</th>
                <th className="p-2.5">Interest Rate</th>
                <th className="p-2.5">Monthly EMI</th>
                <th className="p-2.5">Total Cost</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100">
              {plansForBank.map((plan) => {
                const emi = calculateMonthlyEMI(price, plan.rate, plan.months);
                const totalCost = emi * plan.months;

                return (
                  <tr key={`${plan.bank}-${plan.months}`} className="hover:bg-blue-50/50">
                    <td className="p-2.5 font-medium">
                      <span>{plan.months} Months</span>
                      {plan.isNoCost && (
                        <span className="ml-2 px-1.5 py-0.5 bg-green-100 text-green-700 rounded text-[10px] font-bold">
                          No Cost EMI
                        </span>
                      )}
                    </td>
                    <td className="p-2.5 text-gray-500">
                      {plan.rate === 0 ? '0% p.a.' : `${plan.rate}% p.a.`}
                    </td>
                    <td className="p-2.5 font-bold text-gray-900">
                      ₹{emi.toLocaleString('en-IN')}/mo
                    </td>
                    <td className="p-2.5 text-gray-600">
                      ₹{totalCost.toLocaleString('en-IN')}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>

        <p className="text-[11px] text-gray-400">
          *Bank charges and standard processing fees may apply. EMI interest will be billed by the card issuer.
        </p>
      </div>
    </Modal>
  );
};
