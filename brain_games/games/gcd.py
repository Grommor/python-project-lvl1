from random import randint
import math

TASK = 'Find the greatest common divisor of given numbers.'
INTERVAL_START = 1
INTERVAL_END = 100


def generate_question_and_answer():
    member_1 = randint(INTERVAL_START, INTERVAL_END)
    member_2 = randint(INTERVAL_START, INTERVAL_END)
    question = f'Question: {member_1} {member_2}'
    answer = str((math.gcd(member_1, member_2)))
    return question, answer
