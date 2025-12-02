from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini"
)
x = model.invoke("What is your name?")
print(x.content)
