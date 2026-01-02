from calculator import add, subtract, factorial
import pytest


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


def test_factorial_positive_integers():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


# Note
# pytest.raises() match uses regular expressions
# Hence the need to anchor it with ^ and $
def test_factorial_invalid_input():
    expected = "^Input must be a non-negative integer$"
    with pytest.raises(ValueError, match=expected):
        factorial(-1)
    with pytest.raises(ValueError, match=expected):
        factorial(1.5)
    with pytest.raises(ValueError, match=expected):
        factorial("a")
    with pytest.raises(ValueError, match=expected):
        factorial(None)
