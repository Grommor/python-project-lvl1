#!/usr/bin/env python3

from random import randint
from brain_games import cli
import prompt


def main():
    cli.user_welcome()
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        c = randint(0, 100)
        d = randint(0, 100)

        match randint(0, 2):
            case 0:
              right_answer = c + d
              client_answer = prompt.string(f"Question: {c} + {d}: ")
              cli.check_answer(right_answer, client_answer)
              i += 1
            case 1:
              if c >= d:
                right_answer = c - d
                client_answer = prompt.string(f"Question: {c} - {d}: ")
              else:
                right_answer = d - c
                client_answer = prompt.string(f"Question: {d} - {c}: ")
                cli.check_answer(right_answer, client_answer)
                i += 1
            case 2:
                right_answer = c * d
                client_answer = prompt.string(f"Question: {c} * {d}: ")
                cli.check_answer(right_answer, client_answer)
                i += 1

    cli.user_bye(win=True)
