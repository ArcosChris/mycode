#!/usr/bin/env python3
"""
CARCOS | working on the looping with for challenge
"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


def main():

    print_farm_info('NE Farm')
    prompt_user()

    
       
def prompt_user():
    while True: 
        user_choice = input("\nWhich would you like to know more about? [A] - NE Farm, [B] - W Farm [C] - SE Farm\n")
        lowered = user_choice.lower()

        if lowered == 'a' or lowered == 'b' or lowered == 'c':
            farm = farm_name(lowered)
            print_farm_info(farm)
            break

        else: 
            print("Not a valid choice.")
            continue

def print_farm_info(name):
    
    for farm in farms: 
        if farm.get('name') == name:
            print(f"\n---{name}---")
            agriculture = farm.get('agriculture')

            for i in agriculture:
                print(i)
    
def farm_name(lowered):
    match lowered:
        case 'a':
            return "NE Farm"
        case 'b':
            return "W Farm"
        case 'c':
            return "SE Farm"


if __name__ == "__main__":
    main() 
