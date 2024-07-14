from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")

model = ChatOpenAI(api_key=api_key, model="gpt-4o")

text = """
    안녕? 나는 정한수. 서울에서 태어났고 나이는 28살이야. 만 나이로는 아직 26살이라구. 나는 node.js 백엔드 개발에 관심이 많고 소통을 중요시하는 개발자야.
    개발자로서 소통하는 게 가장 중요하다고 생각해. 그래서 소통을 못하는 사람을 보면 같이 일하기 싫어져.
    대기업보다는 스타트업을 선호하는 편이야. 왜냐하면 다들 열정을 가지고 일을 할 거라고 생각이 돼서 소통도 그만큼 적극적으로 잘 할 거라고 생각하거든.
"""


async def test(a: str):

    input = f"${a}를 요약해줘."

    answer = model.invoke(input)
    res = answer.content
    print("요약 : ")
    print(res)
    return res