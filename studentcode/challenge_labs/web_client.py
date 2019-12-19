#!/usr/bin/env python3

import sys, socket

try:
    website = sys.argv[1]
except IndexError:
    print('Must supply a website as the first argument')
    sys.exit(2)

port = 80
sock = socket.create_connection((website, port))

req = ('GET / HTTP/1.1\r\n\r\n')

sock.sendall(req.encode())
web_bytes = bytearray()

while True:
    buf = sock.recv(4096)
    if not len(buf):
        break
    web_bytes += buf

webpage = web_bytes.decode('utf-8')

with open('webfile.html', 'w') as outfile:
    outfile.write(webpage)

