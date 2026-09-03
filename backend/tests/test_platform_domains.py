import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_support_ticket_requires_authentication(client: AsyncClient):
    response = await client.post(
        "/support/tickets",
        json={"subject": "Delivery question", "category": "DELIVERY", "description": "I need help with my delivery."},
    )
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_warehouse_inspection_rejects_unbalanced_quantities(client: AsyncClient, admin_token: str):
    response = await client.post(
        "/admin/warehouse/inspections",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={
            "receipt_id": 1,
            "variant_id": 1,
            "expected_quantity": 10,
            "accepted_quantity": 7,
            "rejected_quantity": 1,
            "condition": "MIXED",
        },
    )
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_payment_webhook_rejects_unsigned_request(client: AsyncClient):
    response = await client.post(
        "/payments/webhooks/mock",
        json={"event_id": "evt_001", "event_type": "payment.captured"},
    )
    assert response.status_code == 401
