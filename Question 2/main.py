from evaluator import evaluate_file

def main():
    """ Entry point for question 2 script. """
    
    results = evaluate_file("sample_input.txt")
    for r in results:
        print(r)

if __name__ == "__main__":
    main()