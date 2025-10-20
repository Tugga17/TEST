import math
import pytest
from utils import add, divide, is_palindrome, moving_average

# --- add ---
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-5, 7, 2),
    (0.1, 0.2, 0.3),
    (1_000_000_000, 1, 1_000_000_001),
])
def test_add(a, b, expected):
    # floats can have rounding error—use math.isclose where needed
    if any(isinstance(x, float) for x in (a, b, expected)):
        assert math.isclose(add(a, b), expected, rel_tol=1e-9, abs_tol=0.0)
    else:
        assert add(a, b) == expected

# --- divide ---
def test_divide_basic():
    assert math.isclose(divide(10, 4), 2.5)

def test_divide_negative():
    assert math.isclose(divide(-9, 3), -3.0)

def test_divide_raises_on_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

# --- is_palindrome ---
@pytest.mark.parametrize("text,kwargs,expected", [
    ("racecar", {}, True),
    ("RaceCar", {}, True),  # ignore_case default True
    ("nurses run", {}, True),  # ignore_spaces default True
    ("A man a plan a canal Panama", {}, True),
    ("hello", {}, False),
    ("Abba", {"ignore_case": False}, False),
    ("taco cat", {"ignore_spaces": False}, False),
])
def test_is_palindrome(text, kwargs, expected):
    assert is_palindrome(text, **kwargs) == expected

# --- moving_average ---
def test_moving_average_basic():
    assert moving_average([1, 2, 3, 4], window=2) == [1.5, 2.5, 3.5]

def test_moving_average_window_1():
    assert moving_average([5, 6, 7], window=1) == [5.0, 6.0, 7.0]

def test_moving_average_window_equals_len():
    assert moving_average([2, 4, 6], window=3) == [4.0]

def test_moving_average_window_too_large():
    assert moving_average([1, 2], window=3) == []

def test_moving_average_invalid_window():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], window=0)
