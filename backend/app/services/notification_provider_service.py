import logging
from dataclasses import dataclass
from typing import Protocol

logger = logging.getLogger("hashkart.notifications.providers")


@dataclass(frozen=True, slots=True)
class DeliveryResult:
    provider: str
    accepted: bool
    provider_message_id: str | None = None


class EmailProvider(Protocol):
    async def send(self, recipient: str, subject: str, body: str) -> DeliveryResult: ...


class SmsProvider(Protocol):
    async def send(self, recipient: str, body: str) -> DeliveryResult: ...


class LoggingEmailProvider:
    """Safe local adapter; replace with a transactional email provider in production."""

    async def send(self, recipient: str, subject: str, body: str) -> DeliveryResult:
        logger.info("Email delivery queued for %s with subject %s", recipient, subject)
        return DeliveryResult(provider="logging-email", accepted=True)


class LoggingSmsProvider:
    """Safe local adapter; replace with an SMS provider in production."""

    async def send(self, recipient: str, body: str) -> DeliveryResult:
        logger.info("SMS delivery queued for %s (%s chars)", recipient, len(body))
        return DeliveryResult(provider="logging-sms", accepted=True)


class NotificationProviderRegistry:
    def __init__(self) -> None:
        self.email: EmailProvider = LoggingEmailProvider()
        self.sms: SmsProvider = LoggingSmsProvider()

    async def deliver(self, channel: str, recipient: str, subject: str, body: str) -> DeliveryResult:
        if channel == "EMAIL":
            return await self.email.send(recipient, subject, body)
        if channel == "SMS":
            return await self.sms.send(recipient, body)
        raise ValueError(f"Unsupported notification channel: {channel}")


provider_registry = NotificationProviderRegistry()
