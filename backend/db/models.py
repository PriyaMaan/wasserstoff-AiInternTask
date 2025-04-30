# backend/db/models.py  

from sqlalchemy import Column, Integer, String  
from .base import Base  # Make sure this import is correct  

class Guess(Base):  
    __tablename__ = "guesses"  

    id = Column(Integer, primary_key=True, index=True)  
    guess = Column(String, index=True)  
    seed_word = Column(String)  

# Other models can be added similarly  