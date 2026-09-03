import React, { useState } from 'react';
import { ShieldCheck, Lock, Search, Filter, Eye, AlertTriangle, CheckCircle2 } from 'lucide-react';
import { DataTable, ColumnDef } from '../../components/ui/DataTable';
import { Modal } from '../../components/ui/Modal';
import { useToast } from '../../components/ui/Toast';

interface AuditLogRecord {
  id: string;
  actorEmail: string;
  actorRole: string;
  actionType: 'ROLE_CHANGE' | 'PAYOUT_APPROVAL' | 'STOCK_ADJUSTMENT' | 'PRICE_OVERRIDE' | 'GSTIN_VERIFIED';
  resource: string;
  ipAddress: string;
  timestamp: string;
  integrityVerified: boolean;
  diffSummary: string;
}

const MOCK_AUDIT_LOGS: AuditLogRecord[] = [
  { id: 'aud_20260825143001', actorEmail: 'admin@novamart.in', actorRole: 'ADMIN', actionType: 'PAYOUT_APPROVAL', resource: 'SELLER_BATCH_01', ipAddress: '10.0.12.45', timestamp: 'Today, 2:30 PM', integrityVerified: true, diffSummary: 'Approved NEFT transfer of ₹16,605,000 to 42 merchants' },
  { id: 'aud_20260825121522', actorEmail: 'lead_ops@novamart.in', actorRole: 'MANAGER', actionType: 'GSTIN_VERIFIED', resource: 'SELLER_182', ipAddress: '10.0.14.88', timestamp: 'Today, 12:15 PM', integrityVerified: true, diffSummary: 'Verified GSTIN 29AAACB1234K1Z5 via GSTN portal' },
  { id: 'aud_20260824184510', actorEmail: 'sec_officer@novamart.in', actorRole: 'ADMIN', actionType: 'ROLE_CHANGE', resource: 'USER_8921', ipAddress: '10.0.11.19', timestamp: 'Yesterday, 6:45 PM', integrityVerified: true, diffSummary: 'Promoted user to STAFF role' },
];

export const AdminAuditLogsPage: React.FC = () => {
  const { showToast } = useToast();
  const [logs] = useState<AuditLogRecord[]>(MOCK_AUDIT_LOGS);
  const [selectedLog, setSelectedLog] = useState<AuditLogRecord | null>(null);

  const columns: ColumnDef<AuditLogRecord>[] = [
    {
      key: 'timestamp',
      header: 'Timestamp / Hash ID',
      render: (item) => (
        <div>
          <span className="text-xs font-semibold text-gray-900">{item.timestamp}</span>
          <p className="font-mono text-[10px] text-gray-400">{item.id}</p>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'actorEmail',
      header: 'Operator & Role',
      render: (item) => (
        <div>
          <p className="text-xs font-bold text-gray-900">{item.actorEmail}</p>
          <span className="px-1.5 py-0.2 bg-blue-50 text-blue-700 text-[10px] font-bold rounded">
            {item.actorRole}
          </span>
        </div>
      ),
      sortable: true,
    },
    {
      key: 'actionType',
      header: 'Action Performed',
      render: (item) => <span className="font-mono text-xs font-bold text-gray-800">{item.actionType}</span>,
      sortable: true,
    },
    {
      key: 'resource',
      header: 'Target Resource',
      render: (item) => <span className="font-mono text-xs text-gray-600">{item.resource}</span>,
    },
    {
      key: 'integrityVerified',
      header: 'Cryptographic Hash',
      render: (item) => (
        <span className="flex items-center gap-1 text-[11px] text-green-700 font-bold bg-green-50 px-2 py-0.5 rounded">
          <ShieldCheck size={12} />
          <span>SHA-256 Valid</span>
        </span>
      ),
    },
    {
      key: 'actions',
      header: 'Inspector',
      render: (item) => (
        <button
          type="button"
          className="btn btn-neutral btn-sm flex items-center gap-1"
          onClick={() => setSelectedLog(item)}
        >
          <Eye size={12} />
          <span>View Diff</span>
        </button>
      ),
    },
  ];

  return (
    <div className="container py-6 space-y-6">
      <div>
        <h1 className="text-xl font-bold text-gray-900">Security Audit Trail & Compliance Explorer</h1>
        <p className="text-xs text-gray-500 mt-0.5">Immutable cryptographic audit logs for administrative actions, role escalations, and financial overrides.</p>
      </div>

      <DataTable
        data={logs}
        columns={columns}
        searchPlaceholder="Search operator email or action..."
        searchKey="actorEmail"
      />

      {/* Diff Inspector Modal */}
      {selectedLog && (
        <Modal
          isOpen={true}
          onClose={() => setSelectedLog(null)}
          title={`Audit Record: ${selectedLog.id}`}
        >
          <div className="space-y-3 text-xs">
            <div>
              <span className="font-bold text-gray-500">Action Summary:</span>
              <p className="p-2.5 bg-gray-50 rounded font-semibold text-gray-900 mt-1">
                {selectedLog.diffSummary}
              </p>
            </div>

            <div className="grid grid-cols-2 gap-3 text-gray-600">
              <div>
                <span className="font-bold text-gray-500">Source IP Address:</span>
                <p className="font-mono">{selectedLog.ipAddress}</p>
              </div>
              <div>
                <span className="font-bold text-gray-500">Target Resource:</span>
                <p className="font-mono">{selectedLog.resource}</p>
              </div>
            </div>

            <div className="pt-3 border-t flex justify-end">
              <button
                type="button"
                className="btn btn-primary btn-sm"
                onClick={() => setSelectedLog(null)}
              >
                Close Inspector
              </button>
            </div>
          </div>
        </Modal>
      )}
    </div>
  );
};
