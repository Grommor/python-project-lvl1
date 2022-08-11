#!/usr/bin/env python3

from random import randint
import prompt


def main():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        question_number = randint(1, 100)
        print(f'Question: {question_number}')
        answer = prompt.string('Your answer: ')
        right_answer = 'no'
        if 0 == (question_number % 2):
            right_answer = 'yes'
        if (answer.lower() == right_answer):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer.lower()}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            exit()

    print(f'Congratulations, {name}!')
