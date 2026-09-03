import time
from collections import defaultdict
from typing import Dict, Tuple
from fastapi import HTTPException, Request, status
from starlette.middleware.base import BaseHTTPMiddleware


class TokenBucketLimiter:
    """Sliding-window token bucket rate limiter per client IP / API key."""
    def __init__(self, rate_limit_per_minute: int = 120, burst_capacity: int = 150):
        self.rate = rate_limit_per_minute / 60.0  # tokens per second
        self.capacity = burst_capacity
        self.buckets: Dict[str, Tuple[float, float]] = defaultdict(lambda: (self.capacity, time.time()))

    def is_allowed(self, client_key: str) -> bool:
        tokens, last_time = self.buckets[client_key]
        now = time.time()
        elapsed = now - last_time

        # Replenish tokens
        tokens = min(self.capacity, tokens + elapsed * self.rate)

        if tokens >= 1.0:
            self.buckets[client_key] = (tokens - 1.0, now)
            return True
        else:
            self.buckets[client_key] = (tokens, now)
            return False


limiter = TokenBucketLimiter(rate_limit_per_minute=300, burst_capacity=400)


class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Exclude static assets, health probes, and metric endpoints
        path = request.url.path
        if path.startswith(("/static", "/docs", "/openapi.json", "/health", "/metrics")):
            return await call_next(request)

        client_ip = request.client.host if request.client else "unknown"
        if not limiter.is_allowed(client_ip):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Too many requests. Please slow down and try again.",
            )

        return await call_next(request)
