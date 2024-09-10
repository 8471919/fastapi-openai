from fastapi import APIRouter
from src.services.chat import test, quiz
from pydantic import BaseModel

class Text(BaseModel):
    text: str

router = chat_router = APIRouter()

@router.post("/chat")
async def chat(text: Text) :
    res = await test(text.text)

    return res


@router.post("/quiz")
async def get_quiz(text: Text):
    res = await quiz(text.text)

    return res;