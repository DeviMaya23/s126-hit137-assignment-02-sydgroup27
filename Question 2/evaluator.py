from scanner import tokenise
from math_parser import parse

def evaluate_file(input_path: str) -> list[dict]:
    """
    Evaluates the input file and returns a list of results.
    """
    results = []
    
    # read input file line by line
    # call tokenise for each line, then pass to parse

    # TODO: instead of looping dummy_tokenise, this should be done in read line loop, after tokenise is run
    for line in dummy_tokenise():
        tree, result = parse(line)
        results.append({"input": "dummyinput", "token": "dummytoken", # TODO: input and token should come from tokeniser
            "tree": tree, "result": result}) 
        
    # TODO: write result into output.txt, located in the same directory as input_path

    return results

# this is a stub. will delete after tokenise function is finished
def dummy_tokenise():
    example1 = [("NUM", "3"), ("OP", "+"), ("NUM", "5"), ("END", None)]
    example2 = [("NUM", "3"), ("WRONG", "@"), ("NUM", "5"), ("END", None)]
    example3 = [("NUM", "3"), ("OP", "/"), ("NUM", "0"), ("END", None)]
    return [example1, example2, example3]


print(evaluate_file("notafile"))