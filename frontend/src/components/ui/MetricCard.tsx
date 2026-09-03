import React from 'react';
import { ArrowUpRight, ArrowDownRight } from 'lucide-react';

export interface MetricCardProps {
  title: string;
  value: string | number;
  subtitle?: string;
  trendPercentage?: number;
  icon?: React.ReactNode;
  variant?: 'blue' | 'green' | 'purple' | 'amber' | 'neutral';
}

export const MetricCard: React.FC<MetricCardProps> = ({
  title,
  value,
  subtitle,
  trendPercentage,
  icon,
  variant = 'blue',
}) => {
  return (
    <div className={`metric-card metric-card-${variant}`}>
      <div className="metric-card-header">
        <span className="metric-card-title">{title}</span>
        {icon && <div className="metric-card-icon-wrapper">{icon}</div>}
      </div>
      <div className="metric-card-body">
        <h3 className="metric-card-value">{value}</h3>
        {(trendPercentage !== undefined || subtitle) && (
          <div className="metric-card-footer">
            {trendPercentage !== undefined && (
              <span
                className={`metric-trend ${
                  trendPercentage >= 0 ? 'trend-positive' : 'trend-negative'
                }`}
              >
                {trendPercentage >= 0 ? (
                  <ArrowUpRight size={14} />
                ) : (
                  <ArrowDownRight size={14} />
                )}
                <span>{Math.abs(trendPercentage)}%</span>
              </span>
            )}
            {subtitle && <span className="metric-subtitle">{subtitle}</span>}
          </div>
        )}
      </div>
    </div>
  );
};
