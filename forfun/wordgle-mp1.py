#!/usr/bin/env python3
"""
CARCOS | christopher.arcos@tlgcohort.com | WE GOT WORDLE AT HOME.
"""
#important random and regex ops fronm standard lib
import random
import re

#storing random words collected from some website (could be API call but nahhhhhhhh)
words = [
"oral",
"thin",
"old",
"sink",
"pawn",
"seal",
"loot",
"gap",
"fog",
"bean",
"roof",
"glow",
"menu",
"veil",
"dog",
"belt",
"python",
"tree",
"west",
"last"
]

#custom_list empty on init 
#once random word is generated the set_custom_list_items() 
#function will populate it based on word length and amout of tries 
#word bank will store letters that exist in word but not in position given 
custom_list = []
word_bank = []
no_exist = []

rand_word = words[random.randint(0, len(words)-1)].lower();
total_tries = 6 
curr_attempt = 1
game_over = False

def main():
    print("\n\t\tWelcome to Wordgle!")
    print("\tVoted #1 word guessing game in Tuvalu") #small country no one knows about 
    print("**Not to be confused with our main competitor Wordle.**")
    
    print("\n****Directions****\n")
    print("> You have 6 tries to guess the correct word!")
    print("> If a letter exists in the word but is not in the correct position it will be added to your word bank")
    print("> If the letter is in the correct position it will replace that number.\n")

    set_custom_list_items()
    start_game()


#creates a multi-dim list based on the len of the random word per each nested list 
def set_custom_list_items():
    for attempt in range(total_tries):
        custom_list.append([])
        for i in range(len(rand_word)):
            custom_list[attempt].append(i+1) #change number on position to start at 1 not 0

#function to print the multi-dim list in a friendly way :) 
def print_graph():
    for i in custom_list: 
        print(i)
    print_word_bank()
    print_no_exist()

#user word bank stores any letters they may have got correct
def print_word_bank():
    print('\n__________________WORD BANK___________________')
    print(' '.join(word_bank))
    print('______________________________________________')

#user can see any guesses that do not exist in word    
def print_no_exist():
    print('\n__________________NOT IN WORD_________________')
    print(' '.join(no_exist))
    print('______________________________________________')

#game logic used to verify user input and compares it to random word
def start_game():
    global curr_attempt 

    while curr_attempt <= total_tries:
        try: 
            user_guess = input(f"\nPlease enter a {len(rand_word)} letter word\n").lower()
            print("\n")
            
            if not user_guess.isalpha(): #check if user input is only alphabetical chars
                print("\nOnly alphabet characters please!\n")
                continue
            elif len(user_guess) != len(rand_word):
                print(f"\n***Input should be {len(rand_word)} letters***\n")
                continue
            
        except Exception as e:
            print("Something happened: " + e)
        
        else:
            matches = verify_user_input(user_guess)
            print_graph()
            user_won = verify_curr_attempt()
            
            if user_won: 
                print("\n____________________________________________________________________________________")
                print(f"Congrats you win! You guessed the correct word ({rand_word}) in {curr_attempt} tries ")
                print("______________________________________________________________________________________")
                break
            
            else:
                if len(matches) > 0:
                    print(f"\n*Woohoo you got {len(matches)} correct!*\n")
                elif curr_attempt == 6:
                    print("\n___________________________________________________________")
                    print(f"*Well you tried but failed! The word was {rand_word.upper()}")
                    print("_____________________________________________________________")
                else: 
                    print(f"\n*Unfortunately, you're no good at this.*\n")

            curr_attempt += 1

#checks if user has the correct word
def verify_curr_attempt():
    user_won = False

    user_guessed_word = ''.join([str(i) for i in custom_list[curr_attempt-1]])
    
    if user_guessed_word == rand_word:
        user_won = True

    return user_won 


#verifies each char in user input 
def verify_user_input(word):
    word_chars = list(word)
    correct = []

    for char in range(len(word_chars)):
        if word_chars[char] == rand_word[char]:
            update_custom_list(char, word_chars[char])
            correct.append(word_chars[char])

        elif word_chars[char] != rand_word[char] and exists_in_random(word_chars[char]):    
            #adds chars to user word bank (these are letters that exist in word but not in pos)            
            if not word_chars[char] in word_bank:
                word_bank.append(word_chars[char])
            update_custom_list(char, 'X')
        
        else:
            #if not in position and does not exist in word add them to no_exist list
            if not word_chars[char] in no_exist:
                no_exist.append(word_chars[char])
            update_custom_list(char, 'X')
            

    #changes to the next inner list (will now populate next line)
    return correct
            


#finds any occurences of a specific char in a str (could've used a diff solution but am tired)
# returns list with indexes where char is found in str
def exists_in_random(char):
    found = False
    for i in range(len(rand_word)): 
        if rand_word[i] == char: 
            found = True
    return found


#updates the custom_list if the enters letter that exists in word and in correct position
def update_custom_list(pos, item):
    custom_list[(curr_attempt-1)][pos] = item

if __name__ == "__main__":
    main()
