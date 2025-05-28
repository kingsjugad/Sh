def gcd(a, b): 
    while b != 0:           
        a, b = b, a % b     
    return a 

def are_coprime(a, b): 
    return gcd(a, b) == 1

def affine_encrypt(plaintext, first_key, second_key): 
    ciphertext = "" 
    for char in plaintext: 
        if char.isalpha(): 
            char_index = ord(char.lower()) - ord('a')
            cipher_index = (first_key * char_index + second_key) % 26   
            cipher_char = chr(cipher_index + ord('a'))   

            if char.isupper():
                cipher_char = cipher_char.upper()
            ciphertext += cipher_char 
        else: 
            ciphertext += char 
    return ciphertext

def affine_decrypt(ciphertext, first_key, second_key): 
    first_key_inv = pow(first_key,-1,26)
    if first_key_inv is None: 
        return "Error: No modular inverse for the first key" 

    plaintext = "" 
    for char in ciphertext: 
        if char.isalpha(): 
            char_index = ord(char.lower()) - ord('a') 
            plain_index = (first_key_inv * (char_index - second_key)) % 26 
            plain_char = chr(plain_index + ord('a'))
         
            if char.isupper():
                plain_char = plain_char.upper()
            plaintext += plain_char 
        else: 
            plaintext += char 
    return plaintext


first_key = int(input("Enter the first key "))
second_key = int(input("Enter the second key: "))
plaintext = input("Enter the plaintext message: ")

if are_coprime(first_key, 26): 
    print("Keys are co-prime. Proceeding with encryption and decryption...")


    encrypted_message = affine_encrypt(plaintext, first_key, second_key) 
    print("Encrypted message:", encrypted_message) 

    decrypted_message = affine_decrypt(encrypted_message, first_key, second_key) 
    print("Decrypted message:", decrypted_message) 
else: 
    print(f"Error: The first key {first_key} is not co-prime with 26. Please choose another key.")