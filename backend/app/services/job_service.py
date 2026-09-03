import asyncio
import logging
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Awaitable, Callable, Any

logger = logging.getLogger("hashkart.jobs")


@dataclass(slots=True)
class Job:
    name: str
    payload: dict[str, Any]
    queued_at: datetime


class InProcessJobQueue:
    """Development-safe async queue; replace the worker with Redis/Celery in production."""

    def __init__(self) -> None:
        self._queue: asyncio.Queue[Job] = asyncio.Queue()
        self._worker_task: asyncio.Task | None = None
        self._handlers: dict[str, Callable[[dict[str, Any]], Awaitable[None]]] = {}

    def register(self, name: str, handler: Callable[[dict[str, Any]], Awaitable[None]]) -> None:
        self._handlers[name] = handler

    async def start(self) -> None:
        if not self._worker_task:
            self._worker_task = asyncio.create_task(self._consume())

    async def stop(self) -> None:
        if self._worker_task:
            self._worker_task.cancel()
            await asyncio.gather(self._worker_task, return_exceptions=True)
            self._worker_task = None

    async def enqueue(self, name: str, payload: dict[str, Any]) -> None:
        await self._queue.put(Job(name, payload, datetime.now(timezone.utc)))

    async def _consume(self) -> None:
        while True:
            job = await self._queue.get()
            try:
                handler = self._handlers.get(job.name)
                if handler:
                    await handler(job.payload)
                else:
                    logger.warning("No handler registered for job %s", job.name)
            except Exception:
                logger.exception("Background job failed: %s", job.name)
            finally:
                self._queue.task_done()


job_queue = InProcessJobQueue()
