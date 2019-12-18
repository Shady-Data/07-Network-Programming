#!/usr/bin/env python3

import subprocess

interface = 'eth0'

print('Changing MAC address for: ' + interface)

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:22:33:44:55:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
