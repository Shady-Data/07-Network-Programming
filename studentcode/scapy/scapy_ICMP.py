#!/usr/bin/env python3

from scapy.all import *

dst_ip = '10.0.2.1'

pkt = IP(dst=dst_ip)/ICMP()/"hello world"
send(pkt)
