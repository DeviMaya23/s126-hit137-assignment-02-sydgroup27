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
    
