from fastapi import FastAPI
from typing import Dict
import os
import openai

app = FastAPI(title="My Eidolon AI Project", version="1.0.0")

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
async def root():
    return {
        "message": "Welcome to My Eidolon AI Project!", 
        "status": "running",
        "framework": "Eidolon AI inspired"
    }

@app.post("/translate")
async def translate_text(text: str, target_language: str = "Spanish") -> Dict:
    """Simple translation endpoint"""
    return {
        "original_text": text,
        "target_language": target_language,
        "translation": f"[Translation to {target_language}]: {text}",
        "status": "success"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "project": "Eidolon AI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)