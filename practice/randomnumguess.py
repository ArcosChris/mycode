#!/usr/bin/env python3
import random 

total_tries = 4
random_num = random.randint(1,10)

user_tries = 0

print("Welcome to Guess that Number, the hottest new game of this century.")
print("Your job is to guess the number correctly")


while user_tries < total_tries:

    user_guess = int(input("\nPlease enter a number between 1 and 10\n"))

    if user_guess != random_num :
        user_tries += 1
        print(f"\nNo bueno, please try again. You have {(total_tries - user_tries)} tries left.\n")

        if user_tries == 0:
            print("Thanks for playing!")
        continue

    else:
        print(f"Congrats you guessed the correct number {user_guess} in {(user_tries + 1)} guesses")
        break
