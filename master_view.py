import os
import sys
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto import Random
from colorama import Fore, Style, init
init(convert=True)

def decrypt_valuables(f):
    ciphertext = f[256:] # Signature length = 256, I keep forgetting
    with open("master_private_key",'rb') as fi:
        key = RSA.importKey(fi.read())
    dsize = SHA256.digest_size
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(ciphertext)
    digest = SHA256.new(message[:-dsize]).digest()
    if digest==message[-dsize:]:
        print (Fore.GREEN +"[+] Botnet Master> File contents are as follows: \n" +Style.RESET_ALL)
        fcontent=message[:-dsize]
        decd = str(fcontent, 'ascii')
        print(decd)
    else:
        print (Fore.RED +"[-] Botnet Master> Invalid Signature or Bad Encryption" +Style.RESET_ALL)


if __name__ == "__main__": 
    fn = input("[+] Botnet Master> Enter File Name in pastebot.net to view: ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print(Fore.RED +"[-] Botnet Master> The given file doesn't exist on pastebot.net" +Style.RESET_ALL)
        sys.exit(0)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    decrypt_valuables(f)