#!/usr/bin/env python3
"""
CARCOS | Bottles of beer challenge
"""

def main():

    while True:
        try:
            user_amount = int(input("\nAt what number would you like me to start singing from? [1-100]\n"))
        
            
        except ValueError:
            print("Please enter a valid number. This wont do.")
            
        else:
            if user_amount < 1 or user_amount > 100:
                print("1-100 only please!")
                continue

            else:
                for i in reversed(range(user_amount)):
                    bottle_num = i + 1
                    print(f"{bottle_num} bottles of beer on the wall!")
                    print(f"{bottle_num} bottles of beer on the wall! {bottle_num} bottles of beer! You take one down, pass it around!\n")
            break

if __name__ == "__main__":
    main()
