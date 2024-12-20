import numpy as np

def encrypt(n, plainText):
    #mengambil input matriks kunci
    key = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(int(input("Input matriks kunci\n>>")))
        key.append(a)

    key = np.array(key)
    #mengkonversi karakter menjadi angka dan memasukkan kedalam list
    pt = []
    for char in plainText:
        value = ord(char) - 65
        pt.append(value)

    #mengkonversi list menjadi array
    pt = np.array(pt)

    #split setiap n karakter
    splittedPlaintext = pt.reshape(-1, n)

    #cek determinan matriks key
    det = round(np.linalg.det(key))
    
    #error checking
    if det % 26 == 0 or det % 26 == 13:
        print("Matriks kunci tidak memiliki invers: Hill cipher tidak bisa dilakukan")
        exit()

    encrypted = []
    for i in range(len(splittedPlaintext)):
        #perkalian matriks kunci dengan splitted matriks
        hasil = np.matmul(key, splittedPlaintext[i]) % 26
        #mengkonversi hasil menjadi karakter
        for j in range(len(hasil)):
            encrypted.append(chr(int(hasil[j]) + 65))

    cipherText = ''.join(encrypted)
    print("Ciphertext:", cipherText)

def decrypt(n, cipherText):
    key = []
    for i in range(n):
        a = []
        for j in range(n):
            a.append(int(input("Input matriks kunci\n>>")))
        key.append(a)

    key = np.array(key)

    det = round(np.linalg.det(key))
    inv = np.linalg.inv(key).T * det
    
    #error checking
    if det % 26 == 0 or det % 26 == 13:
        print("Matriks kunci tidak memiliki invers: Hill cipher tidak bisa dilakukan")
        exit()
    
    gcd, inverse, _ = extended_gcd(det % 26, 26)

    if inverse < 0:
        inverse += 26

    keyForDecrypt = (inv * inverse) % 26

    ct = []
    for char in cipherText:
        value = ord(char) - 65
        ct.append(value)

    #mengkonversi list menjadi array
    ct = np.array(ct)

    #split setiap n karakter
    splittedCiphertext = ct.reshape(-1, n)
    
    decrypted = []
    for i in range(len(splittedCiphertext)):
        hasil = np.matmul(keyForDecrypt,splittedCiphertext[i]) % 26
        for j in range(len(hasil)):
            decrypted.append(chr(round(hasil[j]) + 65))

    plainText = ''.join(decrypted)
    print("Plaintext:", plainText)

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Keluar")
        
        choice = input("Pilih opsi (1/2/3): ")
        
        if choice == '1':
            n = int(input("Berapa ukuran matriks kunci?\n>> "))
            plainText = input("Masukkan plaintext\n>> ").upper()  # Ensure uppercase for consistency
            encrypt(n, plainText)
        elif choice == '2':
            n = int(input("Berapa ukuran matriks kunci?\n>> "))
            cipherText = input("Masukkan ciphertext:\n>> ").upper()  # Ensure uppercase for consistency
            decrypt(n, cipherText)
        elif choice == '3':
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")