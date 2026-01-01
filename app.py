import os
from dotenv import load_dotenv

# Load environment variables from .env file
# See README.md and https://pypi.org/project/python-dotenv/  for details on usage
load_dotenv()


def get_foo_value():
    """
    Returns the value of the FOO environment variable. Throws a ValueError if FOO is not set.g
    """
    foo_value = os.getenv("FOO")
    if foo_value is None:
        raise ValueError("Error: FOO environment variable is not set.")
    return foo_value


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
