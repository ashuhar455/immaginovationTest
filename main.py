from fastapi import FastAPI, HTTPException
from models import QueryRequest, AIResponse
from rag import retrieve_relevant_context
from llm import generate_response
import json

app = FastAPI()

@app.post("/ask", response_model=AIResponse)
def ask_ai(request: QueryRequest):
    try:
        context = retrieve_relevant_context(request.question)
        raw_output = generate_response(request.question, context)
        parsed_output = json.loads(raw_output)
        return parsed_output
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
