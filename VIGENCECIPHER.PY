def encrypt(plaintext, key):
    result = ""
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            k = ord(key[key_index % key_length]) - ord('a')
            if char.isupper():
                pt = ord(char) - ord('A')
                ct = (pt + k) % 26
                result += chr(ct + ord('A'))
            else:
                pt = ord(char) - ord('a')
                ct = (pt + k) % 26
                result += chr(ct + ord('a'))
            key_index += 1  # Only increment on alphabetic characters
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
            k = ord(key[key_index % key_length]) - ord('a')
            if char.isupper():
                ct = ord(char) - ord('A')
                pt = (ct - k) % 26
                result += chr(pt + ord('A'))
            else:
                ct = ord(char) - ord('a')
                pt = (ct - k) % 26
                result += chr(pt + ord('a'))
            key_index += 1
        else:
            result += char
    return result

# Main execution
plaintext = input("Enter the plain text: ")   
key = input("Enter the key: ")

ciphertext = encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)
