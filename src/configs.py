import os

from dotenv import load_dotenv

# Load values from the .env file and inject them into the local environment
load_dotenv()


def api_token() -> str:
    """
    The API token for HackAttic
    :return: The API token for HackAttic as a string
    """
    return os.getenv("api_key")


def playground_mode() -> int:
    """
    Playground setting
    :return: 1 if in playground mode, 0 if not
    """
    return int(os.getenv("playground", 0))
