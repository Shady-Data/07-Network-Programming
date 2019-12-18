#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()
    print(arp_request_broadcast.summary())

# scan('10.0.2.0/24') # CIDR does not work in python3 for ARP
scan('10.0.2.1')
# for octet in range(256):
#     scan('10.0.2.' + str(octet))
