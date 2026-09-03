import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.trustedhost import TrustedHostMiddleware
from sqlalchemy import text

from app.config import settings
from app.core.exceptions import HashKartException, hashkart_exception_handler
from app.core.middleware import RequestLoggingMiddleware
from app.core.observability import MetricsMiddleware, metrics_snapshot
from app.core.rate_limiter import RateLimitMiddleware
from app.core.telemetry import PrometheusTelemetryMiddleware, metrics_collector
from app.database import async_engine, init_db
from app.api.v1.router import api_router
from app.services.cache_service import cache
from app.services.job_service import job_queue
from app.services.notification_outbox_service import process_notification_delivery

# Configure application logger
logging.basicConfig(
    level=settings.LOG_LEVEL.upper(),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("hashkart.main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown lifecycle context manager."""
    logger.info(f"Starting {settings.APP_NAME} backend in {settings.APP_ENV} mode...")
    await init_db()
    if settings.REDIS_URL:
        await cache.connect()
    job_queue.register("notification.delivery", process_notification_delivery)
    await job_queue.start()
    yield
    await job_queue.stop()
    await cache.close()
    logger.info(f"Shutting down {settings.APP_NAME} backend...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Production-Grade HashKart Indian E-Commerce Marketplace API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan,
)

# Custom Middleware
app.add_middleware(RequestLoggingMiddleware)
app.add_middleware(MetricsMiddleware)
app.add_middleware(PrometheusTelemetryMiddleware)
app.add_middleware(RateLimitMiddleware)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.TRUSTED_HOSTS)

# CORS Configuration
if settings.CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Register Custom Exception Handlers
app.add_exception_handler(HashKartException, hashkart_exception_handler)


@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health"])
async def health_check():
    """Healthcheck endpoint for container orchestration and uptime monitors."""
    return {
        "status": "healthy",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "version": settings.VERSION,
    }


@app.get("/ready", status_code=status.HTTP_200_OK, tags=["Health"])
async def readiness_check():
    """Verify that the application can reach its database."""
    try:
        async with async_engine.connect() as connection:
            await connection.execute(text("SELECT 1"))
    except Exception:
        logger.exception("Readiness check failed")
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "not_ready", "dependency": "database"},
        )

    return {"status": "ready", "app_name": settings.APP_NAME, "version": settings.VERSION}


@app.get("/metrics", status_code=status.HTTP_200_OK, tags=["Health"])
async def metrics():
    """Expose Prometheus-format metrics for Grafana / Datadog scraping."""
    output = metrics_collector.generate_prometheus_output()
    return Response(content=output, media_type="text/plain; version=0.0.4")


# Include API v1 Router
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.PORT, reload=settings.DEBUG)
