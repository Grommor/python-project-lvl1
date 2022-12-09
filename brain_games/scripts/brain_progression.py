#!/usr/bin/env python3

from random import randint
from brain_games import cli
import prompt


def brain_progression_game():
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        d = randint(0, 9)
        progression_list = list(range(randint(1, 15), 150, randint(1, 10)))
        hidden_number = progression_list[d] 
        progression_list[d] = '..'
        print(f'Question: {progression_list[0:10]}')
        cli.check_answer(hidden_number, prompt.string('Your answer: '))
        i += 1


def main():
    cli.user_welcome()
    brain_progression_game()
    cli.user_bye(win=True)
