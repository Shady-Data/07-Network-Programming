#!/usr/bin/env python3 

# This program is optimized for Python 2.7.12 and Python 3.5.2. 
# It may run on any other version with/without modifications. 
 
import socket
import sys
import argparse

host = 'localhost'

def echo_client(port):
    """ A simple echo client """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print(f"Connecting to {server_address[0]} port {server_address[1]}")
    sock.connect(server_address)
     
    # Send data
    try:
        # Send data
        message = "Test message. This will be echoed"
        print(f"Sending {message}")
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f"Received: {data.decode('utf-8')}" )
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Other exception: {e}")
    finally:
        print("Closing connection to the server")
        sock.close()
     
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True) 
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
