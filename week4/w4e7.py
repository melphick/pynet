#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Use Netmiko to change the logging buffer size (logging buffered <size>)
on pynet-rtr2.
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

    #Create a list of config change commands to send
    config_commands = ['logging buffered 121212']

    #Send the config change over the session and print the output
    config_output = pynet_rtr2.send_config_set(config_commands)
    print config_output

if __name__ == "__main__":
    main()
