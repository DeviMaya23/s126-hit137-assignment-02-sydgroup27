from scanner import tokenise
from math_parser import parse
from pathlib import Path
import constants

def format_token(token_list: list[tuple[str, str]]) -> str:

    parts = []

    for token_type, token_value in token_list:
        if token_type == constants.END:
            parts.append("[END]")
        else:
            parts.append(f"[{token_type}:{token_value}]")
    return " ".join(parts)

def evaluate_file(input_path: str) -> list[dict]:
    """
    Evaluates the input file and returns a list of results.
    It also writes the results to output.txt, saved in the same directory as input file.

    Args:
        input_path: path of the input file
    Returns:
        A list of dictionaries containing input, tokens, tree and result for each line in the input
    """
    results = []

    with open(input_path, "r") as file:
        for line in file:
            if not line.strip():
                continue
            try:
                tokens = tokenise(line)
            except ValueError:
                # Skip parsing, append error result
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
                "token": format_token(tokens),
                "tree": "ERROR" if tree is None else tree,
                "result": "ERROR" if result is None else result})
            
    # For empty file, skip writing to output.txt
    if not results:
        return results

    # Write resuls to output.txt 
    output_path = Path(input_path).with_name("output.txt")
    with open(output_path, "w") as f:
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
