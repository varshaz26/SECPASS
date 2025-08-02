import base64
from cryptography.fernet import Fernet
import logging
import traceback
from django.conf import settings

# Encrypts the password
def encrypt_password(password):
    try:
        password_str = str(password)
        cipher = Fernet(settings.ENCRYPT_KEY)
        encrypted_password = cipher.encrypt(password_str.encode('utf-8'))
        encrypted_password = base64.urlsafe_b64encode(encrypted_password).decode("utf-8")
        return encrypted_password
    except Exception as error:
        logging.error(f"Error during encryption: {error}")
        return None

# Decrypts the password
def decrypt_password(password):
    try:
        password = base64.urlsafe_b64decode(password)
        cipher = Fernet(settings.ENCRYPT_KEY)
        decrypted_password = cipher.decrypt(password).decode("utf-8")
        return decrypted_password
    except Exception as error:
        logging.error(f"Error during decryption: {error}")
        return None
