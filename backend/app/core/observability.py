import time
from collections import Counter
from threading import Lock

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

_metrics = Counter()
_metrics_lock = Lock()


class MetricsMiddleware(BaseHTTPMiddleware):
    """Collect low-cardinality request counters without external infrastructure."""

    async def dispatch(self, request: Request, call_next):
        started = time.perf_counter()
        response = await call_next(request)
        duration_ms = (time.perf_counter() - started) * 1000
        route = request.url.path.split("/")[:4]
        route_key = "/".join(route) or "/"
        with _metrics_lock:
            _metrics["http_requests_total"] += 1
            _metrics[f"http_status_{response.status_code}_total"] += 1
            _metrics["http_request_duration_ms_total"] += round(duration_ms, 2)
            _metrics[f"http_route_{route_key}_total"] += 1
        return response


def metrics_snapshot() -> dict[str, int | float]:
    with _metrics_lock:
        return dict(_metrics)
