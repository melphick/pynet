#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Using ciscoconfparse find the crypto maps that are not using AES (based-on the
transform set name). Print these child entries.
"""
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_config.txt")

crypto_maps_not_AES = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"transform-set AES")

for i in crypto_maps_not_AES:
    print i.text
    for child in i.children:
        print child.text
