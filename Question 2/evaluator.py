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

        results.append({
            "input": "dummyinput", # TODO: from read line loop
            "token": "dummytoken", # TODO: from tokenise function, maybe a new function to properly format
            "tree": "ERROR" if tree is None else tree, 
            "result": "ERROR" if result is None else result}) 

    # Write resuls to output.txt 
    # TODO: output file location should match input file
    with open("output.txt", "w") as f:
        for result in results:
            f.write(f"Input: {result['input']}\n")
            f.write(f"Tree: {result['tree']}\n")
            f.write(f"Tokens: {result['token']}\n")

            result_value = result['result']
            if result_value != "ERROR":
                if result_value.is_integer():
                    result_value = str(int(result_value))
                else:
                    result_value = f"{result_value:.4f}"
            f.write(f"Result: {result_value}\n\n")

    return results

# this is a stub. will delete after tokenise function is finished
def dummy_tokenise():
    example1 = [("NUM", "3"), ("OP", "+"), ("NUM", "5"), ("END", None)]
    example2 = [("NUM", "3"), ("WRONG", "@"), ("NUM", "5"), ("END", None)]
    example3 = [("NUM", "3"), ("OP", "/"), ("NUM", "0"), ("END", None)]
    example4 = [("NUM", "10"), ("OP", "/"), ("NUM", "3"), ("END", None)]
    return [example1, example2, example3, example4]

evaluate_file("dummy_input.txt")