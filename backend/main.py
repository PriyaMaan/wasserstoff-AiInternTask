from fastapi import FastAPI  
from api.routes import router  
from db.models import init_db  

app = FastAPI()  

@app.on_event("startup")  
async def startup():  
    await init_db()  

app.include_router(router)  