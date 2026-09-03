import pytest
from app.services.search_service import SearchService


def test_levenshtein_distance():
    assert SearchService.lev_distance("headphone", "headphons") == 1
    assert SearchService.lev_distance("samsung", "samsng") == 1
    assert SearchService.lev_distance("laptop", "laptp") == 1


def test_did_you_mean_generation():
    vocabulary = {"headphones", "wireless", "samsung", "laptop", "mobile"}
    suggestion = SearchService.generate_did_you_mean("wireles headphons", vocabulary)
    assert suggestion == "wireless headphones"


@pytest.mark.asyncio
async def test_autocomplete_endpoint(client):
    response = await client.get("/search/autocomplete?q=head")
    assert response.status_code == 200
    suggestions = response.json()
    assert isinstance(suggestions, list)


@pytest.mark.asyncio
async def test_trending_searches_endpoint(client):
    response = await client.get("/search/trending")
    assert response.status_code == 200
    trending = response.json()
    assert isinstance(trending, list)
