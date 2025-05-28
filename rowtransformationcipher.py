import math

def encrypt(plain, key):
    key = [int(k) for k in key]  # Convert key to list of integers  [2,1,3,4]
    cols = len(key)
    rows = -(-len(plain) // cols)  # Ceiling division prathamtyagi 14/4  4

    # Padding with 'X' to fill the matrix
    while len(plain) < rows * cols:
        plain += 'X'

    # Fill the matrix row-wise
    matrix = []
    i = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(plain[i])
            i += 1
        matrix.append(row)

    # Read the matrix columns in the order defined by the sorted key
    key_with_index = [(key[i], i) for i in range(cols)]  
    sorted_key = sorted(key_with_index)

    cipher = ''
    for _, col_index in sorted_key:
        for row in matrix:
            cipher += row[col_index]

    return cipher


def decrypt(cipher, key):
    key = [int(k) for k in key]
    cols = len(key)
    rows = -(-len(cipher) // cols)

    # Create an empty matrix
    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    # Sort key to get column order
    sorted_key = sorted([(num, idx) for idx, num in enumerate(key)])

    # Fill the matrix column-wise in the sorted key order
    i = 0
    for _, col_index in sorted_key:
        for r in range(rows):
            if i < len(cipher):
                matrix[r][col_index] = cipher[i]
                i += 1

    # Read the matrix row-wise to get the plain text
    plain = ''
    for row in matrix:
        plain += ''.join(row)

    return plain.rstrip('X')  # Remove padding


# ==== USER INPUT ====
plaintext = input("Enter plaintext: ").replace(" ", "")
key = input("Enter numeric key (e.g., 4312): ")

cipher = encrypt(plaintext, key)
print("Encrypted:", cipher)

decrypted = decrypt(cipher, key)
print("Decrypted:", decrypted)
