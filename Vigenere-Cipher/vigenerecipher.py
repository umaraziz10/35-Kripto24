def vigenere_encrypt(plainText, key):
    plainText = plainText.upper()
    key = key.upper()
    encrypted = ""
    key_repeat = (key * (len(plainText) // len(key) + 1))[:len(plainText)]
    
    for p, k in zip(plainText, key_repeat):
        if p.isalpha():
            encrypted += chr((ord(p) - 65 + ord(k) - 65) % 26 + 65)
        else:
            encrypted += p
    return encrypted


def vigenere_decrypt(cipherText, key):
    cipherText = cipherText.upper()
    key = key.upper()
    decrypted = ""
    key_repeat = (key * (len(cipherText) // len(key) + 1))[:len(cipherText)]
    
    for c, k in zip(cipherText, key_repeat):
        if c.isalpha():
            decrypted += chr((ord(c) - 65 - (ord(k) - 65) + 26) % 26 + 65)
        else:
            decrypted += c
    return decrypted


if __name__ == "__main__":
    plaintext = "MAAFTELATHEHEHE"
    key = "UMAR"

    print("Plaintext:", plaintext)
    print("Key:", key)

    ciphertext = vigenere_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)

    decrypted_text = vigenere_decrypt(ciphertext, key)
    print("Decrypted:", decrypted_text)
