#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import paramiko
import time
from getpass import getpass

ip_addr = '184.105.247.70'
username = 'pyclass'
password = '88newclass'
port = 22

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

remote_conn = remote_conn_pre.invoke_shell()

remote_conn.settimeout(6.0)

outp = remote_conn.recv(5000)
print outp

remote_conn.send("show ip int brief\n")

time.sleep(2)

outp = remote_conn.recv(5000)
print outp
