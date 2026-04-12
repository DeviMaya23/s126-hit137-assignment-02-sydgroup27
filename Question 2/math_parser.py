import constants

def expression(token_list:list[tuple[str, str]], index:int) -> tuple[float | None, str, int]:
    """
    Reads token list and returns an expression value, tree and next index.

    Args:
        token_list: list of tokens from tokeniser
        index: current index of token list
    Returns:
        A tuple of (value, tree, next_index). Value is None for errors.
    """
    value, tree, last_index = term(token_list, index)

    # consume all + and - tokens
    while token_list[last_index][0] == constants.OP and token_list[last_index][1] in ["+", "-"]:
        operator = token_list[last_index][1]
        right_term, right_tree, last_index = term(token_list, last_index + 1)

        tree = "(" + operator + " " + tree + " " + right_tree + ")"

        # none value is zero division error handling
        if value is None or right_term is None:
            value = None
            continue
        
        if operator == "+":
            value += right_term
        else:
            value -= right_term
        
    return value, tree, last_index


def term(token_list:list[tuple[str, str]], index:int) -> tuple[float | None, str, int]:
    """
    Reads token list and returns a term value, tree and next index.

    Args:
        token_list: list of tokens from tokeniser
        index: current index of token list
    Returns:
        A tuple of (value, tree, next_index). Value is None for errors.
    """
    value, tree, last_index = factor(token_list, index)

    # consume all * and / tokens
    while (
        ((token_list[last_index][0] == constants.OP and token_list[last_index][1] in ["*", "/"])
        or token_list[last_index][0] == constants.LPAREN)
    ):
        # for implicit multiplication
        if token_list[last_index][0] == constants.LPAREN:
            operator = "*"
            factor_index = last_index
        else:
            operator = token_list[last_index][1]
            factor_index = last_index + 1

        right_factor, right_tree, last_index = factor(token_list, factor_index)
        tree = "(" + operator + " " + tree + " " + right_tree + ")"

        if value is None or right_factor is None:
            value = None
            continue

        if operator == "*":
            value *= right_factor
        else:
            # divide by zero handling
            if right_factor == 0:
                value = None
            else:
                value /= right_factor

    return value, tree, last_index


def factor(token_list:list[tuple[str, str]], index:int) -> tuple[float | None, str, int]:
    """
    Reads token list and returns a factor value, tree and next index.

    Args:
        token_list: list of tokens from tokeniser
        index: current index of token list
    Returns:
        A tuple of (value, tree, next_index). Value is None for errors.
    """
    token = token_list[index]

    # for parentheses expression
    if token[0] == constants.LPAREN:
        value, tree, last_index = expression(token_list, index + 1)
        if token_list[last_index][0] != constants.RPAREN:
                raise SyntaxError(f"Expected RPAREN token at index {last_index}, got {token_list[last_index]}")
        return value, tree, last_index + 1

    # for negative unary
    if token[0] == constants.OP and token[1] == "-":
        value, operand_tree, new_index = factor(token_list, index + 1)
        if value is not None:
            value = -value
        return value, "(neg " + operand_tree + ")", new_index

    if token[0] == constants.NUM:
        return float(token[1]), token[1], index + 1

    raise SyntaxError(f"Unexpected token: {token}")


def parse(token_list:list[tuple[str, str]]) -> tuple[str | None, float | None]:
    """
    Parses the input data and returns tree and result.
    
    Args:
        token_list: List produced by the tokeniser. Must end with END token.
    Returns:
        A tuple of (tree, result). Values are None for errors.
    """
    result = None
    tree = None
    try:
        result, tree, last_index = expression(token_list, 0)
        if token_list[last_index][0] != constants.END:
            result = None
            tree = None
            raise SyntaxError(f"Expected END token at index {last_index}, got {token_list[last_index]}")
    except SyntaxError as e:
        pass
    
    return tree, result

