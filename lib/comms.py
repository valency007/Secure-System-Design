
import struct
from Crypto import Random
from Crypto.Hash import HMAC
from Crypto.Cipher import AES
from lib.helpers import read_hex
from Crypto.Hash import SHA256
from datetime import datetime, time
import time

from dh import create_dh_key, calculate_dh_secret
import colorama
from colorama import Fore, Style, init

init(convert=True)

# For replay protection, we assume that bots over the network are out of sync by 30 secs
# Format the time stamp for replay attack protection (if packet arrives later than 30s, it will be discarded)
timestamp_format = "%H:%M:%S"
timestamp_format_len = 8

class StealthConn(object):
	def __init__(self, conn, client=False, server=False, verbose=False):
		self.conn = conn
		self.cipher = None
		self.client = client
		self.server = server
		self.verbose = verbose
		self.shared_hash = None
		self.last_message_time = datetime.utcnow().time().replace(microsecond=0) #Use the UTC time format
		self.initiate_session()

	def initiate_session(self):
		# Perform the initial connection handshake for agreeing on a shared secret
		self.verbose = True
		if self.server or self.client:
			my_public_key, my_private_key = create_dh_key()
			# Send them our public key
			self.send(str(my_public_key))
			# Receive their public key
			their_public_key = int(self.recv())
			# Obtain our shared secret
			self.shared_hash = calculate_dh_secret(their_public_key, my_private_key)
			if self.verbose:
				print(Fore.MAGENTA + "[+] Shared hash: {}".format(self.shared_hash) + Style.RESET_ALL) #Print the shared key
				self.shared_hash = bytes.fromhex(self.shared_hash)

		# Use AES in CFB mode for encryption as its more secure than ECB. Also AES is used by the US Government
		iv = self.shared_hash[:16] # set the initialization vector
		self.cipher = AES.new(self.shared_hash, AES.MODE_CFB, iv) # create cipher object

	def send(self, data):
		self.verbose = True
		# Sort out encoding problems
		try:
			if type(data) != type(b""):
				data = bytes(data,'utf-8')
		except UnicodeDecodeError:
			#print("Error was here 1")
			if type(data) != type(b""):
				data = bytes(data,'latin-1')


		#Create a HMAC and prepend it to the message
		if self.shared_hash != None:
			h = HMAC.new(self.shared_hash,digestmod=SHA256)
			h.update(data)
			try:
				mac_data = bytes(h.hexdigest() + data.decode("utf-8"),"utf-8")
			except UnicodeDecodeError:
				#print("Error was here 2")
				mac_data = bytes(h.hexdigest() + data.decode("latin-1"),"latin-1")
		else:
			mac_data = data
        
        # Add a timestamp to the message to prevent replay attacks
		timestr = str(datetime.utcnow().time().replace(microsecond=0))
		try:
			mac_data = bytes(timestr, 'utf-8') + mac_data # prepend it to the message
		except UnicodeDecodeError:
			#print("Error was here 3")
			mac_data = bytes(timestr, 'latin-1') + mac_data # prepend it to the message
            
		if self.cipher:
			self.cipher._next = [self.cipher.encrypt, self.cipher.decrypt]     # set AES for both encryption and decryption
			encrypted_data = self.cipher.encrypt(mac_data) # Encrypt the message
			try:
				print(Fore.MAGENTA +"[+] Original data: "+data.decode('utf-8').strip() + Style.RESET_ALL) # Display the original data
			except UnicodeDecodeError:
				#print("Error was here 4")
				print(Fore.MAGENTA +"[+] Original data: "+data.decode('latin-1').strip() + Style.RESET_ALL) # Display the original data
			print(Fore.MAGENTA +"[+] Encrypted data: {}".format(repr(encrypted_data)) + Style.RESET_ALL) # Display the encrypted data
			print(Fore.MAGENTA +"[+] HMAC Signature "+str(mac_data) + Style.RESET_ALL) # Display the appended timestamp, MAC and Data
		else:
			encrypted_data = mac_data

		# Encode the data's length into an unsigned two byte int ('H')
		pkt_len = struct.pack('H', len(encrypted_data))
		self.conn.sendall(pkt_len)
		self.conn.sendall(encrypted_data)


	def recv(self):
		self.verbose = True
		# Decode the data's length from an unsigned two byte int ('H')
		pkt_len_packed = self.conn.recv(struct.calcsize('H'))
		unpacked_contents = struct.unpack('H', pkt_len_packed)
		pkt_len = unpacked_contents[0]
		encrypted_data = self.conn.recv(pkt_len) # Recieve the message
		if self.cipher:
			self.cipher._next = [self.cipher.encrypt, self.cipher.decrypt]     # set AES for both encryption and decryption
			data = self.cipher.decrypt(encrypted_data) # Decrypt the message
			print(Fore.YELLOW +"[+] Encrypted data: {}".format(repr(encrypted_data))+ Style.RESET_ALL) # Display the encrypted data
			try:
				print(Fore.YELLOW +"[+] Decrypted data: "+data.decode('utf-8')+ Style.RESET_ALL) # Display the appended timestamp, MAC and Data
			except UnicodeDecodeError:
				#print("Error was here 5")
				print(Fore.YELLOW +"[+] Decrypted data: "+data.decode('latin-1')+ Style.RESET_ALL) # Display the appended timestamp, MAC and Data
			try:
				datas = data.decode('utf-8')
			except UnicodeDecodeError:
				#print("Error was here 6")
				datas = data.decode('latin-1')
			print(Fore.YELLOW +"[+] Timestamp: "+str(datas[:timestamp_format_len])+ Style.RESET_ALL) #Display timestamp
		else:
			data = encrypted_data

        # Remove timestamp and verify the message
		try:  
			tstamp = str(data[:timestamp_format_len], 'utf-8')
		except UnicodeDecodeError:
			#print("Error was here 7")
			tstamp = str(data[:timestamp_format_len], 'latin-1')
		data = data[timestamp_format_len:]
        
        # Perform HMAC verification for data integrity
		if self.shared_hash != None:
			h = HMAC.new(self.shared_hash, digestmod=SHA256)
			hmac = data[:h.digest_size*2] #Get the HMAC part of the message
			data = data[h.digest_size*2:] # Get the data part of the message
			h.update(data)
			try:
				if h.hexdigest() != str(hmac, 'utf-8'): # This means the message was tampered with
					print(Fore.RED +"[-] Bad message. Authentication Failed"+ Style.RESET_ALL)
				else:
					print(Fore.YELLOW +"[+] Message Authentication Successful" + Style.RESET_ALL)
					print(Fore.YELLOW +"[+] MAC: "+str(hmac)) #Display the MAC appended
					print(Fore.YELLOW +"[+] Actual Data: "+str(datas[timestamp_format_len+len(hmac):]) + Style.RESET_ALL) #Display the original data
			except UnicodeDecodeError:
				#print("Error was here 8")
				if h.hexdigest() != str(hmac, 'latin-1'): # This means the message was tampered with
					print(Fore.RED +"[-] Bad message. Authentication Failed"+ Style.RESET_ALL)
				else:
					print(Fore.YELLOW +"[+] Message Authentication Successful" + Style.RESET_ALL)
					print(Fore.YELLOW +"[+] MAC: "+str(hmac)) #Display the MAC appended
					print(Fore.YELLOW +"[+] Actual Data: "+str(datas[timestamp_format_len+len(hmac):]) + Style.RESET_ALL) #Display the original data

        
		msg_time = tstamp
		#time.sleep(2) #To simulate a timing replay attack. 
		#Change the value from 2 to greater than 31 and watch as the messages get discarded
		time_now = str(datetime.utcnow().time().replace(microsecond=0))
		times = str(datetime.strptime(time_now, timestamp_format) - datetime.strptime(msg_time, timestamp_format))
		interval = sum(x * int(t) for x, t in zip([3600, 60, 1], times.split(":"))) #Difference between time now and the timestamp on message
		if (interval>30):
			print(Fore.RED +"[-] Packet will be discarded (Replay Attack)"+ Style.RESET_ALL)
		else:
			print(Fore.YELLOW +"[+] Packet Timestamp Verified" + Style.RESET_ALL)
		self.last_message_time = msg_time # Update message time      
		return data

	def close(self): #Close the connection
		self.conn.close()