#!/usr/bin/env python3

import socket
import datetime

HOST = 'localhost'
PORT = 13373
ADDR = (HOST, PORT)
BUFF = 1024
token = True

srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvr.bind(ADDR)
srvr.listen(5)

print('Server Running')
try:
    while True:
        print('waiting for connection...')
        Tcli, addr = srvr.accept()
        print('Connected from:', addr)
        while True:
            if token:
                msg = f'The current time is {datetime.datetime.now().strftime("%A, %B %d, %Y %X")}'
                Tcli.send(msg.encode())
                token = False
            else:
                data = Tcli.recv(BUFF)
                if not data:
                    break
                print(data.decode('utf-8'))
                token = True
        Tcli.close()
except KeyboardInterrupt:
    print('Interrupt recieved. Shutting server down')
    srvr.close()

