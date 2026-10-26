"""Application settings loaded from environment variables."""

from typing import Annotated
from urllib.parse import urlsplit

from pydantic import Field, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed configuration for the application."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    secret_key: Annotated[SecretStr, Field(min_length=32)]
    database_url: str = "sqlite:///learning.db"
    cors_allowed_origins: list[str] = Field(default_factory=list)
    access_token_expire_minutes: int = Field(default=60, gt=0)
    github_models_api_key: SecretStr | None = None
    github_models_endpoint: str | None = None
    ai_model_name: str = "gpt-4o"
    ai_max_retries: int = Field(default=3, ge=0)

    @field_validator("cors_allowed_origins")
    @classmethod
    def validate_cors_allowed_origins(cls, origins: list[str]) -> list[str]:
        """Require each configured CORS origin to be an explicit HTTP(S) origin."""
        normalized: list[str] = []
        for origin in origins:
            origin = origin.strip()
            parsed = urlsplit(origin)
            if (
                parsed.scheme not in {"http", "https"}
                or not parsed.hostname
                or parsed.username
                or parsed.password
                or parsed.path not in {"", "/"}
                or parsed.query
                or parsed.fragment
            ):
                raise ValueError("CORS entries must be explicit HTTP(S) origins")
            try:
                port = parsed.port
            except ValueError as exc:
                raise ValueError("CORS origin contains an invalid port") from exc
            if port is not None and not 1 <= port <= 65535:
                raise ValueError("CORS origin contains an invalid port")
            normalized.append(origin.rstrip("/"))
        return normalized
