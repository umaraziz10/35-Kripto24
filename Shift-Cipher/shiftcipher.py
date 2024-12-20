def shift_encrypt(plainText, key):
    """
    Fungsi untuk mengenkripsi teks menggunakan Shift Cipher.
    """
    encrypted = ""
    for char in plainText:
        if char.isalpha():  # Hanya mengenkripsi huruf
            shift = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted += char  # Tidak mengenkripsi karakter non-huruf
    return encrypted


def shift_decrypt(cipherText, key):
    """
    Fungsi untuk mendekripsi teks menggunakan Shift Cipher.
    """
    decrypted = ""
    for char in cipherText:
        if char.isalpha():  # Hanya mengenkripsi huruf
            shift = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift - key) % 26 + shift)
        else:
            decrypted += char  # Tidak mengenkripsi karakter non-huruf
    return decrypted


if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            plainText = input("Enter the plaintext:\n>> ")
            key = int(input("Enter the shift key (0-25):\n>> "))
            cipherText = shift_encrypt(plainText, key)
            print(f"Ciphertext: {cipherText}")
        elif choice == '2':
            cipherText = input("Enter the ciphertext:\n>> ")
            key = int(input("Enter the shift key (0-25):\n>> "))
            plainText = shift_decrypt(cipherText, key)
            print(f"Plaintext: {plainText}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")
