from fastapi import APIRouter,Depends,HTTPException,Query
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.repositories.history import AirportRepository,HistoryRepository
from app.schemas.history import AirportRead,FlightHistoryRead,FlightPositionRead
from app.core.config import get_settings
from app.services.demo_history import DEMO_HISTORY,DEMO_POSITIONS
from app.services.demo_airports import search_major_airports
router=APIRouter()
@router.get('/history',response_model=list[FlightHistoryRead],response_model_by_alias=True)
def history(limit:int=Query(100,ge=1,le=500),db:Session=Depends(get_db)):
    if get_settings().demo_mode:return DEMO_HISTORY[:limit]
    try:return HistoryRepository(db).list(limit)
    except SQLAlchemyError: return []
@router.get('/history/{item_id}',response_model=FlightHistoryRead,response_model_by_alias=True)
def history_item(item_id:int,db:Session=Depends(get_db)):
    if get_settings().demo_mode:
        item=next((value for value in DEMO_HISTORY if value['id']==item_id),None)
        if not item:raise HTTPException(404,'Flight history not found')
        return item
    item=HistoryRepository(db).get(item_id)
    if not item:raise HTTPException(404,'Flight history not found')
    return item
@router.get('/history/{item_id}/positions',response_model=list[FlightPositionRead],response_model_by_alias=True)
def positions(item_id:int,db:Session=Depends(get_db)):
    if get_settings().demo_mode:return [value for value in DEMO_POSITIONS if value['flight_history_id']==item_id]
    return HistoryRepository(db).positions(item_id)
@router.get('/airports/search',response_model=list[AirportRead])
def airports(q:str=Query('',max_length=80),db:Session=Depends(get_db)):
    if get_settings().demo_mode:return search_major_airports(q)
    try:return AirportRepository(db).search(q)
    except SQLAlchemyError:return []
