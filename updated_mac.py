#!/usr/bin/env python
import subprocess
import optparse

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change the mac address")
    parser.add_option("-m","--mac_address",dest="new_mac",help="new Mac address for interface")
    (options,argument) = parser.parse_args()
    if not options.interface:
        parser.error("[+] please spacify an interface , use --help for more info..")
    elif not options.new_mac:
        parser.error("[+] please spacify a new mac Address , use --help for more info..")
    return options

def change_mac(interface,new_mac):
    print("changing mac address for interface "+ interface +" to "+ new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])

options=get_argument()
change_mac(options.interface,options.new_mac)
