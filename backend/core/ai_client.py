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
import httpx
import os
import logging

logger = logging.getLogger(__name__)

async def ask_ai(guess: str, seed_word: str) -> bool:
    try:
        url = os.getenv("AI_ENDPOINT")
        if not url:
            raise ValueError("AI_ENDPOINT environment variable is not set")

        headers = {"Authorization": f"Bearer {os.getenv('AI_API_KEY')}"}
        if not headers["Authorization"]:
            raise ValueError("AI_API_KEY environment variable is not set")

        data = {"prompt": f"Does '{guess}' beat '{seed_word}'?", "max_tokens": 5}

        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, json=data)

        response.raise_for_status()
        result = response.json()
        return "YES" in result['choices'][0]['text'].strip().upper()
    except httpx.HTTPError as e:
        logger.error(f"Failed to make request to AI endpoint: {e}")
        return False
    except KeyError as e:
        logger.error(f"Invalid response from AI endpoint: {e}")
        return False
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return False