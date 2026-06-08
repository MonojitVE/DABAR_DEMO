from fastapi import FastAPI
from pydantic import BaseModel
from ai import ask_ai
from data import transactions, dashboard_summary
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["https://dabar-demo.vercel.app/"], # For demo purposes
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

class AIChatRequest(BaseModel):
    question: str

@app.post("/login")
def login():
    return {"status": "success"}

@app.get("/dashboard")
def dashboard():
    return dashboard_summary()

@app.get("/transactions")
def get_transactions():
    return transactions

@app.post("/ai-chat")
def ai_chat(payload: AIChatRequest):
    return {"answer": ask_ai(payload.question)}