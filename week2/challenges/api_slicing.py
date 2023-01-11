#!/usr/bin/env python3
"""CARCOS | API Slicing
"""

import requests


def main():
    pokenum = input("Pick a number between 1 and 115!\n")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
   
    poke_img = pokeapi.get("sprites").get("front_default")

    print(poke_img)
    img = requests.get(poke_img).content
 
    with open(f"/home/student/static/{pokeapi.get('name')}_{pokenum}.png", "wb") as poimg:
        poimg.write(img)

    print("Image downloaded")
    
    for m in pokeapi.get("moves"):
        print(f"{m.get('move').get('name')}")
    
    print(f"Total games: {len(pokeapi['game_indices'])} ")
main()

