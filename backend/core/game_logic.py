from collections import deque  
from fastapi import HTTPException  

class GuessingGame:  
    def __init__(self, seed_word: str):  
        self.seed_word = seed_word  
        self.guesses = deque()  # This will store the player's guesses  
        self.user_score = 0  

    def make_guess(self, guess: str):  
        if guess in self.guesses:  
            raise HTTPException(status_code=400, detail="Game Over. You've already guessed that!")  
        # Logic to check if guess beats seed_word with AI client here  
        # If correct  
        self.guesses.append(guess)  
        self.user_score += 1  
        return f"✅ Nice! {guess} beats {self.seed_word}. You've guessed {len(self.guesses)} times."  

    def get_history(self):  
        return list(self.guesses)  

# Example to show how to use this class  
# game = GuessingGame("Rock")  
# print(game.make_guess("Paper"))  