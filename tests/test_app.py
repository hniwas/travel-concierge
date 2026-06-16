"""Tests for the Travel Concierge Flask application."""

import pytest
from app import app, DESTINATIONS, TRAVEL_TIPS, PACKING_LISTS


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ===== Route tests =====

def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Travel Concierge" in response.data


def test_home_shows_all_destinations(client):
    response = client.get("/")
    for dest in DESTINATIONS:
        assert dest["name"].encode() in response.data


def test_destination_valid_id(client):
    response = client.get("/destination/1")
    assert response.status_code == 200
    assert b"Paris" in response.data


def test_destination_invalid_id_returns_404(client):
    response = client.get("/destination/9999")
    assert response.status_code == 404


def test_planner_returns_200(client):
    response = client.get("/planner")
    assert response.status_code == 200
    assert b"Trip Planner" in response.data


# ===== API tests =====

def test_api_destinations_returns_all(client):
    response = client.get("/api/destinations")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == len(DESTINATIONS)


def test_api_destinations_search(client):
    response = client.get("/api/destinations?q=paris")
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "Paris, France"


def test_api_destinations_search_no_match(client):
    response = client.get("/api/destinations?q=zzznomatch")
    data = response.get_json()
    assert data == []


def test_api_destinations_filter_by_tag(client):
    response = client.get("/api/destinations?tag=beach")
    data = response.get_json()
    assert all("beach" in d["tags"] for d in data)
    assert len(data) > 0


def test_api_tips_returns_list(client):
    response = client.get("/api/tips")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == len(TRAVEL_TIPS)


# ===== Data integrity tests =====

def test_all_destinations_have_required_fields():
    required = {"id", "name", "emoji", "description", "best_time", "currency", "language", "highlights", "budget_per_day", "tags"}
    for dest in DESTINATIONS:
        assert required.issubset(dest.keys()), f"Missing fields in destination: {dest.get('name')}"


def test_destination_ids_are_unique():
    ids = [d["id"] for d in DESTINATIONS]
    assert len(ids) == len(set(ids))


def test_packing_list_generated_for_destination(client):
    # Bali is tagged beach + relaxation + culture + adventure
    response = client.get("/destination/4")
    assert response.status_code == 200
    # At least one beach packing item should appear
    assert b"Sunscreen" in response.data or b"Swimsuit" in response.data
