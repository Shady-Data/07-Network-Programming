# UDP client-server communication

Unlike the case with TCP transmission which streams messages in an ordered manner, 
UDP is message oriented and does not require a long-lived connection. 
A message in this case has to fit within a single datagram and delivery is not assured

## Echo Server
Here, we’ll only execute the socket() and bind() sequence since, there isn’t really a connection to listen for. 
Instead we only need to bind the socket to a particular address and wait for incoming messages. 
We will then read the incoming messages using the recvfrom() method and send them back with sendto().

```python
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(
        len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data, address)
        print('sent {} bytes back to {}'.format(
            sent, address))
```
## Echo Client
This client is similar to the server above, only that it doesn’t bind the socket to any address. 
Instead, the it uses sendto() to send messages to the server’s address.

```python
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is our message. It will be sent all at once'

try:

    # Send data
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, server_address)

    # Receive response
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()
```
This is the output when the client and server scripts are run on the server:
```
$ python3 echo_server_udp.py                                                                                         
starting up on localhost port 10000
waiting to receive message
received 48 bytes from ('127.0.0.1', 34351)
b'This is our message. It will be sent all at once'
sent 48 bytes back to ('127.0.0.1', 34351)
waiting to receive message
```
And the client:
```
$ python3 echo_client_udp.py                                                                                         
sending b'This is our message. It will be sent all at once'
waiting to receive
received b'This is our message. It will be sent all at once'
closing socket
```
