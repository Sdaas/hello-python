import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

foo_value = os.getenv("FOO")

if foo_value is not None:
    print(f"The value of FOO is: {foo_value}")
else:
    print("Error: FOO environment variable is not set.")