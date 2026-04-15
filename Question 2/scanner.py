import constants
def tokenise(input_line:str) -> list[tuple[str, str]] | None:
    """
    Scans the input data and returns a list of tokens.

    Args:
    input_line: a string of input line, coming from input file.
        Token types: NUM, OP, LPAREN, RPAREN, END
        Must end with END token

    Return:
    [(token_type, token_value), ...]
    If it's an empty line, return None.
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
        if ch.isdigit() or (ch == '.' and i + 1 < len(s) and s[i + 1].isdigit()):
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == '.'):
                j += 1
            num_str = s[i:j]
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