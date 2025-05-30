import numpy as np

# Function to generate the key matrix from a key string
def getKeyMatrix(key):
    keyMatrix = np.zeros((2, 2), dtype=int)
    k = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = ord(key[k]) % 65  # Convert A-Z to 0-25
            k += 1
    return keyMatrix

# Encrypt function: Performs matrix multiplication
def encrypt(messageVector, keyMatrix):
    cipherMatrix = np.dot(keyMatrix, messageVector) % 26
    return cipherMatrix

# Function to perform Hill Cipher encryption
def HillCipher(message, key):
    if len(key) != 4:
        print("Invalid key! The key must be exactly 4 characters.")
        return

    if len(message) != 2:
        print("Invalid message length! The message must be exactly 2 characters.")
        return

    # Generate key matrix
    keyMatrix = getKeyMatrix(key)

    # Convert message to numeric vector
    messageVector = np.array([[ord(message[i]) % 65] for i in range(2)])

    # Encrypt the message
    cipherMatrix = encrypt(messageVector, keyMatrix)

    # Convert numbers back to letters
    cipherText = "".join(chr(int(num) + 65) for num in cipherMatrix.flatten())

    # Print the encrypted text
    print("Ciphertext:", cipherText)

# Driver Code
def main():
    # Take user input for message and key
    message = input("Enter a 2-letter message: ").upper()
    key = input("Enter a 4-letter key: ").upper()

    HillCipher(message, key)

if __name__ == "__main__":
    main()
