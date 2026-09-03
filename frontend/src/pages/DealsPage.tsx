import React, { useState, useEffect } from 'react';
import { Link } from 'lucide-react';
import { Zap, Flame, Clock, Tag, ArrowRight, ShieldCheck } from 'lucide-react';
import { api } from '../services/api';
import { CountdownTimer } from '../components/ui/CountdownTimer';
import { ProgressBar } from '../components/ui/ProgressBar';
import { useCart } from '../context/CartContext';
import { useToast } from '../components/ui/Toast';

export const DealsPage: React.FC = () => {
  const { addToCart } = useCart();
  const { showToast } = useToast();
  const [events, setEvents] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDeals = async () => {
      try {
        setLoading(true);
        const data = await api.getActiveFlashSales();
        setEvents(data);
      } catch (err) {
        console.error('Failed to load flash deals:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchDeals();
  }, []);

  const handleClaimDeal = async (event: any, item: any) => {
    try {
      await api.reserveFlashDeal(event.id, item.product_id, 1);
      const variantId = item.variant_id || item.product_id;
      await addToCart(variantId, 1);
      showToast('success', 'Deal Claimed!', `${item.product_name} reserved at ₹${item.flash_price} and added to cart.`);
    } catch (err: any) {
      showToast('error', 'Unable to claim deal', err.message || 'Deal is sold out or unavailable.');
    }
  };

  return (
    <div className="deals-page container py-6 space-y-6">
      {/* Header Banner */}
      <div className="bg-gradient-to-r from-red-600 via-rose-600 to-orange-500 text-white rounded-2xl p-6 sm:p-8 shadow-lg flex flex-col md:flex-row items-center justify-between gap-6">
        <div className="space-y-2">
          <div className="flex items-center gap-2">
            <Flame size={24} className="text-yellow-300 animate-bounce" />
            <span className="font-bold text-xs uppercase tracking-widest text-yellow-200">
              Flipkart Super Deals & Flash Sales
            </span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-black">Crazy Lightning Deals</h1>
          <p className="text-xs sm:text-sm text-rose-100 max-w-md">
            Unbeatable prices refreshed hourly. Stock is strictly limited. Grab your deals before the timer strikes zero!
          </p>
        </div>

        <div className="bg-black/30 backdrop-blur-md p-4 rounded-xl border border-white/20 text-center">
          <p className="text-xs font-semibold text-yellow-200 uppercase tracking-wide mb-1">
            Sale Closes In
          </p>
          <CountdownTimer secondsRemaining={7200} />
        </div>
      </div>

      {/* Events List */}
      {loading ? (
        <div className="py-12 text-center text-xs text-gray-500">Loading flash sales...</div>
      ) : events.length === 0 ? (
        <div className="py-12 text-center text-xs text-gray-400 bg-white rounded-xl border p-8">
          <Clock size={32} className="mx-auto mb-2 text-gray-300" />
          <p className="font-semibold text-gray-700">Next Flash Sale starts at 12:00 PM</p>
          <p className="text-[11px] text-gray-400 mt-1">Check back soon for new lightning deals.</p>
        </div>
      ) : (
        events.map((event) => (
          <div key={event.id} className="space-y-4">
            <div className="flex items-center justify-between border-b pb-2">
              <div className="flex items-center gap-2">
                <Zap size={20} className="text-red-600" />
                <h3 className="text-lg font-bold text-gray-900">{event.title}</h3>
              </div>
              <CountdownTimer secondsRemaining={event.seconds_remaining} />
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
              {event.items?.map((item: any) => (
                <div
                  key={item.id}
                  className="bg-white border border-gray-200 rounded-xl p-4 hover:shadow-md transition-all flex flex-col justify-between"
                >
                  <div className="space-y-3">
                    <div className="relative aspect-square bg-gray-50 rounded-lg p-3 flex items-center justify-center overflow-hidden">
                      <img
                        src={item.product_image || 'https://via.placeholder.com/200'}
                        alt={item.product_name}
                        className="max-h-full max-w-full object-contain"
                      />
                      <span className="absolute top-2 left-2 px-2 py-0.5 bg-red-600 text-white font-extrabold text-[11px] rounded">
                        {item.discount_percentage}% OFF
                      </span>
                    </div>

                    <div>
                      <h4 className="text-xs font-bold text-gray-900 line-clamp-2">
                        {item.product_name}
                      </h4>
                      <div className="flex items-baseline gap-2 mt-1">
                        <span className="text-base font-black text-gray-900">
                          ₹{item.flash_price.toLocaleString('en-IN')}
                        </span>
                        <span className="text-xs text-gray-400 line-through">
                          ₹{item.regular_price.toLocaleString('en-IN')}
                        </span>
                      </div>
                    </div>

                    <ProgressBar
                      value={item.claimed_percentage}
                      label="Claimed"
                      variant={item.claimed_percentage > 80 ? 'danger' : 'amber'}
                      height={6}
                    />
                  </div>

                  <div className="mt-4 pt-3 border-t">
                    <button
                      type="button"
                      disabled={item.claimed_percentage >= 100}
                      onClick={() => handleClaimDeal(event, item)}
                      className="btn btn-primary btn-sm w-full font-bold"
                    >
                      {item.claimed_percentage >= 100 ? 'Sold Out' : 'Grab Deal'}
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))
      )}
    </div>
  );
};
