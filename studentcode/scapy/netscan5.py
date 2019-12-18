#!/usr/bin/env python3

import scapy.all as scapy
import argparse

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

def parse_args():
    parser = argparse.ArgumentParser(description='ARP Based Network Scanner')
    parser.add_argument('-n', '--net', type=str, required=True, help='Single IP or CIDR notated network to scan')
    return parser.parse_args()

args = parse_args()
scan(args.net) # CIDR does not work with .show() in python3 for ARP
