from functools import lru_cache
from app.core.config import get_settings
from app.providers.demo import DemoProvider
from app.providers.opensky import OpenSkyProvider
from app.services.flight import FlightService
@lru_cache
def get_flight_service()->FlightService:
    s=get_settings();provider=DemoProvider() if s.demo_mode else OpenSkyProvider(s.opensky_client_id,s.opensky_client_secret)
    return FlightService(provider,"demo" if s.demo_mode else "opensky",s.cache_ttl_seconds)
