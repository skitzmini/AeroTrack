from sqlalchemy import or_,select
from sqlalchemy.orm import Session
from app.models.aviation import Airport,FlightHistory,FlightPosition
class HistoryRepository:
    def __init__(self,db:Session):self.db=db
    def list(self,limit:int=100):return list(self.db.scalars(select(FlightHistory).order_by(FlightHistory.first_seen.desc()).limit(limit)))
    def get(self,item_id:int):return self.db.get(FlightHistory,item_id)
    def positions(self,item_id:int):return list(self.db.scalars(select(FlightPosition).where(FlightPosition.flight_history_id==item_id).order_by(FlightPosition.recorded_at)))
class AirportRepository:
    def __init__(self,db:Session):self.db=db
    def search(self,q:str,limit:int=20):
        value=f"%{q}%";return list(self.db.scalars(select(Airport).where(or_(Airport.iata.ilike(value),Airport.icao.ilike(value),Airport.name.ilike(value),Airport.city.ilike(value))).limit(limit)))
