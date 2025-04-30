import httpx  
import os  

async def ask_ai(guess: str, seed_word: str) -> bool:  
    url = os.getenv("AI_ENDPOINT")  
    headers = {"Authorization": f"Bearer {os.getenv('AI_API_KEY')}"}  
    data = {"prompt": f"Does '{guess}' beat '{seed_word}'?", "max_tokens": 5}  
    
    async with httpx.AsyncClient() as client:  
        response = await client.post(url, headers=headers, json=data)  
        
    response.raise_for_status()  
    result = response.json()  
    return "YES" in result['choices'][0]['text'].strip().upper()  