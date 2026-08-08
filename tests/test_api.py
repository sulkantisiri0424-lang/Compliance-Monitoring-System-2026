from fastapi.testclient import TestClient

from backend.app import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "active"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_regulations():
    response = client.get("/regulations")

    assert response.status_code == 200
    assert "regulations" in response.json()


def test_transaction_monitoring():
    response = client.post(
        "/monitor/transaction",
        json={
            "transaction_id": "TXN001",
            "amount": 25000,
            "type": "financial"
        }
    )

    assert response.status_code == 200
    assert "risk_level" in response.json()


def test_communication_monitoring():
    response = client.post(
        "/monitor/communication",
        json={
            "message": "Please review this transaction."
        }
    )

    assert response.status_code == 200
    assert "risk_level" in response.json()


def test_report_generation():
    response = client.post(
        "/report",
        json={
            "title": "Test Compliance Report",
            "risk_level": "LOW",
            "findings": []
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Test Compliance Report"


def test_audit_logs():
    response = client.get("/audit")

    assert response.status_code == 200
    assert "audit_logs" in response.json()
