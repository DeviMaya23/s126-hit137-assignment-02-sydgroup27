# HIT137 Assignment 2 - Question 1
#Author: Susmita Sharma

#Function to encrypt a single character
def encrypt_character(char, shift1, shift2):
    
    # Lowercase letters
    if char.islower():
        
        # First half (a-m)
        if 'a' <= char <= 'm':
            shift = shift1 * shift2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        
        # Second half (n-z)
        elif 'n' <= char <= 'z':
            shift = shift1 + shift2
            return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

    # Uppercase letters
    elif char.isupper():
        
        # First half (A-M)
        if 'A' <= char <= 'M':
            shift = shift1
            return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        
        # Second half (N-Z)
        elif 'N' <= char <= 'Z':
            shift = shift2 ** 2
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

    # Other characters remain unchanged
    return char
# Encryption Function
def encrypt_file(shift1, shift2):

    with open("raw_text.txt", "r") as file:
        content = file.read()

    encrypted_text = ""

    for char in content:
        encrypted_text += encrypt_character(char, shift1, shift2)

    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    print("Encryption completed successfully")



# Verification Function
def verify_files():

    with open("raw_text.txt", "r") as file:
        original = file.read()

    with open("decrypted_text.txt", "r") as file:
        decrypted = file.read()

    if original == decrypted:
        print("Verification Successful: Files Match")
    else:
        print("Verification Failed: Files Do Not Match")


