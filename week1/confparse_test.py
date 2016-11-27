#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_config.txt")

print cisco_cfg

intf = cisco_cfg.find_objects(r"^interface")

print intf

for i in intf:
    print i.text

interface_4 = intf[4]
print interface_4
print interface_4.children

for child in interface_4.children:
    print child.text

no_ip = cisco_cfg.find_objects_w_child(parentspec=r"interface", childspec=r"no ip address")

print no_ip

with_ip = cisco_cfg.find_objects_wo_child(parentspec=r"interface", childspec=r"no ip address")

print with_ip
