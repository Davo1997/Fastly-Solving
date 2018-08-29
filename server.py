import socket
import sys
import time

s = socket.socket()

host = '192.168.1.106'
print("server will start on host: ", host)
port = 9090
s.bind((host, port))
print("\nServer has done binding successfully!")
print("\nServer is waiting for comming connections...")
s.listen(3)
conn, addr = s.accept()
print("\n", addr, "has connected to the server and now is online...\n")

while True:
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    print("message had been sent...\n")
    in_message = conn.recv(1024)
    in_message = in_message.decode()
    print("\nClient: ", in_message)

