import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { FilterSidebar } from '../components/FilterSidebar';
import { FilterChips } from '../components/FilterChips';
import { ProductCard } from '../components/ProductCard';
import { Category, Brand, Product, SearchFacets } from '../types';
import { api } from '../services/api';
import { HelpCircle } from 'lucide-react';

export const ProductListing: React.FC = () => {
  const [searchParams, setSearchParams] = useSearchParams();

  const queryQ = searchParams.get('q') || '';
  const queryCategory = searchParams.get('category_id') ? Number(searchParams.get('category_id')) : undefined;
  const queryCategorySlug = searchParams.get('category_slug') || undefined;
  const queryBrand = searchParams.get('brand_id') ? Number(searchParams.get('brand_id')) : undefined;
  const queryRating = searchParams.get('min_rating') ? Number(searchParams.get('min_rating')) : undefined;
  const queryMinPrice = searchParams.get('min_price') ? Number(searchParams.get('min_price')) : undefined;
  const queryMaxPrice = searchParams.get('max_price') ? Number(searchParams.get('max_price')) : undefined;
  const querySort = searchParams.get('sort') || 'relevance';
  const queryPage = searchParams.get('page') ? Number(searchParams.get('page')) : 1;

  const [categories, setCategories] = useState<Category[]>([]);
  const [brands, setBrands] = useState<Brand[]>([]);
  const [products, setProducts] = useState<Product[]>([]);
  const [facets, setFacets] = useState<SearchFacets | undefined>(undefined);
  const [didYouMean, setDidYouMean] = useState<string | undefined>(undefined);
  const [total, setTotal] = useState<number>(0);
  const [pages, setPages] = useState<number>(1);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    const fetchMetadata = async () => {
      try {
        const [cList, bList] = await Promise.all([api.getCategories(), api.getBrands()]);
        setCategories(cList);
        setBrands(bList);
      } catch (err) {
        console.error('Error fetching catalog metadata:', err);
      }
    };
    fetchMetadata();
  }, []);

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      try {
        const queryStr = searchParams.toString();
        const res = await api.getProducts(queryStr);
        setProducts(res.items);
        setTotal(res.total);
        setPages(res.pages);
        setFacets(res.facets);
        setDidYouMean(res.did_you_mean);
      } catch (err) {
        console.error('Error fetching products:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
  }, [searchParams]);

  const handleFilterChange = (filters: {
    category_id?: number;
    brand_id?: number;
    min_rating?: number;
    min_price?: number;
    max_price?: number;
  }) => {
    const newParams = new URLSearchParams(searchParams);
    newParams.set('page', '1');

    if (filters.category_id) newParams.set('category_id', filters.category_id.toString());
    else newParams.delete('category_id');

    if (filters.brand_id) newParams.set('brand_id', filters.brand_id.toString());
    else newParams.delete('brand_id');

    if (filters.min_rating) newParams.set('min_rating', filters.min_rating.toString());
    else newParams.delete('min_rating');

    if (filters.min_price) newParams.set('min_price', filters.min_price.toString());
    else newParams.delete('min_price');

    if (filters.max_price) newParams.set('max_price', filters.max_price.toString());
    else newParams.delete('max_price');

    setSearchParams(newParams);
  };

  const handleSortChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const newParams = new URLSearchParams(searchParams);
    newParams.set('sort', e.target.value);
    newParams.set('page', '1');
    setSearchParams(newParams);
  };

  const handlePageChange = (newPage: number) => {
    const newParams = new URLSearchParams(searchParams);
    newParams.set('page', newPage.toString());
    setSearchParams(newParams);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleClearFilters = () => {
    setSearchParams({});
  };

  const activeCategoryName = categories.find((c) => c.id === queryCategory)?.name;
  const activeBrandName = brands.find((b) => b.id === queryBrand)?.name;

  return (
    <div style={{ display: 'flex', gap: '16px', marginTop: '16px' }}>
      {/* Filter Sidebar */}
      <FilterSidebar
        categories={categories}
        brands={brands}
        selectedCategoryId={queryCategory}
        selectedBrandId={queryBrand}
        selectedMinRating={queryRating}
        selectedMinPrice={queryMinPrice}
        selectedMaxPrice={queryMaxPrice}
        onFilterChange={handleFilterChange}
        onClear={handleClearFilters}
      />

      {/* Main Listing View */}
      <main style={{ flex: 1 }}>
        <div
          style={{
            backgroundColor: 'var(--bg-card)',
            padding: '16px',
            borderRadius: '4px',
            border: '1px solid var(--border-color)',
            marginBottom: '16px',
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
          }}
        >
          <div>
            <h2 style={{ fontSize: '18px', fontWeight: 700 }}>
              {queryQ ? `Search Results for "${queryQ}"` : 'HashKart Product Catalog'}
            </h2>
            <span style={{ fontSize: '13px', color: 'var(--text-muted)' }}>
              (Showing {products.length} of {total} products)
            </span>
          </div>

          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <span style={{ fontSize: '13px', fontWeight: 600 }}>Sort By:</span>
            <select
              value={querySort}
              onChange={handleSortChange}
              style={{
                padding: '6px 12px',
                border: '1px solid var(--border-dark)',
                borderRadius: '4px',
                backgroundColor: 'var(--bg-card)',
                color: 'var(--text-main)',
                fontSize: '13px',
              }}
            >
              <option value="relevance">Popularity / Relevance</option>
              <option value="price_asc">Price -- Low to High</option>
              <option value="price_desc">Price -- High to Low</option>
              <option value="rating">Customer Rating</option>
              <option value="newest">Newest Arrivals</option>
              <option value="discount_desc">Discount Percentage</option>
            </select>
          </div>
        </div>

        {/* Active Filter Chips */}
        <FilterChips
          query={queryQ}
          categoryName={activeCategoryName}
          brandName={activeBrandName}
          minRating={queryRating}
          minPrice={queryMinPrice}
          maxPrice={queryMaxPrice}
          onRemoveQuery={() => {
            const newP = new URLSearchParams(searchParams);
            newP.delete('q');
            setSearchParams(newP);
          }}
          onRemoveCategory={() => handleFilterChange({ category_id: undefined, brand_id: queryBrand, min_rating: queryRating, min_price: queryMinPrice, max_price: queryMaxPrice })}
          onRemoveBrand={() => handleFilterChange({ category_id: queryCategory, brand_id: undefined, min_rating: queryRating, min_price: queryMinPrice, max_price: queryMaxPrice })}
          onRemoveRating={() => handleFilterChange({ category_id: queryCategory, brand_id: queryBrand, min_rating: undefined, min_price: queryMinPrice, max_price: queryMaxPrice })}
          onRemovePrice={() => handleFilterChange({ category_id: queryCategory, brand_id: queryBrand, min_rating: queryRating, min_price: undefined, max_price: undefined })}
          onClearAll={handleClearFilters}
        />

        {/* Did You Mean Suggestion Prompt */}
        {didYouMean && (
          <div
            style={{
              padding: '12px 16px',
              backgroundColor: '#fff8e1',
              border: '1px solid #ffe082',
              borderRadius: '4px',
              marginBottom: '16px',
              fontSize: '14px',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
            }}
          >
            <HelpCircle size={18} color="#f57f17" />
            <span>
              Did you mean:{' '}
              <button
                onClick={() => {
                  const newP = new URLSearchParams(searchParams);
                  newP.set('q', didYouMean);
                  setSearchParams(newP);
                }}
                style={{
                  background: 'none',
                  border: 'none',
                  color: '#2874f0',
                  fontWeight: 700,
                  fontSize: '14px',
                  cursor: 'pointer',
                  textDecoration: 'underline',
                }}
              >
                {didYouMean}
              </button>
              ?
            </span>
          </div>
        )}

        {loading ? (
          <div style={{ padding: '60px', textAlign: 'center', fontSize: '16px' }}>
            Loading catalog products...
          </div>
        ) : products.length === 0 ? (
          <div
            style={{
              backgroundColor: 'var(--bg-card)',
              padding: '60px',
              textAlign: 'center',
              borderRadius: '4px',
              border: '1px solid var(--border-color)',
            }}
          >
            <h3>No products match your criteria</h3>
            <p style={{ color: 'var(--text-muted)', marginTop: '8px' }}>
              Try adjusting your search keyword or clearing selected filter options.
            </p>
            <button onClick={handleClearFilters} className="btn-primary" style={{ marginTop: '16px' }}>
              Clear All Filters
            </button>
          </div>
        ) : (
          <>
            <div className="product-grid">
              {products.map((prod) => (
                <ProductCard key={prod.id} product={prod} />
              ))}
            </div>

            {/* Pagination Controls */}
            {pages > 1 && (
              <div
                style={{
                  display: 'flex',
                  justifyContent: 'center',
                  alignItems: 'center',
                  gap: '8px',
                  marginTop: '24px',
                  padding: '16px',
                  backgroundColor: '#ffffff',
                  borderRadius: '4px',
                }}
              >
                <button
                  disabled={queryPage <= 1}
                  onClick={() => handlePageChange(queryPage - 1)}
                  style={{
                    padding: '6px 14px',
                    border: '1px solid #ccc',
                    borderRadius: '4px',
                    background: queryPage <= 1 ? '#eee' : '#ffffff',
                    cursor: queryPage <= 1 ? 'not-allowed' : 'pointer',
                    fontSize: '13px',
                    fontWeight: 600,
                  }}
                >
                  Previous
                </button>

                <span style={{ fontSize: '13px', fontWeight: 600, margin: '0 8px' }}>
                  Page {queryPage} of {pages}
                </span>

                <button
                  disabled={queryPage >= pages}
                  onClick={() => handlePageChange(queryPage + 1)}
                  style={{
                    padding: '6px 14px',
                    border: '1px solid #ccc',
                    borderRadius: '4px',
                    background: queryPage >= pages ? '#eee' : '#ffffff',
                    cursor: queryPage >= pages ? 'not-allowed' : 'pointer',
                    fontSize: '13px',
                    fontWeight: 600,
                  }}
                >
                  Next
                </button>
              </div>
            )}
          </>
        )}
      </main>
    </div>
  );
};
