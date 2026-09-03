import React, { useState } from 'react';
import { UploadCloud, FileSpreadsheet, CheckCircle2, AlertCircle, Download, RefreshCw } from 'lucide-react';
import { useToast } from '../../components/ui/Toast';

interface ImportBatchRecord {
  id: string;
  filename: string;
  totalRecords: number;
  successCount: number;
  errorCount: number;
  status: 'PROCESSING' | 'COMPLETED' | 'FAILED';
  uploadedAt: string;
}

const PAST_BATCHES: ImportBatchRecord[] = [
  { id: 'BATCH-20260825-01', filename: 'smartphones_monsoon_catalog.csv', totalRecords: 150, successCount: 148, errorCount: 2, status: 'COMPLETED', uploadedAt: 'Today, 2:30 PM' },
  { id: 'BATCH-20260824-02', filename: 'audio_accessories_restock.csv', totalRecords: 80, successCount: 80, errorCount: 0, status: 'COMPLETED', uploadedAt: 'Yesterday, 11:15 AM' },
];

export const SellerBulkUploadPage: React.FC = () => {
  const { showToast } = useToast();
  const [batches, setBatches] = useState<ImportBatchRecord[]>(PAST_BATCHES);
  const [isUploading, setIsUploading] = useState(false);

  const handleSimulateUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setIsUploading(true);
    setTimeout(() => {
      const newBatch: ImportBatchRecord = {
        id: `BATCH-${Date.now().toString().slice(-6)}`,
        filename: file.name,
        totalRecords: 45,
        successCount: 45,
        errorCount: 0,
        status: 'COMPLETED',
        uploadedAt: 'Just now',
      };
      setBatches((prev) => [newBatch, ...prev]);
      setIsUploading(false);
      showToast('success', 'Catalog Batch Ingested', `Successfully processed ${file.name} (45 listings created).`);
    }, 1500);
  };

  return (
    <div className="container py-6 space-y-6">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="text-xl font-bold text-gray-900">Bulk Product Catalog & Stock Ingestion</h1>
          <p className="text-xs text-gray-500 mt-0.5">Upload multi-attribute CSV/Excel product listings with barcode validation.</p>
        </div>

        <button
          type="button"
          className="btn btn-neutral btn-sm flex items-center gap-1.5"
          onClick={() => showToast('info', 'Template Downloaded', 'NovaMart_Catalog_Template.csv saved to downloads.')}
        >
          <Download size={14} />
          <span>Download Sample CSV Template</span>
        </button>
      </div>

      {/* Drag & Drop Upload Zone */}
      <div className="border-2 border-dashed border-gray-300 hover:border-blue-500 rounded-2xl p-8 text-center bg-white transition-all">
        <UploadCloud size={48} className="mx-auto text-blue-600 mb-3" />
        <h3 className="text-sm font-bold text-gray-900">Upload Merchant Catalog File (.csv, .xlsx)</h3>
        <p className="text-xs text-gray-500 mt-1 max-w-sm mx-auto">
          Drag and drop your spreadsheet here, or browse files from your computer. Max file size: 25 MB.
        </p>

        <label className="mt-4 inline-block">
          <input
            type="file"
            accept=".csv,.xlsx"
            className="hidden"
            onChange={handleSimulateUpload}
            disabled={isUploading}
          />
          <span className="btn btn-primary btn-sm cursor-pointer">
            {isUploading ? 'Processing Ingestion Batch...' : 'Browse Computer Files'}
          </span>
        </label>
      </div>

      {/* Past Ingestion Batches */}
      <div className="bg-white border border-gray-200 rounded-xl overflow-hidden shadow-sm">
        <div className="p-4 border-b flex items-center justify-between">
          <h3 className="text-sm font-bold text-gray-900">Recent Ingestion Batches</h3>
          <button
            type="button"
            className="text-xs text-gray-500 hover:text-gray-900 flex items-center gap-1"
            onClick={() => showToast('info', 'Refreshed', 'Batch status updated.')}
          >
            <RefreshCw size={12} />
            <span>Refresh</span>
          </button>
        </div>

        <div className="divide-y divide-gray-100">
          {batches.map((b) => (
            <div key={b.id} className="p-4 flex items-center justify-between text-xs">
              <div className="flex items-center gap-3">
                <FileSpreadsheet size={24} className="text-green-700" />
                <div>
                  <p className="font-bold text-gray-900">{b.filename}</p>
                  <p className="font-mono text-[11px] text-gray-400 mt-0.5">{b.id} • {b.uploadedAt}</p>
                </div>
              </div>

              <div className="flex items-center gap-6">
                <div className="text-right">
                  <span className="font-semibold text-gray-800">{b.successCount}/{b.totalRecords} Success</span>
                  {b.errorCount > 0 && (
                    <p className="text-red-600 text-[11px] font-bold">{b.errorCount} Errors</p>
                  )}
                </div>

                <span className="px-2.5 py-0.5 bg-green-100 text-green-800 rounded-full font-bold text-[10px]">
                  {b.status}
                </span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
