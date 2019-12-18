#!/usr/bin/env python3

import socket
import datetime

HOST = 'localhost'
PORT = 13
BUFF_SIZE = 1024
ADDR = (HOST, PORT)

srvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srvr.bind(ADDR)
print('Server Active')
try:
    while True:
        data, addr = srvr.recvfrom(BUFF_SIZE)
        message = datetime.datetime.now().strftime('%A, %B %d, %Y %X')
        srvr.sendto(message.encode(), addr)
        print('Answered request from:', addr)
except KeyboardInterrupt:
    print('Interrupt received. Shutting down the server')
    srvr.close()
