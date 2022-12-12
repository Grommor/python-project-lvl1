#!/usr/bin/env python3

from random import randint


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    for i in range(2,int(n/2)+2):
        if n%i==0:
            return False
    return True


def generate_question_and_answer():
    question_number = randint(1, 100)
    question = (f'Question: {question_number}')
    answer = 'no'
    if is_prime(question_number):
        answer = 'yes'
    return question, answer
