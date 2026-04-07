def expression(token_list:list[tuple[str, str]], index:int) -> tuple[float, str, int]:
    """
    Returns an expression value, tree and next index.
    """
    value, tree, last_index = term(token_list, index)

    # consume all + and - tokens
    while token_list[last_index][0] == "OP" and token_list[last_index][1] in ["+", "-"]:
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


def term(token_list:list[tuple[str, str]], index:int) -> tuple[float, str, int]:
    """
    Returns a term value, tree and next index.
    """
    value, tree, last_index = factor(token_list, index)

    # consume all * and / tokens
    while (
        (token_list[last_index][0] == "OP" and token_list[last_index][1] in ["*", "/"])
        or token_list[last_index][0] == "LPAREN"
    ):
        # for implicit multiplication
        if token_list[last_index][0] == "LPAREN":
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


def factor(token_list:list[tuple[str, str]], index:int) -> tuple[float, str, int]:
    """
    Returns a factor value, tree and next index.
    """
    token = token_list[index]

    # for parentheses expression
    if token[0] == "LPAREN":
        value, tree, last_index = expression(token_list, index + 1)
        if token_list[last_index][0] != "RPAREN":
            raise SyntaxError("Expected RPAREN token at index " + str(last_index) + ", got " + str(token_list[last_index]))
        return value, tree, last_index + 1

    # for negative unary
    if token[0] == "OP" and token[1] == "-":
        value, operand_tree, new_index = factor(token_list, index + 1)
        if value is not None:
            value = -value
        return value, "(neg " + operand_tree + ")", new_index

    if token[0] == "NUM":
        return float(token[1]), token[1], index + 1

    raise SyntaxError("Unexpected token: " + str(token))


def parse(token_list:list[tuple[str, str]]) -> tuple[str, str]:
    """
    Parses the input data and returns tree and result.
    """

    value = None
    tree = None
    try:
        value, tree, last_index = expression(token_list, 0)
        if token_list[last_index][0] != "END":
            value = None
            tree = None
            raise SyntaxError("Expect END token at index " + str(last_index) + ", got " + str(token_list[last_index]))
    except SyntaxError as e:
        pass

    if value is None:
        value = "ERROR"
    if tree is None:
        tree = "ERROR"
    
    return tree, value

    
# 3 @ 5
dummy = [("NUM", "3"), ("WRONG", "@"), ("NUM", "5"), ("END", None)]
parse(dummy)