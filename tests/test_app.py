import logging
import os
from app import add, subtract


def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(1, -1) == 2
    assert subtract(-5, -3) == -2


def test_logging():
    # Get and print the current working directory
    logging.info(f"Current working directory: {os.getcwd()}")
    logging.error("this is an error")
