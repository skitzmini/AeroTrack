from datetime import UTC,datetime
from app.providers.base import FlightDataProvider
from app.schemas.aircraft import AircraftResponse
from app.services.cache import TTLCache
class FlightService:
    def __init__(self,provider:FlightDataProvider,source:str,ttl:int=10):self.provider=provider;self.source=source;self.cache=TTLCache[list](ttl)
    async def live(self,bounds=None)->AircraftResponse:
        key="all" if bounds is None else ":".join(f"{v:.2f}" for v in bounds)
        aircraft=await self.cache.get_or_set(key,lambda:self.provider.get_live_aircraft(bounds))
        return AircraftResponse(aircraft=aircraft,count=len(aircraft),source=self.source,fetched_at=datetime.now(UTC))
    async def one(self,icao24:str)->AircraftResponse:
        value=await self.provider.get_aircraft(icao24.lower());items=[value] if value else []
        return AircraftResponse(aircraft=items,count=len(items),source=self.source,fetched_at=datetime.now(UTC))
