#!/usr/bin/env python3

import socket

host='localhost'

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr=(host, 5555)
mysock.connect(addr)

