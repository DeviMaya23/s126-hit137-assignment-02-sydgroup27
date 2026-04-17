import pytest
from decryption import decrypt

test_cases = [
    ("b", 1, 1, "a"),
    ("a", 1, 1, "m"),

    ("y", 1, 1, "n"),
    ("x", 1, 1, "z"),

    ("M", 1, 1, "A"),  # wraps around
    ("K", 2, 1, "M"),

    ("R", 1, 2, "N"),
    ("N", 1, 1, "Z"),  # wraps around

    ("1", 1, 1, "1"),
    (" ", 1, 1, " "),
    ("@", 3, 10, "@"),

    ("Edkku Zuxkc 1!", 3, 4, "Hello World 1!"),
]

@pytest.mark.parametrize("input, shift1, shift2, expected", test_cases)
def test_decrypt(input, shift1, shift2, expected):
    assert decrypt(input, shift1, shift2) == expected