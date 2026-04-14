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
# Function to decrypt a single character
def decrypt_character(char, shift1, shift2):
    
    # Lowercase letters
    if char.islower():
        
        # First half (a-m)
        if 'a' <= char <= 'm':
            shift = shift1 * shift2
            return chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        
        # Second half (n-z)
        elif 'n' <= char <= 'z':
            shift = shift1 + shift2
            return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        # Uppercase letters
    elif char.isupper():
        
        # First half (A-M)
        if 'A' <= char <= 'M':
            shift = shift1
            return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        
        # Second half (N-Z)
        elif 'N' <= char <= 'Z':
            shift = shift2 ** 2
            return chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

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
    
    # Decryption Function
def decrypt_file(shift1, shift2):

    with open("encrypted_text.txt", "r") as file:
        content = file.read()

    decrypted_text = ""

    for char in content:
        decrypted_text += decrypt_character(char, shift1, shift2)

    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_text)

    print("Decryption completed successfully")
# Main Program
def main():

    try:
        shift1 = int(input("Enter shift1 value: "))
        shift2 = int(input("Enter shift2 value: "))

        encrypt_file(shift1, shift2)
        decrypt_file(shift1, shift2)
        verify_files()

    except ValueError:
        print("Please enter valid numbers")


# Run program
if __name__ == "__main__":
    main()
