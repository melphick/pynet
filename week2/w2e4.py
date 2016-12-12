#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
prints out both the MIB2 sysName and sysDescr.
"""

import snmp_helper

def get_snmp_info(device_ip):
    COMMUNITY_STRING = 'galileo'
    SNMP_PORT = 161
    IP = device_ip
    SYSNAME = '1.3.6.1.2.1.1.5.0'
    SYSDESCR = '1.3.6.1.2.1.1.1.0'

    device = (IP, COMMUNITY_STRING, SNMP_PORT)

    snmp_sysname_data = snmp_helper.snmp_get_oid(device, oid=SYSNAME)
    snmp_sysdescr_data = snmp_helper.snmp_get_oid(device, oid=SYSDESCR)
    sysname_output = snmp_helper.snmp_extract(snmp_sysname_data)
    sysdescr_output = snmp_helper.snmp_extract(snmp_sysdescr_data)
    print sysname_output
    print sysdescr_output


get_snmp_info(184.105.247.70)
get_snmp_info('184.105.247.71')
