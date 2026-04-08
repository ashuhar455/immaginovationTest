from fastapi import FastAPI, HTTPException
from api.v1 import chat

app = FastAPI()

app.include_router(router=chat.router, prefix="/api/v1")

