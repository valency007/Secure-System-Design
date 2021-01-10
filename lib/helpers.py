import random
import string

def read_hex(data): #Used this to read that big hex prime number
    data = data.replace(" ", "").replace("\n", "")
    return int(data, 16)

#Used as a helper function only. Its not cryptographically strong as it doesn't come anywhere near
#our encryption, decryption, key exchange or any of their auxillary processes
def generate_random_string(alphabet=None, length=8, exact=False): #Generates a random string
    if not alphabet:
        alphabet = string.ascii_letters + string.digits
    if not exact:
        length = random.randint(length-4 if length-4 > 0 else 1,length+4)
    return ''.join(random.choice(alphabet) for x in range(length))
