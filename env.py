import os
from dotenv import load_dotenv


def load_env():
    """
    Load required environment variables.

    Inputs:
        None

    Returns:
        dict with DEEP_SEEK_API_KEY, PERSIST_DIR,DEEP_SEEK_API_END
    """
    load_dotenv()
    names = [ "DEEP_SEEK_API_KEY", "PERSIST_DIR","DEEP_SEEK_API_END"]

    missing = [name for name in names if not os.environ.get(name)]
    if missing:
        raise ValueError(f"FATAL: Missing env variables: {missing}")

    return {name: os.environ[name] for name in names}
