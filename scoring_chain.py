from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.templates import scoring_prompt
from dotenv import load_dotenv
import os

load_dotenv()

# 🔥 Gemini LLM (same fix as extraction chain)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# 🔗 Chain: Prompt + Gemini
scoring_chain = scoring_prompt | llm