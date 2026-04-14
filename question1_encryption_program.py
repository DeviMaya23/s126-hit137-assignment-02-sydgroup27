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

def encrypt_file(shift1, shift2):

    with open("raw_text.txt", "r") as file:
        content = file.read()

    encrypted = ""

    for char in content:
        encrypted += encrypt_character(char, shift1, shift2)

    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted)

    print("Encryption completed")




if __name__ == "__main__":
    main()

