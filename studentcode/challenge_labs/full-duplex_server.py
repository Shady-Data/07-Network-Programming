#!/usr/bin/env python3

import socket
import datetime
import concurrent.futures

HOST = 'localhost'
PORT = 13373
ADDR = (HOST, PORT)
BUFF = 1024

def server_send(client):
    while True:
        # msg = input('send >')
        msg = f'The current time is {datetime.datetime.now().strftime("%A, %B %d, %Y %X")}'
        client.send(msg.encode())

def server_recieve(client, buff=BUFF):
    while True:
        data = client.recv(BUFF)
        if not data:
            break
        print(data.decode('utf-8'))

srvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srvr.bind(ADDR)
srvr.listen(5)

print('Server Running')
try:
    while True:
        print('waiting for connection...')
        Tcli, addr = srvr.accept()
        print('Connected from:', addr)
        with concurrent.futures.ProcessPoolExecutor() as executor:
            p1 = executor.submit(server_recieve, Tcli)
            p2 = executor.submit(server_send, Tcli)

            p1.add_done_callback(p2.cancel())
            p2.add_done_callback(Tcli.close())

except KeyboardInterrupt:
    print('Interrupt recieved. Shutting server down')
    srvr.close()

