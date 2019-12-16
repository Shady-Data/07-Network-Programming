# Examples

## Python get IP address
With gethostbyname(), we get the IP address of the host.

### File: get_ip.py
```python
#!/usr/bin/env python

import socket

ip = socket.gethostbyname('example.com')
print(ip)
```
The example prints the IP address of example.com.
```
$ ./get_ip.py
93.184.216.34
```
This is the output.

## QOTD example
UDP is a communication protocol that transmits independent packets over the network with no guarantee of arrival and no guarantee of the order of delivery. One service that used UDP is the Quote of the Day (QOTD).

### File: qotd_clt.py
```python
#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    message = b''
    addr = ("djxmmx.net", 17)

    s.sendto(message, addr)

    data, address = s.recvfrom(1024)
    print(data.decode())
```
```
$ ./qotd_client.py
"Oh the nerves, the nerves; the mysteries of this machine called man!
    Oh the little that unhinges it, poor creatures that we are!"
    Charles Dickens (1812-70)
```
This is a sample output.

 
