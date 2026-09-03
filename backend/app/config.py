from typing import List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "HashKart Marketplace API"
    APP_NAME: str = "HashKart"
    APP_ENV: str = "development"
    DEBUG: bool = False
    PORT: int = 8000
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Database Settings
    DATABASE_URL: str = "sqlite+aiosqlite:///./hashkart.db"
    DB_ECHO: bool = False

    # Security & Auth Settings
    JWT_SECRET_KEY: str = "HASHKART_SUPER_SECRET_JWT_KEY_DEV_MODE_32BYTES_LONG"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS Settings
    CORS_ORIGINS: List[str] = Field(default_factory=lambda: [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ])
    TRUSTED_HOSTS: List[str] = Field(
        default_factory=lambda: ["localhost", "127.0.0.1", "testserver"]
    )
    LOG_LEVEL: str = "INFO"
    REDIS_URL: str = ""
    AUTO_CREATE_SCHEMA: bool = True
    PAYMENT_WEBHOOK_SECRET: str = ""

    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @field_validator("CORS_ORIGINS", "TRUSTED_HOSTS", mode="before")
    @classmethod
    def split_csv_values(cls, value):
        if isinstance(value, str):
            return [item.strip() for item in value.split(",") if item.strip()]
        return value

    def validate_runtime_security(self) -> None:
        if self.APP_ENV.lower() in {"production", "prod"}:
            if self.DEBUG:
                raise ValueError("DEBUG must be false in production")
            insecure_markers = ("dev", "development", "change", "replace", "local")
            if (
                self.JWT_SECRET_KEY == "HASHKART_SUPER_SECRET_JWT_KEY_DEV_MODE_32BYTES_LONG"
                or any(marker in self.JWT_SECRET_KEY.lower() for marker in insecure_markers)
            ):
                raise ValueError("JWT_SECRET_KEY must be set to a unique value in production")
            if len(self.JWT_SECRET_KEY) < 32:
                raise ValueError("JWT_SECRET_KEY must contain at least 32 characters")


settings = Settings()
settings.validate_runtime_security()
