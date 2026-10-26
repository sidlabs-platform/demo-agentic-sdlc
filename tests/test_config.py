"""Tests for environment-backed application settings."""

import pytest
from pydantic import ValidationError

from src.config import Settings


def test_settings_defaults_without_optional_ai_configuration() -> None:
    settings = Settings(_env_file=None, secret_key="s" * 32)

    assert settings.database_url == "sqlite:///learning.db"
    assert settings.cors_allowed_origins == []
    assert settings.access_token_expire_minutes == 60
    assert settings.github_models_api_key is None
    assert settings.github_models_endpoint is None
    assert settings.ai_model_name == "gpt-4o"
    assert settings.ai_max_retries == 3


def test_settings_load_environment_overrides(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SECRET_KEY", "e" * 40)
    monkeypatch.setenv("DATABASE_URL", "sqlite:///custom.db")
    monkeypatch.setenv("CORS_ALLOWED_ORIGINS", '["https://learn.example"]')
    monkeypatch.setenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
    monkeypatch.setenv("GITHUB_MODELS_API_KEY", "test-api-key")

    settings = Settings(_env_file=None)

    assert settings.database_url == "sqlite:///custom.db"
    assert settings.cors_allowed_origins == ["https://learn.example"]
    assert settings.access_token_expire_minutes == 30
    assert settings.github_models_api_key.get_secret_value() == "test-api-key"


@pytest.mark.parametrize(
    "settings",
    [
        {"secret_key": "too-short"},
        {"secret_key": "s" * 32, "access_token_expire_minutes": 0},
        {"secret_key": "s" * 32, "cors_allowed_origins": ["*"]},
        {"secret_key": "s" * 32, "cors_allowed_origins": ["https://learn.example:0"]},
        {
            "secret_key": "s" * 32,
            "cors_allowed_origins": ["https://learn.example/path"],
        },
    ],
)
def test_settings_reject_malformed_values(settings: dict[str, object]) -> None:
    with pytest.raises(ValidationError):
        Settings(_env_file=None, **settings)
