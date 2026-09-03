import React, { useState } from 'react';
import { LifeBuoy, Clock, CheckCircle2, MessageSquare, AlertCircle, Send } from 'lucide-react';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { Modal } from '../../components/ui/Modal';
import { useToast } from '../../components/ui/Toast';

interface TicketRecord {
  id: number;
  ticketNumber: string;
  subject: string;
  customerName: string;
  customerEmail: string;
  priority: 'LOW' | 'MEDIUM' | 'HIGH' | 'URGENT';
  status: 'OPEN' | 'IN_PROGRESS' | 'WAITING_FOR_CUSTOMER' | 'RESOLVED';
  slaHoursLeft: number;
  createdDate: string;
}

const MOCK_TICKETS: TicketRecord[] = [
  { id: 1, ticketNumber: 'TKT-2026-901', subject: 'Package marked delivered but not received', customerName: 'Ramesh Kumar', customerEmail: 'ramesh.k@gmail.com', priority: 'URGENT', status: 'OPEN', slaHoursLeft: 2, createdDate: 'Today, 1:30 PM' },
  { id: 2, ticketNumber: 'TKT-2026-899', subject: 'Refund delay for cancelled order #HK-9921', customerName: 'Sita Ram', customerEmail: 'sita.ram@yahoo.com', priority: 'HIGH', status: 'IN_PROGRESS', slaHoursLeft: 8, createdDate: 'Today, 10:00 AM' },
  { id: 3, ticketNumber: 'TKT-2026-895', subject: 'Invoice GST details correction request', customerName: 'Anil Exports', customerEmail: 'accounts@anilexports.in', priority: 'MEDIUM', status: 'RESOLVED', slaHoursLeft: 24, createdDate: 'Yesterday' },
];

export const AdminSupportPage: React.FC = () => {
  const { showToast } = useToast();
  const [tickets, setTickets] = useState<TicketRecord[]>(MOCK_TICKETS);
  const [activeTicket, setActiveTicket] = useState<TicketRecord | null>(null);
  const [replyText, setReplyText] = useState('');

  const handleSendReply = () => {
    if (!activeTicket || !replyText.trim()) return;
    setTickets((prev) =>
      prev.map((t) => (t.id === activeTicket.id ? { ...t, status: 'RESOLVED' } : t))
    );
    showToast('success', 'Ticket Response Sent', `Customer emailed and ticket #${activeTicket.ticketNumber} marked resolved.`);
    setActiveTicket(null);
    setReplyText('');
  };

  const columns: ColumnDef<TicketRecord>[] = [
    {
      key: 'ticketNumber',
      header: 'Ticket Ref / Subject',
      render: (item) => (
        <div>
          <span className="font-mono text-xs font-bold text-gray-900">{item.ticketNumber}</span>
          <p className="text-xs text-gray-600 line-clamp-1">{item.subject}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'customerName',
      header: 'Customer',
      render: (item) => (
        <div>
          <p className="text-xs font-semibold text-gray-900">{item.customerName}</p>
          <p className="text-[11px] text-gray-400 font-mono">{item.customerEmail}</p>
        </div>
      ),
    },
    {
      key: 'priority',
      header: 'Priority',
      render: (item) => {
        const colors: Record<string, string> = {
          LOW: 'bg-gray-100 text-gray-800',
          MEDIUM: 'bg-blue-100 text-blue-800',
          HIGH: 'bg-amber-100 text-amber-800',
          URGENT: 'bg-red-100 text-red-800',
        };
        return <span className={`px-2 py-0.5 rounded font-bold text-[10px] ${colors[item.priority]}`}>{item.priority}</span>;
      },
      sortable: true,
    },
    {
      key: 'slaHoursLeft',
      header: 'SLA Remaining',
      render: (item) => (
        <span className={`text-xs font-semibold ${item.slaHoursLeft <= 4 ? 'text-red-600 font-bold' : 'text-gray-600'}`}>
          {item.slaHoursLeft}h left
        </span>
      ),
      sortable: true,
    },
    {
      key: 'status',
      header: 'Status',
      render: (item) => {
        const colors: Record<string, string> = {
          OPEN: 'bg-red-100 text-red-800',
          IN_PROGRESS: 'bg-blue-100 text-blue-800',
          WAITING_FOR_CUSTOMER: 'bg-amber-100 text-amber-800',
          RESOLVED: 'bg-green-100 text-green-800',
        };
        return <span className={`px-2 py-0.5 rounded font-semibold text-[11px] ${colors[item.status]}`}>{item.status}</span>;
      },
      sortable: true,
    },
    {
      key: 'actions',
      header: 'Action',
      render: (item) => (
        <button
          type="button"
          className="btn btn-neutral btn-sm flex items-center gap-1"
          onClick={() => setActiveTicket(item)}
        >
          <MessageSquare size={12} />
          <span>Reply</span>
        </button>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div>
        <h1 className="text-xl font-bold text-gray-900">Customer Care & Helpdesk SLA Operations</h1>
        <p className="text-xs text-gray-500 mt-0.5">Multi-tiered customer support ticket queues, SLA breach tracking, and resolution workbench.</p>
      </div>

      <DataTable
        data={tickets}
        columns={columns}
        searchPlaceholder="Search ticket or customer..."
        searchKey="subject"
      />

      {/* Reply Modal */}
      {activeTicket && (
        <Modal
          isOpen={true}
          onClose={() => setActiveTicket(null)}
          title={`Ticket ${activeTicket.ticketNumber} — ${activeTicket.customerName}`}
        >
          <div className="space-y-4 text-xs">
            <div>
              <span className="font-semibold text-gray-500">Subject:</span>
              <p className="font-bold text-gray-900 mt-0.5">{activeTicket.subject}</p>
            </div>

            <div>
              <label className="block font-bold text-gray-700 mb-1">Official Support Response</label>
              <textarea
                rows={4}
                placeholder="Type response to customer with escalation resolution..."
                value={replyText}
                onChange={(e) => setReplyText(e.target.value)}
                className="w-full p-2.5 border rounded-lg focus:ring-2 focus:ring-blue-500 text-xs"
              />
            </div>

            <div className="pt-3 flex justify-end gap-2 border-t">
              <button
                type="button"
                className="btn btn-neutral btn-sm"
                onClick={() => setActiveTicket(null)}
              >
                Cancel
              </button>
              <button
                type="button"
                className="btn btn-primary btn-sm flex items-center gap-1.5"
                disabled={!replyText.trim()}
                onClick={handleSendReply}
              >
                <Send size={14} />
                <span>Send & Resolve</span>
              </button>
            </div>
          </div>
        </Modal>
      )}
    </div>
  );
};
