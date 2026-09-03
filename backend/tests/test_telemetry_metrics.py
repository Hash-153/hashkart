import pytest
from app.core.telemetry import metrics_collector


def test_prometheus_metrics_generation():
    """Verify Prometheus-format telemetry output generation."""
    metrics_collector.record_request("GET", "/api/v1/catalog/products", 200, 0.045)
    metrics_collector.record_request("POST", "/api/v1/checkout/process", 201, 0.120)

    output = metrics_collector.generate_prometheus_output()
    assert "novamart_http_requests_total" in output
    assert 'endpoint="/api/v1/catalog/products"' in output
    assert 'endpoint="/api/v1/checkout/process"' in output
    assert "novamart_uptime_seconds" in output
