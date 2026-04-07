from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Backend Running 🚀"}

@app.get("/ai")
def ai_response(q: str):
    return {"response": f"AI says: {q}"}
