#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Write a script that connects using telnet to the pynet-rtr1 router. Execute the 'show ip int brief' command on the router and return the output.

You should be able to do this by using the following items:

telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()
"""
import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')

    time.sleep(1)
    output = remote_conn.read_very_eager()
    print  output

    remote_conn.write('term len 0\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print  output

    remote_conn.write("show ip int br" + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print  output
    
    remote_conn.close

if __name__ == "__main__":
    main()
