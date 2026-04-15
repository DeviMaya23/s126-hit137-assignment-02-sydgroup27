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
