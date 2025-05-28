def encrypt(plaintext, key):
    result = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            pt = ord(char.lower()) - ord('a')
            k = ord(key[key_index % key_length]) - ord('a')
            ct = (pt + k) % 26
            if char.isupper():
                encrypted_char = chr(ct + ord('A'))
            else:
                encrypted_char = chr(ct + ord('a'))

            result += encrypted_char
            key_index += 1
        else:
            result += char

    return result


def decrypt(ciphertext, key):
    result = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            ct = ord(char.lower()) - ord('a')
            k = ord(key[key_index % key_length]) - ord('a')
            pt = (ct - k) % 26
            if char.isupper():
                decrypted_char = chr(pt + ord('A'))
            else:
                decrypted_char = chr(pt + ord('a'))

            result += decrypted_char
            key_index += 1
        else:
            result += char

    return result



plaintext = input("Enter the plain text: ")   
key = input("Enter the key: ")


ciphertext = encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)


decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
