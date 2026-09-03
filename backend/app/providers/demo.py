from datetime import UTC,datetime
from app.providers.base import FlightDataProvider
from app.schemas.aircraft import AircraftState

DEMO=[("e49f80","AZU4412","Brazil",-23.15,-46.72,10668,230,42,2.1),("a1b2c3","UAL860","United States",40.68,-73.75,9754,244,270,-1.4),("4ca123","RYR82Q","Ireland",51.15,-0.18,7620,210,115,4.2),("780abc","CCA818","China",31.20,121.34,11278,252,310,0.1),("3c6444","DLH507","Germany",48.22,11.71,9144,238,75,-2.0),("c01020","ACA091","Canada",43.69,-79.61,3048,178,242,-4.8),("7c6b10","QFA12","Australia",-33.70,151.05,8534,221,190,1.2),("06a0dd","QTR779","Qatar",25.18,51.40,10972,247,305,0.0)]
ROUTES={
 "AZU4412":dict(airline="Azul",aircraft_type="Airbus A320neo",origin_airport="GRU",origin_airport_name="São Paulo/Guarulhos",origin_latitude=-23.4356,origin_longitude=-46.4731,destination_airport="GIG",destination_airport_name="Rio de Janeiro/Galeão",destination_latitude=-22.809,destination_longitude=-43.2506,estimated_duration_minutes=65),
 "UAL860":dict(airline="United Airlines",aircraft_type="Boeing 787-9",origin_airport="IAD",origin_airport_name="Washington Dulles",origin_latitude=38.9531,origin_longitude=-77.4565,destination_airport="GRU",destination_airport_name="São Paulo/Guarulhos",destination_latitude=-23.4356,destination_longitude=-46.4731,estimated_duration_minutes=590),
 "DLH507":dict(airline="Lufthansa",aircraft_type="Airbus A350-900",origin_airport="GRU",origin_airport_name="São Paulo/Guarulhos",origin_latitude=-23.4356,origin_longitude=-46.4731,destination_airport="FRA",destination_airport_name="Frankfurt Airport",destination_latitude=50.0379,destination_longitude=8.5622,estimated_duration_minutes=690),
}
class DemoProvider(FlightDataProvider):
    def _states(self):
        now=datetime.now(UTC);return [AircraftState(icao24=i,callsign=c,country=co,latitude=la,longitude=lo,altitude=al,velocity=ve,heading=he,vertical_rate=vr,on_ground=False,last_seen=now,squawk="2000",flight_number=c,registration="DEMO",photo_url="/images/aircraft-demo.png",**ROUTES.get(c,{})) for i,c,co,la,lo,al,ve,he,vr in DEMO]
    async def get_live_aircraft(self,bounds=None):
        values=self._states()
        if not bounds:return values
        lamin,lomin,lamax,lomax=bounds;return [a for a in values if a.latitude is not None and a.longitude is not None and lamin<=a.latitude<=lamax and lomin<=a.longitude<=lomax]
    async def get_aircraft(self,icao24):return next((a for a in self._states() if a.icao24==icao24.lower()),None)
