import pytest
from math_parser import parse

large_number_string = '1' + '0' * 400

test_cases = [
    # From sample_input.txt
    ("3 + 5", [("NUM", "3"), ("OP", "+"), ("NUM", "5"), ("END", None)], "(+ 3 5)", 8.0),
    ("2 + 3 * 4", [("NUM", "2"), ("OP", "+"), ("NUM", "3"), ("OP", "*"), ("NUM", "4"), ("END", None)], "(+ 2 (* 3 4))", 14.0),
    ("-(3 + 4)", [("OP", "-"), ("LPAREN", "("), ("NUM", "3"), ("OP", "+"), ("NUM", "4"), ("RPAREN", ")"), ("END", None)], "(neg (+ 3 4))", -7.0),
    ("--5", [("OP", "-"), ("OP", "-"), ("NUM", "5"), ("END", None)], "(neg (neg 5))", 5.0),
    ("(10 - 2) * 3 + -4 / 2", [("LPAREN", "("), ("NUM", "10"), ("OP", "-"), ("NUM", "2"), ("RPAREN", ")"), ("OP", "*"), ("NUM", "3"), ("OP", "+"), ("OP", "-"), ("NUM", "4"), ("OP", "/"), ("NUM", "2"), ("END", None)], "(+ (* (- 10 2) 3) (/ (neg 4) 2))", 22.0),
    ("1 / 0", [("NUM", "1"), ("OP", "/"), ("NUM", "0"), ("END", None)], "(/ 1 0)", None),
    # Other cases
    ("-5.72 + 1", [("OP", "-"), ("NUM", "5.72"), ("OP", "+"), ("NUM", "1"), ("END", None)], "(+ (neg 5.72) 1)", -4.72),
    ("bignumber + 1", [("NUM", large_number_string), ("OP", "+"), ("NUM", "1"), ("END", None)], f"(+ {large_number_string} 1)", None),
    ("bignumber*1 - bignumber*1", [("NUM", large_number_string), ("OP", "*"), ("NUM", "1"), ("OP", "-"), ("NUM", large_number_string), ("OP", "*"), ("NUM", "1"), ("END", None)], f"(- (* {large_number_string} 1) (* {large_number_string} 1))", None),
    # Syntax errors
    ("5 +", [("NUM", "5"), ("OP", "+"), ("END", None)], None, None),
    ("empty line", [("END", None)], None, None),
    ("unary minus only", [("OP", "-"), ("END", None)], None, None),
    ("+ 5", [("OP", "+"), ("NUM", "5"), ("END", None)], None, None),
]

@pytest.mark.parametrize("name, input, expected_tree, expected_value", test_cases,
                         ids=[case[0] for case in test_cases])
def test_parser(name, input, expected_tree, expected_value):
    tree, value = parse(input)
    assert tree == expected_tree
    assert value == expected_value