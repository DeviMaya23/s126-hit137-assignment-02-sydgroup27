def expression(token_list:list[tuple[str, str]], index:int) -> tuple[float, int]:
    """
    Returns an expression value and next index.
    """

    result = factor(token_list, index)
    if token_list[result[1]][0] != "END":
        raise SyntaxError("Expect END token at index " + str(result[1]) + ", got " + str(token_list[result[1]]))

    return result

def factor(token_list:list[tuple[str, str]], index:int) -> tuple[float, int]:
    """
    Returns a factor value and next index.
    """
    token = token_list[index]

    if token[0] == "OP" and token[1] == "-":
        value, new_index = factor(token_list, index + 1)
        return -value, new_index

    if token[0] == "NUM":
        return float(token[1]), index + 1
    
    raise SyntaxError("Unexpected token: " + str(token))


def parse():
    """
    Parses the input data and returns tree and result.
    """

    dummy = [("OP", "+"),("OP", "-"),("NUM", "3"),("END", None)]
    
    value = None
    try:
        value = expression(dummy, 0)
    except SyntaxError as e:
        print("Syntax Error:", e)

    if value is None:
        print("No result")
    else:
        print("Result:", value)
    

parse()