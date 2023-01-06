#!/usr/bin/env python3
"""
CARCOS | loop data from file
"""

dnsfile = open("dnsservers.txt", "r") # open file to read

#read each line in file above
dnslist = dnsfile.readlines()


for server in dnslist:
    print(server, end ="")

dnsfile.close() #closing the file
