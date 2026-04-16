
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
    try:
        # Giving the shift value to shift the data 
        shift1 = get_shift("Enter shift1 value:")
        shift2 = get_shift("Enter shift2 value:")

        # Writing the content to be encrypted in the file raw_text.txt
        with open("raw_text.txt", 'r') as file:
            raw_text = file.read()
        print("\n\n"+"Sentences have been saved to 'raw_text.txt'")

        # Encrypting the content of the file using Encrypt function
        encrypt_text = encrypt(raw_text, shift1, shift2)

        # Writing the encrypted text in the file encrypt_text.txt
        with open("encrypt_text.txt", 'w+') as file:
            file.write(encrypt_text)
            print("\n\n" + "Encrypted has been successful.")
            file.seek(0)
            enc_text = file.read()

        print("\n\n"+ "The raw text are: " + "\n")
        print(raw_text)
        print("\n\n"+ "The Encrypted text are: " + "\n")
        print(enc_text)

        # Decrypting the content of the file 'encrypt_text.txt'.
        encrypted_line = enc_text.strip()
        decrypt_text = decrypt(encrypted_line, shift1, shift2)

        # writing the decrypted text in the file Decryption_text.txt 
        with open("Decryption_text.txt", 'w+') as file:
            file.write(decrypt_text)
            file.seek(0)
            decrypted_text = file.read()

        print("\n\n" + "The Decrypted text is: " + "\n")
        print(decrypted_text)
        print("\n\n")

        # Comparison of the texts in the file raw_text.txt and Decryption_text.txt
        file1 = "raw_text.txt"
        file2 = "Decryption_text.txt"
        compare(file1, file2)

    except FileNotFoundError as e:
        print("Error: {e}")

if __name__ == "__main__":
    main()