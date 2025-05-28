"""Diffie-Hellman Key Exchange with Prime & Primitive Root Validation"""

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  # Check all numbers from 2 to n-1
        if n % i == 0:
            return False
    return True


# Function to check if a number is a primitive root modulo p
def is_primitive_root(g, p):
    required_set = {num for num in range(1, p)}  # Set of numbers 1 to p-1
    generated_set = {pow(g, power, p) for power in range(1, p)}  
    return required_set == generated_set  # g is a primitive root if both sets match

# Get prime number p
while True:
    p = int(input("Enter a prime number for p: "))
    if is_prime(p):
        break
    else:
        print("❌ The number you entered is not a prime. Please enter a valid prime number.")

# Get primitive root g
while True:
    g = int(input(f"Enter a primitive root modulo {p}: "))
    if is_primitive_root(g, p):
        break
    else:
        print(f"❌ {g} is not a primitive root of {p}. Please enter a valid primitive root.")

# Get private numbers for Bob and Alice
bob_private_no = int(input("Bob, enter your private number: "))
alice_private_no = int(input("Alice, enter your private number: "))

# Compute public keys
A_bob = pow(g, bob_private_no, p)   # Bob's public key
B_alice = pow(g, alice_private_no, p)  # Alice's public key

# Compute shared secret keys
bob_private_key = pow(B_alice, bob_private_no, p)  # Bob computes shared key
alice_private_key = pow(A_bob, alice_private_no, p)  # Alice computes shared key

# Output public keys
print(f"\n🔓 Alice's Public Key (A): {A_bob}")
print(f"🔓 Bob's Public Key (B): {B_alice}")

# Output shared secret keys
print(f"\n🔐 Alice's Shared Secret Key: {alice_private_key}")
print(f"🔐 Bob's Shared Secret Key: {bob_private_key}")

# Verify that both keys match
assert alice_private_key == bob_private_key, "Error: Shared keys do not match!"
print("\n✅ Both keys match! Secure communication established.")