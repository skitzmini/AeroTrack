from fastapi import APIRouter,Depends,HTTPException,Query
from app.api.dependencies import get_flight_service
from app.providers.base import ProviderError,ProviderRateLimitError
from app.schemas.aircraft import AircraftResponse
from app.services.flight import FlightService
router=APIRouter()
async def safe_live(service:FlightService,bounds=None):
    try:return await service.live(bounds)
    except ProviderRateLimitError as exc:raise HTTPException(429,'Flight data temporarily unavailable') from exc
    except ProviderError as exc:raise HTTPException(503,'API temporarily unavailable') from exc
@router.get('/aircraft',response_model=AircraftResponse,response_model_by_alias=True)
async def aircraft(lamin:float|None=Query(None,ge=-90,le=90),lomin:float|None=Query(None,ge=-180,le=180),lamax:float|None=Query(None,ge=-90,le=90),lomax:float|None=Query(None,ge=-180,le=180),service:FlightService=Depends(get_flight_service)):
    supplied=[v is not None for v in (lamin,lomin,lamax,lomax)]
    if any(supplied) and not all(supplied):raise HTTPException(422,'All bounding box coordinates are required')
    bounds=(lamin,lomin,lamax,lomax) if all(supplied) else None
    if bounds and (bounds[0]>=bounds[2] or bounds[1]>=bounds[3]):raise HTTPException(422,'Invalid bounding box')
    return await safe_live(service,bounds)
@router.get('/aircraft/live',response_model=AircraftResponse,response_model_by_alias=True)
async def live(service:FlightService=Depends(get_flight_service)):return await safe_live(service)
@router.get('/aircraft/{icao24}',response_model=AircraftResponse,response_model_by_alias=True)
async def one(icao24:str,service:FlightService=Depends(get_flight_service)):
    try:return await service.one(icao24)
    except ProviderError as exc:raise HTTPException(503,'Aircraft unavailable') from exc
