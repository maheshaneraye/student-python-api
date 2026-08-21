from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["service"] == "student-python-api"

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_say_hello():
    response = client.get("/api/hello/Alice")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, Alice!"


