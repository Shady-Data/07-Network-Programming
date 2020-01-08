#!/usr/bin/env python3

import socket
import datetime
import concurrent.futures
from time import sleep

def server_send(conn):
    while True:
        msg = input('send >')
        if not msg or msg == 'shutdown':
            conn.send(msg.encode())
            break
        elif msg == '!time':
            msg = f'The current time is {datetime.datetime.now().strftime("%A, %B %d, %Y %X")}'
        conn.send(msg.encode())
    print('send loop broken')
    conn.close()

def server_receive(conn):
    while True:
        data = conn.recv(BUFF)
        if data.decode('utf-8') == 'shutdown' or not data:
            msg = 'shutdown'
            conn.send(msg.encode())
            break
        print(' <', data.decode('utf-8'))
    print('receive loop broken')
    conn.close()

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
        with concurrent.futures.ThreadPoolExecutor() as executor: 
            t1 = executor.submit(server_send, conn.dup())
            t2 = executor.submit(server_receive, conn.dup())
            while True:
                if t1.done() or t2.done():
                    print('threads report done')
                    conn.close()
                    break

except KeyboardInterrupt:
    print('Interrupt recieved. Shutting server down')
    srvr.close()

