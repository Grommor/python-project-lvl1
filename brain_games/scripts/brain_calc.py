#!/usr/bin/env python3

from random import randint
from brain_games import cli
import prompt


def brain_calc_game():
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        c = randint(0, 100)
        d = randint(0, 100)
        match randint(0, 2):
            case 0:
              right_answer = c + d
              client_answer = prompt.string(f"Question: {c} + {d}: ", empty=True)
            case 1:
              if c >= d:
                right_answer = c - d
                client_answer = prompt.string(f"Question: {c} - {d}: ", empty=True)
              else:
                right_answer = d - c
                client_answer = prompt.string(f"Question: {d} - {c}: ", empty=True)
            case 2:
                right_answer = c * d
                client_answer = prompt.string(f"Question: {c} * {d}: ", empty=True)

        cli.check_answer(right_answer, client_answer)
        i += 1



def main():
    cli.user_welcome()
    brain_calc_game()
    cli.user_bye(win=True)
