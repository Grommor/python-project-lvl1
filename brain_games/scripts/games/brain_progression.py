#!/usr/bin/env python3

from random import randint
from brain_games import cli
import prompt

def main():
    cli.user_welcome()  
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        d = randint(0,10)

        progression_list = list(range(randint(1,15), 150, randint(1,10)))
        hidden_number = progression_list[d]
        print(hidden_number)

        progression_list[d] = '..'
        
        print(f'Question: {progression_list[0:10]}')
        cli.check_answer(hidden_number, prompt.string(f'Your answer: '))
        i += 1

    cli.user_bye(win=True)