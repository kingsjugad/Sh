def encrypt(plaintext, rail):
    # Create a list to store characters for each rail
    rail_lines = []
    for i in range(rail):
        rail_lines.append('')     

    row = 0
    direction_down = True

    for ch in plaintext:
        rail_lines[row] += ch

        # Change direction when top or bottom rail is reached
        if row == 0:
            direction_down = True
        elif row == rail - 1:
            direction_down = False

        # Move up or down
        if direction_down:
            row += 1
        else:
            row -= 1

    # Combine all rows to get the final ciphertext
    return ''.join(rail_lines)


def decrypt(ciphertext, rail):
    # Step 1: Create a matrix with placeholders '.'
    matrix = []  
    for i in range(rail):
        row_list = []                           
        for j in range(len(ciphertext)):      
            row_list.append('.')
        matrix.append(row_list)

    # Step 2: Mark zigzag path with '*'
    row = 0
    direction_down = True
    for col in range(len(ciphertext)):   
        matrix[row][col] = '*'

        if row == 0:
            direction_down = True
        elif row == rail - 1:
            direction_down = False

        if direction_down:
            row += 1
        else:
            row -= 1

    # Step 3: Fill matrix with ciphertext characters
    index = 0
    for i in range(rail):  
        for j in range(len(ciphertext)): 
            if matrix[i][j] == '*' and index < len(ciphertext):
                matrix[i][j] = ciphertext[index]
                index += 1

    # Step 4: Read message in zigzag pattern
    result = ''
    row = 0
    direction_down = True
    for col in range(len(ciphertext)):
        result += matrix[row][col]

        if row == 0:
            direction_down = True
        elif row == rail - 1:
            direction_down = False

        if direction_down:
            row += 1
        else:
            row -= 1

    return result


# Input from user
plaintext = input("Enter the plain text: ")
rail = int(input("Enter the number of rails: "))

# Encrypt and Decrypt
encrypted = encrypt(plaintext, rail)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, rail)
print("Decrypted:", decrypted)

