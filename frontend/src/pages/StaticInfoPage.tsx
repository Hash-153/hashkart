import React from 'react';
import { useParams, Link } from 'react-router-dom';
import {
  Building2,
  Phone,
  Mail,
  MapPin,
  ShieldCheck,
  Truck,
  RotateCcw,
  CreditCard,
  FileText,
  HelpCircle,
  Briefcase,
  Gift,
  Megaphone,
  CheckCircle2,
  AlertCircle,
  Sparkles,
  Award,
  Globe,
  ChevronRight,
} from 'lucide-react';

interface InfoSection {
  title: string;
  badge?: string;
  category: string;
  icon: React.ReactNode;
  content: React.ReactNode;
}

export const StaticInfoPage: React.FC = () => {
  const { pageKey = 'about-us' } = useParams<{ pageKey: string }>();

  const infoData: Record<string, InfoSection> = {
    // 1. ABOUT
    'contact-us': {
      title: 'Contact Customer Support',
      badge: '24x7 Helpdesk',
      category: 'About',
      icon: <Phone size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-600 leading-relaxed">
            Need assistance with an order, account, or delivery? Our dedicated 24x7 customer support team is available across voice, email, and live chat.
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 my-6">
            <div className="p-4 bg-blue-50/50 border border-blue-100 rounded-lg">
              <div className="flex items-center gap-3 mb-2">
                <Phone size={20} className="text-blue-600" />
                <h4 className="font-bold text-gray-900">Toll-Free Customer Care</h4>
              </div>
              <p className="text-lg font-bold text-blue-700">1800 208 9898</p>
              <p className="text-xs text-gray-500 mt-1">Available 24 hours a day, 7 days a week.</p>
            </div>

            <div className="p-4 bg-green-50/50 border border-green-100 rounded-lg">
              <div className="flex items-center gap-3 mb-2">
                <Mail size={20} className="text-green-600" />
                <h4 className="font-bold text-gray-900">Email Support</h4>
              </div>
              <p className="text-sm font-bold text-green-800">support@hashkart.demo</p>
              <p className="text-xs text-gray-500 mt-1">Average response time: within 2 business hours.</p>
            </div>
          </div>

          <div className="border-t pt-6">
            <h4 className="font-bold text-gray-900 mb-3">Escalation Matrix</h4>
            <div className="bg-gray-50 p-4 rounded-lg border text-xs text-gray-600 space-y-2">
              <p><strong>Level 1:</strong> 24/7 Frontline Customer Support via in-app Help Center & Chat.</p>
              <p><strong>Level 2:</strong> Senior Support Supervisor & Logistics Resolution Desk (response within 24 hours).</p>
              <p><strong>Level 3:</strong> Principal Grievance Redressal Officer (email: grievance@hashkart.demo).</p>
            </div>
          </div>
        </div>
      ),
    },

    'about-us': {
      title: 'About HashKart',
      badge: 'India’s Next-Gen Marketplace',
      category: 'About',
      icon: <Building2 size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            Founded with the mission to democratize digital commerce across India, <strong>HashKart</strong> connects hundreds of millions of consumers with verified direct-to-consumer (D2C) brands, certified manufacturers, and local artisans.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 my-6">
            <div className="p-4 bg-gray-50 border rounded-lg text-center">
              <h3 className="text-2xl font-black text-blue-600">20,000+</h3>
              <p className="text-xs text-gray-500 mt-1">Pincodes Covered Across India</p>
            </div>
            <div className="p-4 bg-gray-50 border rounded-lg text-center">
              <h3 className="text-2xl font-black text-green-600">100%</h3>
              <p className="text-xs text-gray-500 mt-1">Original & Genuine Certified Products</p>
            </div>
            <div className="p-4 bg-gray-50 border rounded-lg text-center">
              <h3 className="text-2xl font-black text-purple-600">50,000+</h3>
              <p className="text-xs text-gray-500 mt-1">Active Verified Indian Sellers</p>
            </div>
          </div>

          <div className="space-y-3">
            <h4 className="font-bold text-gray-900">Our Core Pillars</h4>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-sm">
              <div className="p-3 border rounded flex items-start gap-2">
                <CheckCircle2 size={16} className="text-blue-600 mt-0.5 shrink-0" />
                <span><strong>Customer First:</strong> Zero-hassle 7-day doorstep replacement and instant refunds.</span>
              </div>
              <div className="p-3 border rounded flex items-start gap-2">
                <CheckCircle2 size={16} className="text-blue-600 mt-0.5 shrink-0" />
                <span><strong>Technological Innovation:</strong> Sub-second search indexing and AI-powered recommendations.</span>
              </div>
              <div className="p-3 border rounded flex items-start gap-2">
                <CheckCircle2 size={16} className="text-blue-600 mt-0.5 shrink-0" />
                <span><strong>Fair Ecosystem:</strong> Empowering sellers with transparent 0% platform hidden fees.</span>
              </div>
              <div className="p-3 border rounded flex items-start gap-2">
                <CheckCircle2 size={16} className="text-blue-600 mt-0.5 shrink-0" />
                <span><strong>Sustainable Future:</strong> 100% recyclable paper packaging and EV delivery fleets.</span>
              </div>
            </div>
          </div>
        </div>
      ),
    },

    careers: {
      title: 'Careers at HashKart',
      badge: 'Join the Builders',
      category: 'About',
      icon: <Briefcase size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            At HashKart, we are engineering distributed systems that process tens of thousands of concurrent checkouts per second, building resilient supply chains, and transforming how Bharat shops online.
          </p>

          <div className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white p-6 rounded-lg">
            <h4 className="text-lg font-bold">Why Build with Us?</h4>
            <p className="text-xs text-blue-100 mt-1">Impact at nationwide scale with world-class engineering teams.</p>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-4 text-center">
              <div className="bg-white/10 p-2.5 rounded">
                <p className="text-xs font-semibold">Competitive ESOPs</p>
              </div>
              <div className="bg-white/10 p-2.5 rounded">
                <p className="text-xs font-semibold">Health & Wellness</p>
              </div>
              <div className="bg-white/10 p-2.5 rounded">
                <p className="text-xs font-semibold">Learning Stipends</p>
              </div>
              <div className="bg-white/10 p-2.5 rounded">
                <p className="text-xs font-semibold">Hybrid Flexibility</p>
              </div>
            </div>
          </div>

          <div className="space-y-3">
            <h4 className="font-bold text-gray-900">Featured Openings</h4>
            <div className="divide-y border rounded-lg">
              <div className="p-4 flex justify-between items-center hover:bg-gray-50">
                <div>
                  <h5 className="font-bold text-gray-900 text-sm">Staff Backend Engineer - Distributed Systems</h5>
                  <p className="text-xs text-gray-500 mt-0.5">Bengaluru, India • Engineering (FastAPI, Redis, Kafka, Distributed SQL)</p>
                </div>
                <button className="px-3 py-1.5 bg-blue-600 text-white text-xs font-semibold rounded hover:bg-blue-700">Apply Now</button>
              </div>
              <div className="p-4 flex justify-between items-center hover:bg-gray-50">
                <div>
                  <h5 className="font-bold text-gray-900 text-sm">Senior Frontend Engineer - React & Web Performance</h5>
                  <p className="text-xs text-gray-500 mt-0.5">Bengaluru, India • Engineering (React 18, TypeScript, Core Web Vitals)</p>
                </div>
                <button className="px-3 py-1.5 bg-blue-600 text-white text-xs font-semibold rounded hover:bg-blue-700">Apply Now</button>
              </div>
              <div className="p-4 flex justify-between items-center hover:bg-gray-50">
                <div>
                  <h5 className="font-bold text-gray-900 text-sm">Product Manager - Checkout & Fraud Prevention Sentinel</h5>
                  <p className="text-xs text-gray-500 mt-0.5">Bengaluru, India • Product Management (Payments, Risk & ML)</p>
                </div>
                <button className="px-3 py-1.5 bg-blue-600 text-white text-xs font-semibold rounded hover:bg-blue-700">Apply Now</button>
              </div>
            </div>
          </div>
        </div>
      ),
    },

    stories: {
      title: 'HashKart Stories & Innovation Tech Blog',
      badge: 'Merchant & Tech Spotlights',
      category: 'About',
      icon: <Sparkles size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            Discover real stories of local artisans who scaled their businesses 10x, and read deep-dive architectural engineering logs from the HashKart core technology team.
          </p>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="border rounded-lg p-4 bg-white hover:shadow-md transition-shadow">
              <span className="text-[10px] font-bold text-blue-600 uppercase tracking-wider bg-blue-50 px-2 py-0.5 rounded">Engineering Blog</span>
              <h4 className="font-bold text-gray-900 mt-2 text-sm">How HashKart Handles 100,000 Concurrent Flash Sale Checkouts with Zero Dropped Orders</h4>
              <p className="text-xs text-gray-500 mt-1">A deep dive into distributed lock managers, Redis inventory atomicity, and idempotent payment webhooks.</p>
            </div>

            <div className="border rounded-lg p-4 bg-white hover:shadow-md transition-shadow">
              <span className="text-[10px] font-bold text-purple-600 uppercase tracking-wider bg-purple-50 px-2 py-0.5 rounded">Seller Spotlight</span>
              <h4 className="font-bold text-gray-900 mt-2 text-sm">From a Small Handloom Unit in Varanasi to ₹5 Crores Annual Turnover on HashKart</h4>
              <p className="text-xs text-gray-500 mt-1">How Royal Weave connected authentic Banarasi silk weaves directly to customers across 28 states.</p>
            </div>
          </div>
        </div>
      ),
    },

    press: {
      title: 'Press & Media Relations',
      badge: 'Company News',
      category: 'About',
      icon: <Megaphone size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            Official press announcements, brand assets, executive bios, and media queries for journalists covering HashKart.
          </p>
          <div className="bg-gray-50 p-4 border rounded-lg">
            <h4 className="font-bold text-gray-900 text-sm">Media Inquiries</h4>
            <p className="text-xs text-gray-600 mt-1">For interview requests, press inquiries, or media statements, please contact:</p>
            <p className="text-sm font-semibold text-blue-600 mt-2">press@hashkart.demo</p>
          </div>
        </div>
      ),
    },

    'corporate-information': {
      title: 'Corporate Governance & Legal Entity Information',
      badge: 'Corporate Disclosure',
      category: 'About',
      icon: <FileText size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4 text-sm text-gray-700">
          <p><strong>Legal Corporate Name:</strong> HashKart Internet Private Limited</p>
          <p><strong>Corporate Identity Number (CIN):</strong> U51109KA2024PTC066107</p>
          <p><strong>Date of Incorporation:</strong> 15th January 2024</p>
          <p><strong>Registered Address:</strong> Buildings Alyssa, Begonia & Clove Embassy Tech Village, Outer Ring Road, Devarabeesanahalli Village, Bengaluru, 560103, Karnataka, India.</p>
          <p><strong>GST Identification Number (GSTIN):</strong> 29AAACH1234F1Z5</p>
          <p><strong>Principal Business:</strong> Multi-category B2C & B2B E-Commerce Marketplace Operations and Logistics Technology.</p>
        </div>
      ),
    },

    // 2. GROUP COMPANIES
    hashpay: {
      title: 'HashPay Digital Payments & Credit Suite',
      badge: 'Fintech Ecosystem',
      category: 'Group Companies',
      icon: <CreditCard size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            <strong>HashPay</strong> powers lightning-fast 1-click checkouts, instant UPI payments, interest-free Pay Later credit lines, and sub-second automated refund settlements for all HashKart customers.
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div className="p-3 border rounded-lg bg-blue-50/50">
              <h4 className="font-bold text-gray-900 text-sm">HashPay UPI</h4>
              <p className="text-xs text-gray-600 mt-1">Direct bank-to-bank instant UPI transfer with 99.99% success rate.</p>
            </div>
            <div className="p-3 border rounded-lg bg-purple-50/50">
              <h4 className="font-bold text-gray-900 text-sm">HashPay Later</h4>
              <p className="text-xs text-gray-600 mt-1">Up to ₹50,000 instant revolving credit with 0% interest for 30 days.</p>
            </div>
            <div className="p-3 border rounded-lg bg-green-50/50">
              <h4 className="font-bold text-gray-900 text-sm">Instant Refunds</h4>
              <p className="text-xs text-gray-600 mt-1">Refunds credited to your bank account within 60 seconds of return pickup.</p>
            </div>
          </div>
        </div>
      ),
    },

    hashlogistics: {
      title: 'HashLogistics Supply Chain & Fulfillment Network',
      badge: 'Nationwide Delivery',
      category: 'Group Companies',
      icon: <Truck size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            Our end-to-end automated supply chain infrastructure features 45+ mega fulfillment centers, 1,200+ last-mile delivery hubs, and temperature-controlled transport across all 28 states and 8 union territories.
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div className="p-4 border rounded-lg bg-gray-50">
              <h4 className="font-bold text-gray-900 text-sm">Same-Day & Next-Day Delivery</h4>
              <p className="text-xs text-gray-600 mt-1">Available in over 150 top metro and Tier-1 cities across India.</p>
            </div>
            <div className="p-4 border rounded-lg bg-gray-50">
              <h4 className="font-bold text-gray-900 text-sm">Live GPS Delivery Tracking</h4>
              <p className="text-xs text-gray-600 mt-1">Real-time driver location and delivery OTP verification for secure handoffs.</p>
            </div>
          </div>
        </div>
      ),
    },

    hashstudio: {
      title: 'HashStudio Creator & Live Commerce Hub',
      badge: 'Creator Commerce',
      category: 'Group Companies',
      icon: <Sparkles size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4">
          <p className="text-gray-700 leading-relaxed">
            <strong>HashStudio</strong> enables digital creators, fashion stylists, and tech reviewers to host interactive live-stream shopping sessions, curate product collections, and earn verified affiliate commissions on HashKart.
          </p>
          <div className="bg-purple-50 p-4 rounded-lg border border-purple-100">
            <h4 className="font-bold text-purple-900 text-sm">Are you a Content Creator?</h4>
            <p className="text-xs text-purple-700 mt-1">Join over 10,000+ creators and start sharing your favorite product edits with your community.</p>
            <button className="mt-3 px-4 py-2 bg-purple-600 text-white text-xs font-bold rounded hover:bg-purple-700">Join HashStudio Creators</button>
          </div>
        </div>
      ),
    },

    cleartrip: {
      title: 'Cleartrip Travel & Bookings by HashKart',
      badge: 'Travel Services',
      category: 'Group Companies',
      icon: <Globe size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4">
          <p className="text-gray-700 leading-relaxed">
            Book domestic and international flights, luxury hotels, and holiday packages with zero cancellation fees on Cleartrip, seamlessly connected with your HashKart SuperCoins account.
          </p>
          <p className="text-xs text-gray-500">Redeem up to 100% of your flight fares using HashKart SuperCoins.</p>
        </div>
      ),
    },

    shopsy: {
      title: 'Shopsy by HashKart',
      badge: 'Hyper-Value Shopping',
      category: 'Group Companies',
      icon: <Gift size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4">
          <p className="text-gray-700 leading-relaxed">
            Shopsy is India’s favorite hyper-value e-commerce platform offering millions of fashion, beauty, and home essentials starting at just ₹99 with zero commission for micro-sellers and homemaker entrepreneurs.
          </p>
        </div>
      ),
    },

    // 3. HELP
    payments: {
      title: 'Payment Methods, EMI & Security',
      badge: '100% Safe Payments',
      category: 'Help',
      icon: <CreditCard size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            HashKart supports all major payment modes with 256-bit bank-grade TLS encryption and PCI-DSS Level 1 compliance.
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <div className="p-3 border rounded bg-gray-50">
              <h5 className="font-bold text-gray-900 text-xs">UPI & QR Codes</h5>
              <p className="text-xs text-gray-600 mt-0.5">Google Pay, PhonePe, Paytm, BHIM & all UPI bank apps.</p>
            </div>
            <div className="p-3 border rounded bg-gray-50">
              <h5 className="font-bold text-gray-900 text-xs">Credit & Debit Cards</h5>
              <p className="text-xs text-gray-600 mt-0.5">Visa, MasterCard, RuPay, Diners Club & American Express.</p>
            </div>
            <div className="p-3 border rounded bg-gray-50">
              <h5 className="font-bold text-gray-900 text-xs">No-Cost & Low-Cost EMI</h5>
              <p className="text-xs text-gray-600 mt-0.5">Available on HDFC, ICICI, SBI, Axis & Bajaj Finserv cards.</p>
            </div>
            <div className="p-3 border rounded bg-gray-50">
              <h5 className="font-bold text-gray-900 text-xs">Cash on Delivery (COD)</h5>
              <p className="text-xs text-gray-600 mt-0.5">Pay with cash or UPI QR scan at your doorstep on delivery.</p>
            </div>
          </div>
        </div>
      ),
    },

    shipping: {
      title: 'Shipping, Delivery Timelines & Tracking',
      badge: 'Fast Delivery',
      category: 'Help',
      icon: <Truck size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4">
          <p className="text-gray-700 leading-relaxed">
            We deliver to over 20,000 pincodes across India. Standard orders are delivered in 2 to 4 business days, while Express orders arrive within 24 hours.
          </p>
          <div className="p-4 bg-blue-50 border border-blue-100 rounded-lg">
            <h4 className="font-bold text-blue-900 text-sm">Free Delivery on Orders Above ₹499</h4>
            <p className="text-xs text-blue-700 mt-1">Orders below ₹499 carry a nominal shipping charge of ₹40 per seller.</p>
          </div>
        </div>
      ),
    },

    'cancellation-returns': {
      title: 'Cancellation & Return Policy',
      badge: 'Hassle-Free Returns',
      category: 'Help',
      icon: <RotateCcw size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4">
          <p className="text-gray-700 leading-relaxed">
            We offer a comprehensive <strong>7-Day Replacement or Return Guarantee</strong> on all eligible items. If your product is damaged, defective, or different from described, you can initiate a return directly from your <Link to="/orders" className="text-blue-600 underline font-semibold">Orders Dashboard</Link>.
          </p>
          <div className="space-y-2 text-xs text-gray-600 border-t pt-4">
            <p>• <strong>Free Doorstep Pickup:</strong> Our logistics partner will pick up the product from your address at no cost.</p>
            <p>• <strong>Instant Refund:</strong> Refunds are processed immediately upon courier quality check.</p>
            <p>• <strong>Original Packaging:</strong> Please ensure all tags, invoices, and product accessories are preserved.</p>
          </div>
        </div>
      ),
    },

    faq: {
      title: 'Frequently Asked Questions (FAQ)',
      badge: 'Help & Knowledgebase',
      category: 'Help',
      icon: <HelpCircle size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4">
          <div className="border rounded-lg p-4 bg-white">
            <h4 className="font-bold text-gray-900 text-sm">How do I track my active order?</h4>
            <p className="text-xs text-gray-600 mt-1">Navigate to your <Link to="/orders" className="text-blue-600 underline">Order History</Link> page, click on any order, and view the real-time fulfillment and courier tracking status.</p>
          </div>
          <div className="border rounded-lg p-4 bg-white">
            <h4 className="font-bold text-gray-900 text-sm">What is the delivery charge?</h4>
            <p className="text-xs text-gray-600 mt-1">Delivery is completely FREE on all orders of ₹499 and above. For orders under ₹499, a flat delivery fee of ₹40 applies.</p>
          </div>
          <div className="border rounded-lg p-4 bg-white">
            <h4 className="font-bold text-gray-900 text-sm">How do SuperCoins work?</h4>
            <p className="text-xs text-gray-600 mt-1">You earn 2 SuperCoins for every ₹100 spent on HashKart. SuperCoins can be used for extra discounts on future purchases or partner vouchers in the <Link to="/supercoins" className="text-blue-600 underline">SuperCoin Zone</Link>.</p>
          </div>
        </div>
      ),
    },

    'report-infringement': {
      title: 'Intellectual Property & Brand Protection',
      badge: 'IP Sentinel',
      category: 'Help',
      icon: <ShieldCheck size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4">
          <p className="text-gray-700 leading-relaxed">
            HashKart respects intellectual property rights. If you are a trademark owner, brand representative, or copyright holder and believe a listed product violates your rights, submit an infringement notice to our IP Sentinel team at <strong className="text-blue-600">infringement@hashkart.demo</strong>.
          </p>
        </div>
      ),
    },

    // 4. CONSUMER POLICY
    terms: {
      title: 'Terms of Use & Marketplace Agreement',
      badge: 'Legal Terms',
      category: 'Consumer Policy',
      icon: <FileText size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4 text-xs text-gray-700 leading-relaxed">
          <p>This document is an electronic record in terms of the Information Technology Act, 2000 and rules there under as applicable and the amended provisions pertaining to electronic records.</p>
          <p>Your use of the HashKart website, mobile applications, APIs, and associated services is governed by the terms and conditions contained herein.</p>
          <p>By browsing, accessing, or shopping on HashKart, you agree to comply with all applicable Indian commercial laws, taxation policies, and user conduct guidelines.</p>
        </div>
      ),
    },

    security: {
      title: 'Security, Fraud Defense & Data Protection',
      badge: 'Bank-Grade Defense',
      category: 'Consumer Policy',
      icon: <ShieldCheck size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4">
          <p className="text-gray-700 leading-relaxed">
            HashKart incorporates multi-layered automated risk controls, device fingerprinting, behavioral heuristics, and biometric 2FA to guarantee that your shopping account and card details remain 100% secure.
          </p>
          <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
            <h4 className="font-bold text-green-900 text-sm">PCI-DSS Level 1 Certified</h4>
            <p className="text-xs text-green-700 mt-1">We never store your complete CVV or bank PIN. All sensitive transactions are tokenized via Reserve Bank of India (RBI) authorized card networks.</p>
          </div>
        </div>
      ),
    },

    privacy: {
      title: 'Privacy Policy & Data Protection',
      badge: 'Privacy Standard',
      category: 'Consumer Policy',
      icon: <ShieldCheck size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4 text-xs text-gray-700 leading-relaxed">
          <p>We value the trust you place in us. That is why we insist upon the highest standards for secure transactions and customer information privacy.</p>
          <p>We do not sell, rent, or trade your personally identifiable information to third-party advertisers. All customer data is encrypted at rest using AES-256 and transmitted using TLS 1.3 encryption.</p>
        </div>
      ),
    },

    sitemap: {
      title: 'Marketplace Sitemap & Directory',
      badge: 'Catalog Index',
      category: 'Consumer Policy',
      icon: <Globe size={24} className="text-blue-600" />,
      content: (
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-4 text-xs">
          <div className="space-y-2">
            <h4 className="font-bold text-gray-900 border-b pb-1">Shop by Category</h4>
            <p><Link to="/products?category_slug=mobiles" className="text-blue-600 hover:underline">Mobiles & Smartphones</Link></p>
            <p><Link to="/products?category_slug=laptops" className="text-blue-600 hover:underline">Laptops & Computers</Link></p>
            <p><Link to="/products?category_slug=audio" className="text-blue-600 hover:underline">Audio & Headphones</Link></p>
            <p><Link to="/products?category_slug=televisions" className="text-blue-600 hover:underline">Televisions</Link></p>
            <p><Link to="/products?category_slug=mens-clothing" className="text-blue-600 hover:underline">Fashion & Footwear</Link></p>
          </div>
          <div className="space-y-2">
            <h4 className="font-bold text-gray-900 border-b pb-1">Customer Account</h4>
            <p><Link to="/account" className="text-blue-600 hover:underline">My Account Dashboard</Link></p>
            <p><Link to="/orders" className="text-blue-600 hover:underline">Order History & Tracking</Link></p>
            <p><Link to="/wishlist" className="text-blue-600 hover:underline">My Wishlist</Link></p>
            <p><Link to="/cart" className="text-blue-600 hover:underline">Shopping Cart</Link></p>
          </div>
          <div className="space-y-2">
            <h4 className="font-bold text-gray-900 border-b pb-1">Merchant Hubs</h4>
            <p><Link to="/seller/orders" className="text-blue-600 hover:underline">Seller Fulfillment Portal</Link></p>
            <p><Link to="/seller/inventory" className="text-blue-600 hover:underline">Seller Inventory Manager</Link></p>
            <p><Link to="/seller/analytics" className="text-blue-600 hover:underline">Seller Analytics & Revenue</Link></p>
          </div>
        </div>
      ),
    },

    grievance: {
      title: 'Grievance Redressal Mechanism',
      badge: 'Consumer Grievance Desk',
      category: 'Consumer Policy',
      icon: <Award size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4 text-xs text-gray-700">
          <p>In accordance with the Information Technology Act 2000 and Consumer Protection (E-Commerce) Rules 2020, the contact details of the Grievance Officer are provided below:</p>
          <div className="p-4 bg-gray-50 border rounded-lg space-y-1">
            <p><strong>Officer Name:</strong> Mr. Vikramaditya Rao</p>
            <p><strong>Designation:</strong> Chief Nodal & Grievance Officer</p>
            <p><strong>Email:</strong> grievance-officer@hashkart.demo</p>
            <p><strong>Address:</strong> HashKart Internet Pvt Ltd, Outer Ring Road, Bengaluru 560103, Karnataka, India.</p>
            <p><strong>Dispute Resolution Timeframe:</strong> Acknowledgment within 48 hours; full resolution within 30 days.</p>
          </div>
        </div>
      ),
    },

    'epr-compliance': {
      title: 'Extended Producer Responsibility (EPR) & E-Waste Management',
      badge: 'Green Commerce',
      category: 'Consumer Policy',
      icon: <Award size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4 text-xs text-gray-700 leading-relaxed">
          <p>HashKart is committed to environmental sustainability and responsible recycling under the E-Waste (Management) Rules, 2022 mandated by the Ministry of Environment, Forest and Climate Change (MoEFCC).</p>
          <p>Customers can deposit old electronics, mobile batteries, and packaging materials at authorized HashKart recycling drop-points across 100+ cities free of charge.</p>
        </div>
      ),
    },

    fssai: {
      title: 'FSSAI Food Safety & Quality Standards',
      badge: 'Food Safety Assured',
      category: 'Consumer Policy',
      icon: <CheckCircle2 size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-4 text-xs text-gray-700">
          <p>All packaged food, gourmet, nutrition, and beverage products sold on HashKart are procured strictly from certified FSSAI-compliant vendors.</p>
          <div className="p-3 bg-green-50 border border-green-200 rounded">
            <p><strong>Central FSSAI License Number:</strong> 10024043000892</p>
          </div>
        </div>
      ),
    },

    // 5. BOTTOM BAR ACTIONS
    advertise: {
      title: 'HashKart Advertising Network for Brands & Sellers',
      badge: 'Growth Engine',
      category: 'Business',
      icon: <Megaphone size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            Reach high-intent shoppers with high-ROI sponsored search ads, category banner takeovers, and personalized video placements.
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            <div className="p-3 border rounded bg-gray-50">
              <h5 className="font-bold text-gray-900 text-xs">Sponsored Product Ads</h5>
              <p className="text-xs text-gray-600 mt-1">Appear at the top of search listings for high-intent keywords.</p>
            </div>
            <div className="p-3 border rounded bg-gray-50">
              <h5 className="font-bold text-gray-900 text-xs">Category Showcase Banners</h5>
              <p className="text-xs text-gray-600 mt-1">High-impact brand positioning on category landing pages.</p>
            </div>
            <div className="p-3 border rounded bg-gray-50">
              <h5 className="font-bold text-gray-900 text-xs">Real-Time Performance Dashboard</h5>
              <p className="text-xs text-gray-600 mt-1">Track ROAS, impressions, click-through rates, and conversions.</p>
            </div>
          </div>
          <Link to="/seller/advertising" className="inline-block px-4 py-2 bg-blue-600 text-white text-xs font-bold rounded hover:bg-blue-700">
            Open Seller Advertising Console
          </Link>
        </div>
      ),
    },

    'gift-cards': {
      title: 'HashKart Digital Gift Cards & Corporate Gifting',
      badge: 'Instant Delivery',
      category: 'Gifting',
      icon: <Gift size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            Give the gift of choice with HashKart digital gift cards. Delivered instantly via email or SMS with custom personalized greeting messages.
          </p>
          <div className="p-4 border rounded-lg bg-gradient-to-r from-amber-50 to-orange-50 border-amber-200">
            <h4 className="font-bold text-amber-900 text-sm">Festive & Corporate Bulk Gifting</h4>
            <p className="text-xs text-amber-700 mt-1">Special bulk discounts and custom corporate co-branding available for orders above ₹50,000.</p>
            <p className="text-xs font-semibold text-amber-800 mt-2">Contact: corporate-gifts@hashkart.demo</p>
          </div>
        </div>
      ),
    },

    'help-center': {
      title: 'HashKart Help Center & Customer Support Desk',
      badge: 'Self-Service Hub',
      category: 'Help',
      icon: <HelpCircle size={24} className="text-blue-600" />,
      content: (
        <div className="space-y-6">
          <p className="text-gray-700 leading-relaxed">
            Welcome to the HashKart Help Center. Find answers to common questions or reach out to our dedicated resolution specialists.
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <Link to="/orders" className="p-4 border rounded-lg hover:border-blue-500 hover:shadow-sm transition-all block">
              <h4 className="font-bold text-gray-900 text-sm">Track & Manage Orders</h4>
              <p className="text-xs text-gray-500 mt-1">Check delivery status, download invoices, or cancel items.</p>
            </Link>
            <Link to="/returns/new" className="p-4 border rounded-lg hover:border-blue-500 hover:shadow-sm transition-all block">
              <h4 className="font-bold text-gray-900 text-sm">Returns & Refunds</h4>
              <p className="text-xs text-gray-500 mt-1">Initiate replacement or return for recently delivered products.</p>
            </Link>
          </div>
        </div>
      ),
    },
  };

  const activeSection = infoData[pageKey] || infoData['about-us'];

  const navCategories = [
    {
      title: 'About HashKart',
      links: [
        { key: 'about-us', label: 'About Us' },
        { key: 'contact-us', label: 'Contact Us' },
        { key: 'careers', label: 'Careers' },
        { key: 'stories', label: 'HashKart Stories' },
        { key: 'press', label: 'Press & Media' },
        { key: 'corporate-information', label: 'Corporate Information' },
      ],
    },
    {
      title: 'Group Companies',
      links: [
        { key: 'hashpay', label: 'HashPay' },
        { key: 'hashlogistics', label: 'HashLogistics' },
        { key: 'hashstudio', label: 'HashStudio Creators' },
        { key: 'cleartrip', label: 'Cleartrip' },
        { key: 'shopsy', label: 'Shopsy by HashKart' },
      ],
    },
    {
      title: 'Help & Support',
      links: [
        { key: 'help-center', label: 'Help Center' },
        { key: 'payments', label: 'Payments' },
        { key: 'shipping', label: 'Shipping & Delivery' },
        { key: 'cancellation-returns', label: 'Cancellation & Returns' },
        { key: 'faq', label: 'FAQ' },
        { key: 'report-infringement', label: 'Report Infringement' },
      ],
    },
    {
      title: 'Consumer Policies',
      links: [
        { key: 'terms', label: 'Terms of Use' },
        { key: 'security', label: 'Security' },
        { key: 'privacy', label: 'Privacy Policy' },
        { key: 'sitemap', label: 'Sitemap' },
        { key: 'grievance', label: 'Grievance Redressal' },
        { key: 'epr-compliance', label: 'EPR Compliance' },
        { key: 'fssai', label: 'FSSAI Safety Connect' },
      ],
    },
    {
      title: 'Business & Gifting',
      links: [
        { key: 'advertise', label: 'Advertise with Us' },
        { key: 'gift-cards', label: 'Gift Cards' },
      ],
    },
  ];

  return (
    <div style={{ maxWidth: '1280px', margin: '24px auto', padding: '0 16px' }}>
      {/* Breadcrumb Navigation */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '12px', color: '#666', marginBottom: '20px' }}>
        <Link to="/" style={{ color: '#2874f0', textDecoration: 'none' }}>Home</Link>
        <ChevronRight size={14} />
        <span>{activeSection.category}</span>
        <ChevronRight size={14} />
        <span style={{ fontWeight: 600, color: '#212121' }}>{activeSection.title}</span>
      </div>

      <div style={{ display: 'flex', gap: '24px', alignItems: 'flex-start' }}>
        {/* Sidebar Navigation */}
        <aside
          style={{
            width: '260px',
            backgroundColor: 'var(--bg-card)',
            border: '1px solid var(--border-color)',
            borderRadius: '8px',
            padding: '16px',
            flexShrink: 0,
          }}
        >
          <h3 style={{ fontSize: '14px', fontWeight: 800, color: '#212121', marginBottom: '16px', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
            Information Desk
          </h3>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {navCategories.map((cat, idx) => (
              <div key={idx}>
                <h4 style={{ fontSize: '11px', fontWeight: 700, color: '#888', textTransform: 'uppercase', marginBottom: '6px' }}>
                  {cat.title}
                </h4>
                <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
                  {cat.links.map((link) => {
                    const isActive = pageKey === link.key;
                    return (
                      <Link
                        key={link.key}
                        to={`/info/${link.key}`}
                        style={{
                          fontSize: '13px',
                          textDecoration: 'none',
                          padding: '6px 8px',
                          borderRadius: '4px',
                          color: isActive ? '#2874f0' : '#444',
                          backgroundColor: isActive ? '#e8f0fe' : 'transparent',
                          fontWeight: isActive ? 700 : 500,
                          transition: 'all 0.15s ease',
                        }}
                      >
                        {link.label}
                      </Link>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        </aside>

        {/* Main Content Area */}
        <main
          style={{
            flex: 1,
            backgroundColor: 'var(--bg-card)',
            border: '1px solid var(--border-color)',
            borderRadius: '8px',
            padding: '32px',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', borderBottom: '1px solid #eee', paddingBottom: '16px', marginBottom: '24px' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
              <div style={{ padding: '8px', backgroundColor: '#f0f5ff', borderRadius: '8px' }}>
                {activeSection.icon}
              </div>
              <div>
                <h1 style={{ fontSize: '22px', fontWeight: 800, color: '#212121', margin: 0 }}>
                  {activeSection.title}
                </h1>
                <span style={{ fontSize: '12px', color: '#666' }}>HashKart Official Information & Policies</span>
              </div>
            </div>

            {activeSection.badge && (
              <span
                style={{
                  backgroundColor: '#e8f0fe',
                  color: '#1a73e8',
                  padding: '4px 10px',
                  borderRadius: '12px',
                  fontSize: '11px',
                  fontWeight: 700,
                }}
              >
                {activeSection.badge}
              </span>
            )}
          </div>

          <div>{activeSection.content}</div>
        </main>
      </div>
    </div>
  );
};
