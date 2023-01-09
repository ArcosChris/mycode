#!/usr/bin/env python3
"""Carcos | Working on OOP Inheritance
"""
#import random from stand lib. 
from random import randint

class Player: 
    def __init__(self):
        self.dice = []

    
    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1,6))
    
    def get_dice(self):
        return self.dice
    
class Cheat_Swapper(Player):
    def cheat(self):
        self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1 

class Mulligan_Cheater(Player):
    def cheat(self):
        if sum(self.get_dice()) < 9: 
            self.dice = []
            self.roll() 

class Additional_Die_Cheater(Player):
    def cheat(self):
        counter = 0
        for i in self.dice:
            if i < 3:
                self.dice[counter] = randint(3,6)
        counter += 1

class Sabotage_Player(Player):
    def cheat(self, other):
        for i in range(other.dice):
            other.dice[i] = randint(1,3)