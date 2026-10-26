"""Tests for FastAPI application creation."""

from fastapi.testclient import TestClient

from src.config import Settings
from src.main import create_app


def test_app_uses_only_configured_cors_origins(tmp_path) -> None:
    settings = Settings(
        _env_file=None,
        secret_key="s" * 32,
        cors_allowed_origins=["https://learn.example"],
        database_url=f"sqlite:///{tmp_path / 'not-created.db'}",
    )
    client = TestClient(create_app(settings))

    allowed_response = client.options(
        "/api/v1/test",
        headers={
            "Origin": "https://learn.example",
            "Access-Control-Request-Method": "GET",
        },
    )
    blocked_response = client.options(
        "/api/v1/test",
        headers={
            "Origin": "https://other.example",
            "Access-Control-Request-Method": "GET",
        },
    )

    assert allowed_response.status_code == 200
    assert allowed_response.headers["access-control-allow-origin"] == "https://learn.example"
    assert blocked_response.status_code == 400
    assert not (tmp_path / "not-created.db").exists()
    assert not any(route.path.startswith("/api/v1") for route in client.app.routes)
