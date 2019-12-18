#!/usr/bin/env python3

import socket

def find_service_name():
    protocolname = 'udp'
    port = 53
    protocol = socket.getservbyport(port, protocolname)
    port = 1
    while protocol != 'daytime':
        try:
            port += 1
            protocol = socket.getservbyport(port, protocolname)
        except OSError:
            continue
    print(f'Port: {port} => service name: {protocol}')

    # print(f'Port: {53} => service name: {socket.getservbyport(53, "udp")}')
    
if __name__ == '__main__':
    find_service_name()
