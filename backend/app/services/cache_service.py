import json
from typing import Any, Optional

from app.config import settings


class CacheService:
    """Small cache facade with an optional Redis backend and local no-op fallback."""

    def __init__(self, redis_url: Optional[str] = None):
        self.redis_url = redis_url
        self._redis = None

    async def connect(self) -> None:
        if not self.redis_url:
            return
        from redis.asyncio import Redis

        self._redis = Redis.from_url(self.redis_url, decode_responses=True)
        await self._redis.ping()

    async def close(self) -> None:
        if self._redis:
            await self._redis.aclose()
            self._redis = None

    async def get_json(self, key: str) -> Optional[Any]:
        if not self._redis:
            return None
        value = await self._redis.get(key)
        return json.loads(value) if value else None

    async def set_json(self, key: str, value: Any, ttl_seconds: int = 300) -> None:
        if self._redis:
            await self._redis.set(key, json.dumps(value), ex=ttl_seconds)

    async def delete(self, key: str) -> None:
        if self._redis:
            await self._redis.delete(key)


cache = CacheService(getattr(settings, "REDIS_URL", None))
