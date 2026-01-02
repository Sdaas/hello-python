import os
from dotenv import load_dotenv
from calculator import add, subtract

# Load environment variables from .env file
# See README.md and https://pypi.org/project/python-dotenv/  for details on usage
load_dotenv()


def get_foo_value():
    """
    Returns the value of the FOO environment variable. Throws a ValueError if FOO is not set.g
    """
    foo_value = os.getenv("FOO")
    if foo_value is None:
        raise ValueError("Error: FOO environment variable is not set")
    return foo_value


def main():
    """Main function to run when the script is executed directly."""
    try:
        foo = get_foo_value()
        print(f"The value of FOO is: {foo}")
        print(f"Result of add(5, 3): {add(5, 3)}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
