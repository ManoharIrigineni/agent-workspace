from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(Path(__file__).parent.parent / ".env")

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0
)


def ask_llm(prompt: str):

    response = llm.invoke(prompt)

    content = response.content

    if isinstance(content, list):
        return content[0]["text"]

    return str(content)