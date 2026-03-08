from app import app
import json


def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Bienvenue sur l'API Secure Task" in response.get_data(as_text=True)


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_add_task():
    client = app.test_client()
    payload = {"title": "Écrire des tests"}
    response = client.post(
        "/tasks",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 201
    assert response.get_json()["title"] == "Écrire des tests"


def test_add_task_without_title():
    client = app.test_client()
    payload = {}
    response = client.post(
        "/tasks",
        data=json.dumps(payload),
        content_type="application/json"
    )
    assert response.status_code == 400