import pytest


@pytest.mark.asyncio
async def test_search_history_requires_auth(client):
    response = await client.get("/search/history")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_search_history_isolation(client, customer_token, admin_token):
    # Customer performs search
    headers_cust = {"Authorization": f"Bearer {customer_token}"}
    await client.get("/search?q=Smartphones", headers=headers_cust)

    # Customer fetches search history
    res_cust = await client.get("/search/history", headers=headers_cust)
    assert res_cust.status_code == 200
    cust_history = res_cust.json()
    assert len(cust_history) >= 1
    assert cust_history[0]["query"] == "Smartphones"

    # Admin fetches own search history (must not see customer's search history)
    headers_admin = {"Authorization": f"Bearer {admin_token}"}
    res_admin = await client.get("/search/history", headers=headers_admin)
    assert res_admin.status_code == 200
    admin_history = res_admin.json()
    # Confirm customer history items are isolated
    cust_ids = [h["id"] for h in cust_history]
    admin_ids = [h["id"] for h in admin_history]
    for cid in cust_ids:
        assert cid not in admin_ids
