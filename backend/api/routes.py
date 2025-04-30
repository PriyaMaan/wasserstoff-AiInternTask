from fastapi import APIRouter, HTTPException  
from core.ai_client import ask_ai  
from core.game_logic import GuessingGame  

router = APIRouter()  
games = {}  # Store game instances in-memory for simplicity  

@router.post("/start/{seed_word}")  
async def start_game(seed_word: str):  
    game = GuessingGame(seed_word)  
    games[seed_word] = game  
    return {"message": "Game started!", "seed_word": seed_word}  

@router.post("/guess/{seed_word}/{guess}")  
async def make_guess(seed_word: str, guess: str):  
    if seed_word not in games:  
        raise HTTPException(status_code=404, detail="Game not started!")  
    
    game = games[seed_word]  
    valid = await ask_ai(guess, game.seed_word)  
    if valid:  
        return game.make_guess(guess)  
    else:  
        return {"message": "Wrong guess!"}  

@router.get("/history/{seed_word}")  
async def get_history(seed_word: str):  
    if seed_word not in games:  
        raise HTTPException(status_code=404, detail="Game not started!")  
    
    game = games[seed_word]  
    return game.get_history()  