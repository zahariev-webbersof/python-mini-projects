from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
encrypt_token = f.encrypt(b"A really secret message. Not for prying eyes.")
print(encrypt_token)

decrypt_token = f.decrypt(encrypt_token)
print(decrypt_token)