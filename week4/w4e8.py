#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Use Netmiko to change the logging buffer size (logging buffered <size>) and to
disable console logging (no logging console) from a file on both pynet-rtr1 and
pynet-rtr2
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

    #list of all of the device dictionarys
    all_devices = [iosrtr1, iosrtr2]
    for a_device in all_devices:
        device_session = ConnectHandler(**a_device)
        prompt = device_session.find_prompt()
        output = device_session.send_config_from_file(config_file='config_cmds.txt')
        print "\n\n>>>>>>>>> {0} <<<<<<<<<".format(prompt)
        print output




if __name__ == "__main__":
    main()
