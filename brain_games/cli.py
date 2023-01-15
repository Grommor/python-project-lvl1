#!/usr/bin/env python3

import prompt


def user_welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
