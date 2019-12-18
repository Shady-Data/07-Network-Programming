#!/usr/bin/env python3

import socket

HOST = 'localhost'
PORT = 13373
ADDR = (HOST, PORT)
BUFF = 1024
token = False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

while True:
    if token:
        msg = input(' > ')
        client.send(msg.encode())
        token = False
    else:
        data = client.recv(BUFF)
        if not data:
            break
        print(data.decode('utf-8'))
        token = True

client.close()
