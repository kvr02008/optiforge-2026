from fastapi.testclient import TestClient

from api.app import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["name"] == "OptiForge"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "online"


def test_high_cpu_triggers_recovery():
    response = client.post(
        "/analyze",
        json={
            "cpu_usage": 0.95,
            "memory_usage": 0.50,
            "response_time": 0.5,
            "error_rate": 0.02,
            "service_available": True,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "recovered"
    assert data["action"] == "reduce_load"
    assert data["detection"]["anomaly_detected"] is True
    assert data["recovery"]["verified"] is True


def test_service_failure_triggers_restart():
    response = client.post(
        "/analyze",
        json={
            "cpu_usage": 0.40,
            "memory_usage": 0.50,
            "response_time": 0.5,
            "error_rate": 0.02,
            "service_available": False,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "recovered"
    assert data["action"] == "restart_service"
    assert data["recovery"]["verified"] is True