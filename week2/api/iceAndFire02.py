#!/usr/bin/env python3
"""Carcos | Working with OpenAPIs with requests
"""


import pprint 
import requests

API = "https://www.anapioficeandfire.com/api/books"


def main():
    resp = requests.get(API).json()

    pprint.pprint(resp)

if __name__ == "__main__":
    main()
