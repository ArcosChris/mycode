#!/usr/bin/env python3
"""Carcos | Working with OpenAPIs with requests
"""


import requests 
import pprint

API_CHARS = "https://www.anapioficeandfire.com/api/characters/"
user_submit = ""

def main():
    global user_submit
    user_submit  = input("Pick a number between 1 and 1000 to return info on a GoT character!\n")
    resp = requests.get(API_CHARS + user_submit).json()

    get_character_info(resp)


def get_character_info(character):
    global user_submit
    name = character['name'] if character['name'] != "" else user_submit

    to_display = ['born', 'culture', 'died', 'father', 'gender', 'mother', 'playedBy', 'povBooks', 'spouse', 'titles', 'tvSeries']
    print('==============')
    print(f"{name}")
    print('==============')
    print('ALIAS')
    for i in character['aliases']:
        print(f"> {i}")
    print('==============')
    print("INFO:")
    for k, v in character.items():
        if (v != "" and v != [] and v != [""]) and k in to_display:
            if isinstance(v, list):
                print(f"> {k.title()} - {v}")
            else:
                print(f"> {k.title()} - {v.title()}")
    print('==============')
    print('BOOKS')
    for book in character['books']:
        print(f"> {requests.get(book).json()['name']}")
    print('===============')
    print("ALLENGIANCES")
    for a in character['allegiances']:
        print(f"> {requests.get(a).json()['name']}")

    print('===============')



if __name__ == "__main__":
    main()

