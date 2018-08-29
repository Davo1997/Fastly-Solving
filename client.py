import socket
import sys
import time

s = socket.socket()

host = '192.168.1.106'
port = 9090

s.connect((host, port))
print("\nconnected to the server...")
while True:
    in_message = s.recv(1024)
    in_message = in_message.decode()
    print("\nServer: ", in_message)
    message = input(str(">>"))
    message = message.encode()
    s.send(message)
    print("message had been sent...")
