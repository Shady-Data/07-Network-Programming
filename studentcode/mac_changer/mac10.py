#!/usr/bin/env python3

import subprocess
import optparse
import re

def change_mac(p_interface, p_mac):
    print('Changing MAC address for: ' + p_interface + " to " + p_mac)

    subprocess.call(["ifconfig", p_interface, "down"])
    subprocess.call(["ifconfig", p_interface, "hw", "ether", p_mac])
    subprocess.call(["ifconfig", p_interface, "up"])
    # subprocess.call(["ifconfig"])

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

def get_current_mac(p_interface):
    ifconfig_results = subprocess.check_output(["ifconfig", p_interface])
    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_results))
    
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could not read MAC address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("MAC address was changed to " + str(current_mac))
else:
    print("MAC address did not change")
