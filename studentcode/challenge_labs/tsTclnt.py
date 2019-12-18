#!/usr/bin/env python3

from socket import *
import argparse

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 21567
BUFSIZ = 1024

parser = argparse.ArgumentParser('Simple TCP Client')
parser.add_argument('--host', action='store', dest='host', default=DEFAULT_HOST, help='Host to connect to')
parser.add_argument('--port', action='store', dest='port', default=DEFAULT_PORT, help='Port to connect to')
args = parser.parse_args()

host = args.host
port = args.port
ADDR = (host, port)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()
