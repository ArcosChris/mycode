#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   CHALLENGE 01 - Solution"""    

def main():

    user_input = input("Please enter an IPv4 IP address: ")
    
    ## the line below creates a single string that is passed to print()
    # print("You told me the IPv4 address is:" + user_input)
    
    ## print() can be given a series of objects separated by a comma
    print("You told me the IPv4 address is:", user_input)
    
    # asking user for 'vendor name'
    vendor = input("Please input the vendor name: ")
    print(vendor)

main()
