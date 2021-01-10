import sys
import os
from Crypto.Signature import PKCS1_PSS
from Cryptodome.Hash import SHA256
from Cryptodome.PublicKey import RSA
from Cryptodome import Random
from colorama import Fore, Style, init
init(convert=True)

def generate_keys():
    keys = RSA.generate(2048)  # Because 4096 bit keys took 3 mins to generate. This took 20 secs
    public_key = keys.publickey().export_key(format='PEM', pkcs=1)  # Index of 1 available to public keys
    private_key = keys.export_key(format='PEM', pkcs=8) # Index of 8 available to private keys only 
    with open('master_public_key','wb') as f:
        f.write(public_key)
    with open('master_private_key', 'wb') as f:
        f.write(private_key)


def sign_file(f):
    with open("master_private_key",'rb') as fi:
        private_key = RSA.importKey(fi.read())
    hashed_msg = SHA256.new()
    hashed_msg.update(f)
    signature = PKCS1_PSS.new(private_key).sign(hashed_msg)
    #print(len(signature)) # From this, I deduced that the sign length was 256 bits. (Silly me, should've seen the documentation)
    #print("Signature: "+str(signature)) # Check the signature by uncommenting this line
    return signature + f


if __name__ == "__main__":
    if not os.path.exists("master_public_key") or not os.path.exists("master_private_key"):
        print(Fore.RED +"[-] Botnet Master> No existing RSA keys found. Generating new keys!" +Style.RESET_ALL)
        generate_keys()
    fn = input("[+] Botnet Master> Which file in pastebot.net should be signed? ")
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print(Fore.RED +"[-] Botnet Master> The given file doesn't exist on pastebot.net" +Style.RESET_ALL)
        sys.exit(0)
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    signed_f = sign_file(f)
    signed_fn = os.path.join("pastebot.net", fn + ".signed")
    out = open(signed_fn, "wb")
    out.write(signed_f)
    out.close()
    print(Fore.GREEN +"[+] Botnet Master> Signed file written to " + str(signed_fn) + Style.RESET_ALL)
