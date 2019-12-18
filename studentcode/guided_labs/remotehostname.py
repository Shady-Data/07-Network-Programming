#!/usr/bin/env python3
import socket

def get_remote_machine_info():
    remote_host = 'notavalidurl'
    try:
        print(f'IP address of {remote_host}: {socket.gethostbyname(remote_host)}')
    except socket.error as e:
        print(f'{remote_host}: {e}')

if __name__ == '__main__':
    get_remote_machine_info()
