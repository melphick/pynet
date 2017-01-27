#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko
to verify your state (i.e. that you are currently in configuration mode).
"""

from netmiko import ConnectHandler

def main():
    #Dictionary definition for pynet-rtr2
    pynet2 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.71',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 22,
    }

    #Establish an SSH session to the the pynet-rtr2
    pynet_rtr2 = ConnectHandler(**pynet2)

    #Enter conig mode
    response = pynet_rtr2.config_mode()

    #Check that we are in config mode
    configmodechk = pynet_rtr2.check_config_mode()

    #Inform user of state
    if configmodechk == True:
        print "You are in config mode"
    else:
        print "You are not in config mode"

if __name__ == "__main__":
    main()
