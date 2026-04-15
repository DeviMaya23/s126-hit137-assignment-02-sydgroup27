# Function to decrypt the content
"""
This function is the decryption function. In this function the encrypted text that is stored in the encryption_text.txt is decrypted.
"""
def decrypt(text, shift1, shift2):
    decrypted = ""
    for char in text:
        if char.isupper():
            if 'A' <= char <=  'M':
                decrypted += chr((ord(char) - ord('A') + shift1) %13 + ord('A')) 
            elif 'N' <= char <= 'z':
                shift = shift2 * shift2
                decrypted += chr((ord(char) - ord('N') - shift) %13 + ord('N'))
        elif char.islower():
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                decrypted += chr((ord(char) - ord('a') - shift) %13 + ord('a'))
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                decrypted += chr((ord(char) - ord('n') + shift) %13 + ord('n'))
        else:
            decrypted += char
    return decrypted
