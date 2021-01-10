#  SkyNet Part 1: Security Essentials

1. Implements Diffie-Hellman algorithm for key exchange.
2. Uses AES in Cipher FeedBack (CFB) for confidentiality.
3. Uses SHA-256 for HMAC Integrity Verification
4. Uses timestamps & timeouts to prevent Replay Attacks

#  Solo Mode ========================

[+] Welcome to SkyNet
[+] Loading OS

+----------------------------------------+
|            SkyNet Commands             |
|                                        |
| p2p echo - Peer to Peer Echo           |
| p2p upload - Peer to Peer File Upload  |
| upload - Upload File to Server         |
| download - Download File from Server   |
| mine - Mine for Bitcoins               |
| harvest - Harvest User Credentials     |
| list - Show List of Files              |
| exit, quit - Exit Network              |
+----------------------------------------+

Checking Port 1337

[+] Waiting for new messages
[+] Enter command: download
[+] Enter Filename: hello.fbi
[+] File Download Starting
[-] The file has not been signed by the botnet master

[+] Enter command: download
[+] Enter Filename: hello.signed
[+] File Download Starting
[+] Stored the received file as hello.signed

[+] Enter command: upload
[+] Enter Filename: test.de
[+] File Upload Starting
[+] Saved valuables to pastebot.net/test.de for the botnet master

[+] Enter command: mine
[+] Bitcoin Mining Starting
[+] Mined and found Bitcoin address: 304EUL0fBFDRPGzVCWhsHVUbZVtbvmQSMks

[+] Enter command: harvest
[+] Harvesting User Credentials Started
[+] Found credentials ('Jenny', 'oebcLjD1OUw')

[+] Enter command: list
[+] List of Files
[+] Files stored by this bot: hello.signed
[+] Valuables stored by this bot: ['Bitcoin: 304EUL0fBFDRPGzVCWhsHVUbZVtbvmQSMks', 'Username/Password: Jenny oebcLjD1OUw']

[+] Enter command: exit
[+] Exiting Network


#  Peer Mode ========================

#  Bot 1 >>>>>>>>>>>>>>>>>>>>>>>>>>>>

[+] Welcome to SkyNet
[+] Loading OS

+----------------------------------------+
|            SkyNet Commands             |
|                                        |
| p2p echo - Peer to Peer Echo           |
| p2p upload - Peer to Peer File Upload  |
| upload - Upload File to Server         |
| download - Download File from Server   |
| mine - Mine for Bitcoins               |
| harvest - Harvest User Credentials     |
| list - Show List of Files              |
| exit, quit - Exit Network              |
+----------------------------------------+

Port Unavailable
Checking Port 1338

[+] Waiting for new messages
[+] Enter command: p2p echo
[+] P2P Echo Engine Starting

[+] Locating other cyber-attack bots
[+] Found bot on port 1337
[+] Packet Timestamp Verified
[+] Shared hash: b3a4e1ea0bf49df7d6715ab6bacd6fd6ff77cffa500382270eccaff04bd050e8
[+] Original data: ECHO
[+] Encrypted data: b'\x8e\xb3\x8f6\xa9|\x06u\xae\x85\xa19T\xedZ~1\x94[\xf5\xf4\x81!\x9c\x86I\xda\xddp#):D\x06h\x06\xd9\xad\x1ao\x0e\xe6\xad\xee\xf7\xca\xb2"7\x84\xe5C{\xa9f\xa7\xea\xf08y\xef\xadmC\xb6\x80&~\x8b\xb1Q\xeb6\r\xe6\x10'
[+] HMAC Signature b'06:19:39f8f21d8f80254658652562c9fc2ee26028cec59cc6cd5ba25869571c92420bd6ECHO'
[+] Message> Hello World of Cryptography
[+] Original data: Hello World of Cryptography
[+] Encrypted data: b'\xfd\t\x13\x98\x82\xf4\x8f\xc5\xfe@\x93Q\x80n\xf1\xff\xce\x8d\xd5\x88Y\xf9\xf3\xc6\xb6\x99\xe0\xa2\x1f\xba\x89\xd4\x1c\xe6\xca\xd3\xd1\xac\x8a\xf3\xce\xba\x10\xd1\x85\x08N\x8aV\x0b\xf7\x98\x17\xf6\xca\xf3^/\xb6DOG~*=j\xff<\x9fk\x91\xa0\xbc\xed<\xec\xad\x89\x81\xe2\xbc\xf7\xc7*\xcd\xaa\x9c\xb0\x05\xf8\xdf\xcd%1\xb5jd\x92~'
[+] HMAC Signature b'06:19:509315ff78ff5f58cf87b283ef7c76945fbe4968f2b66ef78f71a1bbc2cf8cb31eHello World of Cryptography'
[+] Encrypted data: b'"\xce\r\x0eQ\x9e\r\x9bI\xa8\xd5RB\xff\xe4\xc6\xd6}\xa2,\x1fv\xc1\xf7\xa6(<D\x16,Q\xef\x17\xd9\xba\xf0Q\xe2\xa6Uhdd\x87\xbf\xba\x88\xb6\xec\xe1\xa6/H\xad\x98,\xc8\x9c\x8an\xa8-\xf6@\xda\x19\'g\xbbq2r&Q$\xa7x/\xc2\xa0Mz\xd1\xfc\xc9\xeb\x98Of\x88\x88\xf1\x85Ow\x91\xe3\xd3q'
[+] Decrypted data: 06:19:519315ff78ff5f58cf87b283ef7c76945fbe4968f2b66ef78f71a1bbc2cf8cb31eHello World of Cryptography
[+] Timestamp: 06:19:51
[+] Message Authentication Successful
[+] MAC: b'9315ff78ff5f58cf87b283ef7c76945fbe4968f2b66ef78f71a1bbc2cf8cb31e'
[+] Actual Data: Hello World of Cryptography
[+] Packet Timestamp Verified
[+] Message> This is the best cipher ever
[+] Original data: This is the best cipher ever
[+] Encrypted data: b'7\xc0J\x7fa\xeaz\xeeP5\xa6\xe8~]w\xf2\xec\xe6Ec1T +\x1a2\xb2\x837\xc5\x9a\xc9(\x08\xd7\xe4T\xe8\x87s\x1f\xe0\xb5[h<\xd6\xad\xa7\xbf\xe7\tF\xd7\x7fA\xfe\xb2)c\xf8\xbcd\xe2h\xfa\xb0&W\x89\xde1Fr\xf0;\xa0GL\xa2\xb4\xdfQ\x95|B\xcb\x0c\x1b\xb5\x9b\x96\xa9z!\x12\x10\xde\x19\xf3'
[+] HMAC Signature b'06:20:109441c9c741671d4435516ad7e7962c6c015fba9ba2c93829d6194d7e5d333a82This is the best cipher ever'
[+] Encrypted data: b'8\x0fp\x99Ry\xb0\xe6\x87\x14\xe2:\xf7X\x7f-[.gM\x88Bl\x08{\xf2>\xee\xd6\x15\xc5\x1c\xb9*/\xcd7\xa4\x93\x16\x17\x82\xbb\xcc\x0b\xa9\x18\xa8\xc0\xb1_<\xdc|\xc4c\x83\x90\xd3\x05\x86\x18{V\xa07D\xd4\xe2\x13{\xcc\x0cR\xc1\xeb\x1d\x7f\xb0Tm\xa0\xb8\xf5\x15\xc7$J\xef\xc1|\xee!\x18\x90(\xa7\xc3M]'
[+] Decrypted data: 06:20:109441c9c741671d4435516ad7e7962c6c015fba9ba2c93829d6194d7e5d333a82This is the best cipher ever
[+] Timestamp: 06:20:10
[+] Message Authentication Successful
[+] MAC: b'9441c9c741671d4435516ad7e7962c6c015fba9ba2c93829d6194d7e5d333a82'
[+] Actual Data: This is the best cipher ever
[+] Packet Timestamp Verified
[+] Message> exit
[+] Original data: exit
[+] Encrypted data: b'\xe0\x06\xe3\xcd\x8d\xb7.\xf0\xb1\xfeP%+R\xc7T\x15\xcc\x90\xf9\xaaz\x0eO\xc8\x7f\x1d?\xc9\xf8\x95?!\xd2\xfd~S\r\xf3MD\x0c\xffQ\xbe\xd4S\xcb\xa9\xed\xa91D\xdf\x016\x05\xdfx\xf7\xc6\xd5 /\x9d\x92\xd4\xcbZ\xbd\xd6\xa4[g\xa8X'
[+] HMAC Signature b'06:20:11aa2c92b45942043f69823f97d54d99ef33bbf756258684e5cddeb00961dd4d53exit'
[+] Encrypted data: b'x3\n\x1d\xe7\x8b\xd9z\xc1\x15\x1fi\xa1r*\x01\x96\xe3!\x98\x97l\xf0\xac\x8c\x10\xf2\x05\x06\x86X+\x11Z\xa4\x88\xba\xbf\xad\xe4\x95,<+\xddi\x88\xf9\x0c\x1d\xed\xcf\xa1\xb9U\x8e\xf9\x12;>\xec(\x9d\xf0q\xb0\xe1I\xe1\x18XTj\xa1\xf6:'
[+] Decrypted data: 06:20:11aa2c92b45942043f69823f97d54d99ef33bbf756258684e5cddeb00961dd4d53exit
[+] Timestamp: 06:20:11
[+] Message Authentication Successful
[+] MAC: b'aa2c92b45942043f69823f97d54d99ef33bbf756258684e5cddeb00961dd4d53'
[+] Actual Data: exit
[+] Packet Timestamp Verified
[+] Enter command: exit
[+] Exiting Network

#  Bot 2 >>>>>>>>>>>>>>>>>>>>>>>>>>>>

[+] Welcome to SkyNet
[+] Loading OS

+----------------------------------------+
|            SkyNet Commands             |
|                                        |
| p2p echo - Peer to Peer Echo           |
| p2p upload - Peer to Peer File Upload  |
| upload - Upload File to Server         |
| download - Download File from Server   |
| mine - Mine for Bitcoins               |
| harvest - Harvest User Credentials     |
| list - Show List of Files              |
| exit, quit - Exit Network              |
+----------------------------------------+

Checking Port 1337

[+] Waiting for new messages
[+] Enter command:
[+] New bot joined at ('127.0.0.1', 62367)

[+] Waiting for new messages
[+] Packet Timestamp Verified
[+] Shared hash: b3a4e1ea0bf49df7d6715ab6bacd6fd6ff77cffa500382270eccaff04bd050e8
[+] Encrypted data: b'\x8e\xb3\x8f6\xa9|\x06u\xae\x85\xa19T\xedZ~1\x94[\xf5\xf4\x81!\x9c\x86I\xda\xddp#):D\x06h\x06\xd9\xad\x1ao\x0e\xe6\xad\xee\xf7\xca\xb2"7\x84\xe5C{\xa9f\xa7\xea\xf08y\xef\xadmC\xb6\x80&~\x8b\xb1Q\xeb6\r\xe6\x10'
[+] Decrypted data: 06:19:39f8f21d8f80254658652562c9fc2ee26028cec59cc6cd5ba25869571c92420bd6ECHO
[+] Timestamp: 06:19:39
[+] Message Authentication Successful
[+] MAC: b'f8f21d8f80254658652562c9fc2ee26028cec59cc6cd5ba25869571c92420bd6'
[+] Actual Data: ECHO
[+] Packet Timestamp Verified
[+] Encrypted data: b'\xfd\t\x13\x98\x82\xf4\x8f\xc5\xfe@\x93Q\x80n\xf1\xff\xce\x8d\xd5\x88Y\xf9\xf3\xc6\xb6\x99\xe0\xa2\x1f\xba\x89\xd4\x1c\xe6\xca\xd3\xd1\xac\x8a\xf3\xce\xba\x10\xd1\x85\x08N\x8aV\x0b\xf7\x98\x17\xf6\xca\xf3^/\xb6DOG~*=j\xff<\x9fk\x91\xa0\xbc\xed<\xec\xad\x89\x81\xe2\xbc\xf7\xc7*\xcd\xaa\x9c\xb0\x05\xf8\xdf\xcd%1\xb5jd\x92~'
[+] Decrypted data: 06:19:509315ff78ff5f58cf87b283ef7c76945fbe4968f2b66ef78f71a1bbc2cf8cb31eHello World of Cryptography
[+] Timestamp: 06:19:50
[+] Message Authentication Successful
[+] MAC: b'9315ff78ff5f58cf87b283ef7c76945fbe4968f2b66ef78f71a1bbc2cf8cb31e'
[+] Actual Data: Hello World of Cryptography
[+] Packet Timestamp Verified
[+] Echo Data> b'Hello World of Cryptography'
[+] Original data: Hello World of Cryptography
[+] Encrypted data: b'"\xce\r\x0eQ\x9e\r\x9bI\xa8\xd5RB\xff\xe4\xc6\xd6}\xa2,\x1fv\xc1\xf7\xa6(<D\x16,Q\xef\x17\xd9\xba\xf0Q\xe2\xa6Uhdd\x87\xbf\xba\x88\xb6\xec\xe1\xa6/H\xad\x98,\xc8\x9c\x8an\xa8-\xf6@\xda\x19\'g\xbbq2r&Q$\xa7x/\xc2\xa0Mz\xd1\xfc\xc9\xeb\x98Of\x88\x88\xf1\x85Ow\x91\xe3\xd3q'
[+] HMAC Signature b'06:19:519315ff78ff5f58cf87b283ef7c76945fbe4968f2b66ef78f71a1bbc2cf8cb31eHello World of Cryptography'
[+] Encrypted data: b'7\xc0J\x7fa\xeaz\xeeP5\xa6\xe8~]w\xf2\xec\xe6Ec1T +\x1a2\xb2\x837\xc5\x9a\xc9(\x08\xd7\xe4T\xe8\x87s\x1f\xe0\xb5[h<\xd6\xad\xa7\xbf\xe7\tF\xd7\x7fA\xfe\xb2)c\xf8\xbcd\xe2h\xfa\xb0&W\x89\xde1Fr\xf0;\xa0GL\xa2\xb4\xdfQ\x95|B\xcb\x0c\x1b\xb5\x9b\x96\xa9z!\x12\x10\xde\x19\xf3'
[+] Decrypted data: 06:20:109441c9c741671d4435516ad7e7962c6c015fba9ba2c93829d6194d7e5d333a82This is the best cipher ever
[+] Timestamp: 06:20:10
[+] Message Authentication Successful
[+] MAC: b'9441c9c741671d4435516ad7e7962c6c015fba9ba2c93829d6194d7e5d333a82'
[+] Actual Data: This is the best cipher ever
[+] Packet Timestamp Verified
[+] Echo Data> b'This is the best cipher ever'
[+] Original data: This is the best cipher ever
[+] Encrypted data: b'8\x0fp\x99Ry\xb0\xe6\x87\x14\xe2:\xf7X\x7f-[.gM\x88Bl\x08{\xf2>\xee\xd6\x15\xc5\x1c\xb9*/\xcd7\xa4\x93\x16\x17\x82\xbb\xcc\x0b\xa9\x18\xa8\xc0\xb1_<\xdc|\xc4c\x83\x90\xd3\x05\x86\x18{V\xa07D\xd4\xe2\x13{\xcc\x0cR\xc1\xeb\x1d\x7f\xb0Tm\xa0\xb8\xf5\x15\xc7$J\xef\xc1|\xee!\x18\x90(\xa7\xc3M]'
[+] HMAC Signature b'06:20:109441c9c741671d4435516ad7e7962c6c015fba9ba2c93829d6194d7e5d333a82This is the best cipher ever'
[+] Encrypted data: b'\xe0\x06\xe3\xcd\x8d\xb7.\xf0\xb1\xfeP%+R\xc7T\x15\xcc\x90\xf9\xaaz\x0eO\xc8\x7f\x1d?\xc9\xf8\x95?!\xd2\xfd~S\r\xf3MD\x0c\xffQ\xbe\xd4S\xcb\xa9\xed\xa91D\xdf\x016\x05\xdfx\xf7\xc6\xd5 /\x9d\x92\xd4\xcbZ\xbd\xd6\xa4[g\xa8X'
[+] Decrypted data: 06:20:11aa2c92b45942043f69823f97d54d99ef33bbf756258684e5cddeb00961dd4d53exit
[+] Timestamp: 06:20:11
[+] Message Authentication Successful
[+] MAC: b'aa2c92b45942043f69823f97d54d99ef33bbf756258684e5cddeb00961dd4d53'
[+] Actual Data: exit
[+] Packet Timestamp Verified
[+] Echo Data> b'exit'
[+] Original data: exit
[+] Encrypted data: b'x3\n\x1d\xe7\x8b\xd9z\xc1\x15\x1fi\xa1r*\x01\x96\xe3!\x98\x97l\xf0\xac\x8c\x10\xf2\x05\x06\x86X+\x11Z\xa4\x88\xba\xbf\xad\xe4\x95,<+\xddi\x88\xf9\x0c\x1d\xed\xcf\xa1\xb9U\x8e\xf9\x12;>\xec(\x9d\xf0q\xb0\xe1I\xe1\x18XTj\xa1\xf6:'
[+] HMAC Signature b'06:20:11aa2c92b45942043f69823f97d54d99ef33bbf756258684e5cddeb00961dd4d53exit'
[-] Closing connection


