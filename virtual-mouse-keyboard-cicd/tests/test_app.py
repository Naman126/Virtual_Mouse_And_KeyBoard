import app


def test_home_page_is_available():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Virtual Mouse" in response.data


def test_health_endpoint():
    client = app.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"
