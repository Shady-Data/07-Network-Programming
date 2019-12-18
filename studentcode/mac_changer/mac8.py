#!/usr/bin/env python3

import subprocess
import optparse

def change_mac(p_interface, p_mac):
    print('Changing MAC address for: ' + p_interface + " to " + p_mac)

    subprocess.call(["ifconfig", p_interface, "down"])
    subprocess.call(["ifconfig", p_interface, "hw", "ether", p_new_mac])
    subprocess.call(["ifconfig", p_interface, "up"])
    subprocess.call(["ifconfig"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="add the new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle the error
        print("Please specify an interface, use --help for more details")
    elif not options.new_mac:
        # code to handle the error
        print("Please specify a new MAC, use --help for more details")
    else:
        return options

options = get_arguments()
change_mac(options.interface, options.new_mac)
