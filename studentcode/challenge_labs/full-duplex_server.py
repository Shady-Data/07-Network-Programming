#!/usr/bin/env python3

import socket
import datetime
import threading
from time import sleep

HOST = 'localhost'
PORT = 13373
ADDR = (HOST, PORT)
BUFF = 1024
    
srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvr.bind(ADDR)
srvr.listen(5)

print('Server Running')
try:
    while True:
        conn, addr = srvr.accept()

        def server_send():
            while True:
                # msg = input('send >')
                msg = f'The current time is {datetime.datetime.now().strftime("%A, %B %d, %Y %X")}'
                conn.send(msg.encode())
                sleep(5)

        def server_receive():
            while True:
                data = conn.recv(BUFF)
                if not data:
                    break
                print(data.decode('utf-8'))

        t1 = threading.Thread(target=server_send, name=1)
        t2 = threading.Thread(target=server_receive, name=2)

        t1.start()
        t2.start()


except KeyboardInterrupt:
    print('Interrupt recieved. Shutting server down')
    srvr.close()

