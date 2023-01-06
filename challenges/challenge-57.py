#!/usr/bin/env python3
"""
CARCOS | Christopher.arcos@tlgcohort.com | challenge 57
"""

import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

def main():
    print(f"{trivia.get('question')}")
    print(f'''
              [A] - {html.unescape(trivia.get('correct_answer'))}
              [B] - {html.unescape(trivia.get('incorrect_answers')[0])}
              [C] - {html.unescape(trivia.get('incorrect_answers')[1])}
              [D] - {html.unescape(trivia.get('incorrect_answers')[2])}''')

    user_answer = input("Please enter your answer\n")

    if user_answer == 'A' or user_answer == 'a':
        print("Congrats! You win!")
    
    else:
        print("No, thanks for trying it out.")


if __name__ == "__main__":    
    main()
