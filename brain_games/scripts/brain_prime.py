#!/usr/bin/env python3

from random import randint
from brain_games import cli
import prompt


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def brain_prime_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        question_number = randint(1, 100)
        print(f'Question: {question_number}')
        right_answer = 'no'
        if is_prime(question_number):
            right_answer = 'yes'
        cli.check_answer(right_answer, prompt.string('Your answer: ', empty=True))
        i += 1


def main():
    cli.user_welcome()
    brain_prime_game()
    cli.user_bye(win=True)
