import asyncio
from datetime import UTC, datetime
import httpx
from app.providers.base import FlightDataProvider, ProviderError, ProviderRateLimitError
from app.schemas.aircraft import AircraftState

class OpenSkyProvider(FlightDataProvider):
    base_url="https://opensky-network.org/api"
    def __init__(self,client_id:str|None=None,client_secret:str|None=None): self.auth=(client_id,client_secret) if client_id and client_secret else None
    @staticmethod
    def normalize(raw:list[object]) -> AircraftState:
        def val(index:int): return raw[index] if len(raw)>index else None
        return AircraftState(icao24=str(val(0)),callsign=(str(val(1)).strip() or None) if val(1) is not None else None,country=str(val(2) or "Unknown"),longitude=float(val(5)) if val(5) is not None else None,latitude=float(val(6)) if val(6) is not None else None,altitude=float(val(13) if val(13) is not None else val(7)) if (val(13) is not None or val(7) is not None) else None,on_ground=bool(val(8)),velocity=float(val(9)) if val(9) is not None else None,heading=float(val(10)) if val(10) is not None else None,vertical_rate=float(val(11)) if val(11) is not None else None,last_seen=datetime.fromtimestamp(int(val(4) or 0),tz=UTC),squawk=str(val(14)) if val(14) else None)
    async def _request(self,params:dict[str,str|float]) -> dict[str,object]:
        for attempt in range(3):
            async with httpx.AsyncClient(timeout=12) as client:
                response=await client.get(f"{self.base_url}/states/all",params=params,auth=self.auth)
            if response.status_code==429:
                if attempt==2: raise ProviderRateLimitError("OpenSky rate limit reached")
                await asyncio.sleep(2**attempt);continue
            if response.is_error: raise ProviderError(f"OpenSky returned HTTP {response.status_code}")
            return response.json()
        raise ProviderError("OpenSky unavailable")
    async def get_live_aircraft(self,bounds:tuple[float,float,float,float]|None=None)->list[AircraftState]:
        params:dict[str,str|float]={}
        if bounds: params.update(zip(("lamin","lomin","lamax","lomax"),bounds,strict=True))
        data=await self._request(params);states=data.get("states") or []
        return [self.normalize(item) for item in states if isinstance(item,list)]
    async def get_aircraft(self,icao24:str)->AircraftState|None:
        data=await self._request({"icao24":icao24});states=data.get("states") or []
        return self.normalize(states[0]) if states else None
