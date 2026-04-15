from scanner import tokenise
from math_parser import parse

def evaluate_file(input_path: str) -> list[dict]:
    """
    Evaluates the input file and returns a list of results.
    """
    results = []

    with open(input_path, "r") as file:
        for line in file:
            if not line.strip():
                continue
            try:
                tokens = tokenise(line)
            except ValueError:
                results.append({
                    "input": line.rstrip('\n'),
                    "token": "ERROR",
                    "tree": "ERROR",
                    "result": "ERROR"
                })
                continue

            tree, result = parse(tokens)

            results.append({
                "input": line.rstrip('\n'),
                "token": tokens,
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
