import pytest
from evaluator import evaluate_file, format_token


format_token_test_cases = [
    (
        "3 + 5",
        [("NUM", "3"), ("OP", "+"), ("NUM", "5"), ("END", None)],
        "[NUM:3] [OP:+] [NUM:5] [END]",
    ),
    (
        "2 + 3 * 4",
        [("NUM", "2"), ("OP", "+"), ("NUM", "3"), ("OP", "*"), ("NUM", "4"), ("END", None)],
        "[NUM:2] [OP:+] [NUM:3] [OP:*] [NUM:4] [END]",
    ),
    (
        "-(3 + 4)",
        [("OP", "-"), ("LPAREN", "("), ("NUM", "3"), ("OP", "+"), ("NUM", "4"), ("RPAREN", ")"), ("END", None)],
        "[OP:-] [LPAREN:(] [NUM:3] [OP:+] [NUM:4] [RPAREN:)] [END]",
    ),
    (
        "--5",
        [("OP", "-"), ("OP", "-"), ("NUM", "5"), ("END", None)],
        "[OP:-] [OP:-] [NUM:5] [END]",
    ),
    (
        "",
        [("END", None)],
        "[END]",
    ),
]


@pytest.mark.parametrize(
    "name, input, expected_formatted", format_token_test_cases,
    ids=[case[0] for case in format_token_test_cases]
)
def test_format_token(name, input, expected_formatted):
    formatted = format_token(input)
    assert formatted == expected_formatted


def test_evaluate_file_success(tmp_path):

    # Create temp input file
    input_path = tmp_path / "input.txt"
    input_path.write_text("3 + 5\n3 @ 5\n")

    # Run evaluate file & assert results
    result = evaluate_file(str(input_path))

    expected_result = [
        {
            "input": "3 + 5",
            "tokens": "[NUM:3] [OP:+] [NUM:5] [END]",
            "tree": "(+ 3 5)",
            "result": 8.0},
        {
            "input": "3 @ 5",
            "tokens": "ERROR",
            "tree": "ERROR",
            "result": "ERROR"
        },
    ]
    assert result == expected_result

    # File output assertions
    output_path = tmp_path / "output.txt"
    assert output_path.exists()

    expected_file_content = """Input: 3 + 5
Tree: (+ 3 5)
Tokens: [NUM:3] [OP:+] [NUM:5] [END]
Result: 8

Input: 3 @ 5
Tree: ERROR
Tokens: ERROR
Result: ERROR

"""

    assert output_path.read_text() == expected_file_content


def test_evaluate_file_empty(tmp_path):

    # Create empty input file
    input_path = tmp_path / "input.txt"
    input_path.write_text("\n")

    result = evaluate_file(str(input_path))
    assert result == []

    # No output file should be created for empty input
    output_path = tmp_path / "output.txt"
    assert not output_path.exists()


def test_evaluate_file_nonexistent():
    with pytest.raises(FileNotFoundError):
        evaluate_file("nonexistent_file.txt")


def test_evaluate_file_invalid_encoding(tmp_path):
    input_path = tmp_path / "input.txt"
    # Write bytes that aren't UTF-8
    input_path.write_bytes(b'\x80\x81\x82')

    with pytest.raises(UnicodeDecodeError):
        evaluate_file(str(input_path))
