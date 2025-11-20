import os
from dotenv import load_dotenv


def load_env():
    """
    Load required environment variables.

    Inputs:
        None

    Returns:
        dict with , PERSIST_DIR, GEMINI_API
    """
    load_dotenv()
    names = [ "PERSIST_DIR","GEMINI_API"]

    missing = [name for name in names if not os.environ.get(name)]
    if missing:
        raise ValueError(f"FATAL: Missing env variables: {missing}")

    return {name: os.environ[name] for name in names}
