from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.templates import matching_prompt

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0
)

matching_chain = matching_prompt | llm