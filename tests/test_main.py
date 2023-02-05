from fastapi.testclient import TestClient

from app.main import HELLO_WORLD, app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == HELLO_WORLD
