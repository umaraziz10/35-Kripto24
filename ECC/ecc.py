import argparse

def modinv(n,p):
    return pow(n, -1, p)

def quadraticResidues(n):
    store = []
    for i in range(1,7):
        res = pow(i, 2, n)
        print(res)
        if res not in store:
            store.append(res)
    
    store.sort()
    return store

def addition(x1,y1,x2,y2,a,p):
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    
    if x1 == x2 and y1 == y2:
        lamda_top = ((3 * pow(x1, 2)) + a)
        lamda_bot = modinv((2 * y1) % p, p)
        lamda = (lamda_top * lamda_bot) % p
    else:
        lamda_top = (y2 - y1)
        lamda_bot = modinv((x2 - x1) % p, p)
        lamda = (lamda_top * lamda_bot) % p
    
    x3 = (pow(lamda, 2) - x1 - x2) % p
    y3 = ((lamda * (x1 - x3)) - y1) % p

    return x3, y3

def encrypt(p,a,b,pt1,pt2,q,r,x1,y1,x2,y2):
    x1_start = x1
    y1_start = y1
    for i in range (1, q):
        x3, y3 = addition(x1,y1,x2,y2,a,p)
        x1 = x3
        y1 = y3

    res_y1 = x3,y3
    
    x1 = x1_start
    y1 = y1_start
    for i in range (1, r):
        x3_for_y2_res, y3_for_y2_res = addition(x1, y1, x2, y2, a, p)
        x1 = x3_for_y2_res
        y1 = y3_for_y2_res

    y2_res = x3_for_y2_res, y3_for_y2_res

    x2 = x3_for_y2_res
    y2 = y3_for_y2_res

    for i in range (1, q):
        final_x1, final_y1 = addition(x1, y1, x2, y2, a, p)
        x1 = final_x1
        y1 =  final_y1

    y3_res = final_x1, final_y1
    
    res_y2 = addition(pt1,pt2,final_x1,final_y1,a,p)

    return res_y1, res_y2

def decrypt(p,a,b,x1,y1,x2,y2,r):
    x1_start = x1
    y1_start = y1
    
    for i in range (1,r):
        res_x, res_y = addition(x1,y1,x1_start,y1_start,a,p)
        x1 = res_x
        y1 = res_y
    
    #reflect res
    res_temp = (res_x,-res_y % p)
    res = addition(x2,y2,res_temp[0],res_temp[1],a,p)
    
    return res


# x3,y3 = encrypt(11,1,6,10,9,3,7,2,7,2,7)
# print(x3,y3)

# pt = decrypt(11, 1, 6, 8, 3, 10, 2 , 7)
# print(pt)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Elliptic Curve Cryptography (ECC) basic demo.\n\n"
                    "Gunakan mode encrypt atau decrypt untuk menjalankan operasi.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", help="Pilih perintah yang ingin dijalankan")

    # --- ENCRYPT ---
    encrypt_parser = subparsers.add_parser(
        "encrypt",
        help="Melakukan enkripsi menggunakan ECC"
    )
    encrypt_parser.add_argument("p", type=int, help="Modulus prima (p)")
    encrypt_parser.add_argument("a", type=int, help="Koefisien a dari kurva eliptik")
    encrypt_parser.add_argument("b", type=int, help="Koefisien b dari kurva eliptik")
    encrypt_parser.add_argument("pt1", type=int, help="Koordinat x plaintext (Pt)")
    encrypt_parser.add_argument("pt2", type=int, help="Koordinat y plaintext (Pt)")
    encrypt_parser.add_argument("q", type=int, help="Konstanta enkripsi q (random integer)")
    encrypt_parser.add_argument("r", type=int, help="Kunci publik penerima (integer r)")
    encrypt_parser.add_argument("x1", type=int, help="Koordinat x dari titik pembangkit α")
    encrypt_parser.add_argument("y1", type=int, help="Koordinat y dari titik pembangkit α")
    encrypt_parser.add_argument("x2", type=int, help="Koordinat x dari kunci publik penerima β")
    encrypt_parser.add_argument("y2", type=int, help="Koordinat y dari kunci publik penerima β")

    # --- DECRYPT ---
    decrypt_parser = subparsers.add_parser(
        "decrypt",
        help="Melakukan dekripsi menggunakan ECC"
    )
    decrypt_parser.add_argument("p", type=int, help="Modulus prima (p)")
    decrypt_parser.add_argument("a", type=int, help="Koefisien a dari kurva eliptik")
    decrypt_parser.add_argument("b", type=int, help="Koefisien b dari kurva eliptik")
    decrypt_parser.add_argument("x1", type=int, help="Koordinat x dari cipher (C1)")
    decrypt_parser.add_argument("y1", type=int, help="Koordinat y dari cipher (C1)")
    decrypt_parser.add_argument("x2", type=int, help="Koordinat x dari cipher (C2)")
    decrypt_parser.add_argument("y2", type=int, help="Koordinat y dari cipher (C2)")
    decrypt_parser.add_argument("r", type=int, help="Kunci privat penerima (r)")

    args = parser.parse_args()

    if args.command == "encrypt":
        c1, c2 = encrypt(args.p, args.a, args.b, args.pt1, args.pt2, args.q, args.r, args.x1, args.y1, args.x2, args.y2)
        print(f"\nHasil Enkripsi:")
        print(f"C1 = {c1}")
        print(f"C2 = {c2}")

    elif args.command == "decrypt":
        pt = decrypt(args.p, args.a, args.b, args.x1, args.y1, args.x2, args.y2, args.r)
        print(f"\nHasil Dekripsi:")
        print(f"Plaintext = {pt}")

    else:
        parser.print_help()