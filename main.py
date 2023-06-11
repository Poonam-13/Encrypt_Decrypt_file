from cryptography.fernet import Fernet

def generate_key():
    """Generate a random encryption key"""
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    """Encrypt the file using the provided key"""
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(file_path, key):
    """Decrypt the file using the provided key"""
    cipher = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    decrypted_data = cipher.decrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Example usage
file_path = 'example.txt'
encryption_key = generate_key()

print("Original file content:")
with open(file_path, 'r') as file:
    print(file.read())

encrypt_file(file_path, encryption_key)

print("\nFile encrypted!")

print("\nEncrypted file content:")
with open(file_path, 'rb') as file:
    print(file.read())

decrypt_file(file_path, encryption_key)

print("\nFile decrypted!")

print("\nDecrypted file content:")
with open(file_path, 'r') as file:
    print(file.read())
