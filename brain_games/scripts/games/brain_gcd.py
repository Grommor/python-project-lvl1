#!/usr/bin/env python3

from random import randint
from brain_games import cli
import prompt
import math

def main():
    cli.user_welcome()  
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        c = randint(1,100)
        d = randint(1,100)

        print(f'Question: {c} {d}')
        print(math.gcd(c, d))
        cli.check_answer(math.gcd(c, d), prompt.string(f'Your answer: '))
        i += 1

    
    cli.user_bye(win=True)
