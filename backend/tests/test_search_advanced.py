import pytest
from app.services.search_service import SearchService


def test_query_normalization():
    assert SearchService.normalize_query("  WIRELESS headphones! ") == "wireless headphones"
    assert SearchService.normalize_query("SAMSUNG-Galaxy   S24") == "samsung galaxy s24"


def test_tokenization_and_stemming():
    tokens = SearchService.tokenize("Wireless Headphones 256GB")
    assert "wireless" in tokens
    assert "headphones" in tokens
    assert "headphone" in tokens  # stemmed
    assert "256gb" in tokens


def test_relevance_scoring_and_explanation():
    score, reasons = SearchService.calculate_relevance_score(
        query_raw="wireless headphones",
        product_name="HashKart Wireless Bluetooth Headphones",
        sku_list=["HK-SKU-AUDIO1"],
        brand_name="HashTech",
        category_name="Audio & Headphones",
        description="Premium noise cancelling wireless headphones",
    )
    assert score > 50.0
    assert "NAME_PREFIX" in reasons or "NAME_MATCH" in reasons
    assert "CATEGORY_MATCH" in reasons
    assert "DESCRIPTION_MATCH" in reasons


def test_exact_sku_matching():
    score, reasons = SearchService.calculate_relevance_score(
        query_raw="HK-SKU-AUDIO1",
        product_name="Generic Audio Device",
        sku_list=["HK-SKU-AUDIO1"],
    )
    assert score >= 100.0
    assert "SKU_MATCH" in reasons


@pytest.mark.asyncio
async def test_search_api_endpoint(client):
    response = await client.get("/search?q=Headphones")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert "total" in data
    assert "facets" in data
    assert "categories" in data["facets"]
