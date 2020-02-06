import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
if __name__=='main':
    exit()
else:
    def password2key():
        password_provided=raw_input("Enter the Encryption Key: ")
        password=password_provided.encode()
        salt=b'\x82w\x0c@\x8fI\x8b\xdc\x89n\xe9\xaa\x85\xf0\xef\x7f'      		   				       
        kdf=PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000,backend=default_backend())
        key= base64.urlsafe_b64encode(kdf.derive(password))
        return key
