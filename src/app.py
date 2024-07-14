from fastapi import FastAPI
from src.routers.chat import chat_router

app = FastAPI(docs_url="/api-docs")

app.include_router(chat_router)


