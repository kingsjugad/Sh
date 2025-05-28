def rc4_ksa(key, s_size=256):
    key = [ord(c) for c in key]
    keylen = len(key)

    S = list(range(s_size))
    K = [key[i % keylen] for i in range(s_size)]

    j = 0
    for i in range(s_size):
        j = (j + S[i] + K[i]) % s_size
        S[i], S[j] = S[j], S[i]
    return S

def rc4_prga(S, data_length):
    i = 0
    j = 0
    keystream = []
    for _ in range(data_length):
        i = (i + 1) % len(S)
        j = (j + S[i]) % len(S)
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % len(S)
        keystream.append(S[t])
    return keystream

def rc4_encrypt_decrypt(input_text, key):
    S = rc4_ksa(key)
    keystream = rc4_prga(S, len(input_text))

    output = ''.join([chr(ord(c) ^ k) for c, k in zip(input_text, keystream)])
    return output

# 🔹 User Input
key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

# 🔐 Encryption
ciphertext = rc4_encrypt_decrypt(plaintext, key)
print("\nEncrypted (hex):", ciphertext.encode().hex())

# 🔓 Decryption (RC4 is symmetric, so same function)
decrypted_text = rc4_encrypt_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
