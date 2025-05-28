def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# User input
text = input("Enter text: ")
shift = int(input("Enter shift value: "))

# Encrypt
encrypted_text = caesar_cipher(text, shift)
print("Encrypted:", encrypted_text)

# Decrypt
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted:", decrypted_text)


