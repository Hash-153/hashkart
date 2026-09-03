import React, { useState, useEffect } from 'react';
import { Coins, Award, Gift, Sparkles, Zap, ArrowRight, ShieldCheck, Gamepad2 } from 'lucide-react';
import { api } from '../services/api';
import { useAuth } from '../context/AuthContext';
import { useToast } from '../components/ui/Toast';
import { Tabs } from '../components/ui/Tabs';

export const SuperCoinZonePage: React.FC = () => {
  const { user } = useAuth();
  const { showToast } = useToast();
  const [profile, setProfile] = useState<any | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        setLoading(true);
        if (user) {
          const data = await api.getLoyaltyProfile();
          setProfile(data);
        } else {
          setProfile({
            supercoin_balance: 50,
            tier: 'BRONZE',
            lifetime_coins_earned: 50,
            is_flipkart_plus_member: false,
            recent_transactions: [],
          });
        }
      } catch (err) {
        console.error('Failed to load SuperCoin profile:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchProfile();
  }, [user]);

  const handleClaimReward = (rewardName: string, coinCost: number) => {
    if (!user) {
      showToast('warning', 'Sign in required', 'Please log in to claim SuperCoin rewards.');
      return;
    }
    if ((profile?.supercoin_balance || 0) < coinCost) {
      showToast('error', 'Insufficient Coins', `You need ${coinCost} SuperCoins to redeem this voucher.`);
      return;
    }
    showToast('success', 'Reward Claimed!', `You successfully redeemed ${rewardName}. Voucher code sent to your email.`);
  };

  const rewardsTab = (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mt-4">
      {[
        { title: '₹100 NovaMart Gift Voucher', coins: 100, partner: 'NovaMart Shopping', code: 'NM-VOUCH-100' },
        { title: '3 Months SonyLIV Premium', coins: 150, partner: 'Entertainment', code: 'SONY-3M-PASS' },
        { title: 'Flat ₹500 Off Flight Tickets', coins: 200, partner: 'Travel & Flights', code: 'FLIGHT-500' },
        { title: '1 Year Gaana Plus Subscription', coins: 80, partner: 'Music Streaming', code: 'GAANA-YEAR' },
        { title: '20% Off Swiggy Gourmet', coins: 50, partner: 'Food & Dining', code: 'SWIGGY-20' },
        { title: '₹250 Cleartrip Hotel Coupon', coins: 120, partner: 'Hotels', code: 'HOTEL-250' },
      ].map((r, i) => (
        <div key={i} className="p-4 bg-white border border-gray-200 rounded-xl hover:shadow-md transition-all flex flex-col justify-between">
          <div>
            <span className="text-[10px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded-full uppercase tracking-wider">
              {r.partner}
            </span>
            <h4 className="text-sm font-bold text-gray-900 mt-2">{r.title}</h4>
          </div>
          <div className="mt-4 pt-3 border-t flex items-center justify-between">
            <span className="flex items-center gap-1 font-bold text-sm text-amber-600">
              <Coins size={16} />
              <span>{r.coins} Coins</span>
            </span>
            <button
              type="button"
              className="btn btn-primary btn-sm"
              onClick={() => handleClaimReward(r.title, r.coins)}
            >
              Claim
            </button>
          </div>
        </div>
      ))}
    </div>
  );

  const historyTab = (
    <div className="bg-white border border-gray-200 rounded-xl overflow-hidden mt-4">
      <div className="p-4 border-b">
        <h4 className="text-sm font-bold text-gray-900">Coin Activity History</h4>
      </div>
      <div className="divide-y divide-gray-100">
        {(profile?.recent_transactions || []).length > 0 ? (
          profile.recent_transactions.map((t: any) => (
            <div key={t.id} className="p-3.5 flex items-center justify-between text-xs">
              <div>
                <p className="font-semibold text-gray-900">{t.description}</p>
                <p className="text-gray-400 text-[11px] mt-0.5">
                  {new Date(t.created_at).toLocaleDateString('en-IN', { dateStyle: 'medium' })}
                </p>
              </div>
              <span className={`font-bold ${t.coins >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                {t.coins >= 0 ? `+${t.coins}` : t.coins} Coins
              </span>
            </div>
          ))
        ) : (
          <div className="p-6 text-center text-xs text-gray-400">
            No coin transactions recorded yet. Shop to earn!
          </div>
        )}
      </div>
    </div>
  );

  return (
    <div className="supercoin-zone-page container py-6 space-y-6">
      {/* Hero Banner */}
      <div className="supercoin-hero-banner bg-gradient-to-r from-amber-500 via-amber-600 to-yellow-600 text-white rounded-2xl p-6 sm:p-8 shadow-lg relative overflow-hidden">
        <div className="relative z-10 max-w-xl">
          <div className="flex items-center gap-2 mb-2">
            <Sparkles size={20} className="text-yellow-200" />
            <span className="font-semibold text-xs tracking-wider uppercase text-yellow-100">
              Flipkart-Grade Loyalty Hub
            </span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold">NovaMart SuperCoin Zone</h1>
          <p className="text-xs sm:text-sm text-yellow-50 mt-2">
            Earn SuperCoins on every purchase. Use 1 Coin = ₹1 at checkout or redeem exclusive brand rewards!
          </p>

          <div className="mt-6 flex flex-wrap items-center gap-4 bg-white/10 backdrop-blur-md p-4 rounded-xl border border-white/20">
            <div className="flex items-center gap-3">
              <div className="w-12 h-12 rounded-full bg-yellow-400 text-amber-900 flex items-center justify-center font-bold text-xl shadow-inner">
                <Coins size={28} />
              </div>
              <div>
                <span className="text-xs text-yellow-100">Your Coin Balance</span>
                <h3 className="text-2xl font-black">{profile?.supercoin_balance || 0} SuperCoins</h3>
              </div>
            </div>

            <div className="sm:ml-auto flex items-center gap-2">
              <span className="text-xs px-3 py-1 bg-yellow-300 text-amber-950 font-bold rounded-full uppercase tracking-wide">
                Tier: {profile?.tier || 'BRONZE'}
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Perks Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div className="p-4 bg-white border border-gray-200 rounded-xl flex items-start gap-3">
          <Zap size={24} className="text-amber-500 mt-1" />
          <div>
            <h4 className="text-sm font-bold text-gray-900">Earn 4 Coins / ₹100</h4>
            <p className="text-xs text-gray-500 mt-0.5">Plus members earn double reward points on every order.</p>
          </div>
        </div>
        <div className="p-4 bg-white border border-gray-200 rounded-xl flex items-start gap-3">
          <ShieldCheck size={24} className="text-green-600 mt-1" />
          <div>
            <h4 className="text-sm font-bold text-gray-900">100% Usable at Checkout</h4>
            <p className="text-xs text-gray-500 mt-0.5">Redeem coins directly for instant rupee discounts.</p>
          </div>
        </div>
        <div className="p-4 bg-white border border-gray-200 rounded-xl flex items-start gap-3">
          <Gamepad2 size={24} className="text-purple-600 mt-1" />
          <div>
            <h4 className="text-sm font-bold text-gray-900">Reward Store</h4>
            <p className="text-xs text-gray-500 mt-0.5">Access OTT passes, travel vouchers, and dining deals.</p>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <Tabs
        tabs={[
          { id: 'rewards', label: 'Reward Catalog', icon: <Gift size={16} />, content: rewardsTab },
          { id: 'history', label: 'Coin Passbook', icon: <Coins size={16} />, content: historyTab },
        ]}
      />
    </div>
  );
};
