# backend/database.py
import os
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Create a MongoDB client
client = AsyncIOMotorClient(DATABASE_URL)
database = client.get_default_database()  # This will use the database specified in the connection string