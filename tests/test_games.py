import requests


BASE_URL = "http://localhost:8000"


def test_crud_flow():
    # Create
    r = requests.post(f"{BASE_URL}/games", json={"title": "Zelda", "status": "to_play"})
    assert r.status_code == 200
    game = r.json()
    game_id = game["id"]


    # Read
    r = requests.get(f"{BASE_URL}/games/{game_id}")
    assert r.status_code == 200
    assert r.json()["title"] == "Zelda"


    # Update
    r = requests.put(f"{BASE_URL}/games/{game_id}", json={"status": "playing"})
    assert r.status_code == 200
    assert r.json()["status"] == "playing"


    # Delete
    r = requests.delete(f"{BASE_URL}/games/{game_id}")
    assert r.status_code == 200
    assert r.json()["ok"] is True