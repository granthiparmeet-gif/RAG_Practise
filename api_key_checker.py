import os
from dotenv import load_dotenv

load_dotenv()

print("ENV VAR:", os.getenv("OPENAI_API_KEY"))
