#!/usr/bin/env python3

import socket
from random import randint
import threading
from time import sleep

HOST = 'localhost'
PORT = 13373
ADDR = (HOST, PORT)
BUFF = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def client_send():
    try:
        while True:
            msg = input(' > ')
            if not msg:
                break
            client.send(msg.encode())
    except KeyboardInterrupt:
        return

def client_receive():
    try:
        while True:
            data = client.recv(BUFF)
            print(data.decode('utf-8'))
    except KeyboardInterrupt:
        return

t1 = threading.Thread(target=client_send, name=3)
t2 = threading.Thread(target=client_receive, name=4)

t1.start()
t2.start()

