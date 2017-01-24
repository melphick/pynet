#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import pexpect
import sys
import re


def main():
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'
    port = 22

    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword')
    ssh_conn.sendline(password)

    ssh_conn.expect('#')

    ssh_conn.sendline('term len 0')
    ssh_conn.expect('#')

    ssh_conn.sendline('show ip int brief')
    ssh_conn.expect('#')
    print ssh_conn.before

    ssh_conn.sendline('show version')
    ssh_conn.expect('pynet-rtr1#')
    print ssh_conn.before

    pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
    ssh_conn.sendline('show version')
    ssh_conn.expect(pattern)


    print ssh_conn.after

if __name__ == "__main__":
    main()
