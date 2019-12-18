#!/usr/bin/env python3

import subprocess

interface = 'eth0'
new_mac = "00:33:44:55:66:77"

print('Changing MAC address for: ' + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
