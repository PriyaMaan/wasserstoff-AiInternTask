from pydantic import BaseModel

class GuessInput(BaseModel):
    seed_word: str
    user_guess: str
    session_id: str

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class GuessInput(BaseModel):
    seed_word: str
    user_guess: str
    session_id: str

def does_beat(seed, guess):
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    return rules.get(guess.lower()) == seed.lower()

@router.post("/guess")
async def guess_word(data: GuessInput):
    seed_word = data.seed_word
    user_guess = data.user_guess
    session_id = data.session_id

    if does_beat(seed_word, user_guess):
        result = f"✅ {user_guess} beats {seed_word}!"
        game_over = False
        score = 1
    else:
        result = f"❌ {user_guess} does not beat {seed_word}."
        game_over = True
        score = 0

    return {
        "status": "success",
        "session_id": session_id,
        "seed": seed_word,
        "guess": user_guess,
        "result": result,
        "score": score,
        "game_over": game_over
    }

