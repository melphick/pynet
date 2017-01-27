#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

from netmiko import ConnectHandler

#Dictionary definition for pynet-rtr1
pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22,
}

#Dictionary definition for pynet-rtr2
pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22,
}

#Establish an SSH session to the the two routers
#The ** passes in the pynet1 dictionary into the function
pynet_rtr1 = ConnectHandler(**pynet1) 
pynet_rtr2 = ConnectHandler(**pynet2)

#Print the prompts from both routers
prompt1 = pynet_rtr1.find_prompt()
prompt2 = pynet_rtr2.find_prompt()
print prompt1
print prompt2

#Get into config mode
response1 = pynet_rtr1.config_mode()
response2 = pynet_rtr2.config_mode()
print response1
print response2

#Double check config mode
response1 = pynet_rtr1.check_config_mode()
response2 = pynet_rtr2.check_config_mode()
print response1
print response2

#Exit config mode
response1 = pynet_rtr1.exit_config_mode()
response2 = pynet_rtr2.exit_config_mode()
print response1
print response2

#Send the command 'show ip int br' and print the output
response1 = pynet_rtr1.send_command('show ip int brief')
response2 = pynet_rtr2.send_command('show ip int brief')
print response1
print response2

#Send the command 'show versio' and print the output.
#note that you don't need to worry about paging
response1 = pynet_rtr1.send_command('show version')
response2 = pynet_rtr2.send_command('show version')
print response1
print response2

#Create a list of config change commands to send
config_commands = ['logging buffered 121212']

#Send the config change over the session and print teh output
output1 = pynet_rtr1.send_config_set(config_commands)
print output1
