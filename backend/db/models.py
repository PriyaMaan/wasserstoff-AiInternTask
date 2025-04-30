# backend/db/models.py
from pydantic import BaseModel
from bson import ObjectId

class GuessCount(BaseModel):
    id: str
    guess: str
    count: int

    class Config:
        json_encoders = {
            ObjectId: str
        }