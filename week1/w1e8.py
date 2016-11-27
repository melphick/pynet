#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A Python program using ciscoconfparse that parses a file to find all of the
crypto map entries in the file (lines that begin with 'crypto map CRYPTO')
and for each crypto map entry print out its children.
"""

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_config.txt")

crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for i in crypto_maps:
    print i.text
    for child in i.children:
        print child.text
