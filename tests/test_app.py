import logging
import os
from unittest.mock import patch
import pytest
from app import get_foo_value


def test_logging():
    # Get and print the current working directory
    logging.info(f"Current working directory: {os.getcwd()}")
    logging.error("this is an error")


@patch("os.getenv")  # Mock os.getenv to control environment variable access
def test_get_foo_value_when_set(mock_getenv):
    """
    Tests that get_foo_value returns the value of the FOO environment variable when it is set.
    """
    # Set the mock to return a specific value
    mock_getenv.return_value = "bar"

    # Call the function and assert the result
    assert get_foo_value() == "bar"

    # Ensure that os.getenv was called with the correct argument
    mock_getenv.assert_called_once_with("FOO")


@patch("os.getenv")
def test_get_foo_value_when_not_set(mock_getenv):
    """
    Tests that get_foo_value raises a ValueError when the FOO environment variable is not set.
    """
    # Set the mock to return a specific value
    mock_getenv.return_value = None

    # Call the function and verify that it raises a ValueError
    # Note - pytest.raises() match uses regular expressions
    # Hence the need to anchor it with ^ and $
    with pytest.raises(
        ValueError, match="^Error: FOO environment variable is not set$"
    ):
        get_foo_value()

    # Ensure that os.getenv was called with the correct argument
    mock_getenv.assert_called_once_with("FOO")
