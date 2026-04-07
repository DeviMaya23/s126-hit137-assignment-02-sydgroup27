def expression(token_list:list[tuple[str, str]], index:int) -> tuple[float, int, str]:
    """
    Returns an expression value and next index.
    """

    result, last_index, tree = factor(token_list, index)

    return result, last_index, tree

def factor(token_list:list[tuple[str, str]], index:int) -> tuple[float, int, str]:
    """
    Returns a factor value and next index.
    """
    token = token_list[index]

    if token[0] == "OP" and token[1] == "-":
        value, new_index, operand_tree = factor(token_list, index + 1)
        return -value, new_index, "(neg " + operand_tree + ")"

    if token[0] == "NUM":
        return float(token[1]), index + 1, str(token[1])
    
    raise SyntaxError("Unexpected token: " + str(token))


def parse():
    """
    Parses the input data and returns tree and result.
    """

    dummy = [("OP", "-"),("OP", "-"),("OP", "-"),("NUM", "3"),("END", None)]
    # dummy = [("OP", "-"),("NUM", "3"),("END", None)]
    # dummy = [("NUM", "3"),("END", None)]

    value = None
    try:
        value, last_index, tree = expression(dummy, 0)
        if dummy[last_index][0] != "END":
            raise SyntaxError("Expect END token at index " + str(last_index) + ", got " + str(dummy[last_index]))
        
    except SyntaxError as e:
        print("Syntax Error:", e)

    if value is None:
        print("No result")
    else:
        print("Result:", value)
        print("Tree:", tree)
    

parse()