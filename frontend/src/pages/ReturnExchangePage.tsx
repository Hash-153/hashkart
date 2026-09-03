import React, { useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { RotateCcw, CheckCircle2, AlertCircle, ArrowLeft, Upload } from 'lucide-react';
import { api } from '../services/api';
import { useToast } from '../components/ui/Toast';

export const ReturnExchangePage: React.FC = () => {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const { showToast } = useToast();

  const orderNumber = searchParams.get('order') || '';
  const [reason, setReason] = useState('DEFECTIVE');
  const [actionType, setActionType] = useState<'RETURN_REFUND' | 'REPLACEMENT'>('RETURN_REFUND');
  const [details, setDetails] = useState('');
  const [pickupPincode, setPickupPincode] = useState('560001');
  const [loading, setLoading] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!details.trim()) {
      showToast('warning', 'Details Required', 'Please describe why you are requesting a return.');
      return;
    }

    setLoading(true);
    try {
      // Simulate API submit return
      await new Promise((resolve) => setTimeout(resolve, 800));
      setIsSubmitted(true);
      showToast('success', 'Return Request Registered', 'Pickup scheduled within 2 business days.');
    } catch (err: any) {
      showToast('error', 'Submission Failed', err.message || 'Failed to submit return request.');
    } finally {
      setLoading(false);
    }
  };

  if (isSubmitted) {
    return (
      <div className="container py-12 max-w-lg mx-auto text-center space-y-4 bg-white border border-gray-200 rounded-xl p-8 shadow-sm">
        <div className="w-16 h-16 rounded-full bg-green-100 text-green-700 flex items-center justify-center mx-auto">
          <CheckCircle2 size={36} />
        </div>
        <h2 className="text-xl font-bold text-gray-900">Return Request Confirmed!</h2>
        <p className="text-xs text-gray-500">
          Your return pickup request for Order #{orderNumber || 'HK-83921'} has been scheduled. Our logistics partner will inspect the item at doorstep pickup.
        </p>
        <div className="pt-4 flex justify-center gap-3">
          <button
            type="button"
            className="btn btn-primary btn-sm"
            onClick={() => navigate('/orders')}
          >
            Go to My Orders
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="container py-6 max-w-2xl mx-auto space-y-6">
      <div className="flex items-center gap-3">
        <button
          type="button"
          onClick={() => navigate(-1)}
          className="p-2 border rounded-lg hover:bg-gray-50"
          aria-label="Back"
        >
          <ArrowLeft size={16} />
        </button>
        <div>
          <h1 className="text-xl font-bold text-gray-900">Request Return or Exchange</h1>
          <p className="text-xs text-gray-500 mt-0.5">Order Ref: #{orderNumber || 'HK-DEMO'}</p>
        </div>
      </div>

      <form onSubmit={handleSubmit} className="bg-white border border-gray-200 rounded-xl p-6 space-y-5 shadow-sm">
        {/* Action Choice */}
        <div>
          <label className="block text-xs font-bold text-gray-800 mb-2">Select Resolution Type</label>
          <div className="grid grid-cols-2 gap-3">
            <button
              type="button"
              className={`p-3 rounded-lg border text-left text-xs font-semibold flex items-center gap-2 ${
                actionType === 'RETURN_REFUND'
                  ? 'border-blue-600 bg-blue-50/50 text-blue-900 ring-2 ring-blue-600/20'
                  : 'border-gray-200 text-gray-700 hover:bg-gray-50'
              }`}
              onClick={() => setActionType('RETURN_REFUND')}
            >
              <RotateCcw size={16} className="text-blue-600" />
              <div>
                <p>Refund to Bank / UPI</p>
                <span className="text-[10px] text-gray-400 font-normal">Direct refund upon pickup</span>
              </div>
            </button>

            <button
              type="button"
              className={`p-3 rounded-lg border text-left text-xs font-semibold flex items-center gap-2 ${
                actionType === 'REPLACEMENT'
                  ? 'border-blue-600 bg-blue-50/50 text-blue-900 ring-2 ring-blue-600/20'
                  : 'border-gray-200 text-gray-700 hover:bg-gray-50'
              }`}
              onClick={() => setActionType('REPLACEMENT')}
            >
              <RotateCcw size={16} className="text-green-600" />
              <div>
                <p>Free Replacement</p>
                <span className="text-[10px] text-gray-400 font-normal">Brand new unit sent</span>
              </div>
            </button>
          </div>
        </div>

        {/* Reason Selector */}
        <div>
          <label className="block text-xs font-bold text-gray-800 mb-1">Reason for Return</label>
          <select
            value={reason}
            onChange={(e) => setReason(e.target.value)}
            className="w-full text-xs p-2.5 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
          >
            <option value="DEFECTIVE">Product is defective or not working</option>
            <option value="DAMAGED">Damaged packaging or physical transit defect</option>
            <option value="WRONG_ITEM">Received completely different product or color</option>
            <option value="MISSING_PARTS">Missing accessories or parts in package</option>
            <option value="PERFORMANCE">Quality not meeting expectations</option>
          </select>
        </div>

        {/* Details Textarea */}
        <div>
          <label className="block text-xs font-bold text-gray-800 mb-1">Additional Comments & Details</label>
          <textarea
            rows={3}
            placeholder="Please specify exact issue details to expedite refund processing..."
            value={details}
            onChange={(e) => setDetails(e.target.value)}
            className="w-full text-xs p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
          />
        </div>

        {/* Pickup Pincode */}
        <div>
          <label className="block text-xs font-bold text-gray-800 mb-1">Pickup PIN Code</label>
          <input
            type="text"
            maxLength={6}
            value={pickupPincode}
            onChange={(e) => setPickupPincode(e.target.value)}
            className="w-full text-xs p-2.5 border border-gray-300 rounded-lg"
          />
        </div>

        <button
          type="submit"
          disabled={loading}
          className="btn btn-primary btn-md w-full font-bold"
        >
          {loading ? 'Submitting Request...' : 'Confirm Return Request'}
        </button>
      </form>
    </div>
  );
};
