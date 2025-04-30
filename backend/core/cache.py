import redis  
import os  

redis_client = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379, db=0)  

def cache_verdict(guess: str, seed_word: str, verdict: bool):  
    key = f"{guess}:{seed_word}"  
    redis_client.set(key, verdict)  

def get_cached_verdict(guess: str, seed_word: str):  
    key = f"{guess}:{seed_word}"  
    return redis_client.get(key)  