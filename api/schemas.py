from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    question: str
    department: str | None = None

class ChatResponse(BaseModel):
    answer: str

