from fastapi import FastAPI
from backend.ai_engine import generate_story

app = FastAPI(
    title="Nasty AI Studio",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "status": "online",
        "project": "Nasty AI Studio"
    }

@app.get("/generate_episode")
def generate_episode():

    prompt = """
Create one original viral YouTube Shorts episode.

Use only:

Banana Boss
Shark Bro
Potato Legend
Coffee Queen
Wooden Guy

Exactly 5 scenes.

Funny.

Family Friendly.

Strong cliffhanger.
"""

    story = generate_story(prompt)

    return {
        "episode": story
    }
