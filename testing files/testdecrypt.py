from cryptography.fernet import Fernet
import base64
import os

key = base64.urlsafe_b64encode(b"AMQABGAAXSHKALABRIAPIAWTGAFUAABV")
key_obj = Fernet(key)

def decrypt_file(input_file, output_file):
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
        decrypted_data = key_obj.decrypt(encrypted_data)
    
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

encrypted_file = 'a.txt'
decrypted_file = 'decrypted.txt'

if os.path.exists(decrypted_file):
  os.remove(decrypted_file)

decrypt_file(encrypted_file, decrypted_file)

if os.path.exists(encrypted_file):
  os.remove(encrypted_file)