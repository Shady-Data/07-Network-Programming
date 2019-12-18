#!/usr/bin/env python3

import socket

size = 512
host = ''
port = 9899

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((host, port))

data, addr = sock.recvfrom(size)
if data:
    f = open('storageUDP.dat', '+w')
    print("connection from: ", addr[0])
    f.write(addr[0])
    f.write(':')
    f.write(data.decode('utf-8'))
    f.close()
    sock.sendto(b'Datagram Received!', addr)
sock.close()

