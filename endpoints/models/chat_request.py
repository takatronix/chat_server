from pydantic import BaseModel


class ChatRequest(BaseModel):
    profile_name: str
    question: str
    session_name: str = None
