from fastapi import FastAPI, HTTPException
from app.api.v1 import chat

app = FastAPI()

