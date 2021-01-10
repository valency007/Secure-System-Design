import random
import time

from lib.helpers import generate_random_string

#Used as helper functions only. Its not cryptographically strong as it doesn't come anywhere near
#our encryption, decryption, key exchange or any of their auxillary processes

def bitcoin_mine(): #Generates a fake bitcoin address
    return random.choice("13") + generate_random_string(length=30)

def harvest_user_pass(): #generates a pair of FAKE user credentials - username, password pairs
    names = "Bob Tim Ben Adam Lois Julie Daniel Lucy Sam Stephen Matt Luke Jenny Becca".split()
    return random.choice(names), generate_random_string(length=10)
