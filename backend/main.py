
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from backend.detector import analyze_text

app = FastAPI(
    title="TrustCheck AI API",
    description="Multilingual text scam detection system",
    version="2.0.0"
)


class ScanRequest(BaseModel):
    text: str = Field(min_length=1, max_length=10000)
    category: str = "general"


@app.get("/")
def home():
    return {
        "message": "Welcome to TrustCheck AI",
        "status": "Backend is running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/scan")
def scan_message(request: ScanRequest):

    try:
        result = analyze_text(
            request.text,
            request.category
        )

        return result

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
