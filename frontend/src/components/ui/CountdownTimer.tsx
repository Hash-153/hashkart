import React, { useState, useEffect } from 'react';
import { Clock } from 'lucide-react';

export interface CountdownTimerProps {
  targetDate?: string | Date;
  secondsRemaining?: number;
  onExpire?: () => void;
  showIcon?: boolean;
}

export const CountdownTimer: React.FC<CountdownTimerProps> = ({
  targetDate,
  secondsRemaining: initialSeconds,
  onExpire,
  showIcon = true,
}) => {
  const [seconds, setSeconds] = useState<number>(() => {
    if (initialSeconds !== undefined) return initialSeconds;
    if (targetDate) {
      const diff = Math.max(0, Math.floor((new Date(targetDate).getTime() - Date.now()) / 1000));
      return diff;
    }
    return 3600;
  });

  useEffect(() => {
    if (seconds <= 0) {
      if (onExpire) onExpire();
      return;
    }

    const timer = setInterval(() => {
      setSeconds((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          if (onExpire) onExpire();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [seconds, onExpire]);

  const hours = Math.floor(seconds / 3600);
  const minutes = Math.floor((seconds % 3600) / 60);
  const secs = seconds % 60;

  const pad = (n: number) => n.toString().padStart(2, '0');

  return (
    <div className="countdown-timer-root">
      {showIcon && <Clock size={16} className="text-amber-500 animate-pulse" />}
      <div className="countdown-blocks">
        <span className="countdown-digit">{pad(hours)}</span>
        <span className="countdown-colon">:</span>
        <span className="countdown-digit">{pad(minutes)}</span>
        <span className="countdown-colon">:</span>
        <span className="countdown-digit">{pad(secs)}</span>
      </div>
      <span className="countdown-label">Left</span>
    </div>
  );
};
