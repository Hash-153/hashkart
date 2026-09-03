import React, { useState } from 'react';
import { Image as ImageIcon, Star, X } from 'lucide-react';
import { Modal } from './ui/Modal';

export interface CustomerPhoto {
  id: number;
  imageUrl: string;
  authorName: string;
  rating: number;
  comment: string;
  reviewDate: string;
}

export interface ReviewGalleryProps {
  photos: CustomerPhoto[];
}

export const ReviewGallery: React.FC<ReviewGalleryProps> = ({ photos }) => {
  const [selectedPhoto, setSelectedPhoto] = useState<CustomerPhoto | null>(null);

  if (!photos || photos.length === 0) return null;

  return (
    <div className="review-photo-gallery-section mt-6 border-t pt-4">
      <div className="flex items-center gap-2 mb-3">
        <ImageIcon size={18} className="text-gray-700" />
        <h4 className="text-sm font-bold text-gray-900">
          Customer Images & Photos ({photos.length})
        </h4>
      </div>

      <div className="grid grid-cols-4 sm:grid-cols-6 md:grid-cols-8 gap-2">
        {photos.slice(0, 8).map((photo) => (
          <button
            key={photo.id}
            type="button"
            className="aspect-square rounded-lg overflow-hidden border border-gray-200 hover:opacity-90 hover:ring-2 hover:ring-blue-500 transition-all"
            onClick={() => setSelectedPhoto(photo)}
          >
            <img
              src={photo.imageUrl}
              alt={`Customer photo by ${photo.authorName}`}
              className="w-full h-full object-cover"
            />
          </button>
        ))}
      </div>

      {/* Lightbox Modal */}
      {selectedPhoto && (
        <Modal
          isOpen={true}
          onClose={() => setSelectedPhoto(null)}
          title={`Review by ${selectedPhoto.authorName}`}
          maxWidth="lg"
        >
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
            <div className="aspect-square bg-black rounded-lg overflow-hidden flex items-center justify-center">
              <img
                src={selectedPhoto.imageUrl}
                alt="Selected review"
                className="max-h-full max-w-full object-contain"
              />
            </div>
            <div className="space-y-3">
              <div className="flex items-center gap-2">
                <span className="px-2 py-0.5 bg-green-700 text-white font-bold text-xs rounded flex items-center gap-1">
                  <span>{selectedPhoto.rating}</span>
                  <Star size={12} className="fill-current" />
                </span>
                <span className="text-xs text-gray-500">{selectedPhoto.reviewDate}</span>
              </div>
              <p className="text-xs text-gray-800 leading-relaxed">
                "{selectedPhoto.comment}"
              </p>
              <p className="text-[11px] text-gray-400 font-medium">
                Verified Purchase by {selectedPhoto.authorName}
              </p>
            </div>
          </div>
        </Modal>
      )}
    </div>
  );
};
