from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

key = b"H" * 32
IV = b"H" * 16

cipher = AES.new(key, AES.MODE_CBC, IV)

message = "Hello"
paddedmessage = Padding.pad(message.encode(), 16)
encrypted = cipher.encrypt(paddedmessage)

print(encrypted)

decipher = AES.new(key, AES.MODE_CBC, IV)
paddeddecrypted = decipher.decrypt(encrypted)
unpaddedencrypted = Padding.unpad(paddeddecrypted, 16)

print(unpaddedencrypted.decode())
