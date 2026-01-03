from unittest.mock import patch
import pytest
from envtool import getenv


@patch("os.getenv")
def test_getenv_when_set(mock_getenv):
    """
    Tests that getenv returns the value of the environment variable when it is set.
    """
    # Set the mock to return a specific value
    mock_getenv.return_value = "hello"

    # Call the function and assert the result
    assert getenv("FOO") == "hello"

    # Ensure that os.getenv was called with the correct argument
    mock_getenv.assert_called_once_with("FOO")


@patch("os.getenv")
def test_getenv_when_not_set(mock_getenv):
    """
    Tests that getenv returns None when the environment variable is not set.
    """
    # Set the mock to return a specific value
    mock_getenv.return_value = None

    # Call the function and assert the result
    assert getenv("FOO") is None

    # Ensure that os.getenv was called with the correct argument
    mock_getenv.assert_called_once_with("FOO")
