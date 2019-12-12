Open challenge101-3.pcapng and answer these Challenge questions. 
You will practice your display filter to locate traffic based on addresses,protocols, and keywords.

![image](https://user-images.githubusercontent.com/47218880/68698422-75c64880-0546-11ea-8e91-78f8fabb14c0.png)

3-1. 32 # statistics -> conversations
3-2. 8  # filter = dns or filter = udp.port == 53 || tcp.port == 53
3-3. 12 # filter = tcp.flags.syn == 1
3-4. 3  # filter = frame matches "set-cookie"
3-5. 18 # filter = tcp.time_delta > 1