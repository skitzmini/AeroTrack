from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AeroTrack API"
    database_url: str = "postgresql+psycopg://aerotrack:aerotrack@localhost:5432/aerotrack"
    opensky_client_id: str | None = None
    opensky_client_secret: str | None = None
    demo_mode: bool = True
    frontend_url: str = "http://localhost:5173"
    cache_ttl_seconds: int = 10
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

@lru_cache
def get_settings() -> Settings:
    return Settings()
