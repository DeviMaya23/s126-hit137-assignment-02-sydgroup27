import pytest
import constants
from scanner import tokenise


# Helpers
def tok(type_, value):
    """Shorthand for building an expected token tuple."""
    return (type_, value)


END = (constants.END, None)


# 1. Empty / blank input


class TestBlankInput:
    def test_empty_string_returns_none(self):
        assert tokenise("") is None

    def test_whitespace_only_returns_none(self):
        assert tokenise("   ") is None

    def test_newline_only_returns_none(self):
        assert tokenise("\n") is None

    def test_tab_only_returns_none(self):
        assert tokenise("\t") is None

# 2. Always ends with END token


class TestEndToken:
    def test_single_number_ends_with_end(self):
        result = tokenise("5")
        assert result[-1] == END

    def test_expression_ends_with_end(self):
        result = tokenise("3 + 4")
        assert result[-1] == END

# 3. Number literals


class TestNumbers:
    def test_single_digit(self):
        assert tokenise("5") == [tok(constants.NUM, "5"), END]

    def test_multi_digit(self):
        assert tokenise("123") == [tok(constants.NUM, "123"), END]

    def test_decimal_number(self):
        assert tokenise("3.14") == [tok(constants.NUM, "3.14"), END]

    def test_leading_dot_decimal(self):
        # 5. should tokenise as a decimal number
        assert tokenise(".5") == [tok(constants.NUM, ".5"), END]

    def test_zero(self):
        assert tokenise("0") == [tok(constants.NUM, "0"), END]

    def test_large_number(self):
        assert tokenise("99999") == [tok(constants.NUM, "99999"), END]

    def test_invalid_double_dot_raises(self):
        with pytest.raises(ValueError):
            tokenise("1.2.3")

# 4. Operators



class TestOperators:
    @pytest.mark.parametrize("op", ["+", "-", "*", "/"])
    def test_single_operator(self, op):
        result = tokenise(f"1 {op} 2")
        assert result[1] == tok(constants.OP, op)

    def test_unary_minus_is_op_token(self):
        # -5 must produce [OP:-] [NUM:5] [END], NOT [NUM:-5] [END]
        result = tokenise("-5")
        assert result == [
            tok(constants.OP, "-"),
            tok(constants.NUM, "5"),
            END,
        ]

    def test_double_unary_minus(self):
        result = tokenise("--5")
        assert result == [
            tok(constants.OP, "-"),
            tok(constants.OP, "-"),
            tok(constants.NUM, "5"),
            END,
        ]

    def test_unary_minus_after_operator(self):
        # 3 * -2
        result = tokenise("3 * -2")
        assert result == [
            tok(constants.NUM, "3"),
            tok(constants.OP, "*"),
            tok(constants.OP, "-"),
            tok(constants.NUM, "2"),
            END,
        ]

# 5. Parentheses


class TestParentheses:
    def test_lparen(self):
        result = tokenise("(1)")
        assert result[0] == tok(constants.LPAREN, "(")

    def test_rparen(self):
        result = tokenise("(1)")
        assert result[2] == tok(constants.RPAREN, ")")

    def test_nested_parentheses(self):
        result = tokenise("((1))")
        assert result == [
            tok(constants.LPAREN, "("),
            tok(constants.LPAREN, "("),
            tok(constants.NUM, "1"),
            tok(constants.RPAREN, ")"),
            tok(constants.RPAREN, ")"),
            END,
        ]

# 6. Whitespace handling


class TestWhitespace:
    def test_spaces_are_ignored(self):
        assert tokenise("3 + 5") == tokenise("3+5")

    def test_leading_and_trailing_spaces(self):
        result = tokenise("  42  ")
        assert result == [tok(constants.NUM, "42"), END]

    def test_tabs_are_ignored(self):
        assert tokenise("3\t+\t5") == tokenise("3+5")

# 7. Full expressions


class TestFullExpressions:
    def test_simple_addition(self):
        assert tokenise("3 + 5") == [
            tok(constants.NUM, "3"),
            tok(constants.OP, "+"),
            tok(constants.NUM, "5"),
            END,
        ]

    def test_operator_precedence_expression(self):
        result = tokenise("1 + 2 * 3")
        assert result == [
            tok(constants.NUM, "1"),
            tok(constants.OP, "+"),
            tok(constants.NUM, "2"),
            tok(constants.OP, "*"),
            tok(constants.NUM, "3"),
            END,
        ]

    def test_parenthesised_expression(self):
        result = tokenise("(3 + 5) * 2")
        assert result == [
            tok(constants.LPAREN, "("),
            tok(constants.NUM, "3"),
            tok(constants.OP, "+"),
            tok(constants.NUM, "5"),
            tok(constants.RPAREN, ")"),
            tok(constants.OP, "*"),
            tok(constants.NUM, "2"),
            END,
        ]

    def test_implicit_multiplication(self):
        result = tokenise("2(3+4)")
        assert result == [
            tok(constants.NUM, "2"),
            tok(constants.LPAREN, "("),
            tok(constants.NUM, "3"),
            tok(constants.OP, "+"),
            tok(constants.NUM, "4"),
            tok(constants.RPAREN, ")"),
            END,
        ]

    def test_complex_expression(self):
        result = tokenise("(10 - 2) * 3 + -4 / 2")
        assert result == [
            tok(constants.LPAREN, "("),
            tok(constants.NUM, "10"),
            tok(constants.OP, "-"),
            tok(constants.NUM, "2"),
            tok(constants.RPAREN, ")"),
            tok(constants.OP, "*"),
            tok(constants.NUM, "3"),
            tok(constants.OP, "+"),
            tok(constants.OP, "-"),
            tok(constants.NUM, "4"),
            tok(constants.OP, "/"),
            tok(constants.NUM, "2"),
            END,
        ]

    def test_division_by_zero_tokenises_normally(self):
        result = tokenise("1 / 0")
        assert result == [
            tok(constants.NUM, "1"),
            tok(constants.OP, "/"),
            tok(constants.NUM, "0"),
            END,
        ]

# 8. Invalid / error inputs


class TestInvalidInput:
    def test_unknown_character_raises_value_error(self):
        with pytest.raises(ValueError):
            tokenise("3 @ 5")

    def test_hash_raises_value_error(self):
        with pytest.raises(ValueError):
            tokenise("3 # 5")

    def test_letter_raises_value_error(self):
        with pytest.raises(ValueError):
            tokenise("3 + x")

    def test_double_dot_number_raises_value_error(self):
        with pytest.raises(ValueError):
            tokenise("1.2.3")

    def test_error_is_value_error_not_other(self):
        # Make sure the exception type is exactly ValueError
        with pytest.raises(ValueError):
            tokenise("$100")