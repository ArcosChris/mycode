#!/usr/bin/env python3 
"""Carcos | First OOP in python
"""
#bring in randint from stand lib (random)
from random import randint

#creating the player class
class Player: 
    def __init__(self):
        self.dice = []

    #method for roll 
    def roll(self):
        self.dice = [] #clearing current dice
        for i in range(3):
            self.dice.append(randint(1,6)) #1-6 incl

    def get_dice(self):
        return self.dice


def main():
    """Run time function"""
    # create both player objs
    player1 = Player()
    player2 = Player()

    #roll dice for players
    player1.roll()
    player2.roll()

    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"Player 2 rolled {player2.get_dice()}")

    check_winner(player1, player2)


def check_winner(p1, p2):
    p1score = sum(p1.get_dice())
    p2score = sum(p2.get_dice()) 

    if p1score == p2score:
        print("\nIt's a tie")
    elif p1score > p2score:
        print("\nPlayer 1 wins!")
    else:
        print("\nPlayer 1 wins!")

if __name__ == "__main__":
    main()