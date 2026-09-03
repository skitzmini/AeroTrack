from fastapi import APIRouter,Depends,HTTPException,Query
from app.api.dependencies import get_flight_service
from app.schemas.aircraft import AircraftResponse
from app.services.flight import FlightService
router=APIRouter()
@router.get('/flights/search',response_model=AircraftResponse,response_model_by_alias=True)
async def search(q:str=Query(min_length=2,max_length=30),service:FlightService=Depends(get_flight_service)):
    data=await service.live();term=q.strip().lower();items=[a for a in data.aircraft if term in a.icao24.lower() or term in (a.callsign or '').lower()]
    return AircraftResponse(aircraft=items,count=len(items),source=data.source,fetched_at=data.fetched_at)
@router.get('/flights/{flight_id}',response_model=AircraftResponse,response_model_by_alias=True)
async def flight(flight_id:str,service:FlightService=Depends(get_flight_service)):
    data=await service.one(flight_id)
    if not data.count:raise HTTPException(404,'Flight not found')
    return data
