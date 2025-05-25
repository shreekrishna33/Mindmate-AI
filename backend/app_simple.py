from fastapi import FastAPI
from fastapi.responses import JSONResponse 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    user_input = request.message
    # Simple mock response without loading models
    return {
        "response": f"You said: {user_input}. This is a test response from the simplified backend.",
        "sentiment": "POSITIVE",
        "confidence": 0.95
    }

@app.get("/")
def root():
    return {"message": "Mental Health Chatbot Backend is running (simplified version)."}