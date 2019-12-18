#!/usr/bin/env python3

from socket import *
import argparse

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 21567
BUFSIZ = 1024

parser = argparse.ArgumentParser('Simple UDP Client')
parser.add_argument('--host', action='store', dest='host', default=DEFAULT_HOST, help='Host to connect to')
parser.add_argument('--port', action='store', dest='port', default=DEFAULT_PORT, help='Port to connect to')
args = parser.parse_args()

host = args.host
port = args.port
ADDR = (host, port)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode(), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

udpCliSock.close()
