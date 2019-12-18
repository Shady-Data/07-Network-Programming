#!/usr/bin/env python3

import socket
import concurrent.futures

HOST = 'localhost'
PORT = 13373
ADDR = (HOST, PORT)
BUFF = 1024

def client_send(conn):
    try:
        while True:
            msg = input(' > ')
            if not msg:
                break
            conn.send(msg.encode())
    except KeyboardInterrupt:
        return

def client_receive(conn):
    try:
        while True:
            data = conn.recv(BUFF)
            print(data.decode('utf-8'))
    except KeyboardInterrupt:
        return

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

with concurrent.futures.ThreadPoolExecutor() as executor: 
    t1 = executor.submit(client_send, client)
    t2 = executor.submit(client_receive, client)

    t1.add_done_callback(t2.cancel())
    t2.add_done_callback(client.close())
