import requests

BASE_URL = "http://localhost:8000"

def test_get_nth_prime():
    response = requests.get(f"{BASE_URL}/prime/5")
    assert response.status_code == 200
    assert response.json() == {"nth_prime": 11}

def test_get_nth_fibonacci():
    response = requests.get(f"{BASE_URL}/fibonacci/5")
    assert response.status_code == 200
    assert response.json() == {"nth_fibonacci": 5}

def test_invalid_prime():
    response = requests.get(f"{BASE_URL}/prime/-1")
    assert response.status_code == 400

def test_invalid_fibonacci():
    response = requests.get(f"{BASE_URL}/fibonacci/-1")
    assert response.status_code == 400