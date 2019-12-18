#!/usr/bin/env python3

import socket

def convert_integer():
    data = 1234
    # 32-bit
    print(f'Original: {data} => Long host byte order: {socket.ntohl(data)}, Network byte order: {socket.htonl(data)}')
    # 16-bit
    print(f'Original: {data} => Long host byte order: {socket.ntohs(data)}, Network byte order: {socket.htons(data)}')

if __name__ == '__main__':
    convert_integer()
