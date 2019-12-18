#!/usr/bin/env python3

import socket

host = 'localhost'
port = 9899
size = 512
addr = (host, port)

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

while True:
    data = input(' > ')
    if not data:
        break
    sock.sendto(data.encode(), addr)
    data, addr = sock.recvfrom(size)
    if not data:
        break
    print(data.decode('utf-8'))

sock.close()
