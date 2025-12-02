import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Ensure project root is on path when running tests directly
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.main import app, notes_db


@pytest.fixture(autouse=True)
def reset_notes_db():
    original = [note.copy() for note in notes_db]
    yield
    notes_db[:] = original


client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_list_notes():
    resp = client.get("/notes")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) == len(notes_db)
    assert data[0]["id"] == notes_db[0]["id"]


def test_get_note_success():
    resp = client.get("/notes/1")
    assert resp.status_code == 200
    assert resp.json()["title"] == notes_db[0]["title"]


def test_get_note_not_found():
    resp = client.get("/notes/999")
    assert resp.status_code == 404


def test_create_note():
    payload = {"title": "New note", "content": "Created in test"}
    resp = client.post("/notes", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == payload["title"]
    assert data["content"] == payload["content"]
    assert any(n["id"] == data["id"] for n in notes_db)


def test_create_note_missing_field():
    resp = client.post("/notes", json={"title": "Missing content"})
    assert resp.status_code == 422


def test_update_note():
    payload = {"title": "Updated", "content": "Updated content"}
    resp = client.put("/notes/1", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == payload["title"]
    assert data["content"] == payload["content"]


def test_update_note_not_found():
    resp = client.put("/notes/999", json={"title": "x"})
    assert resp.status_code == 404


def test_delete_note():
    resp = client.delete("/notes/1")
    assert resp.status_code == 204
    assert all(n["id"] != 1 for n in notes_db)


def test_delete_note_not_found():
    resp = client.delete("/notes/999")
    assert resp.status_code == 404
