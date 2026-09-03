import React, { useState, useEffect } from 'react';
import { HelpCircle, ThumbsUp, MessageSquare, Send, CheckCircle2 } from 'lucide-react';
import { api } from '../services/api';
import { useAuth } from '../context/AuthContext';
import { useToast } from './ui/Toast';

export interface ProductQAProps {
  productId: number;
}

export const ProductQA: React.FC<ProductQAProps> = ({ productId }) => {
  const { user } = useAuth();
  const { showToast } = useToast();
  const [questions, setQuestions] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [newQuestionText, setNewQuestionText] = useState('');
  const [activeReplyQuestionId, setActiveReplyQuestionId] = useState<number | null>(null);
  const [replyText, setReplyText] = useState('');

  const fetchQuestions = async () => {
    try {
      setLoading(true);
      const data = await api.getProductQA(productId);
      setQuestions(data);
    } catch (err) {
      console.error('Failed to load Q&A:', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchQuestions();
  }, [productId]);

  const handlePostQuestion = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!user) {
      showToast('warning', 'Sign in required', 'Please log in to post a question.');
      return;
    }
    if (!newQuestionText.trim()) return;

    try {
      await api.postProductQuestion(productId, newQuestionText.trim());
      setNewQuestionText('');
      showToast('success', 'Question Posted', 'Your question is now visible to the community.');
      fetchQuestions();
    } catch (err: any) {
      showToast('error', 'Error', err.message || 'Failed to submit question.');
    }
  };

  const handlePostAnswer = async (questionId: number) => {
    if (!user) {
      showToast('warning', 'Sign in required', 'Please log in to answer.');
      return;
    }
    if (!replyText.trim()) return;

    try {
      await api.postProductAnswer(questionId, replyText.trim());
      setReplyText('');
      setActiveReplyQuestionId(null);
      showToast('success', 'Answer Submitted', 'Thank you for helping fellow shoppers!');
      fetchQuestions();
    } catch (err: any) {
      showToast('error', 'Error', err.message || 'Failed to post answer.');
    }
  };

  const handleUpvote = async (questionId: number) => {
    try {
      await api.upvoteQuestion(questionId);
      setQuestions((prev) =>
        prev.map((q) =>
          q.id === questionId ? { ...q, upvote_count: q.upvote_count + 1 } : q
        )
      );
    } catch (err) {
      console.error('Failed to upvote:', err);
    }
  };

  return (
    <div className="product-qa-section bg-white border border-gray-200 rounded-xl p-5 mt-6">
      <div className="flex items-center justify-between gap-3 border-b pb-4 mb-4">
        <div className="flex items-center gap-2">
          <HelpCircle size={20} className="text-primary" />
          <h3 className="text-base font-bold text-gray-900">
            Questions and Answers ({questions.length})
          </h3>
        </div>
      </div>

      {/* Ask Question Form */}
      <form onSubmit={handlePostQuestion} className="mb-6">
        <div className="flex gap-2">
          <input
            type="text"
            placeholder="Have a question? Ask other buyers & seller..."
            value={newQuestionText}
            onChange={(e) => setNewQuestionText(e.target.value)}
            className="flex-1 px-3.5 py-2 text-xs border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="submit"
            disabled={!newQuestionText.trim()}
            className="btn btn-primary btn-sm flex items-center gap-1.5"
          >
            <span>Post</span>
            <Send size={14} />
          </button>
        </div>
      </form>

      {/* Q&A List */}
      {loading ? (
        <div className="py-6 text-center text-xs text-gray-500">Loading questions...</div>
      ) : questions.length === 0 ? (
        <div className="py-8 text-center text-xs text-gray-400">
          No questions yet. Be the first to ask!
        </div>
      ) : (
        <div className="space-y-4 divide-y divide-gray-100">
          {questions.map((q) => (
            <div key={q.id} className="pt-4 first:pt-0">
              <div className="flex items-start justify-between gap-3">
                <div className="flex items-start gap-2">
                  <span className="font-bold text-sm text-gray-900">Q:</span>
                  <div>
                    <h4 className="text-xs font-semibold text-gray-900">{q.question_text}</h4>
                    <p className="text-[11px] text-gray-400 mt-0.5">Asked by {q.author_name}</p>
                  </div>
                </div>

                <button
                  type="button"
                  className="flex items-center gap-1 text-xs text-gray-500 hover:text-blue-600 bg-gray-50 px-2 py-1 rounded border border-gray-200"
                  onClick={() => handleUpvote(q.id)}
                >
                  <ThumbsUp size={12} />
                  <span>{q.upvote_count}</span>
                </button>
              </div>

              {/* Answers */}
              <div className="ml-5 mt-2 space-y-2">
                {q.answers?.map((ans: any) => (
                  <div key={ans.id} className="bg-gray-50/80 p-2.5 rounded-lg border border-gray-100">
                    <p className="text-xs text-gray-800">
                      <strong className="text-green-700 font-semibold mr-1.5">A:</strong>
                      {ans.answer_text}
                    </p>
                    <div className="flex items-center gap-2 mt-1.5 text-[11px] text-gray-400">
                      <span>{ans.author_name}</span>
                      {ans.is_seller_answer && (
                        <span className="px-1.5 py-0.2 bg-blue-100 text-blue-700 rounded font-semibold text-[10px]">
                          Seller
                        </span>
                      )}
                      {ans.is_verified_buyer && (
                        <span className="flex items-center gap-0.5 text-green-700 font-medium">
                          <CheckCircle2 size={12} />
                          <span>Verified Buyer</span>
                        </span>
                      )}
                    </div>
                  </div>
                ))}

                {/* Reply Form */}
                {activeReplyQuestionId === q.id ? (
                  <div className="mt-2 flex gap-2">
                    <input
                      type="text"
                      placeholder="Write your answer..."
                      value={replyText}
                      onChange={(e) => setReplyText(e.target.value)}
                      className="flex-1 px-3 py-1.5 text-xs border rounded focus:ring-1 focus:ring-blue-500"
                    />
                    <button
                      type="button"
                      className="btn btn-primary btn-sm"
                      onClick={() => handlePostAnswer(q.id)}
                    >
                      Submit
                    </button>
                    <button
                      type="button"
                      className="btn btn-neutral btn-sm"
                      onClick={() => setActiveReplyQuestionId(null)}
                    >
                      Cancel
                    </button>
                  </div>
                ) : (
                  <button
                    type="button"
                    className="text-xs text-blue-600 font-medium hover:underline flex items-center gap-1 mt-1"
                    onClick={() => {
                      setActiveReplyQuestionId(q.id);
                      setReplyText('');
                    }}
                  >
                    <MessageSquare size={12} />
                    <span>Answer this question</span>
                  </button>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
