from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    question: str
    user_id: str

class AIResponse(BaseModel):
    routine: List[str]
    products: List[str]
    warnings: List[str]
    message: str
