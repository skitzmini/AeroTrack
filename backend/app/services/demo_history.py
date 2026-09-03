from datetime import UTC,datetime,timedelta

NOW=datetime.now(UTC)
DEMO_HISTORY=[{
    'id':1,'icao24':'e49f80','callsign':'AZU4412','flight_number':None,
    'aircraft_registration':None,'aircraft_type':None,'origin_airport':None,
    'destination_airport':None,'departure_time':None,'arrival_time':None,
    'first_seen':NOW-timedelta(minutes=38),'last_seen':NOW,'max_altitude':10668.0,
    'average_speed':226.0,'status':'demo','created_at':NOW,'updated_at':NOW,
}]
DEMO_POSITIONS=[{
    'id':index+1,'flight_history_id':1,'latitude':-25.4+(index*.25),
    'longitude':-49.1+(index*.27),'altitude':7000+(index*330),
    'speed':205+(index*2),'heading':42.0,'vertical_rate':1.2,
    'recorded_at':NOW-timedelta(minutes=(11-index)*3),
} for index in range(12)]
