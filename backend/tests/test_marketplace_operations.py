import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_seller_onboarding_requires_authentication(client: AsyncClient):
    response = await client.post(
        "/seller/onboarding",
        json={
            "business_name": "Acme Retail",
            "legal_name": "Acme Retail Private Limited",
            "tax_identifier": "GST-ACME-001",
            "phone": "9876543210",
        },
    )

    assert response.status_code == 401


@pytest.mark.asyncio
async def test_admin_can_approve_seller(client: AsyncClient, customer_token: str, admin_token: str):
    onboarding = await client.post(
        "/seller/onboarding",
        headers={"Authorization": f"Bearer {customer_token}"},
        json={
            "business_name": "Acme Retail",
            "legal_name": "Acme Retail Private Limited",
            "tax_identifier": "GST-ACME-002",
            "phone": "9876543210",
        },
    )
    assert onboarding.status_code == 201

    seller_id = onboarding.json()["id"]
    approval = await client.patch(
        f"/admin/sellers/{seller_id}/approval",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={"status": "APPROVED"},
    )

    assert approval.status_code == 200
    assert approval.json()["status"] == "APPROVED"


@pytest.mark.asyncio
async def test_return_quantity_is_validated(client: AsyncClient, customer_token: str):
    response = await client.post(
        "/orders/returns",
        headers={"Authorization": f"Bearer {customer_token}"},
        json={"order_item_id": 999999, "quantity": 1, "reason": "DAMAGED"},
    )

    assert response.status_code == 404
