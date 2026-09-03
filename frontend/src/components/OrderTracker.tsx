import React from 'react';
import { CheckCircle2, Circle, Truck, Package, Home, Clock } from 'lucide-react';

export interface TimelineEvent {
  status: string;
  label: string;
  description?: string;
  timestamp?: string;
  isCompleted: boolean;
  isCurrent?: boolean;
}

export interface OrderTrackerProps {
  currentStatus: string;
  orderNumber: string;
  estimatedDelivery?: string;
  trackingNumber?: string;
  carrierName?: string;
}

const ORDER_STAGES = [
  { key: 'CONFIRMED', label: 'Order Confirmed', icon: CheckCircle2 },
  { key: 'PACKED', label: 'Packed in Hub', icon: Package },
  { key: 'SHIPPED', label: 'Dispatched & In Transit', icon: Truck },
  { key: 'OUT_FOR_DELIVERY', label: 'Out for Delivery', icon: Clock },
  { key: 'DELIVERED', label: 'Delivered', icon: Home },
];

export const OrderTracker: React.FC<OrderTrackerProps> = ({
  currentStatus,
  orderNumber,
  estimatedDelivery,
  trackingNumber,
  carrierName,
}) => {
  const statusMap: Record<string, number> = {
    PENDING: 0,
    CONFIRMED: 1,
    PROCESSING: 1,
    PACKED: 2,
    SHIPPED: 3,
    IN_TRANSIT: 3,
    OUT_FOR_DELIVERY: 4,
    DELIVERED: 5,
  };

  const currentLevel = statusMap[currentStatus.toUpperCase()] || 1;

  return (
    <div className="order-tracker-card p-5 bg-white border border-gray-200 rounded-xl">
      <div className="flex flex-wrap items-center justify-between gap-3 border-b pb-4 mb-6">
        <div>
          <span className="text-xs text-gray-500 font-medium">Order Reference</span>
          <h4 className="text-base font-bold text-gray-900">#{orderNumber}</h4>
        </div>
        {estimatedDelivery && (
          <div className="text-right">
            <span className="text-xs text-gray-500 font-medium">Estimated Delivery</span>
            <p className="text-sm font-semibold text-green-700">{estimatedDelivery}</p>
          </div>
        )}
      </div>

      {/* Stepper Timeline */}
      <div className="order-stepper-container relative">
        <div className="order-stepper-line" />
        <div className="order-stepper-grid grid grid-cols-5 gap-2 relative z-10">
          {ORDER_STAGES.map((stage, idx) => {
            const stepNumber = idx + 1;
            const isCompleted = stepNumber <= currentLevel;
            const isCurrent = stepNumber === currentLevel;
            const Icon = stage.icon;

            return (
              <div key={stage.key} className="flex flex-col items-center text-center">
                <div
                  className={`w-10 h-10 rounded-full flex items-center justify-center transition-all ${
                    isCompleted
                      ? 'bg-green-600 text-white shadow-md'
                      : 'bg-gray-100 text-gray-400 border-2 border-gray-200'
                  } ${isCurrent ? 'ring-4 ring-green-100 scale-110' : ''}`}
                >
                  <Icon size={18} />
                </div>
                <p
                  className={`text-xs mt-2 font-medium ${
                    isCompleted ? 'text-gray-900 font-semibold' : 'text-gray-400'
                  }`}
                >
                  {stage.label}
                </p>
              </div>
            );
          })}
        </div>
      </div>

      {trackingNumber && (
        <div className="mt-6 pt-4 border-t flex items-center justify-between text-xs text-gray-600">
          <span>Carrier: <strong className="text-gray-900">{carrierName || 'NovaExpress Logistics'}</strong></span>
          <span>AWB / Tracking: <strong className="font-mono text-blue-600">{trackingNumber}</strong></span>
        </div>
      )}
    </div>
  );
};
