import React, { useState } from 'react';
import { FileText, Download, Printer, CheckCircle2 } from 'lucide-react';
import { Modal } from './ui/Modal';
import { useToast } from './ui/Toast';

export interface InvoiceDownloadButtonProps {
  orderNumber: string;
  orderDate?: string;
  grandTotal: number;
}

export const InvoiceDownloadButton: React.FC<InvoiceDownloadButtonProps> = ({
  orderNumber,
  orderDate = '25 Aug 2026',
  grandTotal,
}) => {
  const { showToast } = useToast();
  const [isPreviewOpen, setIsPreviewOpen] = useState(false);

  const handlePrint = () => {
    window.print();
  };

  const handleDownloadPDF = () => {
    showToast('success', 'Invoice Downloaded', `Tax Invoice for ${orderNumber} downloaded as PDF.`);
    setIsPreviewOpen(false);
  };

  return (
    <>
      <button
        type="button"
        className="btn btn-neutral btn-sm flex items-center gap-1.5 text-xs text-gray-700"
        onClick={() => setIsPreviewOpen(true)}
      >
        <FileText size={14} />
        <span>GST Invoice</span>
      </button>

      {isPreviewOpen && (
        <Modal
          isOpen={true}
          onClose={() => setIsPreviewOpen(false)}
          title={`GST Tax Invoice — ${orderNumber}`}
          maxWidth="lg"
          footer={
            <div className="flex gap-2">
              <button
                type="button"
                className="btn btn-neutral btn-sm flex items-center gap-1"
                onClick={handlePrint}
              >
                <Printer size={14} />
                <span>Print Invoice</span>
              </button>
              <button
                type="button"
                className="btn btn-primary btn-sm flex items-center gap-1"
                onClick={handleDownloadPDF}
              >
                <Download size={14} />
                <span>Download PDF</span>
              </button>
            </div>
          }
        >
          <div className="space-y-4 text-xs bg-white p-4 border rounded-lg print:border-none">
            {/* Header */}
            <div className="flex justify-between items-start border-b pb-3">
              <div>
                <h2 className="text-base font-extrabold text-blue-900">NovaMart Retail Hub LLP</h2>
                <p className="text-gray-500">GSTIN: 29AAACB1234K1Z5</p>
                <p className="text-gray-500">Bangalore, Karnataka, India - 560001</p>
              </div>
              <div className="text-right">
                <span className="font-bold uppercase text-[10px] bg-gray-100 px-2 py-0.5 rounded">
                  Tax Invoice (Rule 46)
                </span>
                <p className="font-bold text-gray-900 mt-1">INV-202608-8921</p>
                <p className="text-gray-400 text-[11px]">{orderDate}</p>
              </div>
            </div>

            {/* Order Ref */}
            <div className="grid grid-cols-2 gap-4 bg-gray-50 p-2.5 rounded">
              <div>
                <p className="font-semibold text-gray-500">Billed To (Customer):</p>
                <p className="font-bold text-gray-900">Valued Shopper</p>
                <p className="text-gray-500">State: Karnataka (Code: 29)</p>
              </div>
              <div className="text-right">
                <p className="font-semibold text-gray-500">Order Reference:</p>
                <p className="font-mono font-bold text-gray-900">#{orderNumber}</p>
                <p className="text-gray-500">Place of Supply: 29 - Karnataka</p>
              </div>
            </div>

            {/* Line Items Table */}
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="border-b bg-gray-100/70 text-gray-600 font-bold text-[11px]">
                  <th className="p-2">Item Description</th>
                  <th className="p-2">HSN</th>
                  <th className="p-2 text-right">Qty</th>
                  <th className="p-2 text-right">Taxable</th>
                  <th className="p-2 text-right">CGST+SGST</th>
                  <th className="p-2 text-right">Total</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-100">
                <tr>
                  <td className="p-2 font-medium text-gray-900">Marketplace Merchandise Item</td>
                  <td className="p-2 font-mono text-gray-500">85171300</td>
                  <td className="p-2 text-right">1</td>
                  <td className="p-2 text-right">₹{(grandTotal / 1.18).toFixed(2)}</td>
                  <td className="p-2 text-right">₹{(grandTotal - (grandTotal / 1.18)).toFixed(2)}</td>
                  <td className="p-2 text-right font-bold">₹{grandTotal.toLocaleString('en-IN')}</td>
                </tr>
              </tbody>
            </table>

            <div className="pt-2 border-t flex justify-between items-center">
              <span className="text-[11px] text-gray-400">
                Digitally Signed by NovaMart Marketplace Authorized Signatory
              </span>
              <div className="text-right">
                <span className="text-xs text-gray-500">Grand Total: </span>
                <span className="text-base font-extrabold text-gray-900">₹{grandTotal.toLocaleString('en-IN')}</span>
              </div>
            </div>
          </div>
        </Modal>
      )}
    </>
  );
};
