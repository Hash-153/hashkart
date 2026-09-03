import time
from collections import defaultdict
from typing import Dict, Tuple
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class MetricsCollector:
    """Thread-safe in-memory Prometheus-compatible metrics aggregator."""
    def __init__(self):
        self.request_count = defaultdict(int)
        self.request_latency_sum = defaultdict(float)
        self.active_connections = 0
        self.db_query_count = 0
        self.start_time = time.time()

    def record_request(self, method: str, path: str, status_code: int, duration_sec: float):
        key = (method, path, str(status_code))
        self.request_count[key] += 1
        self.request_latency_sum[key] += duration_sec

    def generate_prometheus_output(self) -> str:
        lines = [
            "# HELP novamart_http_requests_total Total number of HTTP requests processed",
            "# TYPE novamart_http_requests_total counter",
        ]
        for (method, path, status), count in self.request_count.items():
            lines.append(
                f'novamart_http_requests_total{{method="{method}",endpoint="{path}",status="{status}"}} {count}'
            )

        lines.extend([
            "# HELP novamart_http_request_duration_seconds_total Total duration of HTTP requests in seconds",
            "# TYPE novamart_http_request_duration_seconds_total counter",
        ])
        for (method, path, status), duration in self.request_latency_sum.items():
            lines.append(
                f'novamart_http_request_duration_seconds_total{{method="{method}",endpoint="{path}",status="{status}"}} {duration:.4f}'
            )

        uptime = time.time() - self.start_time
        lines.extend([
            "# HELP novamart_uptime_seconds Total seconds the server has been running",
            "# TYPE novamart_uptime_seconds gauge",
            f"novamart_uptime_seconds {uptime:.2f}",
        ])
        return "\n".join(lines) + "\n"


metrics_collector = MetricsCollector()


class PrometheusTelemetryMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        response = await call_next(request)
        duration = time.perf_counter() - start

        # Normalize path to avoid high-cardinality metrics explosions
        path = request.url.path
        if path.startswith("/api/v1/products/"):
            path = "/api/v1/products/{id}"
        elif path.startswith("/api/v1/orders/"):
            path = "/api/v1/orders/{id}"

        metrics_collector.record_request(
            method=request.method,
            path=path,
            status_code=response.status_code,
            duration_sec=duration,
        )
        return response
