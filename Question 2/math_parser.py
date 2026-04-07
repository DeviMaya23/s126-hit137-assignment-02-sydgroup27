def expression(token_list:list[tuple[str, str]], index:int):
    """
    Returns an expression value.
    """
    result = factor(token_list, index)

    return result

def factor(token_list:list[tuple[str, str]], index:int):
    """
    Returns a factor value.
    """
    token = token_list[index]

    if token[0] == "OP" and token[1] == "-":
        return -factor(token_list, index + 1)

    if token[0] == "NUM":
        return float(token[1])
    
    return None


def parse():
    """
    Parses the input data and returns tree and result.
    """

    dummy = [("OP", "-"),("OP", "-"),("NUM", "3"),]
    res = expression(dummy, 0)
    print(res)
    

parse()