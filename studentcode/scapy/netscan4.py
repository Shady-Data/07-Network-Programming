#!/usr/bin/env python3

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    print('IP\t\t\tMAC Address')
    print('--------------------------------------------------')
    for element in answered_list:
        print(element[1].psrc +'\t\t' + element[1].hwsrc)
        print('--------------------------------------------------')

scan('10.0.2.0/24') # CIDR does not work with .show() in python3 for ARP
