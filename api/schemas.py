from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str
    department: str | None = None

class ChatResponse(BaseModel):
    answer: str

