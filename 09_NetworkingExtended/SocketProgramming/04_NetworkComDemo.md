# Review of Sending Data
Now we are ready to look at the definition of the actions of the server in "tcp_server.py." 
This script with the definition of the setup starts as follows:
```python
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = ''      # blank so any address can be used
PORTNUMBER = 41267 # number for the port
BUFFER = 80        # size of the buffer

SERVER_ADDRESS = (HOSTNAME, PORTNUMBER)
SERVER = Socket(AF_INET, SOCK_STREAM)
SERVER.bind(SERVER_ADDRESS)
SERVER.listen(2)
```
Then the interaction with the client are defined in the continuation of the script "tcp_server.py" listed below:
```python

print('server waits for connection')
CLIENT, CLIENT_ADDRESS = SERVER.accept()
print('server accepted connection request from ',\
    CLIENT_ADDRESS)
print('server waits for data')
DATA = CLIENT.recv(BUFFER).decode()
print('server received \"%s\"' % DATA)

SERVER.close()
```
The script "tcp_client.py" is shorter than "tcp_server.py." 
The client script is listed below.
```python
from socket import socket as Socket
from socket import AF_INET, SOCK_STREAM

HOSTNAME = 'localhost'  # on same host
PORTNUMBER = 41267      # same port number
BUFFER = 80             # size of the buffer

SERVER_ADDRESS = (HOSTNAME, PORTNUMBER)
CLIENT = Socket(AF_INET, SOCK_STREAM)
CLIENT.connect(SERVER_ADDRESS)

print('client is connected')
DATA = input('Give message : ')
CLIENT.send(DATA.encode())
```
