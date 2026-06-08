from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from ai import ask_ai
from data import transactions, dashboard_summary

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://dabar-demo.vercel.app",
        # Uncomment for local development:
        # "http://localhost:3000",
        # "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AIChatRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {"message": "DABAR Demo API Running"}


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