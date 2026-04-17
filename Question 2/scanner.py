import constants


def tokenise(input_line: str) -> list[tuple[str, str]] | None:
    """
    Scans the input data and returns a list of tokens.

    Args:
        input_line: a string of input line, coming from input file.
    Returns:
        A list of tuples (token_type, token_value) where token_type is one of:
        NUM, OP, LPAREN, RPAREN, or END. Returns None for empty lines.
    Raises:
        ValueError: if an unexpected character is encountered or
                    if a number literal is invalid.
    """

    if not input_line.strip():
        return None

    tokens = []
    i = 0

    while i < len(input_line):
        ch = input_line[i]

        # Skip whitespace
        if ch.isspace():
            i += 1
            continue

        # Numeric literal — collect all consecutive digit/dot characters
        if ch.isdigit() or (
            ch == '.'
            and i + 1 < len(input_line)
            and input_line[i + 1].isdigit()
        ):
            j = i
            while (
                j < len(input_line)
                and (input_line[j].isdigit() or input_line[j] == '.')
            ):
                j += 1
            num_str = input_line[i:j]
            if num_str.count('.') > 1:
                raise ValueError(f"Invalid number literal: {num_str!r}")
            tokens.append((constants.NUM, num_str))
            i = j
            continue

        # Operators
        if ch in ('+', '-', '*', '/'):
            tokens.append((constants.OP, ch))
            i += 1
            continue

        # Parentheses
        if ch == '(':
            tokens.append((constants.LPAREN, '('))
            i += 1
            continue
        if ch == ')':
            tokens.append((constants.RPAREN, ')'))
            i += 1
            continue

        # Unknown character — propagate as ValueError so evaluator catches it
        raise ValueError(f"Unexpected character: {ch!r}")

    tokens.append((constants.END, None))
    return tokens
