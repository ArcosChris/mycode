#!/usr/bin/env python3
"""Carcos | Trivia Game using the opentdb api"""

import html
import requests
import random
import crayons

def user_choices():
    categories = {
        9  : "General Knowledge",
        10 : "Entertainment: Books",
        11 : "Entertainment: Film",
        12 : "Entertainment: Music",
        13 : "Entertainment: Musicals & Theatres",
        14 : "Entertainment: Television",
        15 : "Entertainment: Video Games",
        16 : "Entertainment: Board Games",
        17 : "Science & Nature",
        18 : "Science: Computers",
        19 : "Science: Mathematics",
        20 : "Mythology",
        21 : "Sports",
        22 : "Geography",
        23 : "History",
        24 : "Politics",
        25 : "Art",
        26 : "Celebrities",
        27 : "Animals",
        28 : "Vehicles",
        29 : "Entertainment: Comics",
        30 : "Science: Gadgets",
        31 : "Entertainment: Japanese Anime & Manga",
        32 : "Entertainment: Cartoon & Animations"
    }

    base = 'https://opentdb.com/api.php?'
    amount = input("How many questions would you like? 1-100\n")
    print("\nCODE \t\t CATEGORY\n")
    for k,v in categories.items():
        print(f"{k} - {v}")

    category = input("\nPlease enter a category code:\n")
    difficulty = input("\nPlease enter a difficulty level (Easy | Medium | Hard)\n").lower()
    custom_api_url = (f"{base}amount={amount}&category={category}&type=multiple&difficulty={difficulty}")
    start_game(custom_api_url)

def start_game(api):
    resp = requests.get(api).json()
    cat = resp['results'][0].get('category').title()
    print('\n=======================')
    print(f"{cat}")
    print('=======================')
    
    for question in resp['results']:
        answer = html.unescape(question['correct_answer'])
        options = [html.unescape(question['correct_answer'])]
        options.extend(question['incorrect_answers'])
        counter = 1

        print(crayons.green(f"\n{html.unescape(question['question'])}\n"))
        random.shuffle(options)

        for option in options:
            print(crayons.blue(html.unescape(f"{counter}. {option}")))
            counter += 1

        while True:
            try:
                user_answer = int(input(crayons.cyan("\nPlease enter the number associated with the answer.\n")))
                if user_answer < 1 or user_answer > len(options):
                    print(crayons.red(f"\n==========================="))
                    print(crayons.red("Not a valid answer. Do better."))
                    print(crayons.red(f"===========================\n"))
                    continue

            except ValueError:
                print(crayons.red("Please enter a valid number"))
                continue
            else:
                index = user_answer - 1
                if options[index] == answer:
                    print(crayons.yellow(f"\n==========================="))
                    print(crayons.yellow(f"Good Job! {answer} is correct"))
                    print(crayons.yellow(f"===========================\n"))
                    break
                else:
                    print(crayons.red(f"\n=========================================================="))
                    print(crayons.red(f"Sorry that is not correct. The correct answer is {answer}."))
                    print(crayons.red(f"==========================================================\n"))
                    break



def main():
    print('=======================')
    print('WELCOME to TRIVIA HOUSE')
    print('=======================')
    user_choices()

if __name__ == "__main__":
    main() 
