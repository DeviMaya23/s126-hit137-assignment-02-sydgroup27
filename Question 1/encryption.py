def encrypt(text: str, shift1: int, shift2: int) -> str:
    """
    Encrypts the given text using a custom encryption algorithm.

    A-M, the character is shifted backwards by the shift1 value.
    N-Z: shifted forwards by the square of shift2 value.
    a-m: shifted forwards by the product of shift1 and shift2 value.
    n-z: shifted backwards by the sum of shift1 and shift2 value.
    Encryption result wraps around the range of letters in each group.
    Non-alphabetic characters are not changed.

    Args:
        text: The text to be encrypted
        shift1: First shift value, from user input
        shift2: Second shift value, from user input

    Returns:
        The encrypted text.
    """
    encrypted = ""
    for char in text:
        if char.isupper():
            if 'A' <= char <= 'M':
                encrypted += chr(
                    (ord(char) - ord('A') - shift1) % 13 + ord('A')
                )
            elif 'N' <= char <= 'Z':
                shift = shift2 * shift2
                encrypted += chr(
                    (ord(char) - ord('N') + shift) % 13 + ord('N')
                )
        elif char.islower():
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                encrypted += chr(
                    (ord(char) - ord('a') + shift) % 13 + ord('a')
                )
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                encrypted += chr(
                    (ord(char) - ord('n') - shift) % 13 + ord('n')
                )
        else:
            encrypted += char
    return encrypted
