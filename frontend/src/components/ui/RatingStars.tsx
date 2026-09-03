import React from 'react';
import { Star, StarHalf } from 'lucide-react';

export interface RatingStarsProps {
  rating: number; // 0.0 to 5.0
  maxRating?: number;
  size?: number;
  showValue?: boolean;
  count?: number;
}

export const RatingStars: React.FC<RatingStarsProps> = ({
  rating,
  maxRating = 5,
  size = 14,
  showValue = false,
  count,
}) => {
  const rounded = Math.round(rating * 2) / 2;

  return (
    <div className="rating-stars-container">
      <div className="rating-stars-badge">
        <span>{rating.toFixed(1)}</span>
        <Star size={size} className="fill-current text-white" />
      </div>
      {count !== undefined && (
        <span className="rating-count-text">
          ({count.toLocaleString('en-IN')})
        </span>
      )}
    </div>
  );
};
