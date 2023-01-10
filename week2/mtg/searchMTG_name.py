#!/usr/bin/env python3
"""Carcos | Python practice API 


    Description: 
    Script to make requests to "https://api.magicthegathering.io/v1/
    User can search by name and will return card information"""

import requests as r

def main():

    user_input = input("Please eter the name and we will get you the information for that card: \n")


    API = "https://api.magicthegathering.io/v1/"

    card  = r.get(f"{API}cards?name={user_input}").json()

    print(card)

if __name__ == "__main__":
    main()
