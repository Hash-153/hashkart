from fastapi import APIRouter, Response
from app.core.telemetry import metrics_collector

router = APIRouter()


@router.get("/metrics")
async def get_prometheus_metrics():
    """Prometheus-compatible plain text metrics scraping endpoint."""
    output = metrics_collector.generate_prometheus_output()
    return Response(content=output, media_type="text/plain; version=0.0.4")
