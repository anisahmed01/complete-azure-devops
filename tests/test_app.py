from app.app import app


def test_homepage_renders_portfolio():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.content_type.startswith("text/html")
    assert b"DevOps Engineer" in response.data
    assert b"Jenkins CI/CD Automation" in response.data
    assert b"Azure Container Deployment" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}