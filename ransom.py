import os
from crypto.PublicKey import RSA
from crypto.Cipher import PKCS1_OAEP

# Generate an RSA key pair
key = RSA.generate(2048)

# Define the file extension to be encrypted and decrypted
ext = '.txt'


##############################################################################################
# Define a function to encrypt a file
def encrypt_file(file_path):
    # Read the contents of the file
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    # Create an RSA cipher object using the public key
    cipher = PKCS1_OAEP.new(key.publickey())

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)

    # Write the encrypted data to a new file
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as f:
        f.write(ciphertext)

    # Delete the original unencrypted file
    os.remove(file_path)
##############################################################################################


##############################################################################################
# Define a function to decrypt a file
def decrypt_file(file_path):
    # Read the contents of the encrypted file
    with open(file_path, 'rb') as f:
        ciphertext = f.read()

    # Create an RSA cipher object using the private key
    cipher = PKCS1_OAEP.new(key)

    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)

    # Write the decrypted data to a new file
    decrypted_file_path = file_path[:-10] # remove '.encrypted' from the file name
    with open(decrypted_file_path, 'wb') as f:
        f.write(plaintext)

    # Delete the encrypted file
    os.remove(file_path)
##############################################################################################


# Encrypt all files with the given extension in a directory
dir_path = 'C:/Users/sam/Desktop/test'

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(ext):
            file_path = os.path.join(root, file)
            encrypt_file(file_path)

# Decrypt all encrypted files with the given extension in a directory
'''
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(ext + '.encrypted'):
            file_path = os.path.join(root, file)
            decrypt_file(file_path)
'''
