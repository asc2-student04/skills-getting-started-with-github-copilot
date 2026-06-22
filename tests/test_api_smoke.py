from fastapi.testclient import TestClient

from src.app import app


def test_root_redirects_to_static_index() -> None:
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_activity_dict() -> None:
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get("/activities")
    body = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(body, dict)
    assert "Chess Club" in body
    assert isinstance(body["Chess Club"], dict)
