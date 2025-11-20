import os
from pydantic import SecretStr
from langchain_google_genai import ChatGoogleGenerativeAI


def create_llm(env):
    """
    Create the DeepSeek-chat LLM client.

    Inputs:
        env (dict): must contain "GEMINI_API"

    Returns:
        ChatOpenAI instance
    """
    llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-pro",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key = SecretStr(env["GEMINI_API"])

)
    return llm
