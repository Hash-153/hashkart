import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { Search, TrendingUp, History, X, Tag, Package, Folder } from 'lucide-react';
import { api } from '../services/api';
import { AutocompleteSuggestion, TrendingSearchItem, UserSearchHistoryItem } from '../types';
import { useAuth } from '../context/AuthContext';

export const SearchBar: React.FC = () => {
  const { user } = useAuth();
  const [query, setQuery] = useState('');
  const [suggestions, setSuggestions] = useState<AutocompleteSuggestion[]>([]);
  const [trending, setTrending] = useState<TrendingSearchItem[]>([]);
  const [history, setHistory] = useState<UserSearchHistoryItem[]>([]);
  const [isOpen, setIsOpen] = useState(false);
  const [selectedIndex, setSelectedIndex] = useState(-1);

  const navigate = useNavigate();
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Fetch initial trending searches
    api.getTrendingSearches().then(setTrending).catch(console.error);
    if (user) {
      api.getUserSearchHistory().then(setHistory).catch(console.error);
    }
  }, [user]);

  // Debounced Autocomplete
  useEffect(() => {
    if (query.trim().length < 2) {
      setSuggestions([]);
      return;
    }

    const timer = setTimeout(() => {
      api.getAutocompleteSuggestions(query.trim())
        .then(setSuggestions)
        .catch(console.error);
    }, 250);

    return () => clearTimeout(timer);
  }, [query]);

  // Close dropdown on outside click
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (containerRef.current && !containerRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const handleSelectQuery = (searchTerm: string, slug?: string, type?: string) => {
    setIsOpen(false);
    setQuery(searchTerm);
    if (type === 'category' && slug) {
      navigate(`/products?category_slug=${slug}`);
    } else if (type === 'brand' && slug) {
      navigate(`/products?q=${encodeURIComponent(searchTerm)}`);
    } else if (type === 'product' && slug) {
      navigate(`/products/${slug}`);
    } else {
      navigate(`/products?q=${encodeURIComponent(searchTerm)}`);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (selectedIndex >= 0 && suggestions[selectedIndex]) {
      const item = suggestions[selectedIndex];
      handleSelectQuery(item.label, item.slug, item.type);
    } else if (query.trim()) {
      handleSelectQuery(query.trim());
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (!isOpen) return;

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev < suggestions.length - 1 ? prev + 1 : 0));
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setSelectedIndex((prev) => (prev > 0 ? prev - 1 : suggestions.length - 1));
    } else if (e.key === 'Escape') {
      setIsOpen(false);
    }
  };

  const handleClearHistoryItem = async (e: React.MouseEvent, id: number) => {
    e.stopPropagation();
    try {
      await api.deleteSearchHistoryItem(id);
      setHistory(history.filter((h) => h.id !== id));
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div ref={containerRef} className="search-container" style={{ position: 'relative', width: '100%', maxWidth: '560px' }}>
      <form onSubmit={handleSubmit} className="search-input-wrapper">
        <input
          type="text"
          className="search-input"
          placeholder="Search for products, brands and more..."
          value={query}
          onFocus={() => setIsOpen(true)}
          onChange={(e) => {
            setQuery(e.target.value);
            setIsOpen(true);
            setSelectedIndex(-1);
          }}
          onKeyDown={handleKeyDown}
        />
        {query && (
          <button
            type="button"
            onClick={() => setQuery('')}
            style={{ border: 'none', background: 'none', cursor: 'pointer', padding: '4px', display: 'flex', alignItems: 'center' }}
          >
            <X size={16} color="#878787" />
          </button>
        )}
        <button type="submit" className="search-btn" aria-label="Search">
          <Search size={18} />
        </button>
      </form>

      {/* Autocomplete & Discovery Dropdown */}
      {isOpen && (
        <div
          style={{
            position: 'absolute',
            top: '105%',
            left: 0,
            right: 0,
            backgroundColor: '#ffffff',
            borderRadius: '4px',
            boxShadow: '0 8px 24px rgba(0,0,0,0.18)',
            zIndex: 1200,
            overflow: 'hidden',
            color: '#212121',
          }}
        >
          {/* Autocomplete Suggestions */}
          {suggestions.length > 0 && (
            <div style={{ borderBottom: '1px solid #f0f0f0' }}>
              <div style={{ padding: '8px 16px', fontSize: '11px', fontWeight: 700, color: '#878787', textTransform: 'uppercase' }}>
                Suggestions
              </div>
              {suggestions.map((item, idx) => (
                <div
                  key={idx}
                  onClick={() => handleSelectQuery(item.label, item.slug, item.type)}
                  style={{
                    padding: '10px 16px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    cursor: 'pointer',
                    fontSize: '13px',
                    backgroundColor: selectedIndex === idx ? '#f2f7fe' : 'transparent',
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                    {item.type === 'category' && <Folder size={15} color="#2874f0" />}
                    {item.type === 'brand' && <Tag size={15} color="#ff9f00" />}
                    {item.type === 'product' && <Package size={15} color="#388e3c" />}
                    {item.type === 'keyword' && <Search size={15} color="#878787" />}
                    <span style={{ fontWeight: 500 }}>{item.label}</span>
                  </div>
                  <span style={{ fontSize: '11px', color: '#878787', textTransform: 'capitalize' }}>{item.type}</span>
                </div>
              ))}
            </div>
          )}

          {/* User Recent Searches */}
          {user && history.length > 0 && query.trim().length === 0 && (
            <div style={{ borderBottom: '1px solid #f0f0f0' }}>
              <div style={{ padding: '8px 16px', fontSize: '11px', fontWeight: 700, color: '#878787', textTransform: 'uppercase', display: 'flex', justifyContent: 'space-between' }}>
                <span>Recent Searches</span>
                <button
                  onClick={() => {
                    api.clearUserSearchHistory();
                    setHistory([]);
                  }}
                  style={{ background: 'none', border: 'none', color: '#2874f0', cursor: 'pointer', fontSize: '11px', fontWeight: 600 }}
                >
                  Clear All
                </button>
              </div>
              {history.slice(0, 4).map((h) => (
                <div
                  key={h.id}
                  onClick={() => handleSelectQuery(h.query)}
                  style={{
                    padding: '8px 16px',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    cursor: 'pointer',
                    fontSize: '13px',
                  }}
                >
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <History size={14} color="#878787" />
                    <span>{h.query}</span>
                  </div>
                  <button
                    onClick={(e) => handleClearHistoryItem(e, h.id)}
                    style={{ background: 'none', border: 'none', cursor: 'pointer', padding: '2px' }}
                  >
                    <X size={13} color="#999" />
                  </button>
                </div>
              ))}
            </div>
          )}

          {/* Trending Searches */}
          {trending.length > 0 && query.trim().length === 0 && (
            <div>
              <div style={{ padding: '8px 16px', fontSize: '11px', fontWeight: 700, color: '#878787', textTransform: 'uppercase' }}>
                Popular & Trending Searches
              </div>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', padding: '8px 16px 14px' }}>
                {trending.map((t, idx) => (
                  <button
                    key={idx}
                    onClick={() => handleSelectQuery(t.query)}
                    style={{
                      padding: '4px 10px',
                      backgroundColor: '#f5f5f5',
                      border: '1px solid #e0e0e0',
                      borderRadius: '16px',
                      fontSize: '12px',
                      color: '#333',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '4px',
                    }}
                  >
                    <TrendingUp size={12} color="#2874f0" /> {t.query}
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
