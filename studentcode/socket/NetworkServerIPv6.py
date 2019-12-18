#!/usr/bin/env python3

import socket

size = 512
host = '::1'
port = 9898

sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


sock.bind((host, port))
sock.listen(5)


c, addr = sock.accept()
data = c.recv(size)
if data:
    f = open('storageIPv6.dat', '+w')
    print("connection from: ", addr[0])
    f.write(addr[0])
    f.write(':')
    f.write(data.decode('utf-8'))
    f.close()
sock.close()

