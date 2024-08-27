## Implement Caesar Cipher {Task_01} Prodigy_Info tech Cybersecurity Internship ##
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged

    return encrypted_text
def decrypt(text, shift):
    return encrypt(text, -shift)
def main():
    print("Caesar Cipher Encryption/Decryption")

    while True:
        choice = input("Type 'encrypt' to encrypt, 'decrypt' to decrypt, or 'exit' to quit: ").lower()

        if choice == 'exit':
            print("Exiting the program.")
            break
        elif choice in ['encrypt', 'decrypt']:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value: "))

            if choice == 'encrypt':
                result = encrypt(message, shift)
                print(f"Encrypted message: {result}")
            elif choice == 'decrypt':
                result = decrypt(message, shift)
                print(f"Decrypted message: {result}")
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
