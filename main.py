from fastapi import FastAPI
import os

app = FastAPI()

# ======================
# 🧠 HOME
# ======================
@app.get("/")
def home():
    return {"message": "BlackHoleX AI Brain Running 🚀"}

# ======================
# 🧠 ROUTER LOGIC
# ======================
def ai_router(prompt: str):
    length = len(prompt)

    # Simple intelligent routing logic
    if length < 30:
        return "OpenAI (fast brain selected)"
    elif length < 100:
        return "Mistral (balanced brain selected)"
    else:
        return "Claude (deep reasoning brain selected)"

# ======================
# 🤖 CHAT ENDPOINT
# ======================
@app.get("/chat")
def chat(q: str):
    ai_used = ai_router(q)

    return {
        "input": q,
        "selected_ai": ai_used,
        "response": f"Processed by {ai_used}"
    }