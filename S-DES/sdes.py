import numpy as np

s0 = np.array([[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]])
s1 = np.array([[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]])

p10 = np.array([3,5,2,7,4,10,1,9,8,6])
p8 = np.array([6,3,7,4,8,5,10,9])
p4 = np.array([2,4,3,1])

ip = np.array([2,6,3,1,4,8,5,7])
ipInv = np.array([4,1,3,5,7,2,8,6])
ep = np.array([4,1,2,3,2,3,4,1])

def shiftLeft(amount, arrayList):
    return arrayList[amount:] + arrayList[:amount]

def swap(leftBits, rightBits):
    return rightBits + leftBits

def generateKeys(char):
    print("\nGENERATING KEYS...")
    charInt = ord(char)
    binary_digit = bin(charInt)[2:].zfill(8)
    masterKey = binary_digit + "01"
    print(f"[V] Masterkey => {masterKey}")
    newMasterKey = []

    for i in p10:
        newMasterKey.append(masterKey[i-1])

    ls1left = shiftLeft(1, newMasterKey[:5])
    ls1right = shiftLeft(1, newMasterKey[5:10])

    ls2left = shiftLeft(2, ls1left)
    ls2right = shiftLeft(2, ls1right)

    K1temp = ls1left + ls1right
    K2temp = ls2left + ls2right

    K1 = ""
    K2 = ""
    for i in p8:
        K1 += K1temp[i-1]
        K2 += K2temp[i-1]

    print(f"[V] K1 => {K1}")
    print(f"[V] K2 => {K2}\n")

    return K1, K2

def lastHalfBitProcess(leftBin, rightBin, key):
    leftBinFirst = leftBin

    rightBinEP = ""
    for i in ep:
        rightBinEP += rightBin[i-1]
    
    print(f"[V] 8 bits after EP => {rightBinEP}")

    resXOR = bin(int(rightBinEP,2) ^ int(key,2))[2:].zfill(8)
    print(f"[V] 8 bits after XOR with key => {resXOR}")
    leftBin = resXOR[:4]
    rightBin = resXOR[4:]

    leftRn = leftBin[0] + leftBin[3]
    rightRn = rightBin[0] + rightBin[3]

    leftCn = leftBin[1] + leftBin[2]
    rightCn = rightBin[1] + rightBin[2]

    leftBits = bin(s0[int(leftRn, 2), int(leftCn, 2)])[2:].zfill(2)
    rightBits = bin(s1[int(rightRn,2), int(rightCn,2)])[2:].zfill(2)
    
    resBits = leftBits + rightBits
    finalBits = ""
    for i in p4:
        finalBits += resBits[i-1]
    
    finalXOR = bin((int(finalBits, 2)) ^ (int(leftBinFirst, 2)))[2:].zfill(4)
    return finalXOR

def encrypt(pt, k1, k2):
    print(f"\nENCRYPTING START...")
    print(f"Encrypt for char: {pt}")
    ptInt = ord(pt)
    ptBin = bin(ptInt)[2:].zfill(8)
    
    newBin = ""
    for i in ip:
        newBin += ptBin[i-1]
    print(f"[V] After initial permutation => {newBin}")

    leftBinFirst = newBin[:4]
    rightBinFirst = newBin[4:]
    print(f"[V] Right 4 bits after IP => {rightBinFirst}\n")

    print(f"First process with K1...")
    firstFinalXOR = lastHalfBitProcess(leftBinFirst, rightBinFirst, k1)
    print(f"[V] 4 Right Bits After Processes => {firstFinalXOR}")
    firstFinalBits = swap(rightBinFirst, firstFinalXOR)
    print(f"[V] First final bits after swap => {firstFinalBits}\n")
    
    print(f"Second process with K2...")
    finalXOR = lastHalfBitProcess(rightBinFirst, firstFinalXOR, k2)
    print(f"[V] 4 Right Bits After Processes => {finalXOR}")
    finalByte = finalXOR + firstFinalXOR
    print(f"[V] Final bits => {finalByte}\n")

    resultByte = ""
    for i in ipInv:
        resultByte += finalByte[i-1]
    print(f"[V] Final Ciphertext in Bits => {resultByte}")
    print(f"ENCRYPTING FINISH...\n\n")

    return resultByte

def decrypt(ct, k1, k2):
    print(f"\nDECRYPTING START...")
    print(f"Decrypt for ciphertext: {ct}")

    newBits = ""
    for i in ip:
        newBits += ct[i-1]
    print(f"[V] After initial permutation => {newBits}")
    
    firstLeftBits = newBits[:4]
    firstRightBits = newBits[4:]
    print(f"[V] Right 4 bits after IP => {firstRightBits}\n")

    print(f"First process with K2...")
    firstFinalXOR = lastHalfBitProcess(firstLeftBits, firstRightBits, k2)
    print(f"[V] 4 Right Bits After Processes => {firstFinalXOR}")
    firstFinalBits = swap(firstFinalXOR, firstRightBits)
    print(f"[V] First final bits after swap => {firstFinalBits}\n")

    print(f"Second process with K1...")
    finalXOR = lastHalfBitProcess(firstRightBits, firstFinalXOR, k1)
    print(f"[V] 4 Right Bits After Processes => {finalXOR}")
    finalByte = finalXOR + firstFinalXOR
    print(f"[V] Final bits => {finalByte}\n")
    
    resultByte = ""
    for i in ipInv:
        resultByte += finalByte[i-1]
    
    hurufAkhir = chr(int(resultByte, 2))

    print(f"[V] Final Plaintext in Bits => {resultByte}")
    print(f"[V] Final Plaintext in Char => {hurufAkhir}")
    print(f"DECRYPTING FINISH...\n\n")
    
    return hurufAkhir

if __name__ == "__main__":
    exit_flag = False
    while not exit_flag:
        print("\nS-DES Symmetric Cryptography Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        option = input("\nChoose Option: ")
        match option:
            case "1":
                key = input("Insert Key: ")
                pt = input("Insert Plaintext (Char): ")
                k1, k2 = generateKeys(key)
                encrypt(pt, k1, k2)
            case "2":
                key = input("Insert Key: ")
                ct = input("Insert Ciphertext (Binary 8 Bit): ")
                k1, k2 = generateKeys(key)
                decrypt(ct, k1, k2)
            case "3":
                print("\n\nExiting...")
                print("Goodbyee!!!\n\n")
                exit_flag = True
            case _:
                print("Option not Available")