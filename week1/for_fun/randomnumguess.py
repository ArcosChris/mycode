#!/usr/bin/env python3

#importing random from standard lib
import random 

#user gets a total of 4 tries
total_tries = 4

#get random int between 1 and 10 
random_num = random.randint(1,10)

#when application runs user is using first try
user_tries = 0



print("\nWelcome to Guess that Number, the hottest new game of this century.")
print("Your job is to guess the number correctly")

# continue to loop if the user attemps is less than the 4 given
while user_tries < total_tries:

    #try to convert user input to int (if not possible will ask them again)
    try: 
        user_guess = int(input("\nPlease enter a number between 1 and 10\n"))

        if user_guess < 0 or user_guess > 10:
            print("\nBetween 1 and 10 please!")
            continue

    #if not able to convert to int will give message (ValueError) 
    except ValueError:
        print("\nNo clue what that is but a number will work.")

    #when input successfully converted to int
    else: 
        # if not equal to random num check inner conditions
        if user_guess != random_num:
            #when not correct increase user tries by one
            user_tries += 1
            #used for sentence structure
            total_left = total_tries - user_tries
            for_tries = 'try' if total_left == 1 else 'tries'

            #guess is less than random 
            if user_guess < random_num :
                print(f"\nNo bueno, you are guessing too low. Think Big. You have {(total_tries - user_tries)} {for_tries} left.\n")
            #guess is more than random 
            elif user_guess > random_num:
                print(f"\nNah that ain't it, too high. You have {(total_tries - user_tries)} {for_tries} left.\n")

            #when use has used all tries, say goodbye
            if user_tries == 4:
                print(f"The number was {random_num}. Thanks for playing!")
            
            continue
        
        #user guess correct print their guess and amount of tries then break out of loop
        else:
            user_tries += 1
            for_guess = 'guess' if user_tries == 1 else 'guesses'  
            print(f"\nCongrats you guessed the correct number {user_guess} in {user_tries} {for_guess}")
            break
