def expression(token_list:list[tuple[str, str]], index:int) -> tuple[float, str, int]:
    """
    Returns an expression value, tree and next index.
    """
    # TODO: parentheses logic unimplemented

    value, tree, last_index = factor(token_list, index)

    # consume all + and - tokens
    while token_list[last_index][0] == "OP" and token_list[last_index][1] in ["+", "-"]:
        operator = token_list[last_index][1]
        right_factor, right_tree, last_index = factor(token_list, last_index + 1)

        if operator == "+":
            value += right_factor
        else:
            value -= right_factor
        tree = "(" + operator + " " + tree + " " + right_tree + ")"
    
    # check for END token
    if token_list[last_index][0] == "END":
        return value, tree, last_index
    
    raise SyntaxError("Unexpected token: " + str(token_list[last_index]))


def factor(token_list:list[tuple[str, str]], index:int) -> tuple[float, str, int]:
    """
    Returns a factor value, tree and next index.
    """
    token = token_list[index]

    # for negative unary
    if token[0] == "OP" and token[1] == "-":
        value, operand_tree, new_index = factor(token_list, index + 1)
        return -value, "(neg " + operand_tree + ")", new_index

    if token[0] == "NUM":
        return float(token[1]), token[1], index + 1

    raise SyntaxError("Unexpected token: " + str(token))


def parse():
    """
    Parses the input data and returns tree and result.
    """

    # --3 + 3 + -4
    # dummy = [("OP", "-"), ("OP", "-"), ("NUM", "3"), ("OP", "+"), ("NUM", "3"), ("OP", "+"), ("OP", "-"), ("NUM", "4"), ("END", None)]
    # dummy = [("OP", "-"),("OP", "-"),("NUM", "3"),("END", None)]
    # dummy = [("OP", "-"),("NUM", "3"),("END", None)]
    # dummy = [("NUM", "3"),("END", None)]
    # dummy = [("NUM", "0"),("END", None)]

    dummy = [("OP", "-"), ("NUM", "10"), ("OP", "+"), ("NUM", "5"), ("OP", "-"), ("NUM", "2"), ("END", None)]

    value = None
    tree = None
    try:
        value, tree, last_index = expression(dummy, 0)
        if dummy[last_index][0] != "END":
            raise SyntaxError("Expect END token at index " + str(last_index) + ", got " + str(dummy[last_index]))
        
    except SyntaxError as e:
        print("Syntax Error:", e)

    if value is None:
        value = "ERROR"
    if tree is None:
        tree = "ERROR"

    print("Result:", value)
    print("Tree:", tree)
    

parse()