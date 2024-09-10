from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")

model = ChatOpenAI(api_key=api_key, model="gpt-4o")


async def test(text: str):

    input = f"""이 내용을 바탕으로 타이틀, 요약, 키워드를 생성해 줘. 내용의 핵심을 뽑아서 타이틀로 만들고, 핵심이 되는 키워드 있으면 '#키워드' 형식으로 나타내줘. 

    [내용]
    {text}

    [출력 형식 예시]
    타이틀:

    요약:

    키워드: #000"""
    
    answer = model.invoke(input)
    res = answer.content
    print("요약 : ")
    print(res)
    return res

async def quiz(text: str):

    input = f"""이 내용을 바탕으로 문제와 답안 10개를 생성해 줘. 내용의 핵심을 잘 파악했는지 확인하는 문제들이어야 해. 한 문제에 대한 답은 붙여서 적고, 다른 번호의 문항이 분리되도록 작성해줘. Q에는 질문을 적고 A에는 답안을 적어줘. 질문과 답이 항상 짝을 이뤄야해 

    [내용]
    {text}

    [출력 형식 예시]
    Q1:{{질문}}
    A1:{{답안}}""" 

    answer = model.invoke(input)
    res = answer.content
    print("퀴즈 : ")
    print(res)
    return res