from datetime import datetime, timezone
import pytest

from app.services.notification_engine import (
    NotificationChannel,
    NotificationEngine,
    NotificationMessagePayload,
)


def test_dlt_template_formatting():
    msg = NotificationEngine.render_sms_template(
        "ORDER_CONFIRMED",
        {"customer_name": "Rahul", "order_number": "HK-9921", "amount": "14,999", "delivery_date": "28th August"},
    )
    assert "Rahul" in msg
    assert "HK-9921" in msg
    assert "14,999" in msg


@pytest.mark.asyncio
async def test_notification_dispatch_channels():
    payload_sms = NotificationMessagePayload(
        user_id=1,
        channel=NotificationChannel.SMS,
        template_id="OTP_LOGIN",
        recipient_address="+919876543210",
        subject=None,
        parameters={"otp": "492810"},
        created_at=datetime.now(timezone.utc),
    )

    res_sms = await NotificationEngine.dispatch_notification(payload_sms)
    assert res_sms.is_success is True
    assert res_sms.channel == NotificationChannel.SMS
    assert res_sms.provider == "Gupshup DLT Gateway"

    payload_wa = NotificationMessagePayload(
        user_id=2,
        channel=NotificationChannel.WHATSAPP,
        template_id="ORDER_CONFIRMED",
        recipient_address="+919876543210",
        subject=None,
        parameters={"customer_name": "Priya", "order_number": "HK-1234", "amount": "999", "delivery_date": "Tomorrow"},
        created_at=datetime.now(timezone.utc),
    )

    res_wa = await NotificationEngine.dispatch_notification(payload_wa)
    assert res_wa.is_success is True
    assert res_wa.channel == NotificationChannel.WHATSAPP
