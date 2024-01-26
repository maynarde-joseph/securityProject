from cryptography.fernet import Fernet
import base64
key = base64.urlsafe_b64encode(b"AMQABGAAXSHKALABRIAPIAWTGAFUAABV")
print(key)
message = "Hello World".encode()
key_obj = Fernet(key)
encrypted_message = key_obj.encrypt(message)
print(encrypted_message)
decrypted_message = key_obj.decrypt(encrypted_message)
print(decrypted_message)