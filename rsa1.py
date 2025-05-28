def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keys():
    p = int(input("Enter the first prime number: "))
    q = int(input("Enter the second prime number: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    print("Enter a value for e that satisfies: (a) 1 < e < phi (b) gcd(e, phi) == 1")
    while True:
        e = int(input("Enter e: "))
        if 1 < e < phi and gcd(e, phi) == 1:
            break
        print("Invalid e, please try again.")

    d = pow(e, -1, phi)  # Compute modular inverse of e mod phi

    print(f"Public Key: (e={e}, n={n})")
    print(f"Private Key: (d={d}, n={n})")
    return e, d, n

e, d, n = generate_keys()
text=int(input("enter the plain text  "))
encrypted=pow(text,e,n)
print(encrypted)
decrypted=pow(encrypted,d,n)
print(decrypted)