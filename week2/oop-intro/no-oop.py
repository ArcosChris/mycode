#!/usr/bin/env python3 
"""Carcos | christopher.arcos@tlgcohort.com | Working on OOP in Python
"""
import random 
import crayons

def main():
    """run time function"""
    player1_dice = []
    player2_dice = []

    for i in range(3):
        ## 1-6 inclusive
        player1_dice.append(random.randint(1,6)) 
        player2_dice.append(random.randint(1,6)) 

    print(crayons.yellow(f"Player 1 rolled {player1_dice}"))
    print(crayons.blue(f"Player 2 rolled {player2_dice}"))
    

    #determine who won
    check_winner(player1_dice, player2_dice)

def check_winner(p1, p2):
    p1_sum = sum(p1)
    p2_sum = sum(p2)
   
    if p1_sum == p2_sum:
        print("It's a tie. Try again")
    elif p1_sum > p2_sum:
        print(crayons.yellow(f"\nPlayer 1 wins with {p1_sum} points."))
    else:
        print(crayons.blue(f"\nPlayer 2 wins with {p2_sum} points."))

if __name__ == "__main__":
    main()