from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

def alias_config() -> ConfigDict: return ConfigDict(from_attributes=True, populate_by_name=True)
class FlightHistoryRead(BaseModel):
    id:int; icao24:str; callsign:str|None=None
    flight_number:str|None=Field(default=None,serialization_alias="flightNumber")
    aircraft_registration:str|None=Field(default=None,serialization_alias="aircraftRegistration")
    aircraft_type:str|None=Field(default=None,serialization_alias="aircraftType")
    origin_airport:str|None=Field(default=None,serialization_alias="originAirport")
    destination_airport:str|None=Field(default=None,serialization_alias="destinationAirport")
    departure_time:datetime|None=Field(default=None,serialization_alias="departureTime")
    arrival_time:datetime|None=Field(default=None,serialization_alias="arrivalTime")
    first_seen:datetime=Field(serialization_alias="firstSeen");last_seen:datetime=Field(serialization_alias="lastSeen")
    max_altitude:float|None=Field(default=None,serialization_alias="maxAltitude")
    average_speed:float|None=Field(default=None,serialization_alias="averageSpeed")
    status:str;created_at:datetime=Field(serialization_alias="createdAt");updated_at:datetime=Field(serialization_alias="updatedAt")
    model_config=alias_config()
class FlightPositionRead(BaseModel):
    id:int;flight_history_id:int=Field(serialization_alias="flightHistoryId");latitude:float;longitude:float;altitude:float|None=None;speed:float|None=None;heading:float|None=None;vertical_rate:float|None=Field(default=None,serialization_alias="verticalRate");recorded_at:datetime=Field(serialization_alias="recordedAt")
    model_config=alias_config()
class AirportRead(BaseModel):
    id:int;iata:str|None=None;icao:str;name:str;city:str|None=None;country:str;latitude:float;longitude:float
    model_config=alias_config()
