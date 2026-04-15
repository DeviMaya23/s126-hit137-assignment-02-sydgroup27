from evaluator import evaluate_file

def main():
    """
    Entry point for question 2 script.
    """
    
    while True:
        input_path = input("Enter the path of the input file (example: C:\\path\\to\\input.txt): ").strip()
        if not input_path:
            print("Input path cannot be empty. Please try again.")
            continue
        try:
            result = evaluate_file(input_path)
            print("Result:")
            print(result)
            print("Evaluation complete. Results written to output.txt")
            break
        except FileNotFoundError:
            print(f"File not found: {input_path}. Please try again.")
        except OSError as e:
            print(f"File error: {e}")
            break


if __name__ == "__main__":
    main()