#!/usr/bin/env python3
"""Carcos | Working with APIs in python

    Description:
    A script to interact with an "open" api, 
     https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""


import requests

def main():
    """run time code"""

    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    print(dir(resp))

if __name__ == "__main__":
    main()

