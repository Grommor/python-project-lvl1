#!/usr/bin/env python3

import prompt

def user_welcome():
    global name
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

def check_answer(right_answer, client_answer):
    right_answer = str(right_answer)
    client_answer = str(client_answer)
    if right_answer == client_answer: 
        print('Correct!')
    else: 
        user_bye(client_answer, right_answer)

def user_bye(answer=0, right_answer=0, win=0):
    if win:
        print(f'Congratulations, {name}!')
        exit()
    else:    
        print(f"'{answer.lower()}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
        print(f"Let's try again, {name}!")
        exit()