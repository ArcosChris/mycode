#!/usr/bin/env python3
"""Carcos | christopher.arcos@tlgcohort.com
Testing simple dice game
"""

from cheatdice import *

def main():
    """run time code"""
    cheater1 = Steal_All_Player()
    cheater2 = Sabotage_Player()

    cheater1.roll()
    cheater2.roll()

    cheater1.cheat(cheater2)
    cheater2.cheat(cheater1)

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 1 wins!")

    else:
        print("Cheater 2 wins!")

if __name__ == "__main__":
    main()