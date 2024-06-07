from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_note():
    response = client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Note"

def test_read_note():
    response = client.post("/notes/", json={"title": "Test Note", "content": "This is a test note."})
    note_id = response.json()["id"]
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Note"
