from random import randint
import math

task = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    c = randint(1, 100)
    d = randint(1, 100)
    question = f'Question: {c} {d}'
    answer = str((math.gcd(c, d)))
    return question, answer
