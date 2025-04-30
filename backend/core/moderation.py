import re

def is_clean(text):
    profanity = ["badword1", "badword2"]  # Add more
    return not any(word in text.lower() for word in profanity)