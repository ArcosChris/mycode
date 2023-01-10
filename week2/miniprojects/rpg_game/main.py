#!/usr/bin/env python3 
"""Carcos | christopher.arcos@tlgcohort.com | RPG Game Mini Project |
   Prep for The Purge
"""


#prepared is things user needs to do ex/w1 is a window that needs to be covered
rooms = {
    'Living Room' : {
        'north' : 'Dining Room',
        'west' : 'Office',
        'items': ['Hammer'],
        'prepared' : [{'w1': False}, {'w2': False }, {'w3': False}]
    }, 
    'Dining Room' : {
        'north': 'Backyard',
        'west' : 'Kitchen',
        'items': ['Sandwich', 'Water'],
        'prepared' : [{'w1': False}, {'w2': False}, {'backyard_door': False}]
    },
    'Kitchen':{
        'south' : 'Basement Door',
        'prepared' : [{'w1': False}, {'w2': False}, {'basement_door': False}],
        'items' : ['Knife']
    },
    'Basement' : {
        'north' : 'Kitchen',
        'items' : ['Wood', 'Chainsaw, Gas Mask']
    },
    'Backyard' : {
        'south': 'Dining Room',
        'items': ['Wood', 'Axe', 'Nail Gun'],
    },
    'Office': {
        'east' : 'Living Room',
        'items': ['Shotgun', 'Nails']
    }
}

class Player: 
    health = 100
    inventory = []
    name = ''

    def __init__(self, name):
        self.name = name

    def get_health(self):
        return self.health

    def get_inventory(self):
        return self.inventory

def main():
    player = prompt_user()
    show_instructions(player)
    start_game()

def show_instructions(player):
    print("=========================================")
    print(f"\t\tWelcome {player.name.title()}!")
    print('Prepare your house for before the Zombies get to you.\nIf you do not get this done in time.\nWho knows what could happen.')
    print('Collect anything that may be useful.\nGood luck to you and Good luck to us all.')
    print("=========================================")


def prompt_user():
    print("=========================================")
    user_prompt = input("Welcome please enter your name to begin\n")
    print("=========================================")
    return Player(user_prompt)

def show_instructions():
    print("It's time to crack open a cold one (soda) sit back and watch some TV in your living room.")
    print("[static on television] WE INTERRUPT YOUR REGULARY SCHEDULED PROGRAM WITH AND EMERGENCY SERVICE ANNOUNCEMENT.")
    print("[on television] There seems to be an outbreak of some kind and we are warning everyone to stay inside and prepare for the worst.")
    print("[on television] People are beginning to eat each other and no one understands why...")
    print('\n**If I were you I would probably get wood from the backyard or basement to cover everything up before its too late**.')

    print("========")
    print("COMMANDS")
    print("get [item]")
    print("go [direction]")
    print("========")

def start_game():
    user_location = 'Living Room'
    show_instructions()

        
    while True: 
        get_room_info(user_location)
        move = ''

        while move == '':
            move = input('>')
        
        move = move.lower().split(" ", 1)

        




def get_room_info(location):
    print(f"You are in the {location.title()}")





if __name__ == "__main__":
    main()


