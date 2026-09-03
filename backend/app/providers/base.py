from abc import ABC, abstractmethod
from app.schemas.aircraft import AircraftState

class ProviderError(Exception): pass
class ProviderRateLimitError(ProviderError): pass
class FlightDataProvider(ABC):
    @abstractmethod
    async def get_live_aircraft(self, bounds: tuple[float,float,float,float] | None = None) -> list[AircraftState]: ...
    @abstractmethod
    async def get_aircraft(self, icao24: str) -> AircraftState | None: ...
    async def get_flight(self, flight_id: str) -> AircraftState | None: return await self.get_aircraft(flight_id)
    async def get_aircraft_in_bounds(self, lamin:float,lomin:float,lamax:float,lomax:float)->list[AircraftState]: return await self.get_live_aircraft((lamin,lomin,lamax,lomax))
