import requests

def test_duplicate_guess():
    seed_word = "Rock"
    guess = "Paper"
    
    # First guess
    response = requests.post("http://localhost:8000/game/guess", json={"seed_word": seed_word, "user_guess": guess})
    assert response.json()['status'] == 'success'

    # Duplicate guess
    response = requests.post("http://localhost:8000/game/guess", json={"seed_word": seed_word, "user_guess": guess})
    assert response.json()['status'] == 'game_over'