from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_health():
    response=client.get('/api/health');assert response.status_code==200;assert response.json()['status']=='ok'
def test_aircraft_is_normalized():
    response=client.get('/api/aircraft/live');assert response.status_code==200;body=response.json();assert body['source']=='demo';assert isinstance(body['aircraft'],list);assert 'onGround' in body['aircraft'][0]
def test_search():
    response=client.get('/api/flights/search?q=AZU');assert response.status_code==200;assert response.json()['count']==1
