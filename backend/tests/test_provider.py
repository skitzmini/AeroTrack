from app.providers.opensky import OpenSkyProvider
def test_opensky_normalization():
    raw=['abc123',' TEST1 ','Brazil',0,1700000000,-46.6,-23.5,10000,False,200,90,1.5,None,9800,'2000',False,0]
    item=OpenSkyProvider.normalize(raw)
    assert item.icao24=='abc123' and item.callsign=='TEST1' and item.altitude==9800 and item.longitude==-46.6
