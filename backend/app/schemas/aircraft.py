from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class AircraftState(BaseModel):
    icao24: str
    callsign: str | None = None
    country: str
    latitude: float | None = None
    longitude: float | None = None
    altitude: float | None = None
    velocity: float | None = None
    heading: float | None = None
    vertical_rate: float | None = Field(default=None, serialization_alias="verticalRate")
    on_ground: bool = Field(serialization_alias="onGround")
    last_seen: datetime = Field(serialization_alias="lastSeen")
    squawk: str | None = None
    registration: str | None = None
    aircraft_type: str | None = Field(default=None, serialization_alias="aircraftType")
    origin_airport: str | None = Field(default=None, serialization_alias="originAirport")
    destination_airport: str | None = Field(default=None, serialization_alias="destinationAirport")
    flight_number: str | None = Field(default=None, serialization_alias="flightNumber")
    airline: str | None = None
    origin_airport_name: str | None = Field(default=None, serialization_alias="originAirportName")
    destination_airport_name: str | None = Field(default=None, serialization_alias="destinationAirportName")
    origin_latitude: float | None = Field(default=None, serialization_alias="originLatitude")
    origin_longitude: float | None = Field(default=None, serialization_alias="originLongitude")
    destination_latitude: float | None = Field(default=None, serialization_alias="destinationLatitude")
    destination_longitude: float | None = Field(default=None, serialization_alias="destinationLongitude")
    estimated_duration_minutes: int | None = Field(default=None, serialization_alias="estimatedDurationMinutes")
    photo_url: str | None = Field(default=None, serialization_alias="photoUrl")
    model_config = ConfigDict(populate_by_name=True)

class AircraftResponse(BaseModel):
    aircraft: list[AircraftState]
    count: int
    source: str
    fetched_at: datetime = Field(serialization_alias="fetchedAt")
    stale: bool = False
    model_config = ConfigDict(populate_by_name=True)
