from encryption import encrypt
from decryption import decrypt
from compare import compare


def get_shift(prompt: str) -> int:
    """
    Prompts the user for a shift value and validates the input.

    Args:
        prompt: The message to display when asking for input
    Returns:
        The validated shift value as an integer.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a number only.")


def main():
    """
    Entry point for question 1 script.
    """

    # Receive the shift value to shift the data
    shift1 = get_shift("Enter shift1 value:")
    shift2 = get_shift("Enter shift2 value:")

    try:
        with open("raw_text.txt", 'r') as file:
            raw_text = file.read()
    except FileNotFoundError:
        print("Error: raw_text.txt not found in current directory.")
        return
    except UnicodeDecodeError:
        print("Error: File raw_text.txt is not a valid text file.")
        return
    except OSError as e:
        print(f"Error reading file: {e}")
        return

    # Encrypting the content of the file using Encrypt function
    encrypt_text = encrypt(raw_text, shift1, shift2)

    # Writing the encrypted text in the file encrypt_text.txt
    try:
        with open("encrypt_text.txt", 'w') as file:
            file.write(encrypt_text)
    except OSError as e:
        print(f"Error writing encrypted file: {e}")
        return

    print("\n\nEncryption has been successful.")

    print("\n\nThe raw text are: \n")
    print(raw_text)
    print("\n\nThe Encrypted text are: \n")
    print(encrypt_text)

    # Decrypting the content of the file 'encrypt_text.txt'.
    decrypt_text = decrypt(encrypt_text.strip(), shift1, shift2)

    # writing the decrypted text in the file decryption_text.txt
    try:
        with open("decryption_text.txt", 'w') as file:
            file.write(decrypt_text)
    except OSError as e:
        print(f"Error writing decrypted file: {e}")
        return

    print("\n\nThe Decrypted text is: \n")
    print(decrypt_text)
    print("\n\n")

    compare("raw_text.txt", "decryption_text.txt")


if __name__ == "__main__":
    main()
