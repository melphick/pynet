#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
"""

from netmiko import ConnectHandler

def main():

    #Dictionary definition for iosrtr1
    iosrtr1 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.70',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 22,
    }

    #Dictionary definition for iosrtr2
    iosrtr2 = {
        'device_type': 'cisco_ios',
        'ip': '184.105.247.71',
        'username': 'pyclass',
        'password': '88newclass',
        'port': 22,
    }


    #Dictionary definition for junosrtr1
    junosrtr1 = {
        'device_type': 'juniper',
        'ip': '184.105.247.76',
        'port': 22,
        'username': 'pyclass',
        'password': '88newclass',
    }

    #list of all of th device dictionarys
    all_devices = [iosrtr1, iosrtr2, junosrtr1]

    #loop through all of the devices, connect and then run show arp
    for a_device in all_devices:
        device_session = ConnectHandler(**a_device)
        output = device_session.send_command('show arp')
        prompt = device_session.find_prompt()
        print "\n\n>>>>>>>>> {0} <<<<<<<<<".format(prompt)
        print output


if __name__ == "__main__":
    main()
