from fastapi import APIRouter, HTTPException
from api.v1.models import *
from database.rag import retrieve_relevant_context
from services.llm import generate_response
import json





router = APIRouter(prefix="/chat", tags=["chat"])




@router.post("/ask", response_model=AIResponse)
def ask_ai(request: QueryRequest):
    try:
        context = retrieve_relevant_context(request.question)
        raw_output = generate_response(request.question, context)
        
        parsed_output = json.loads(raw_output)
        return parsed_output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))