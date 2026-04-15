# Function to compare the content of the two raw_text.txt and decryption_text.txt 
def compare(raw_file, decrypt_file):
    try:
        with open(raw_file, 'r') as file1, open(decrypt_file, 'r') as file2:
            raw = file1.read()
            decpt = file2.read()

        if len(raw) != len(decpt):
            print(f"There is a diiference in length of the files {raw_file} is {len(raw)} and {decrypt_file} is {len(decpt)}")

        min_len = min(len(raw), len(decpt))
        for i in range(min_len):
            if raw[i] != decpt[i]:
                print(f"There is difference in character {raw[i]} in {raw_file} and {decpt[i]} in {decrypt_file}")
        
        if raw == decpt:
            print(f"Both the files {raw_file} and {decrypt_file} are same.")
        else:
            print("File differs.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
