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