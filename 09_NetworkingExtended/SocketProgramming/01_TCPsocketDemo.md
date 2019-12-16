# TCP/IP client-server communication

As we have established, sockets can either be configured to act as a server or client, 
to achieve bi-directional communication over TCP using the SOCK_STREAM family. In this example, 
we shall implement a simple echo application that receives all incoming data and sends them back to the sender. 
For that we will implement both client and server sockets. 
Furthermore, we will use the local loopback address 127.0.0.1 or localhost for our connections.

## Echo Server
```python
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        print("Closing current connection")
        connection.close()
```
## Echo Client
Unlike a server, a client only needs to execute the sequence of socket() and connect().

```python
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'This is our message. It is very long but will only be transmitted in chunks of 16 at a time'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
 ```
 
 Running out server and client scripts on separate terminal windows, this is the output from the server;
 
 ```
$ python3 echo_server.py
Starting up on localhost port 10000
waiting for a connection
connection from ('127.0.0.1', 49964)
received b'This is our mess'
sending data back to the client
received b'age. It is very '
sending data back to the client
received b'long but will on'
sending data back to the client
received b'ly be transmitte'
sending data back to the client
received b'd in chunks of 1'
sending data back to the client
received b'6 at a time'
sending data back to the client
received b''
no data from ('127.0.0.1', 49964)
Closing current connection
waiting for a connection
```
And the client;
```
$ python3 echo_client.py                                                                                             
connecting to localhost port 10000
sending b'This is our message. It is very long but will only be transmitted in chunks of 16 at a time'
received b'This is our mess'
received b'age. It is very '
received b'long but will on'
received b'ly be transmitte'
received b'd in chunks of 1'
received b'6 at a time'
closing socket
```
