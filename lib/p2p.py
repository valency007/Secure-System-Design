import socket
import threading

from lib.comms import StealthConn
from lib.files import p2p_download_file
from colorama import Fore, Style, init

server_port = 1337 #So we can keep track of ourselves

init(convert=True)

def find_bot(): #Find other bots listening on the network
    print(Fore.GREEN + "[+] Locating other cyber-attack bots"+ Style.RESET_ALL)
    port = 1337
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while 1:
        if port == server_port: #Don't connect to yourself, you dingbat bot!
            port += 1
        else:
            try:
                conn.connect(("localhost", port))
                print(Fore.MAGENTA + "[+] Found bot on port " + str(port) + Style.RESET_ALL) #Aha, found a bot on the network
                sconn = StealthConn(conn, client=True)
                return sconn
            except socket.error:
                print(Fore.RED +"[-] No bot was listening on port " + str(port) + Style.RESET_ALL) #Aww, no bot found
                port += 1

def echo_server(sconn):
    while 1:
        data = sconn.recv()
        print(Fore.GREEN + "[+] Echo Data> " + str(data) + Style.RESET_ALL) #Sending the data back as an echo
        sconn.send(data)
        if data == b'exit' or data == b'quit':
            print(Fore.CYAN + "[-] Closing connection\n" + Style.RESET_ALL) #User entered 'exit' or 'quit'. THis closed the connection
            sconn.close()
            return

def accept_connection(conn):
    try:
        sconn = StealthConn(conn, server=True)
        cmd = sconn.recv()
        if cmd == b'ECHO': #Echo 
            echo_server(sconn)
        elif cmd == b'FILE': #File download
            p2p_download_file(sconn)
    except socket.error:
        print(Fore.CYAN + "[-] Connection closed unexpectedly\n" + Style.RESET_ALL) #Something went wrong

def bot_server(): #Act as server or client
    global server_port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            s.bind(("localhost", server_port))
            print(Fore.RED + "[+] Checking Port " + str(server_port) + Style.RESET_ALL)
            break
        except socket.error:
            print(Fore.RED + "[-] Port Unavailable" + Style.RESET_ALL)
            server_port += 1
    s.listen(5)

    while 1:
        print(Fore.GREEN + "\n[+] Waiting for new messages" + Style.RESET_ALL)
        conn, address = s.accept()
        print (Fore.GREEN + "\n[+] New bot joined at "+str(address,) + Style.RESET_ALL)
        # Start a new thread per connection
        # We don't need to specify it's a daemon thread as daemon status is inherited
        threading.Thread(target=accept_connection, args=(conn,)).start()
