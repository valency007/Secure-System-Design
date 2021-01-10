Welcome to SkyNet :: Commanding the Legion
Part 2 :: Protecting the Castle

PS: This code sub-repository contains Part 1 + Part 2
======================================================

Usage -- uploading and viewing secrets
======================================

------ Uploading Valuables ------

C:\Users\Valency Colaco\Desktop\Project SKYNET\Part 1\Submission\Skynet Part 2>py bot.py

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

[+] Checking Port 1337

[+] Waiting for new messages
[+] Enter command: mine
[+] Bitcoin Mining Starting
[+] Mined and found Bitcoin address: 1iLWn8sTUI4TguqIsGpeOMGOSet

[+] Enter command: harvest
[+] Harvesting User Credentials Started
[+] Found credentials ('Tim', '4frJs1m8oor2')

[+] Enter command: upload
[+] Enter Filename: hello.test
[+] File Upload Starting
[+] Saved valuables to pastebot.net/hello.test for the botnet master

------ Viewing Secrets ------

C:\Users\Valency Colaco\Desktop\Project SKYNET\Part 1\Submission\Skynet Part 2>py master_view.py
[+] Botnet Master> Enter File Name in pastebot.net to view: hello.test.signed
[+] Botnet Master> File contents are as follows:

Bitcoin: 1iLWn8sTUI4TguqIsGpeOMGOSet
Username/Password: Tim 4frJs1m8oor2


Usage -- signing updates and downloading updates
================================================

------ Signing Updates ------

C:\Users\Valency Colaco\Desktop\Project SKYNET\Part 1\Submission\Skynet Part 2>py master_sign.py
[+] Botnet Master> Which file in pastebot.net should be signed? hello.test
[+] Botnet Master> Signed file written to pastebot.net\hello.test.signed

------ Downloading Signed Updates ------

C:\Users\Valency Colaco\Desktop\Project SKYNET\Part 1\Submission\Skynet Part 2>py bot.py

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

[+] Checking Port 1337

[+] Waiting for new messages
[+] Enter command: download
[+] Enter Filename: hello.test
[+] File Download Starting
[-] The file has not been signed by the botnet master

[+] Enter command: download
[+] Enter Filename: hello.test.signed
[+] File Download Starting
[+] Signature Verified. Stored the received file as hello.test.signed

[+] Enter command: list
[+] List of Files
[+] Files stored by this bot: hello.test.signed
[+] Valuables stored by this bot: []

[+] Enter command: exit
[+] Exiting Network

Usage -- p2p File Uploads between Bots
======================================

------ Activity on Bot 1 ------

C:\Users\Valency Colaco\Desktop\Project SKYNET\Part 1\Submission\Skynet Part 2>py bot.py

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

[+] Checking Port 1337

[+] Waiting for new messages
[+] Enter command: download
[+] Enter Filename: hello.test.signed
[+] File Download Starting
[+] Signature Verified. Stored the received file as hello.test.signed

[+] Enter command: p2p upload
[+] Enter Filename: hello.test.signed
[+] P2P Upload Starting
[+] Locating other cyber-attack bots
[+] Found bot on port 1338
[+] Packet Timestamp Verified
[+] Shared hash: 9d1111f12b1460c4e5d2d4e645769a07f43ddce6aa8d1dd2551d167bfee2a451
[+] Original data: FILE
[+] Encrypted data: b'\xe6\xc3\x84J\xe2\x04a\x08\xbc\x93\xb7\'\x99\xce\xa6Y\x961f\x08\xdc.u\xa5\xf8\x10\xbfw0l\xb5\xc1\x00*L\x02\x86\x8c:\xcbS\x89T\xe1\xaa\x98"\x18\x98)\x86\xb3\xf6$c\x892\x97\xf5\xe8w\x88e-2\xe1\xca\xde\xfeG\xc5UA\x02\x8df'
[+] HMAC Signature b'19:41:30cc7589626a5ee761ac73786dd528c0ecf4ebdfa14149852d7efc9c1ff80b499dFILE'
[+] Sending hello.test.signed via P2P

[+] Original data: hello.test.signed
[+] Encrypted data: b'-Pl\x97\x1f\xb2\xe1\x93\x84b\xa73\xa0\x01\xf4\xc0\xc1\xea2\xd3\x9a\xd7Z\xd5\r\x0ffDe\x86\x96Q\xf6\n\xb5\xda\xc4\xacl\x95Qw\x9ak\x0b!U\xbc\x18\x01\x86\xa3\xaa\x03Q\xe6:0$.\xd8\xa8\xce\td\xd5\xa5:\x0eR\xb5\xa9J}\xf9`\x93\x00T9\xac\x9a\x08\xd0p$\xaca)'
[+] HMAC Signature b'19:41:30735fd4b611b54201e18365f307879a0f2b409488d66be707290730983237dccchello.test.signed'
[+] Original data: F'+vÖU'ðMç.Ñpo=¡¨åÍãàsrc$§ý$ºW@õ«S9R÷y q5ÅõBån(Õ[D¼QeÔ³{õ0Âö#=?ï  nðTæ¢á¹ò¯Ò?È=ó4Vcûk1®zèäÑ±*öLl?¢Q¨¿¹QF7/uÓÕ>2Õ%m8Pé[ó°-²"aã´³¸&(¸LIHüíûbPá0v:åÕ4Eõi;ÛG8 ;Þ¾¨ºnéöm§XHà@E¢³áØQ:6w¤]±©~¬¾ÖÒ¹»n;`#¶ C(c%%iËláòå|3jè­3W%·fYsF<ëÞ!FÕ[ø±ÖDeïHÏìÃ>ñ6L¥x7éÞ)ùnÊó½ÄËÄ2Qù¨G±³´Ñ$©*dAÌÀf²ÌoVæ³!blbÒÏh ýEHWçµz{ÞâÕt2¸I®þyæ]²î#GýQ¯¿Ã¿p³V Øò^çNÅCåùtâa·mÌ§í¼>[å.ÉiLhá½7Û½ÏLG3¬!ÅJCµ×/°«Î:Àü.£ò¡EfSÉõ¬­
[+] Encrypted data: b'\xf4\x0f\xef\xcd\xbb\xf88\r%\x05\x90\xe07\xa0m{\x82\x1f\xcc\xee\r\x1d5?\xb2\x8e3\x00_\xd9\xbf7h\xd4G\xb8\x8b\x9d\xf2`\xa3\x14\xe1\x1a\xa4<\xdc\xf3hrh\xc6\xd5"v\xdd\'u\xd2\x04\r\xd3\x1ar\x1e\x89\xb8H<\xe0\x8b\xe5\x1f\xa8\x04\x85\x10\x7f=V\x1b]f\xf7<\x0e:\xbd-\x90i|\xf1\t8\xb5\r\xa3\xa6\xec\xfe\xd7WF\xc6\xfa\xcb\x83\xca\xb8E\xc34_\xd7@\x0c\xf6\xe5n\xd22s0\r_iN|\xfe\x9e\'\x87\r\x93c\x9c\xe77G\xec\x0b\xf49\xfcw\xdfdm\x05D\x81\xe0\x95\x97\xd6\xfa\xa2!\x0c\x0f!\x92\x90\x8b\x8b5\x00\xbem[\xe5\xf8\xb1\x9a\xdfc4<D@\xdb\x04\x8aT\xc8sF\xecC-\x98\x11\xdfrk\x0eKY\x9c\xb2b\xa5\xafEJt\xa0.\x8ak\xe7a\x80g\x16v4\xd4H\x1d\r\xb6\xf2[4VbL\x03\x7fw\xb6\xde\xcbk!\x0e\x8d\xd8P[\xb8\x90\xf4 \xafK\xb1\xdcK\x96\x12\xc6\xdf\xee\x1b\xf2Y\xe9\xabs\xab)\xed\xd8t\xab\xd5\xf9/\xddCt\'\xfa\x8f\x9b\x03o\x91\xae\x01\xdav\xf8\xd1l\x9f\x10\xe2\xd6(\x9c\t~a}\x08wP\xea\xde\x95c\xa0\xd5m\xb6\x04\xfc%\x8ep\xba/\x9d#KS\xa6/h\xfec\xca\x89(\xde\xd7\x81Sa6\x9f\x93\x1bG\xbe\xe7\\0\x1c)T\xc7\xae\rN\xebZ\xb0b-\x15w\x1c\xd2\xe7\xdb\x1d\x8e\x05\x0f(\xcd\xefG\x18b\xb4;m\x8af\x8b\x9e\xcc\x937"\x84\xb2\x07\xaax\x10mO\x0b\xeb\xfb\xa5\xb1\xd4\xc6\x07?\xd05\xdc\xc9\xcf\xae\xe950\x1a\xb4\x8fYy\x8e\xa2\x1ei\x14\x82\x0b\xd3R\xdc\x83\x88*B\xacn|\xea\xc4\xa4yl\x94M\xec\x16\x1f\x93\x80\xb5:8\x15~z}.\x9d\xd5\x0ed\xb7\x9e\xc0w\xd6\xa7\xb5\xad\x94d\xbd\xa4\xdbK\xc0u\x9dx\xc8\xaa?\xe8\xf9}W\xaeC\xbbr\xe5\xa7\x07z\xdb\x8ehq\xea\xc8\xbe\x9d\x91\xc1\x13f\x89\xa0\xf5 \xc3\x1f\x1a\xa9\xb8\xae\x8aA\x0b -\xa3\xda\x13\x9f\x8f\xc0\xc6:6\xa1\xda\xb2s\xe5\xa5\xfc\xc3\x80\xac\xdd9Y\xa3\xbd\x90\x95\xa1\x1f \xc2EG\x16L\xcf\x00\xc7|\x16(\xa0\xe2~\xf7]2\xa9\xfb\xf6\x17\xce3u\xa1\x9f*81q\xc8\x14\xe3a\x86\x86\x19\xc4\xb5\xdd&R'
[+] HMAC Signature b'19:41:30552d4c971004e6c946093a4d1f2e1d7a1684b423737ef5833be0775832c70167\x91F\'+v\xd6\x91U\x0b\'\xf0M\xe7.\x96\xd1p\x8do=\x8a\xa1\x0e\x98\x8a\x93\xa8\xe5\xcd\xe3\xe0s\x10rc\x9d$\xa7\x94\x7f\xfd$\xbaW\x9c@\x93\xf5\x10\x03\x17\xabS9\x02R\xf7y\xa0q5\x11\xc5\xf5B\xe5\x8dn(\x89\xd5[D\xbcQe\xd4\xb3{\x16\x07\xf5\x1b\x800\xc2\x10\xf6#=?\xef\tn\xf0T\xe6\xa2\xe1\xb9\x10\xf2\xaf\xd2?\xc8\x8c=\xf34Vc\xfbk1\xaez\xe8\xe4\xd1\x15\x8d\xb1\x8d\x19\x99*\xf6\x87Ll\x82?\xa2Q\xa8\xbf\xb9Q\x9f\x95F7/u\xd3\x11\xd5>2\xd5%m8\x01\x87P\xe9[\xef\x08\xf3\xb0\x95\x1f\x1d-\xb2"a\x9a\xe3\xb4\xb3\xb8\x89&\x83(\xb8LIH\xfc\x9a\xed\xfb\x9ab\x15P\xe10v:\x82\xe5\x95\xd5\x0c4E\xf5i;\xdb\x7fG8\x05\x96\xa0;\xde\xbe\x0c\xa8\xban\x0e\xe9\xf6m\xa7\x1aX\x02\x0bH\xe0@E\xa2\xb3\xe1\xd8Q:6\x1fw\x9c\xa4\x97\x8b]\xb1\xa9\x8f~\xac\x1e\xbe\xd6\xd2\xb9\xbbn\x91;`#\x1c\x1e\x9e\x80\xb6\x1a \x92C(c%%i\xcbl\xe1\x17\xf2\xe5\x8e|3j\xe8\x90\x8f\xad3W\x12\x06%\xb7fYsF\x95\x04<\xeb\xde!F\xd5[\xf8\xb1\xd6D\x05e\xefH\xcf\x87\xec\xc3>\x9d\xf16L\xa5x7\xe9\xde)\xf9\x8f\x0bn\xca\x1d\xf3\x1e\xbd\xc4\xcb\x83<\xf9\x91\r\xc42Q\xf9\xa8G\xb1\xb3\x91\x8f\xb4\xd1$\xa9*dA\xcc\x15\x04\x91\x19\xc0f\xb2\x87\xccoV\xe6\xb3!blb\xd2\xcf\x9eh\xa0\xfd\x1bEHW\xe7\xb5\x15z{\xde\xe2\xd5t2\xb8I\x1a\xae\xfey\xe6]\xb2\x83\xee#\x90G\xfdQ\x05\x7f\xaf\xbf\xc3\xbfp\x9c\xb3V \xd8\xf2^\xe7N\x8b\x08\xc5C\xe5\xf9t\x04\xe2\x97\x9ea\xb7m\xcc\xa7\xed\xbc>[\xe5\x88.\x06\xc9\x1e\x0biLh\x90\xe1\xbd7\xdb\xfcG\xd3\xda\x9eG3\xac\x1d!\xc5J\x9eC\xb5\xd7\x94/\xb0\xab\xce:\xc0\xfc.\xa3\xf2\xa1EfS\xc9\xf5\x86\x95\xac\xad\r\xbd\x89\xcfL'
[+] Enter command: exit
[+] Exiting Network


------ Activity on Bot 2 ------

C:\Users\Valency Colaco\Desktop\Project SKYNET\Part 1\Submission\Skynet Part 2>py bot.py

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

[-] Port Unavailable
[+] Checking Port 1338

[+] Waiting for new messages
[+] Enter command:
[+] New bot joined at ('127.0.0.1', 55086)

[+] Waiting for new messages
[+] Packet Timestamp Verified
[+] Shared hash: 9d1111f12b1460c4e5d2d4e645769a07f43ddce6aa8d1dd2551d167bfee2a451
[+] Encrypted data: b'\xe6\xc3\x84J\xe2\x04a\x08\xbc\x93\xb7\'\x99\xce\xa6Y\x961f\x08\xdc.u\xa5\xf8\x10\xbfw0l\xb5\xc1\x00*L\x02\x86\x8c:\xcbS\x89T\xe1\xaa\x98"\x18\x98)\x86\xb3\xf6$c\x892\x97\xf5\xe8w\x88e-2\xe1\xca\xde\xfeG\xc5UA\x02\x8df'
[+] Decrypted data: 19:41:30cc7589626a5ee761ac73786dd528c0ecf4ebdfa14149852d7efc9c1ff80b499dFILE
[+] Timestamp: 19:41:30
[+] Message Authentication Successful
[+] MAC: b'cc7589626a5ee761ac73786dd528c0ecf4ebdfa14149852d7efc9c1ff80b499d'
[+] Actual Data: FILE
[+] Packet Timestamp Verified
[+] Encrypted data: b'-Pl\x97\x1f\xb2\xe1\x93\x84b\xa73\xa0\x01\xf4\xc0\xc1\xea2\xd3\x9a\xd7Z\xd5\r\x0ffDe\x86\x96Q\xf6\n\xb5\xda\xc4\xacl\x95Qw\x9ak\x0b!U\xbc\x18\x01\x86\xa3\xaa\x03Q\xe6:0$.\xd8\xa8\xce\td\xd5\xa5:\x0eR\xb5\xa9J}\xf9`\x93\x00T9\xac\x9a\x08\xd0p$\xaca)'
[+] Decrypted data: 19:41:30735fd4b611b54201e18365f307879a0f2b409488d66be707290730983237dccchello.test.signed
[+] Timestamp: 19:41:30
[+] Message Authentication Successful
[+] MAC: b'735fd4b611b54201e18365f307879a0f2b409488d66be707290730983237dccc'
[+] Actual Data: hello.test.signed
[+] Packet Timestamp Verified
[+] Encrypted data: b'\xf4\x0f\xef\xcd\xbb\xf88\r%\x05\x90\xe07\xa0m{\x82\x1f\xcc\xee\r\x1d5?\xb2\x8e3\x00_\xd9\xbf7h\xd4G\xb8\x8b\x9d\xf2`\xa3\x14\xe1\x1a\xa4<\xdc\xf3hrh\xc6\xd5"v\xdd\'u\xd2\x04\r\xd3\x1ar\x1e\x89\xb8H<\xe0\x8b\xe5\x1f\xa8\x04\x85\x10\x7f=V\x1b]f\xf7<\x0e:\xbd-\x90i|\xf1\t8\xb5\r\xa3\xa6\xec\xfe\xd7WF\xc6\xfa\xcb\x83\xca\xb8E\xc34_\xd7@\x0c\xf6\xe5n\xd22s0\r_iN|\xfe\x9e\'\x87\r\x93c\x9c\xe77G\xec\x0b\xf49\xfcw\xdfdm\x05D\x81\xe0\x95\x97\xd6\xfa\xa2!\x0c\x0f!\x92\x90\x8b\x8b5\x00\xbem[\xe5\xf8\xb1\x9a\xdfc4<D@\xdb\x04\x8aT\xc8sF\xecC-\x98\x11\xdfrk\x0eKY\x9c\xb2b\xa5\xafEJt\xa0.\x8ak\xe7a\x80g\x16v4\xd4H\x1d\r\xb6\xf2[4VbL\x03\x7fw\xb6\xde\xcbk!\x0e\x8d\xd8P[\xb8\x90\xf4 \xafK\xb1\xdcK\x96\x12\xc6\xdf\xee\x1b\xf2Y\xe9\xabs\xab)\xed\xd8t\xab\xd5\xf9/\xddCt\'\xfa\x8f\x9b\x03o\x91\xae\x01\xdav\xf8\xd1l\x9f\x10\xe2\xd6(\x9c\t~a}\x08wP\xea\xde\x95c\xa0\xd5m\xb6\x04\xfc%\x8ep\xba/\x9d#KS\xa6/h\xfec\xca\x89(\xde\xd7\x81Sa6\x9f\x93\x1bG\xbe\xe7\\0\x1c)T\xc7\xae\rN\xebZ\xb0b-\x15w\x1c\xd2\xe7\xdb\x1d\x8e\x05\x0f(\xcd\xefG\x18b\xb4;m\x8af\x8b\x9e\xcc\x937"\x84\xb2\x07\xaax\x10mO\x0b\xeb\xfb\xa5\xb1\xd4\xc6\x07?\xd05\xdc\xc9\xcf\xae\xe950\x1a\xb4\x8fYy\x8e\xa2\x1ei\x14\x82\x0b\xd3R\xdc\x83\x88*B\xacn|\xea\xc4\xa4yl\x94M\xec\x16\x1f\x93\x80\xb5:8\x15~z}.\x9d\xd5\x0ed\xb7\x9e\xc0w\xd6\xa7\xb5\xad\x94d\xbd\xa4\xdbK\xc0u\x9dx\xc8\xaa?\xe8\xf9}W\xaeC\xbbr\xe5\xa7\x07z\xdb\x8ehq\xea\xc8\xbe\x9d\x91\xc1\x13f\x89\xa0\xf5 \xc3\x1f\x1a\xa9\xb8\xae\x8aA\x0b -\xa3\xda\x13\x9f\x8f\xc0\xc6:6\xa1\xda\xb2s\xe5\xa5\xfc\xc3\x80\xac\xdd9Y\xa3\xbd\x90\x95\xa1\x1f \xc2EG\x16L\xcf\x00\xc7|\x16(\xa0\xe2~\xf7]2\xa9\xfb\xf6\x17\xce3u\xa1\x9f*81q\xc8\x14\xe3a\x86\x86\x19\xc4\xb5\xdd&R'
[+] Decrypted data: 19:41:30552d4c971004e6c946093a4d1f2e1d7a1684b423737ef5833be0775832c70167F'+vÖU'ðMç.Ñpo=¡¨åÍãàsrc$§ý$ºW@õ«S9R÷y q5ÅõBån(Õ[D¼QeÔ³{õ0Âö#=?ï nðTæ¢á¹ò¯Ò?È=ó4Vcûk1®zèäÑ±*öLl?¢Q¨¿¹QF7/uÓÕ>2Õ%m8Pé[ó°-²"aã´³¸&(¸LIHüíûbPá0v:åÕ4Eõi;ÛG8 ;Þ¾¨ºnéöm§XHà@E¢³áØQ:6w¤]±©~¬¾ÖÒ¹»n;`#¶ CÄ2Qù¨G±³´Ñ$©*dAÌÀf²ÌoVæ³!blbÒÏh ýEHWçµz{ÞâÕt2¸I®þyæ]²î#GýQ¯¿Ã¿p³V Øò^çNÅCåùtâa·mÌ§í¼>[å.ÉiLhá½7Û½ÏLG3¬!ÅJCµ×/°«Î:Àü.£ò¡EfSÉõ¬­
[+] Timestamp: 19:41:30
[+] Message Authentication Successful
[+] MAC: b'552d4c971004e6c946093a4d1f2e1d7a1684b423737ef5833be0775832c70167'
[+] Actual Data: F'+vÖU'ðMç.Ñpo=¡¨åÍãàsrc$§ý$ºW@õ«S9R÷y q5ÅõBån(Õ[D¼QeÔ³{õ0Âö#=?ï    nðTæ¢á¹ò¯Ò?È=ó4Vcûk1®zèäÑ±*öLl?¢Q¨¿¹QF7/uÓÕ>2Õ%m8Pé[ó°-²"aã´³¸&(¸LIHüíûbPá0v:åÕ4Eõi;ÛG8 ;Þ¾¨ºnéöm§XHà@E¢³áØQ:6w¤]±©~¬¾ÖÒ¹»n;`#¶ C(c%%iËláòå|3jè­3W%·fYsF<ëÞ!FÕ[ø±ÖDeïHÏìÃ>ñ6L¥x7éÞ)ùnÊó½ÄËÄ2Qù¨G±³´Ñ$©*dAÌÀf²ÌoVæ³!blbÒÏh ýEHWçµz{ÞâÕt2¸I®þyæ]²î#GýQ¯¿Ã¿p³V Øò^çNÅCåùtâa·mÌ§í¼>[å.ÉiLhá½7Û½ÏLG3¬!ÅJCµ×/°«Î:Àü.£ò¡EfSÉõ¬­
[+] Packet Timestamp Verified
[+] Receiving  hello.test.signed via P2P
[+] Signature Verified. Stored the received file as hello.test.signed