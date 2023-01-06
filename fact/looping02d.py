#!/usr/bin/env python3
"""
Carcos | looping through files separating based on the ending of the string
"""

with open("dnsservers.txt", "r") as dnsfile:

    for server in dnsfile:
        server = server.rstrip('\n')

        if server.endswith('org'):
            with open("org-domain.txt", "a") as org_file:
                org_file.write(server + '\n')

        elif server.endswith('com'):
            with open('com-domain.txt',  'a') as com_file:
                com_file.write(server + '\n')

