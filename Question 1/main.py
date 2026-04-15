
from encryption import encrypt
from decryption import decrypt
from compare import compare
# Operations for the input of the shift value and content of the file.

def main():
    try:
        # Givin the shif value to shift the data 
        shift1 = int(input("Enter the first shift value: "))
        shift2 = int(input("Enter  the second shift value: "))


        # creating the  file and inserting the text in the file 
        # raw_text = input("Write the file content: ")

        # Writing the content to be encrypted in the file raw_text.txt
        with open("raw_text.txt", 'r') as file:
            # file.write(raw_text)
            # file.seek(0)
            raw_text = file.read()
        print("\n\n"+"Sentences have been saved to 'raw_text.txt'")

        # Encrypting the content of the file using Encrypt function
        encrypt_text = encrypt(raw_text, shift1, shift2)

        # Writing the encrypted text in the file encrypt_text.txt
        with open("encrypt_text.txt", 'w+') as file:
            file.write(encrypt_text)
            print("\n\n" + "Encrypted has been sucessfull.")
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