
# Elliptic-curve cryptography (ECC)

This is implementation code of encrypt and decrypt of ECC algorithm

## How to use

Look for general help
```bash
  python3 ecc.py -h
```
It will looks like this
```bash
usage: ecc.py decrypt [-h] p a b x1 y1 x2 y2 r

positional arguments:
  p           Modulus prima (p)
  a           Koefisien a dari kurva eliptik
  b           Koefisien b dari kurva eliptik
  x1          Koordinat x dari cipher (C1)
  y1          Koordinat y dari cipher (C1)
  x2          Koordinat x dari cipher (C2)
  y2          Koordinat y dari cipher (C2)
  r           Kunci privat penerima (r)

options:
  -h, --help  show this help message and exit
```
Look help for encrypt
```bash
  python3 ecc.py encrypt -h
```

It will looks like this
```bash
usage: ecc.py encrypt [-h] p a b pt1 pt2 q r x1 y1 x2 y2

positional arguments:
  p           Modulus prima (p)
  a           Koefisien a dari kurva eliptik
  b           Koefisien b dari kurva eliptik
  pt1         Koordinat x plaintext (Pt)
  pt2         Koordinat y plaintext (Pt)
  q           Konstanta enkripsi q (random integer)
  r           Kunci publik penerima (integer r)
  x1          Koordinat x dari titik pembangkit α
  y1          Koordinat y dari titik pembangkit α
  x2          Koordinat x dari kunci publik penerima β
  y2          Koordinat y dari kunci publik penerima β

options:
  -h, --help  show this help message and exit
```

Look help for decrypt
```bash
  python3 ecc.py decrypt -h
```

It will looks like this
```bash
usage: ecc.py decrypt [-h] p a b x1 y1 x2 y2 r

positional arguments:
  p           Modulus prima (p)
  a           Koefisien a dari kurva eliptik
  b           Koefisien b dari kurva eliptik
  x1          Koordinat x dari cipher (C1)
  y1          Koordinat y dari cipher (C1)
  x2          Koordinat x dari cipher (C2)
  y2          Koordinat y dari cipher (C2)
  r           Kunci privat penerima (r)

options:
  -h, --help  show this help message and exit
```

## Usage/Examples

Encryption
```bash
  python3 ecc.py encrypt 11 1 6 10 9 3 7 2 7 2 7
```

Encryption
```bash
  python3 ecc.py decrypt 11 1 6 8 3 10 2 7
```