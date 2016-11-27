#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
like exercise 8 but find all of the crypto map entries that are using PFS group2
"""
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_config.txt")

crypto_maps_PFS_group2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"pfs group2")

for i in crypto_maps_PFS_group2:
    print i.text
    for child in i.children:
        print child.text
