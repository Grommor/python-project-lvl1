#!/usr/bin/env python3

from random import randint
from brain_games import cli
import prompt


def main():
    cli.user_welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0
    while i < 3:
        question_number = randint(1, 100)
        print(f'Question: {question_number}')
        right_answer = 'no'
        if 0 == (question_number % 2):
            right_answer = 'yes'

        cli.check_answer(right_answer, prompt.string('Your answer: '))

        i += 1

    cli.user_bye(win=True)
