from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from api.schemas import ChatRequest, ChatResponse
from llm.rag import generate_answer

app = FastAPI(
    title="TechCorp RAG API",
    version="1.0.0"
)

# -------------------------
# Warm up DeepSeek on startup
# -------------------------
@app.on_event("startup")
def warm_up_model():
    import requests
    try:
        requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "deepseek-r1:1.5b", "prompt": "warm up", "stream": False}
        )
    except:
        pass


# -------------------------
# Serve frontend
# -------------------------
frontend_path = Path(__file__).resolve().parent.parent / "frontend"

app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# Path to frontend folder (same level as main.py)
frontend_path = Path(__file__).resolve().parent.parent / "frontend"

# Serve static files
app.mount("/static", StaticFiles(directory=frontend_path), name="static")


@app.get("/", response_class=HTMLResponse)
def serve_index():
    index_file = frontend_path / "index.html"
    return index_file.read_text(encoding="utf-8")


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    print(request.question, request.department)
    answer = generate_answer(request.question, request.department)
    return ChatResponse(answer=answer)
