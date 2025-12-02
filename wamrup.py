import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")

if not api_key:
	raise ValueError("API KEY not found")

llm = ChatOpenAI(
	# model='gpt-4o-mini'
)

prompt = llm.invoke("What is the time in connecticut right now")

print(prompt.content)