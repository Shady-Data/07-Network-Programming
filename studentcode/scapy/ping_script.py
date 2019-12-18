#!/usr/bin/env python3

import os

def pinger(p_ip):
    pinged = os.popen('ping -c 1 ' + p_ip)
    return pinged.read()

def get_ip():
    ip2ping = input('Enter the IP address of the system you want to ping: ')
    return ip2ping

print(pinger(get_ip()))
