import React from 'react';
import { Award, CheckCircle2, AlertTriangle, TrendingUp, Star, ShieldCheck } from 'lucide-react';
import { ProgressBar } from './ui/ProgressBar';

export interface SellerScorecardProps {
  sellerTier: 'GOLD' | 'SILVER' | 'BRONZE';
  performanceScore: number; // 0 to 100
  dispatchSLAMetPercentage: number;
  cancellationRatePercentage: number;
  customerReturnRatePercentage: number;
  averageRating: number;
}

export const SellerPerformanceScorecard: React.FC<SellerScorecardProps> = ({
  sellerTier = 'GOLD',
  performanceScore = 92,
  dispatchSLAMetPercentage = 98.8,
  cancellationRatePercentage = 0.2,
  customerReturnRatePercentage = 1.4,
  averageRating = 4.8,
}) => {
  const tierBadges = {
    GOLD: { label: 'Gold Merchant', color: 'bg-yellow-400 text-amber-950 border-yellow-500', discount: '1.5% Fee Discount' },
    SILVER: { label: 'Silver Merchant', color: 'bg-gray-200 text-gray-800 border-gray-300', discount: '0.75% Fee Discount' },
    BRONZE: { label: 'Bronze Merchant', color: 'bg-amber-700 text-amber-50 border-amber-800', discount: 'Standard Commission' },
  };

  const badge = tierBadges[sellerTier] || tierBadges.GOLD;

  return (
    <div className="seller-scorecard-card p-5 bg-white border border-gray-200 rounded-xl shadow-sm space-y-4">
      <div className="flex items-center justify-between border-b pb-3">
        <div className="flex items-center gap-2">
          <Award size={20} className="text-amber-500" />
          <h3 className="text-sm font-bold text-gray-900">Seller Performance Scorecard</h3>
        </div>
        <span className={`px-2.5 py-0.5 text-xs font-black rounded-full border ${badge.color}`}>
          {badge.label}
        </span>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 items-center">
        <div>
          <span className="text-xs text-gray-500">Quarterly Holistic Score</span>
          <div className="flex items-baseline gap-2 mt-0.5">
            <h4 className="text-2xl font-black text-gray-900">{performanceScore}/100</h4>
            <span className="text-xs text-green-700 font-bold">{badge.discount}</span>
          </div>
          <ProgressBar value={performanceScore} variant="success" height={6} />
        </div>

        <div className="grid grid-cols-2 gap-2 text-xs">
          <div className="p-2 bg-gray-50 rounded border">
            <span className="text-gray-400">Dispatch SLA</span>
            <p className="font-bold text-gray-900">{dispatchSLAMetPercentage}% On-Time</p>
          </div>
          <div className="p-2 bg-gray-50 rounded border">
            <span className="text-gray-400">Cancellation Rate</span>
            <p className="font-bold text-green-700">{cancellationRatePercentage}% (&lt;0.5%)</p>
          </div>
          <div className="p-2 bg-gray-50 rounded border">
            <span className="text-gray-400">Return Defect</span>
            <p className="font-bold text-gray-900">{customerReturnRatePercentage}%</p>
          </div>
          <div className="p-2 bg-gray-50 rounded border">
            <span className="text-gray-400">Avg Rating</span>
            <p className="font-bold text-amber-600 flex items-center gap-0.5">
              <span>{averageRating}</span>
              <Star size={12} className="fill-current" />
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
