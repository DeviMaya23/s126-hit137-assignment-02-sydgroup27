# HIT137 Assignment 2 - Question 1
# Encryption and Decryption Program
def encrypt_character(char, shift1, shift2):

    if char.islower():

        if 'a' <= char <= 'm':
            shift = shift1 * shift2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        else:
            shift = shift1 + shift2
            return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

    elif char.isupper():

        if 'A' <= char <= 'M':
            shift = shift1
            return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

        else:
            shift = shift2 ** 2
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

    return char



def encrypt_file():
    pass


def decrypt_file():
    pass


def verify_files():
    pass


def main():
    pass


if __name__ == "__main__":
    main()

