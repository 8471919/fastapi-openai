from fastapi import APIRouter
from src.services.chat import test
from pydantic import BaseModel

class Text(BaseModel):
    text: str

router = chat_router = APIRouter()

@router.post("/chat")
async def chat(text: Text) :
    res = await test(text)

    return res
