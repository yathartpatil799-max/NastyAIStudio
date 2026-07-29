from fastapi import FastAPI

app = FastAPI(
    title="Nasty AI Studio",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "status": "online",
        "project": "Nasty AI Studio",
        "version": "1.0"
    }
