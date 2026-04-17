def decrypt(text: str, shift1: int, shift2: int) -> str:
    """
    Decrypts the given text using a custom decryption algorithm.

    Args:
        text: The text to be decrypted
        shift1: First shift value, from user input
        shift2: Second shift value, from user input

    Returns:
        The decrypted text.
    """
    decrypted = ""
    for char in text:
        if char.isupper():
            if 'A' <= char <= 'M':
                decrypted += chr(
                    (ord(char) - ord('A') + shift1) % 13 + ord('A')
                )
            elif 'N' <= char <= 'Z':
                shift = shift2 * shift2
                decrypted += chr(
                    (ord(char) - ord('N') - shift) % 13 + ord('N')
                )
        elif char.islower():
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                decrypted += chr(
                    (ord(char) - ord('a') - shift) % 13 + ord('a')
                )
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                decrypted += chr(
                    (ord(char) - ord('n') + shift) % 13 + ord('n')
                )
        else:
            decrypted += char
    return decrypted
