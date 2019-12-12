# Open Challenge101-0.pcapng and answer these challenge questions. 

This is to focus on what you can learn about communications based on the main wireshark view.

![image](https://user-images.githubusercontent.com/47218880/68697729-0f8cf600-0545-11ea-854e-21cd80e74b07.png)

0-1. 20 # bottom status bar in "Packets: # / Displayed: #" section (bottm right in the wireshark window)
0-2. 192.168.1.108 -> 50.19.229.205 # packet 1 source to Destination
0-3. GET /Tracking/V3/Instream/Impression/?start|2873|72147|75904|9028|26105|undefined|1338|3379|807|BBEEND|&iari=148373&cb=634687327792649999&internalRedirect=false HTTP/1.1\r\n # Packet data
0-4. 1428   # statistics -> Packet Lengths (Max val)
0-5. Frame, Ethernet, IPv4, TCP, HTTP # Statistics -> Protocol Hierarchy
0-6. HTTP/1.1 302 Found\r\n # filter = http.response
0-7. No # # Statistics -> Protocol Hierarchy