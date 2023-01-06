#!/usr/bin/env python3
"""
CARCOS | christopher.arcos@tlgcohort.com | IF continued..
"""


ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk:
   print("Looks like the IP address was set: " + ipchk) # indented under if
else: 
    #if no value is passed this will be default
    print("You did not provide an input")
