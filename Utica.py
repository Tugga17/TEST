from typing import Iterable, Union, List

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b

def divide(a: Number, b: Number) -> float:
    """Return a / b. Raises ValueError on divide-by-zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def is_palindrome(text: str, *, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    """
    Check if text reads the same forward and backward.
    Options to ignore case and spaces.
    """
    s = text
    if ignore_spaces:
        s = "".join(s.split())
    if ignore_case:
        s = s.lower()
    return s == s[::-1]

def moving_average(values: Iterable[Number], window: int) -> List[float]:
    """
    Simple moving average with a fixed window size.
    Returns a list of averages (length = len(values) - window + 1).
    """
    vals = list(values)
    if window <= 0:
        raise ValueError("window must be >= 1")
    if window > len(vals):
        return []
    out = []
    curr_sum = sum(vals[:window])
    out.append(curr_sum / window)
    for i in range(window, len(vals)):
        curr_sum += vals[i] - vals[i - window]
        out.append(curr_sum / window)
    return out
