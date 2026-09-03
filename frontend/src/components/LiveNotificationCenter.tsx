import React, { useState } from 'react';
import { Bell, Check, Trash2, Package, Tag, ShieldAlert } from 'lucide-react';
import { Notification } from '../types';

export interface LiveNotificationCenterProps {
  notifications?: Notification[];
  onMarkRead?: (id: number) => void;
  onClearAll?: () => void;
}

const DEFAULT_NOTIFICATIONS: any[] = [
  { id: 1, type: 'ORDER', title: 'Order Dispatched!', message: 'Your package #HK-20260825-99A is on the way with EKART Logistics.', created_at: '10 mins ago', is_read: false },
  { id: 2, type: 'PROMOTION', title: 'Lightning Flash Sale Live!', message: 'Up to 60% OFF on Audio & Smartphones for next 2 hours.', created_at: '1 hour ago', is_read: false },
  { id: 3, type: 'SECURITY', title: 'New Login Detected', message: 'Logged in from Chrome on Windows (Bengaluru, India).', created_at: 'Yesterday', is_read: true },
];

export const LiveNotificationCenter: React.FC<LiveNotificationCenterProps> = ({
  notifications = DEFAULT_NOTIFICATIONS,
  onMarkRead,
  onClearAll,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [items, setItems] = useState<any[]>(notifications);

  const unreadCount = items.filter((n) => !n.is_read).length;

  const handleMarkAllRead = () => {
    setItems((prev) => prev.map((n) => ({ ...n, is_read: true })));
  };

  const getIcon = (type: string) => {
    switch (type) {
      case 'ORDER':
        return <Package size={16} className="text-blue-600" />;
      case 'PROMOTION':
        return <Tag size={16} className="text-amber-600" />;
      default:
        return <ShieldAlert size={16} className="text-green-600" />;
    }
  };

  return (
    <div className="relative">
      <button
        type="button"
        className="relative p-2 text-gray-700 hover:text-blue-600 rounded-full hover:bg-gray-100 transition-colors"
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Notifications"
      >
        <Bell size={20} />
        {unreadCount > 0 && (
          <span className="absolute top-1 right-1 w-4 h-4 bg-red-600 text-white rounded-full text-[10px] font-bold flex items-center justify-center animate-pulse">
            {unreadCount}
          </span>
        )}
      </button>

      {isOpen && (
        <>
          <div
            className="fixed inset-0 z-40"
            onClick={() => setIsOpen(false)}
          />
          <div className="absolute right-0 mt-2 w-80 sm:w-96 bg-white border border-gray-200 rounded-xl shadow-xl z-50 overflow-hidden">
            <div className="p-3.5 bg-gray-50 border-b flex items-center justify-between">
              <span className="text-xs font-bold text-gray-900">
                Notifications ({unreadCount} unread)
              </span>
              <button
                type="button"
                className="text-[11px] text-blue-600 hover:underline font-semibold"
                onClick={handleMarkAllRead}
              >
                Mark all read
              </button>
            </div>

            <div className="max-h-80 overflow-y-auto divide-y divide-gray-100">
              {items.map((n) => (
                <div
                  key={n.id}
                  className={`p-3 text-xs flex items-start gap-3 hover:bg-gray-50/80 transition-colors ${
                    !n.is_read ? 'bg-blue-50/30' : ''
                  }`}
                >
                  <div className="mt-0.5">{getIcon(n.type)}</div>
                  <div className="flex-1">
                    <p className="font-bold text-gray-900">{n.title}</p>
                    <p className="text-gray-600 text-[11px] mt-0.5 leading-relaxed">{n.message}</p>
                    <span className="text-[10px] text-gray-400 mt-1 block">{n.created_at}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </>
      )}
    </div>
  );
};
