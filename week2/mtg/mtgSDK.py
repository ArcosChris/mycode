#!/usr/bin/env python3 
"""Carcos | Using MTG Python SDK

    Description: 
    Using the MTG Python SDK
"""

from mtgsdk import Card 

def main():
    user_search = input("Please enter a card name to begin your search: \n")

    cards = Card.where(name=user_search).all()
    
    for card in cards:
        print(f"{card.name}, {card.power}, {card.layout}\nInfo:{card.text}\n")


if __name__ == "__main__":
    main()
