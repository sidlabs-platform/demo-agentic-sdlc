"""FastAPI application factory and default application instance."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import Settings


def create_app(settings: Settings | None = None) -> FastAPI:
    """Create the application with environment-backed settings and shared middleware."""
    settings = settings or Settings()
    application = FastAPI(title="Agentic SDLC Learning Platform")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return application


app = create_app()
