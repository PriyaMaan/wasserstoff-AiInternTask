# backend/core/game_logic.py
import os
import requests
from backend.database import database  # Import the database client
from bson import ObjectId

class GameLogic:
    def __init__(self):
        self.guesses = []
        self.score = 0
        self.ai_api_key = os.getenv("AI_API_KEY")
        self.ai_api_url = os.getenv("AI_API_URL")

    async def process_guess(self, seed_word, user_guess):
        ai_response = await self.check_ai(seed_word, user_guess)
        if ai_response == "YES":
            if user_guess in self.guesses:
                return {"status": "game_over", "message": "Game Over! You've guessed this before."}
            self.guesses.append(user_guess)
            self.score += 1
            await self.update_guess_count(user_guess)
            return {"status": "success", "message": f"Nice! '{user_guess}' beats '{seed_word}'.", "score": self.score}
        return {"status": "failure", "message": "AI says it does not beat."}

    async def update_guess_count(self, guess):
        # Update the guess count in MongoDB
        collection = database["guess_counts"]
        await collection.update_one({"guess": guess}, {"$inc": {"count": 1}}, upsert=True)

    async def check_ai(self, seed_word, user_guess):
        headers = {
            "Authorization": f"Bearer {self.ai_api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": f"Does '{user_guess}' beat '{seed_word}'?",
            "max_tokens": 5
        }
        response = requests.post(self.ai_api_url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            return result.get("choices")[0].get("text").strip()  # Adjust based on actual API response
        return "NO"  # Fallback if the API call fails