"""
NovaMart Omnichannel Transactional Notification Hub
===================================================
Coordinates multi-channel customer communications:
- Transactional SMS via Twilio / Gupshup DLT-registered templates
- WhatsApp Business interactive templates with action buttons
- Rich Responsive HTML transactional email via Jinja2
- In-App realtime notifications & WebPush / FCM alerts
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from typing import Dict, List, Optional
import json


class NotificationChannel(str, Enum):
    SMS = "SMS"
    WHATSAPP = "WHATSAPP"
    EMAIL = "EMAIL"
    IN_APP = "IN_APP"
    PUSH = "PUSH"


@dataclass
class NotificationMessagePayload:
    user_id: int
    channel: NotificationChannel
    template_id: str
    recipient_address: str # Phone number or Email
    subject: Optional[str]
    parameters: Dict[str, str]
    created_at: datetime


@dataclass
class NotificationDispatchResult:
    is_success: bool
    channel: NotificationChannel
    message_id: str
    provider: str
    error_message: Optional[str] = None


# DLT Registered Template Registry
DLT_TEMPLATES: Dict[str, str] = {
    "OTP_LOGIN": "Your NovaMart verification OTP is {otp}. Valid for 5 minutes. Do not share with anyone.",
    "ORDER_CONFIRMED": "Dear {customer_name}, your NovaMart order #{order_number} for Rs.{amount} has been confirmed. Delivery by {delivery_date}.",
    "OUT_FOR_DELIVERY": "Your order #{order_number} is out for delivery with {carrier_name}. Driver: {driver_name} (Ph: {driver_phone}). Delivery OTP: {delivery_otp}.",
    "ORDER_DELIVERED": "Order #{order_number} delivered successfully! We hope you loved your items. Rate your experience on NovaMart.",
    "REFUND_INITIATED": "Refund of Rs.{amount} for order #{order_number} has been processed to your original payment method. UTR: {utr}.",
}


class NotificationEngine:
    @staticmethod
    def render_sms_template(template_id: str, params: Dict[str, str]) -> str:
        """Format DLT approved message body with dynamic customer parameters."""
        template_text = DLT_TEMPLATES.get(template_id, "Notification from NovaMart")
        try:
            return template_text.format(**params)
        except KeyError as e:
            return f"{template_text} [Missing Param: {e}]"

    @classmethod
    async def dispatch_notification(
        cls,
        payload: NotificationMessagePayload
    ) -> NotificationDispatchResult:
        """Simulate real-time multi-channel delivery across cloud communications providers."""
        rendered = cls.render_sms_template(payload.template_id, payload.parameters)

        if payload.channel == NotificationChannel.SMS:
            return NotificationDispatchResult(
                is_success=True,
                channel=NotificationChannel.SMS,
                message_id=f"sms_{payload.user_id}_{int(datetime.now(timezone.utc).timestamp())}",
                provider="Gupshup DLT Gateway",
            )
        elif payload.channel == NotificationChannel.WHATSAPP:
            return NotificationDispatchResult(
                is_success=True,
                channel=NotificationChannel.WHATSAPP,
                message_id=f"wa_{payload.user_id}_{int(datetime.now(timezone.utc).timestamp())}",
                provider="Meta WhatsApp Cloud API",
            )
        elif payload.channel == NotificationChannel.EMAIL:
            return NotificationDispatchResult(
                is_success=True,
                channel=NotificationChannel.EMAIL,
                message_id=f"email_{payload.user_id}_{int(datetime.now(timezone.utc).timestamp())}",
                provider="Amazon SES",
            )
        else:
            return NotificationDispatchResult(
                is_success=True,
                channel=payload.channel,
                message_id=f"push_{payload.user_id}_{int(datetime.now(timezone.utc).timestamp())}",
                provider="Firebase Cloud Messaging (FCM)",
            )
