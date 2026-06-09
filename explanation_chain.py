from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.templates import explanation_prompt

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.2
)

explanation_chain = explanation_prompt | llm