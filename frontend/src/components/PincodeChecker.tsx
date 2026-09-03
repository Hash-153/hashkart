import React, { useState } from 'react';
import { MapPin, CheckCircle2, Truck, AlertCircle, ShieldCheck } from 'lucide-react';
import { api } from '../services/api';

export interface PincodeCheckerProps {
  cartTotal?: number;
  onPincodeValidated?: (pincode: string, isServiceable: boolean) => void;
}

export const PincodeChecker: React.FC<PincodeCheckerProps> = ({
  cartTotal,
  onPincodeValidated,
}) => {
  const [pincode, setPincode] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleCheck = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!/^\d{6}$/.test(pincode)) {
      setError('Please enter a valid 6-digit Indian PIN code');
      return;
    }

    setLoading(true);
    setError(null);
    try {
      const data = await api.checkPincodeServiceability(pincode, cartTotal);
      setResult(data);
      if (onPincodeValidated) {
        onPincodeValidated(pincode, data.is_serviceable);
      }
    } catch (err: any) {
      setError(err.message || 'Unable to verify pincode at this time.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="pincode-checker-card">
      <div className="pincode-header">
        <MapPin size={16} className="text-primary" />
        <span className="font-medium text-sm text-gray-700">Delivery & Services</span>
      </div>

      <form onSubmit={handleCheck} className="pincode-input-row">
        <input
          type="text"
          maxLength={6}
          placeholder="Enter Delivery Pincode"
          value={pincode}
          onChange={(e) => {
            setPincode(e.target.value.replace(/\D/g, ''));
            setError(null);
          }}
          className="pincode-field"
        />
        <button
          type="submit"
          disabled={loading || pincode.length !== 6}
          className="pincode-btn"
        >
          {loading ? 'Checking...' : 'Check'}
        </button>
      </form>

      {error && (
        <div className="pincode-error flex items-center gap-1.5 text-xs text-red-600 mt-2">
          <AlertCircle size={14} />
          <span>{error}</span>
        </div>
      )}

      {result && (
        <div className="pincode-result-box">
          <div className="flex items-center gap-2 text-green-700 font-medium text-xs">
            <CheckCircle2 size={16} />
            <span>Delivery available to {result.city}, {result.state}</span>
          </div>

          <div className="pincode-perks-grid">
            <div className="pincode-perk-item">
              <Truck size={14} className="text-blue-600" />
              <div>
                <p className="text-xs font-semibold text-gray-800">
                  Standard Delivery: {result.estimated_delivery_date}
                </p>
                <p className="text-[11px] text-gray-500">
                  {result.shipping_charge === 0 ? 'FREE Delivery' : `₹${result.shipping_charge} Delivery Charge`}
                </p>
              </div>
            </div>

            <div className="pincode-perk-item">
              <ShieldCheck size={14} className="text-green-600" />
              <div>
                <p className="text-xs font-semibold text-gray-800">
                  {result.is_cod_available ? 'Cash on Delivery Available' : 'Prepaid Only'}
                </p>
                <p className="text-[11px] text-gray-500">7 Days Replacement Policy</p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
