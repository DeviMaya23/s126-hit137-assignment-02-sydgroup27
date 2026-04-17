import pytest
from encryption import encrypt

test_cases = [
    # a-m: shift forward by shift1 * shift2
    ("a", 1, 1, "b"),
    ("m", 1, 1, "a"),
    # n-z: shift backward by shift1 + shift2
    ("n", 1, 1, "y"),
    ("z", 1, 1, "x"),
    # A-M: shift backward by shift1
    ("A", 1, 1, "M"),  # wraps around
    ("M", 2, 1, "K"),
    # N-Z: shift forward by shift2^2
    ("N", 1, 2, "R"),
    ("Z", 1, 1, "N"),  # wraps around
    # non-alpha unchanged
    ("1", 1, 1, "1"),
    (" ", 1, 1, " "),
    ("@", 3, 10, "@"),
    # sentences
    ("Hello World 1!", 3, 4, "Edkku Zuxkc 1!"),
]


@pytest.mark.parametrize("input, shift1, shift2, expected", test_cases)
def test_encrypt(input, shift1, shift2, expected):
    assert encrypt(input, shift1, shift2) == expected
