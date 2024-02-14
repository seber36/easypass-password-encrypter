import hashlib
import secrets

def encrypt_password(password):

    salt = secrets.token_hex(16)

    salted_password = password + salt

    salted_password_bytes = salted_password.encode('utf-8')
    hash_algorithm = hashlib.sha256()
    hash_algorithm.update(salted_password_bytes)
    hashed_password = hash_algorithm.hexdigest()

    return hashed_password, salt

password = input("enter password to encrypt: ")

encrypted_password, salt = encrypt_password(password)
print("Encrypted Password:", encrypted_password)
print("salt:", salt)
