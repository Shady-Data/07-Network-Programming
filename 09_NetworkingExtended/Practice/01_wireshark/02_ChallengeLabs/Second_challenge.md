# Open challenge101-1.pcapng and answer these Challenge questions.

Important: This trace file includes an HTTP communication running over a non-standard port number. Before you can answer these questions, you must force 
wireshark to dissect this traffic as HTTP.

![image](https://user-images.githubusercontent.com/47218880/68698067-bec9cd00-0545-11ea-84d7-31ae215a6ecb.png)

1-1. 13 # filter = http && frame matches "GET / "
1-2. HTTP/1.1 200 OK\r\n    # read from packet
1-3. 15.438 # filter = tcp.time_delta > 15 packet 285
1-4. 4  # filter == tcp.flags.syn == 1 && tcp.time_delta > 1