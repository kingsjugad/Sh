from sympy import mod_inverse, isprime
import random
import hashlib
from math import gcd

# Generate a random prime number between 50 and 200
def generate_prime():
    while True:
        num = random.randint(50, 200)
        if isprime(num):
            return num

# Pick a public exponent `e` such that gcd(e, phi) = 1
def pick_public_key(phi):
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            return e

# Generate public and private keys
def generate_key():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = pick_public_key(phi)
    d = pow(e,-1,phi)
    return (e, n), (d, n)

# Encrypt message using public/private key
def encrypt(message, key):
    e, n = key
    return [pow(ord(char), e, n) for char in message]

# Decrypt message using private/public key
def decrypt(cipher, key):
    d, n = key
    return ''.join([chr(pow(c, d, n)) for c in cipher])

def main():
    # Generate keys for Alice and Bob
    public_A, private_A = generate_key()
    public_B, private_B = generate_key()

    print("\n--- Key Information ---")
    print(f"Alice's Public Key: {public_A}")
    print(f"Alice's Private Key: {private_A}")
    print(f"Bob's Public Key: {public_B}")
    print(f"Bob's Private Key: {private_B}\n")

    # Alice sends a message
    print("--- Alice's Side ---")
    message = input("Enter a message to send: ")

    # Generate message hash
    msg_hash = hashlib.sha256(message.encode()).hexdigest()
    print(f"SHA-256 Hash: {msg_hash}")

    # Concatenate message with hash
    full_msg = message + "@" + msg_hash

    # Encrypt message using Bob's public key
    encrypted_msg = encrypt(full_msg, public_B)

    # Alice signs by encrypting the original message with her private key
    signature = encrypt(message, private_A)

    print("\nEncrypted Message Sent: ", encrypted_msg)
    print("Digital Signature Sent: ", signature)

    # Bob receives the message
    print("\n--- Bob's Side ---")
    decrypted_msg = decrypt(encrypted_msg, private_B)
    decrypted_signature = decrypt(signature, public_A)

    print(f"Decrypted Message: {decrypted_msg}")
    print(f"Verified Signature: {decrypted_signature}")

    if '@' in decrypted_msg:
        msg_part, hash_part = decrypted_msg.split('@')
        calculated_hash = hashlib.sha256(msg_part.encode()).hexdigest()

        print(f"\nReceived Hash: {hash_part}")
        print(f"Calculated Hash: {calculated_hash}")

        if hash_part == calculated_hash and msg_part == decrypted_signature:
            print("\n✓ Message Integrity Verified!")
            print("✓ Digital Signature Verified!")
        else:
            print("\n✗ Verification Failed: Message or Signature is Invalid.")
    else:
        print("\n✗ Invalid Message Format.")

if __name__ == "__main__":
    main()
