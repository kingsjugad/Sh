import hashlib

def encrypt_this_string(input_string):
    """
    Calculate the SHA-1 hash of the input string
    
    Args:
        input_string: The string to hash
        
    Returns:
        The hexadecimal representation of the hash
    """
    
    input_bytes = input_string.encode('utf-8')
    
    sha1_hash = hashlib.new('sha1')
    
    
    sha1_hash.update(input_bytes)
    

    hash_text = sha1_hash.hexdigest()
    
    return hash_text


if __name__ == "__main__":
    
   
    user_input = input("Enter a string to hash: ")

    hash_result = encrypt_this_string(user_input)
    print("\nSHA-1 hash: " + hash_result)