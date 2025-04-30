import pytest  
from fastapi.testclient import TestClient  
from backend.main import app  

client = TestClient(app)  

def test_duplicate_guess():  
    response = client.post("/start/Rock")  
    assert response.status_code == 200  
    
    response = client.post("/guess/Rock/Paper")  
    assert response.status_code == 200  
    
    response = client.post("/guess/Rock/Paper")  # Duplicate guess  
    assert response.status_code == 400  # Expect game over  