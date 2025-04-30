# wasserstoff-AiInternTask
# GenAI Guessing Game

This project is a minimum-viable clone of the "What Beats Rock?" interactive game, built as part of the Wasserstoff Generative AI Internship. It uses FastAPI, Redis, OpenAI's GPT model, and a minimal frontend to demonstrate GenAI integration in backend systems.

---

## 🚀 Features

- OpenAI GPT-3.5-turbo based game validation
- Caching using Redis to prevent redundant API calls
- Linked list-based session memory to track guesses
- Global guess counters persisted in database
- Frontend with confetti-style feedback, emoji responses, and recent guess history
- Dockerized for one-click startup

---

## 🧪 How to Play

1. Run the backend using Docker:
   ```bash
   docker-compose up --build
   ```

2. Open the `frontend/index.html` file in your browser.

3. Type a guess (e.g., "Paper") that you think beats the seed word ("Rock").

4. If your guess is validated by the AI, your score goes up and the guess is added to history. If it's wrong or repeated — game over!

---

## ⚙️ Setup

1. Clone the repo or extract the zip
2. Add your OpenAI key in `.env`:
   ```env
   OPENAI_API_KEY=your_openai_key
   REDIS_URL=redis://localhost
   ```

3. Run with Docker:
   ```bash
   docker-compose up --build
   ```

---

## 🧠 Prompt Design

The prompt used to query OpenAI is:
```
As a {persona} game host, does '{guess}' beat '{seed}'? Reply YES or NO.
```

Two personas (`cheery`, `serious`) are supported via query parameter.

---

## 🏗️ Architecture

- **FastAPI** handles HTTP requests and routes
- **ai_client.py** sends prompts to OpenAI
- **cache.py** uses Redis to store (guess, seed) verdicts
- **game_logic.py** manages sessions using in-memory linked list
- **moderation.py** checks for profanity
- **PostgreSQL/MongoDB** (optional) stores global counters
- **Frontend**: HTML/JS with confetti and guess history display

---

## 🧪 Testing

- An e2e test script is provided in `/tests/e2e_duplicate_test.py`
- It tests duplicate guesses and validates "game over" logic

---

## 📦 Deployment

- Built with Docker
- Runs with:
  ```bash
  docker-compose up --build
  ```


