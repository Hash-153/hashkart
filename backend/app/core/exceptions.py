from fastapi import Request, status
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("hashkart.exceptions")


class HashKartException(Exception):
    """Base exception for HashKart domain logic errors."""
    def __init__(self, message: str, code: str = "BAD_REQUEST", status_code: int = 400):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(message)


class InsufficientStockException(HashKartException):
    def __init__(self, message: str = "Insufficient inventory available"):
        super().__init__(message, code="INSUFFICIENT_STOCK", status_code=400)


class InvalidCouponException(HashKartException):
    def __init__(self, message: str = "Coupon code is invalid or expired"):
        super().__init__(message, code="INVALID_COUPON", status_code=400)


class PaymentFailedException(HashKartException):
    def __init__(self, message: str = "Payment processing failed"):
        super().__init__(message, code="PAYMENT_FAILED", status_code=402)


async def hashkart_exception_handler(request: Request, exc: HashKartException):
    logger.warning(f"Domain exception on {request.url.path}: {exc.code} - {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "path": str(request.url.path),
            }
        },
    )
