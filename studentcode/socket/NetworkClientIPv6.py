#!/usr/bin/env python3

import socket

host = '::1'
port = 9898
size = 512
addr = (host, port)

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.connect(addr)

while True:
    data = input(' > ')
    if not data:
        break
    sock.send(data.encode())
    data = sock.recv(size)
    if not data:
        break
    print(data.decode('utf-8'))

sock.close()
