#!/usr/bin/env python3
"""Carcos | Working with OpenAPIs with requests
"""

import requests

API = "https://www.anapioficeandfire.com/api"   


def main():
    resp = requests.get(API).json()

    print(resp)
    print(resp.keys())


if __name__ == "__main__":
    main()
