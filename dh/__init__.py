from Crypto.Random import random
from Crypto.Cipher import AES
from Crypto import Random
from Cryptodome.Util import Padding
from Cryptodome.Hash import HMAC
from Crypto.Hash import SHA256
from datetime import datetime, time
import time

def read_hex(data): #Reads the huge hex prime number
    data = data.replace(" ", "").replace("\n", "")
    return int(data, 16)

#Selected 2048 bit as it was more secure than the inbuilt version of 1536 bits. 
#Also, 1024 bit prime factorisation is extremely hard by itself, so 2048 is secure
#Prime Number selected from RFC 3526

prime = """FFFFFFFF FFFFFFFF C90FDAA2 2168C234 C4C6628B 80DC1CD1 
      29024E08 8A67CC74 020BBEA6 3B139B22 514A0879 8E3404DD
      EF9519B3 CD3A431B 302B0A6D F25F1437 4FE1356D 6D51C245
      E485B576 625E7EC6 F44C42E9 A637ED6B 0BFF5CB6 F406B7ED
      EE386BFB 5A899FA5 AE9F2411 7C4B1FE6 49286651 ECE45B3D
      C2007CB8 A163BF05 98DA4836 1C55D39A 69163FA8 FD24CF5F
      83655D23 DCA3AD96 1C62F356 208552BB 9ED52907 7096966D
      670C354E 4ABC9804 F1746C08 CA18217C 32905E46 2E36CE3B
      E39E772C 180E8603 9B2783A2 EC07A28F B5C55DF0 6F4C52C9
      DE2BCBF6 95581718 3995497C EA956AE5 15D22618 98FA0510
      15728E5A 8AACAA68 FFFFFFFF FFFFFFFF"""

PRIME = read_hex(prime)
GENERATOR = 2 #As defined in RFC 3526

class DiffieHellmanKeyExchange:
    def __init__(self, key_length=1024):
        self.key_length = max(1024, key_length)
        self.prime = PRIME
        self.generator = GENERATOR

    def generate_private_key(self, length): #generates user private key
        _bytes = length // 8 + 8
        self.private_key = random.getrandbits(length)

    def generate_public_key(self): #generates user public key
        self.public_key = pow(self.generator, self.private_key, self.prime)

    def generate_secret(self, public_key, private_key): #Generates the secret key
        self.shared_secret = pow(public_key, private_key, self.prime)
        shared_secret_bytes = self.shared_secret.to_bytes(self.shared_secret.bit_length() // 8 + 1, byteorder='big')
        hash_alg = SHA256.new() 
        hash_alg.update(bytes(shared_secret_bytes))
        self.key = hash_alg.hexdigest()

def create_dh_key(): #Creates a secret key for both the bots
    a = DiffieHellmanKeyExchange()
    a.generate_private_key(2048)
    a.generate_public_key()
    return (a.public_key, a.private_key)

def calculate_dh_secret(their_public, my_private): #passes on the secret key to both the bots
    a = DiffieHellmanKeyExchange()
    a.generate_secret(their_public, my_private)
    return a.key
