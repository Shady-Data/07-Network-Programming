#!/usr/bin/env python3

import socket
import concurrent.futures

HOST = 'localhost'
PORT = 13373
ADDR = (HOST, PORT)
BUFF = 1024

def client_send(conn):
    while True:
        msg = input(' > ')
        if not msg:
            msg = 'shutdown'
            conn.send(msg.encode())
            break
        conn.send(msg.encode())
    # print('>>>Send loop broken<<<')

def client_receive(conn):
    while True:
        data = conn.recv(BUFF)
        if data.decode('utf-8') == 'shutdown':
            print('shutdown received')
            break
        print(' <', data.decode('utf-8'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

with concurrent.futures.ThreadPoolExecutor() as executor: 
    t1 = executor.submit(client_send, client.dup())
    t2 = executor.submit(client_receive, client.dup())

    while True:
        if t1.done() and t2.done():
            # print('t1 and t2 complete')
            client.close()
            break
