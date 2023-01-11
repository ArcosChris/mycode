#!/usr/bin/env python3
"""Carcos | Trivia Game using the opentdb api"""

import html
import requests
import random

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
    difficulty = input("\nPlease enter a difficulty level\nEasy\nMedium\nHard\n").lower()
    custom_api_url = (f"{base}amount={amount}&category={category}&type=multiple&difficulty={difficulty}")
    start_game(custom_api_url)

def start_game(api):
    resp = requests.get(api).json()
    cat = resp['results'][0].get('category').title()
    print('=======================')
    print(f"{cat}")
    print('=======================')
    
    for question in resp['results']:
        answers = [{question['correct_answer']: True}]
        print(f"{html.unescape(question['question'])}\n")
       
        for incorrect in question['incorrect_answers']:
            answers.append({incorrect: False})
        
        random.shuffle(answers)

        for answer in (answers):
            print(answer)

def main():
    print('=======================')
    print('WELCOME to TRIVIA HOUSE')
    print('=======================')
    user_choices()

if __name__ == "__main__":
    main() 
