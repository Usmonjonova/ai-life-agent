from fastapi import FastAPI

from app.db.database import init_db


app = FastAPI(title="AI Life Agent")


init_db()


@app.get("/")
def root():
    return {
        "message": "AI Life Agent is running!"
    }