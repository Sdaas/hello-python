import os
from dotenv import load_dotenv

# Load environment variables from .env file
# See README.md and https://pypi.org/project/python-dotenv/  for details on usage
load_dotenv()


def getenv(name):
    """
    Returns the value of the environment variable with the given name.
    """
    return os.getenv(name)
