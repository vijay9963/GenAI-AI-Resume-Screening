from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from templates import extraction_prompt
load_dotenv()

# 🔥 THIS IS WHERE YOUR CODE GOES
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

extraction_chain = extraction_prompt | llm
