from fastapi import FastAPI

app = FastAPI(title="AI Life Agent")


@app.get("/")
def root():
    return {
        "message": "AI Life Agent is running!"
    }