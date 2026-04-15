# Function to encrypt the content
def encrypt(text, shift1, shift2):
    encrypted = ""
    for char in text:
        ''' 
        Checking the condition that the text is Captial aplhabet or not. 
        If the aplhabet lies between (A-M) then the character is shifted backward by the shift1 value.
        Encryption is done between (A-M) only, and the alphabets don't exceed than M.
        If the alphabet is captila and lies between (N-Z) then the character is shifted forward by the addition of the shift1 and shift2 value
        '''
        if char.isupper():
            if 'A' <= char <=  'M':
                encrypted += chr((ord(char) - ord('A') - shift1) %13 + ord('A')) 
            elif 'N' <= char <= 'z':
                shift = shift2 * shift2
                encrypted += chr((ord(char) - ord('N') + shift) %13 + ord('N'))
        elif char.islower():
            if 'a' <= char <= 'm':
                shift = shift1 * shift2
                encrypted += chr((ord(char) - ord('a') + shift) %13 + ord('a'))
            elif 'n' <= char <= 'z':
                shift = shift1 + shift2
                encrypted += chr((ord(char) - ord('n') - shift) %13 + ord('n'))
        else:
            encrypted += char
    return encrypted



